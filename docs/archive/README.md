# Historical archive register

This folder is for reversible, indexed historical documentation. It is not a source of current client process truth. Do not unpack it into the active tree except during a reviewed restore.

| Archive | Original member | Reason | Verification | Restore |
| --- | --- | --- | --- | --- |
| `2026-10-13-history.zip` | `docs/plans/2026-10-01-0859-chore-soobshchenie-agentam-vypolnenie-plan.md` | Dated one-off plan, with no inbound filename/path reference found in tracked `docs/` at the archive decision. | ZIP member and CRC checked 2026-10-13. | `unzip -p docs/archive/2026-10-13-history.zip <member>` to inspect; restore through a reviewed Git change. |
| `2026-10-13-history.zip` | `docs/plans/2026-10-01-1544-chore-aktualizatsiya-hvosty-plan.md` | Dated one-off plan, same bounded reference check. | ZIP member and CRC checked 2026-10-13. | Same recovery route. |

ZIP SHA-256 on 2026-10-13: `3d0b12f76d90635dac9b353269ee02298e6e46b06608cd772c69f00c5dcb2dba`. `unzip -t` reported no errors. The two original paths were removed in the earlier local interim revision and are retained only as ZIP members on this branch.

The dated review records and the `docs/ppo/*/_parts/` audit records checked on 2026-10-13 still have inbound references. Keep them at their linked paths; classify them as historical or technical records in [the directory guide](../README.md), not as current client facts. The PPO builders, checkers, and page parts remain available for future edits. Private recordings, transcripts, answers, and CRM exports are outside this archive.
