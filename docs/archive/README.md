# Historical archive register

This folder is for reversible, indexed historical documentation. It is not a source of current client process truth. Do not unpack it into the active tree except during a reviewed restore.

| Archive | Original member | Reason | Verification | Restore |
| --- | --- | --- | --- | --- |
| `2026-10-13-history.zip` | `docs/plans/2026-10-01-0859-chore-soobshchenie-agentam-vypolnenie-plan.md` | Dated one-off plan, with no inbound filename/path reference found in tracked `docs/` at the archive decision. | ZIP member and CRC checked 2026-10-13. | `unzip -p docs/archive/2026-10-13-history.zip <member>` to inspect; restore through a reviewed Git change. |
| `2026-10-13-history.zip` | `docs/plans/2026-10-01-1544-chore-aktualizatsiya-hvosty-plan.md` | Dated one-off plan, same bounded reference check. | ZIP member and CRC checked 2026-10-13. | Same recovery route. |
| `2026-10-13-work-drafts/` (folder, not zipped) | 36 files; each keeps its original path under this folder prefix: `docs/process/parts/part-1.md`, `part-3.md`; `docs/process/work/cr3.md`, `f1-log.md`…`f4-log.md`; `specs/006-ispravlenie-kart/PLAN-e4.md`; `specs/006-ispravlenie-kart/kritika/e2-c1-1…4-*.md`, `e2-c2-1…2-*.md`; `specs/008-proverka-karty/blocks/` D, D1a, D1a1–3, D1b, D1c, D2a–c, E1a–d, E1c1–3, E1d1–2, E2, E3; `specs/009-voprosy-konfliktov/blocks/D.md` | Intermediate agent drafts and work logs of finished specs; no inbound filename reference in tracked files outside this folder (`git grep` 2026-10-13, atom eurosteklo-2o0.5). Files with inbound references (`kritika/c1-*`, `c2-*`, `blocks/povtor-*`) stay at their paths. | `git mv` only: 36 renames at 100% similarity, tracked file count unchanged. | `git mv docs/archive/2026-10-13-work-drafts/<original path> <original path>` |

ZIP SHA-256 on 2026-10-13: `3d0b12f76d90635dac9b353269ee02298e6e46b06608cd772c69f00c5dcb2dba`. `unzip -t` reported no errors. The two original paths were removed in the earlier local interim revision and are retained only as ZIP members on this branch.

The dated review records and the `docs/ppo/*/_parts/` audit records checked on 2026-10-13 still have inbound references. Keep them at their linked paths; classify them as historical or technical records in [the directory guide](../README.md), not as current client facts. The PPO builders, checkers, and page parts remain available for future edits. Private recordings, transcripts, answers, and CRM exports are outside this archive.
