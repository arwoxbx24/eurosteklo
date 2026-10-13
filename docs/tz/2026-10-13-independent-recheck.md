# TZ: independent re-check of Eurosteklo source verification (epic eurosteklo-2o0, claude-5a83)

## U1 — read-only re-check of claims AC1–AC4

Goal: independently confirm or refute four claims by running your own commands. Read-only: do not edit, move or delete any file; temp output only under /tmp/oc-5a83-*. Confidential: never print client text longer than 40 characters.

Exploration: repowise not needed (data files); use sha256sum, unzip, jq, ffprobe, diff, cmp, wc, grep.

Base: /root/workspaces/projects/clients/eurosteklo/client-materials/private (P).

Claims to check:
1. AC1: P/2026-10-13-owner-links has 4 .docx whose sha256 begin 04a72425, 7fd5ed31, 12e77a85, ec5b240d, and each appears in P/INVENTORY.md.
2. AC2: every 64-hex SHA-256 in P/INVENTORY.md and P/2026-10-04-dialogue/INVENTORY.md matches the file it names (resolve paths relative to P or the batch folder; GR8/Hkb webm names are in inventory.json). Report matched/total and any mismatch.
3. AC3: for P/2026-10-04-dialogue GR8 (GR8/*.webm) and Hkb (Hkb/*.webm): ffprobe duration vs transcripts/<id>/full.json .audio_duration within 2 s; .words|length equals 6342 (GR8) and 9123 (Hkb); max gap between consecutive .utterances (start − previous end) in ms.
4. AC4: (a) client Word P/2026-10-13-owner-links/sharex-Eirzsk.docx has 18 numbered answer rows, all non-empty; (b) Word P/2026-10-13-owner-links/sharex-QmZYdE.docx document text with all whitespace removed equals ../sanitized-tz.md lines 6–42 with all whitespace removed (cmp); (c) P/2026-10-08-client-answers/otvety-klienta.v1-2026-10-08.md sha256 begins 8e758c6a.

Output (stdout, max 30 lines): one line per claim: `C<n> CONFIRMED|REFUTED — <measured values>`, then any discrepancy in full. Facts only from command output; unknown = UNVERIFIED.
