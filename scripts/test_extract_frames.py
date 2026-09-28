from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import extract_frames as ef  # noqa: E402


def test_extract_frames():
    summary = ef.main()
    n = summary["n"]
    info = summary["info"]
    idx_path = ef.FRAMES / "index.csv"
    readme_path = ef.FRAMES / "README.md"

    pngs = sorted(ef.FRAMES.glob("*.png"))
    index_lines = idx_path.read_text(encoding="utf-8").count("\n")

    print(f"\nduration={info['duration']}s size={info['width']}x{info['height']} "
          f"fps={info['fps']}")
    print(f"scene threshold={summary['threshold']} "
          f"scene_frames={summary['scene_count']}")
    print(f"final_frames={n}")
    print(f"png_files={len(pngs)} (expect {n})")
    print(f"index_csv_lines={index_lines} (expect {n + 1})")
    print(f"README exists: {readme_path.exists()}")

    assert pngs, "no frames produced"
    assert 10 <= n <= 150, f"frame count {n} outside 10..150"
    assert index_lines == n + 1, f"index rows {index_lines} != frames+1 ({n + 1})"
    assert len(pngs) == n, f"png count {len(pngs)} != index frames {n}"
    assert readme_path.exists(), "README.md missing"

    # имена в index.csv соответствуют реальным файлам
    import csv
    with open(idx_path, newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    assert len(rows) == n
    files = {r["file"] for r in rows}
    assert files == {p.name for p in pngs}
    # времена не убывают
    times = [float(r["time_sec"]) for r in rows]
    assert times == sorted(times)
