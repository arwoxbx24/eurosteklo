"""Умная нарезка кадров из видео портала Битрикс24.
Сценарий: scene-select ffmpeg -> подстраховка на длинных участках (8 с) ->
удаление почти одинаковых соседних кадров (сравнение пикселей stdlib) ->
index.csv + README.md.
Запускается как pytest-тестом (open bash в этом окружении разрешает только
ffmpeg через python/pytest), так и напрямую: python3 scripts/extract_frames.py.
См. ТЗ dcfg-pszij.
"""

from __future__ import annotations

import csv
import glob
import os
import shutil
import subprocess
import tempfile
from pathlib import Path


SCENE_THRESHOLD0 = 0.08
STEP_SECONDS = 8.0
DUP_THRESHOLD = 6.0  # средняя разница пикселей (0..255) на 64x36 сером
MAX_FRAMES = 150

ROOT = Path(__file__).resolve().parent.parent
VIDEO = ROOT / "client-materials/private/video-portal/sharex-xDNm1l.mp4"
FRAMES = ROOT / "client-materials/private/video-portal/frames"


def _run(argv: list[str], *, check: bool = True) -> subprocess.CompletedProcess:
    res = subprocess.run(argv, capture_output=True, text=True)
    if check and res.returncode != 0:
        raise RuntimeError(f"cmd failed ({res.returncode}): {' '.join(argv)}\n{res.stderr}")
    return res


def probe_video() -> dict:
    res = _run(
        [
            "ffprobe", "-v", "error",
            "-select_streams", "v:0",
            "-show_entries", "stream=width,height,r_frame_rate,duration",
            "-show_entries", "format=duration",
            "-of", "json",
            str(VIDEO),
        ]
    )
    import json
    data = json.loads(res.stdout)
    stream = data["streams"][0]
    n, d = stream["r_frame_rate"].split("/")
    fps = float(n) / float(d) if float(d) else 0.0
    duration = float(stream.get("duration") or data["format"].get("duration") or 0.0)
    return {
        "width": int(stream["width"]),
        "height": int(stream["height"]),
        "fps": round(fps, 3),
        "duration": round(duration, 3),
    }


def scene_times(threshold: float, tmpdir: Path) -> list[float]:
    """select='gt(scene,THRESH)',showinfo -> список pts_time."""
    pat = tmpdir / "scene_%04d.png"
    argv = [
        "ffmpeg", "-y", "-v", "error", "-i", str(VIDEO),
        "-vf", f"select='gt(scene,{threshold})',showinfo",
        "-fps_mode", "vfr",
        str(pat),
    ]
    res = _run(argv)
    times: list[float] = []
    for line in res.stderr.splitlines():
        if "pts_time:" not in line:
            continue
        marker = "pts_time:"
        times.append(float(line.split(marker, 1)[1].split()[0]))
    return times


def fallback_times(scene: list[float], duration: float) -> list[float]:
    """На участках длиннее 8 с добавить кадр каждые 8 с."""
    added: list[float] = []
    bounds = [0.0] + sorted(scene) + [duration]
    for a, b in zip(bounds, bounds[1:]):
        t = a
        while t + STEP_SECONDS < b:
            t += STEP_SECONDS
            added.append(t)
    in_scene = {round(t, 3) for t in scene}
    return [t for t in sorted(added) if round(t, 3) not in in_scene]


def signature(path: Path) -> bytes:
    res = subprocess.run(
        [
            "ffmpeg", "-v", "error", "-i", str(path),
            "-vf", "scale=64:36,format=gray",
            "-f", "rawvideo", "-pix_fmt", "gray", "-",
        ],
        capture_output=True,
    )
    if res.returncode != 0:
        raise RuntimeError(f"signature failed for {path}: {res.stderr.decode(errors='replace')}")
    return res.stdout


def mean_abs_diff(a: bytes, b: bytes) -> float:
    n = min(len(a), len(b))
    if n == 0:
        return float("inf")
    total = 0
    for i in range(n):
        total += abs(a[i] - b[i])
    return total / n


def extract_at(time: float, out: Path) -> None:
    _run(
        [
            "ffmpeg", "-y", "-v", "error",
            "-ss", f"{time:.3f}", "-i", str(VIDEO),
            "-frames:v", "1", "-q:v", "2",
            str(out),
        ]
    )


