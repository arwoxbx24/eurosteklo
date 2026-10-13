# Eurosteklo directory contract delivery

## U2 — Structure, source locator, and archive classification

Owner direction: 2026-10-13. This unit documents where current and future Eurosteklo materials belong, preserves the existing HTML editing structure, and identifies the already compressed historical records. It does not certify the meaning of the lead/deal maps or decide DNS, Bitrix24, or 1C integration behavior.

Architecture: use the existing project `AGENTS.md`, `docs/README.md`, private receipt ledger, PPO builders, and ZIP archive. The root `PROJECT-STRUCTURE.md` is the single placement contract; `docs/SOURCE-REGISTER.md` is a non-confidential locator; `docs/archive/README.md` lists the archive members. No new runtime mechanism.

Allowed files: `AGENTS.md`, `PROJECT-STRUCTURE.md`, `docs/README.md`, `docs/SOURCE-REGISTER.md`, `docs/archive/README.md`, and this passport. The existing ZIP and PPO pages are read-only inputs. Client originals, CRM exports, tool settings, unrelated sessions, and other project files remain unchanged.

Ordered work: (1) confirm canonical source filenames and existing dependencies; (2) write the placement policy and locator; (3) classify historical records without moving referenced files; (4) independently check links, private boundary, ZIP integrity, PPO structure, and diff; (5) submit the accepted local revision through the guarded courier.

Acceptance: the four current key source files (latest dated Miro SVG, GR8 transcript, Hkb transcript, and answer file) are present and nonempty in the canonical private directory; all new local Markdown links resolve; `python3 docs/ppo/check_ppo.py --lidy` exits 0 with `итого: ошибок 0`; the two-member ZIP passes `unzip -t`; `git diff --check` passes; `git ls-files client-materials/private` is empty; no private material is added to Git. Independent review must not turn the transcript validation's `semantic_acceptance=false` into a process acceptance claim.

Completion: the guarded local `ship-post --submit` command creates one scoped commit and closes the own Beads atom with a SHA. Remote publication needs a separate courier receipt and is not inferred from local submission.

Rollback: revert this unit's scoped commit; the previous ZIP and PPO pages remain available unchanged.
