# Current source locator

Inventory check: 2026-10-13 against the canonical directory `/root/workspaces/projects/clients/eurosteklo`, where all eight listed source files/directories existed. Private originals are intentionally absent from the isolated Git worktree. This file lists paths and verification state only; it does not reproduce confidential content or certify any process statement. The private `client-materials/private/INVENTORY.md` is the receipt ledger. `PROVEN` below means a nonempty file or directory was observed in the canonical directory, not that its content is correct or the latest client-approved version.

| Source group | Relative private path | File presence | Meaning/currentness |
| --- | --- | --- | --- |
| Latest locally dated Miro snapshot | `client-materials/private/miro-2026-10-08/board.svg` | PROVEN | UNVERIFIED; compare with client delivery and earlier export before claiming approval. |
| Earlier Miro export | `client-materials/private/miro/` | PROVEN directory | Historical version; retain for provenance. |
| Original CSV and five JPGs | `client-materials/private/mindmaps/` | PROVEN directory and matching files | UNVERIFIED against the later board and answers. |
| GR8 video and transcript | `client-materials/private/2026-10-04-dialogue/GR8/sharex-7tKKjc.webm`; `client-materials/private/2026-10-04-dialogue/transcripts/GR8/dialogue.txt` | PROVEN | UNVERIFIED semantics; transcript validation reports `semantic_acceptance=false`. |
| Hkb video and transcript | `client-materials/private/2026-10-04-dialogue/Hkb/sharex-KqTiK6.webm`; `client-materials/private/2026-10-04-dialogue/transcripts/Hkb/dialogue.txt` | PROVEN | UNVERIFIED semantics; transcript validation reports `semantic_acceptance=false`. |
| Client answers supplied through Roman | `client-materials/private/2026-10-08-client-answers/otvety-klienta.md` | PROVEN | Eighteen distinct `Q<number>` IDs counted on 2026-10-13; effects on every map point remain UNVERIFIED. |

The root private inventory names the answer file but did not contain the exact strings `miro-2026-10-08`, `transcripts/GR8`, or `transcripts/Hkb` in the 2026-10-13 check. The video batch has its own `INVENTORY.md` and `inventory.json` mentioning both transcript groups. Reconcile receipt details in the private ledger before a later task uses these as certified evidence; do not infer missing source content from this locator.

Owner-facing process pages: [lead HTML](ppo/lidy/karta-lidy.html), [deal HTML](ppo/sdelki/karta-sdelki.html), reached from [PPO index](ppo/index.html). Their claims require the separate media-to-claim verification task; see [source status](ppo/source-status.md).
