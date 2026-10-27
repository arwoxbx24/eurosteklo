# Registry check — 2026-10-13 (claude-5a83, atom eurosteklo-2o0.2.1)

Confidential. Read-only check of `client-materials/private/` against `INVENTORY.md` and `2026-10-04-dialogue/INVENTORY.md`.

## Hash check (sha256sum, run from client-materials/private)

| Entry | Expected (register) | Disk | Result |
| --- | --- | --- | --- |
| sharex-miOIdC.rar | 130e4002… | 130e4002… | PASS |
| mindmaps/sharex-win-ifBLjU.mp4 | 31e9834a… | 31e9834a… | PASS |
| mindmaps/Евростекло (1).jpg | 888a59ee… | 888a59ee… | PASS |
| mindmaps/Евростекло (2).jpg | a96ced8b… | a96ced8b… | PASS |
| mindmaps/Евростекло (3).jpg | b5153f9e… | b5153f9e… | PASS |
| mindmaps/Евростекло (4).jpg | e2e4d1c3… | e2e4d1c3… | PASS |
| mindmaps/Евростекло.csv | 669e7013… | 669e7013… | PASS |
| mindmaps/Евростекло.jpg | c7885377… | c7885377… | PASS |
| transcription/eurosteklo-source.mp3 | 5bd5636e… | 5bd5636e… | PASS |
| transcription/eurosteklo-transcript.txt | e3b0c442… (empty) | e3b0c442… | PASS |
| SRC01 miro-2026-10-08/board.svg | 74fa7e3d… | 74fa7e3d… | PASS |
| SRC02 2026-10-08-client-answers/otvety-klienta.md | 8e758c6a… | 8e758c6a… | PASS |
| SRC05 transcripts/GR8/dialogue.txt | 30c39ad8… | 30c39ad8… | PASS |
| SRC06 transcripts/Hkb/dialogue.txt | 1e333024… | 1e333024… | PASS |
| sct/sharex-PHr1YX.md | 7428a60a… | 7428a60a… | PASS |
| GR8 webm | 3fcde9c1… | 3fcde9c1… | PASS (transcripts-check.md) |
| Hkb webm | 12ec85a6… | 12ec85a6… | PASS (transcripts-check.md) |
| 2026-10-13-owner-links (4 docx) | rows added today | equal to independent fetch | PASS |

Mismatches: 0 of 21.

## Directory counts

| Directory | Register | Disk | Result |
| --- | --- | --- | --- |
| b24-export/ | 26 files | 26 | PASS |
| miro/ | 5 files | 5 | PASS |
| video-portal/ | 2 files (mp4, srt) | 2 | PASS |
| video-portal/frames/ | 37 files | 37 | PASS |

## Items without a register row (found on disk)

15 items (1 SOURCE, 14 DERIVED). Each is now a row in `INVENTORY.md` § "Registry reconciliation 2026-10-13" with hash or file count and class. Unexplained items: 0.

## Limits

- Hash equality proves the bytes are unchanged since registration; it does not prove the meaning of a source.
- `otvety-klienta.md` is not verbatim against the client Word file (see docs-crosscheck.md); its hash is kept unchanged on purpose.
