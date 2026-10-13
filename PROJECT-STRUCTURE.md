# Eurosteklo directory contract

Owner direction: 2026-10-13. Scope: documentation and classification in this project. This contract routes files; it does not approve client process claims, Bitrix24 changes, or publication. The current owner instruction and `AGENTS.md` control if a conflict arises. The source locator is [docs/SOURCE-REGISTER.md](docs/SOURCE-REGISTER.md); the documentation entry point is [docs/README.md](docs/README.md).

## Operating boundary

1. Keep client originals, recordings, CRM exports, answers, and any personal data under `client-materials/private/`. Do not commit or publish them. Preserve received bytes. Record receipt date, origin, exact relative path, confidentiality, and checksum in the private `INVENTORY.md` before using a new source as evidence.
   Private originals live in the canonical client directory; an isolated Git worktree may intentionally omit them. Verify source presence in the canonical directory without copying originals into the worktree.
2. Keep derived, publishable documentation under `docs/`, with a date, source locator, and `PROVEN`, `INFERRED`, `UNVERIFIED`, or `CONTRADICTED` status for material claims. A file's presence proves only its presence. An unanswered or contradictory point cannot become an accepted technical requirement.
3. Current work is documentation only. DNS verification, semantic certification of the lead/deal maps, integration implementation, Bitrix24/1C writes, and deployment are separate owner-authorized tasks.
4. Owner-reported context (2026-10-13): organize future analysis around Bitrix24. The owner reports the client currently uses Bitrix24 cloud Professional and a 1C connector. The exact 1C application, including whether it is UNF, is `UNVERIFIED`. Do not infer connector behavior, cloud/box parity, fields, or a deployment requirement from this note.

## Stable locations

| Material or output | Location and rule |
| --- | --- |
| Latest dated Miro snapshot | Keep the received/exported files under `client-materials/private/miro-YYYY-MM-DD/`; the locally present dated snapshot is `miro-2026-10-08/`. Keep the earlier `miro/` export as a separate historical source. Register each version; a later filename does not certify its meaning. |
| Received CSV and JPG map material | Keep original bytes in `client-materials/private/mindmaps/`; use them as cited inputs, not as editable working documents. |
| Received videos and transcripts | Keep each received batch in `client-materials/private/YYYY-MM-DD-<batch>/`, with recording identifiers and `transcripts/<recording-id>/`. Keep validation receipts beside the transcript. A transcript is a locator until semantic review passes. |
| Received Word, DOC, PDF, Google Docs export, or other client file | Store the received/exported original under `client-materials/private/incoming/YYYY-MM-DD/` with its original filename; record its source URL or sender privately when supplied. Put an edited summary only in the appropriate `docs/` area, linked to the original inventory entry. Do not create an empty intake folder in advance. |
| Client answers and meeting evidence | Store received answers in a dated private batch; route derived meeting notes to `docs/meetings/`. Do not copy answer text into a public registry. |
| Pre-project survey (PPO) | `docs/ppo/` is the working survey area. The owner-facing lead and deal process maps are HTML pages at `docs/ppo/lidy/karta-lidy.html` and `docs/ppo/sdelki/karta-sdelki.html`. Their survey pages and source parts stay within those same `lidy/` and `sdelki/` trees; shared page parts stay in `docs/ppo/_common/`. |
| Current state and process synthesis | `docs/as-is/` records the observed state; `docs/process/` and `docs/business-processes/` hold derived process descriptions. Every assertion cites private evidence. Do not treat a draft process as client-approved. |
| Technical assignments | Existing assignments stay in `docs/tz/` to preserve links. For new work, use `docs/tz/client/` for a client-readable, approval-ready assignment and `docs/tz/developer/` for an implementation-ready assignment; both trace to the same accepted process points and identify their audience. Create those subfolders only when the first real document exists. |
| Decisions, specifications, handoff | Durable repository/process rules go in `docs/specifications/`; proposed solutions in `docs/solutions/`; an actual delivery packet in `docs/package/`. `packet/` and `is/` are not canonical directory names. |
| Work records | `docs/research/`, `docs/review/`, `docs/plans/`, and `docs/idei/<agent>/` are dated technical records, not client truth. Agent ideas remain in their owner's folder. `docs/archive/` holds indexed historical files only. |
| Reusable local tools | Keep existing `scripts/` source-extraction and read-only export tools outside the documentation archive while their use is unresolved. Keep the PPO builders and checkers beside their page parts. Classify a script by actual callers and purpose before archiving it. |

## Survey-to-assignment route

For each lead or deal point: register the received source; place a dated finding or question in the relevant PPO tree; distinguish observation, interpretation, contradiction, and unanswered question; update the HTML page from its maintained parts; run the existing PPO build/check; obtain the required review and client approval before promoting a point to a client or developer assignment. A future client assignment and developer assignment may differ in detail, but must refer to the same approved point and source. The two HTML pages are navigation and working maps; overall semantic currentness remains `UNVERIFIED` until the separate source-certification task passes.

## Paths that must stay stable

Keep `client-materials/private/` isolated, the two HTML page URLs above stable, `docs/ppo/index.html` as the entry page, `docs/ppo/_common/` and each map's `_parts/` as maintained build inputs, and existing linked legacy paths stable. `docs/ppo/ppo-eurosteklo.html` is a dated standalone page, not the current lead/deal source. Keep `docs/ppo/build_all.py` and its called builders/checkers available for later HTML edits. Do not archive a script solely because it is old.

To change an allowed path: identify its owner and all inbound references with `git grep`; confirm whether a builder consumes it; preserve the previous version in Git or an indexed archive; move the file and update links, inventory, guide, and build inputs in the same change; then run the affected build, link check, archive CRC, and privacy check. Do not relocate a private original merely to simplify a public tree. If its path must change, make that a separate approved migration with identical-byte/hash verification and an updated private inventory.

## Archive and extension rule

Archive a file only after classifying it as historical, confirming no active build input or inbound link depends on its path, checking for protected/private data, and recording the original path, reason, date, archive path, and recovery command in [docs/archive/README.md](docs/archive/README.md). Use one compressed ZIP for a coherent historical batch; verify its member list and CRC before removing any tracked source. Never archive private originals, current HTML parts/scripts, or referenced records merely because they look noisy. Referenced history stays in place but is labelled historical in the guide.

New material types may get a new dated subfolder when an actual file arrives. Add one row here and in the source locator, state its owner and confidentiality, and check whether an existing folder already fits. Do not invent a new top-level directory for a single draft or duplicate a source of truth. This gives agents room to extend the structure without silently changing its protected paths.

Method note: this separates source/reference, working survey, assignments, and historical records using the existing repository layout. Diataxis distinguishes reference, how-to, explanation, and tutorial content (https://diataxis.fr/); this project adopts the separation principle without creating four extra trees.
