# Transcripts check (2026-10-13)

Base: client-materials/private/2026-10-04-dialogue. No transcript text recorded here. Intermediate files: /tmp/claude-5a83-s2b-gr8.txt, /tmp/claude-5a83-s2b-hkb.txt.

## GR8 (GR8/sharex-7tKKjc.webm)

| # | Check | Command | Measured | Result |
|---|-------|---------|----------|--------|
| 1 | SHA256 = INVENTORY.md:7 | `sha256sum GR8/sharex-7tKKjc.webm` | 3fcde9c1535f295698c82b30f71993e33be1c492f92cbc1f86dba5c7ab531060 (identical) | PASS |
| 2 | duration vs audio_duration, <= 2 s | `ffprobe -v error -show_entries format=duration -of csv=p=0` | 3881.337 vs 3882; diff -0.663 s | PASS |
| 3 | coverage | `jq .utterances[0].start / [-1].end` | first 7270 ms, last end 3877658 ms; tail 3.679 s before end | PASS (info) |
| 4 | word count = INVENTORY (6342); words/min | `jq '.words\|length'` | 6342; 98.04 words/min | PASS |
| 5 | rebuilt dialogue vs dialogue.txt | jq template `[start–end] Speaker X: text` then `diff` | 196 utterances; 0 content differences; only diff: dialogue.txt has no newline at EOF (line 196) | PASS |
| 6 | gaps > 30000 ms | jq over consecutive utterances | 0 gaps; max gap 27026 ms (n=195); ffmpeg silencedetect not needed | PASS |
| 7 | confidence | `jq .confidence`; words with confidence < 0.5 | 0.78896666; 374 of 6342 words < 0.5 | info |

## Hkb (Hkb/sharex-KqTiK6.webm)

| # | Check | Command | Measured | Result |
|---|-------|---------|----------|--------|
| 1 | SHA256 = INVENTORY.md:9 | `sha256sum Hkb/sharex-KqTiK6.webm` | 12ec85a66628d4b0386737aa4c9fc5b93893526f6b7e23218406ca20cc8e9097 (identical) | PASS |
| 2 | duration vs audio_duration, <= 2 s | `ffprobe -v error -show_entries format=duration -of csv=p=0` | 6604.943 vs 6605; diff -0.057 s | PASS |
| 3 | coverage | `jq .utterances[0].start / [-1].end` | first 2242 ms, last end 6590561 ms; tail 14.382 s before end | PASS (info) |
| 4 | word count = INVENTORY (9123); words/min | `jq '.words\|length'` | 9123; 82.87 words/min | PASS |
| 5 | rebuilt dialogue vs dialogue.txt | jq template then `diff` | 388 utterances; 0 content differences; only diff: no newline at EOF (line 388) | PASS |
| 6 | gaps > 30000 ms | jq over consecutive utterances | 0 gaps; max gap 16293 ms (n=387); ffmpeg silencedetect not needed | PASS |
| 7 | confidence | `jq .confidence`; words with confidence < 0.5 | 0.7886422; 540 of 9123 words < 0.5 | info |

## Gaps table

| Recording | Gap start (ms) | Gap end (ms) | Length (ms) | Silence ratio | Explained |
|-----------|----------------|--------------|-------------|---------------|-----------|
| GR8 | none > 30000 ms | - | - | - | - |
| Hkb | none > 30000 ms | - | - | - | - |

Scope limits (UNVERIFIED): this check proves file identity, duration, counts and dialogue.txt = full.json. It does NOT prove that the words match what was spoken (no audio comparison done). Utterance gaps <= 30 s were not checked with silencedetect. Low-confidence words (374 / 540) mean accuracy of wording is not established.

GR8 result: PASS unexplained_gaps=0
Hkb result: PASS unexplained_gaps=0