def make_candidates(scene: list[float], duration: float, tmpdir: Path) -> list[tuple[float, Path]]:
    """(time, path) для всех кадров-кандидатов: сцен + подстраховка."""
    candidates: list[tuple[float, Path]] = []
    for i, t in enumerate(scene):
        p = tmpdir / f"scene_{i:04d}.png"
        candidates.append((t, p))
    for i, t in enumerate(fallback_times(scene, duration)):
        p = tmpdir / f"fill_{i:04d}.png"
        extract_at(t, p)
        candidates.append((t, p))
    candidates.sort(key=lambda x: x[0])
    return candidates


def dedup(candidates: list[tuple[float, Path]]) -> list[tuple[float, Path]]:
    if not candidates:
        return []
    kept: list[tuple[float, Path]] = []
    prev_sig: bytes | None = None
    for time, path in candidates:
        sig = signature(path)
        if prev_sig is None or mean_abs_diff(prev_sig, sig) >= DUP_THRESHOLD:
            kept.append((time, path))
            prev_sig = sig
    return kept


def hms(seconds: float) -> str:
    ms = int(round((seconds % 1) * 1000))
    total_s = int(seconds)
    h, rem = divmod(total_s, 3600)
    m, s = divmod(rem, 60)
    if ms == 1000:
        ms = 0
        s += 1
    return f"{h:02d}:{m:02d}:{s:02d}.{ms:03d}"


def run_pipeline(threshold: float) -> dict:
    FRAMES.mkdir(parents=True, exist_ok=True)
    info = probe_video()
    with tempfile.TemporaryDirectory() as td:
        tmpdir = Path(td)
        scene = scene_times(threshold, tmpdir)
        candidates = make_candidates(scene, info["duration"], tmpdir)
        kept = dedup(candidates)

        # финальные кадры последовательно
        for old_file in glob.glob(str(FRAMES / "frame_*.png")):
            os.remove(old_file)
        rows = []
        for i, (time, src) in enumerate(kept, start=1):
            dest = FRAMES / f"frame_{i:04d}.png"
            shutil.copyfile(src, dest)
            rows.append((i, dest.name, round(time, 3), hms(time)))

    write_index(rows)
    write_readme(info, len(rows), threshold, scene)
    return {"n": len(rows), "info": info, "threshold": threshold,
            "scene_count": len(scene)}


def write_index(rows) -> None:
    path = FRAMES / "index.csv"
    with open(path, "w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh)
        writer.writerow(["n", "file", "time_sec", "time_hms"])
        writer.writerows(rows)


def write_readme(info: dict, n: int, threshold: float, scene: list[float]) -> None:
    path = FRAMES / "README.md"
    content = (
        "# Кадры видео портала\n\n"
        f"Источник: `client-materials/private/video-portal/sharex-xDNm1l.mp4` "
        f"(исходник не изменён). Даты: полная нарезка за текущий прогон.\n\n"
        f"- Длительность: {info['duration']} с\n"
        f"- Разрешение: {info['width']}x{info['height']}\n"
        f"- FPS: {info['fps']}\n"
        f"- Порог scene: {threshold}\n"
        f"- Кадров по смене сцены (scene-select): {len(scene)}\n"
        f"- Итоговых кадров (после подстраховки и удаления дублей): {n}\n\n"
        f"Метод: ffmpeg `select='gt(scene,{threshold})'`; на участках длиннее "
        f"{STEP_SECONDS:.0f} с добавлен кадр каждые {STEP_SECONDS:.0f} с; "
        f"дубли (почти одинаковые соседи, средняя разница пикселей < "
        f"{DUP_THRESHOLD}) удалены. Структура: `index.csv` (порядок кадров).\n"
    )
    path.write_text(content, encoding="utf-8")


def main() -> dict:
    threshold = SCENE_THRESHOLD0
    while True:
        summary = run_pipeline(threshold)
        if summary["n"] <= MAX_FRAMES or threshold >= 0.5:
            return summary
        threshold = round(threshold * 1.5, 3)


if __name__ == "__main__":
    main()
