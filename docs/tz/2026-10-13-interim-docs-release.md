# Interim Eurosteklo documentation release

## U1 — Owner-approved interim delivery

Owner decision: the 2026-10-13 conversation approved immediate publication of the checked HTML and archive with the maps' currentness explicitly UNVERIFIED. This release does not certify the full semantic content of either recording or every map claim.

Goal: make the reviewed navigation, historical-page notice, source-status report, folder guide, and safe historical archive available through the repository's normal delivery route.

Architecture: reuse the existing PPO generator, HTML pages, Git worktree, Beads atom, and `ship-post` local submission. No Bitrix24 write or new public object.

Allowed changes: `docs/ppo/build_all.py`, `docs/ppo/index.html`, `docs/ppo/ppo-eurosteklo.html`, `docs/ppo/ppo-evrosteklo.zip`, `docs/ppo/source-status.md`, `docs/README.md`, `docs/archive/2026-10-13-history.zip`, this passport, and removal of the two archived 1 October one-off plans. No client original, key, private export, or other session file may enter Git.

Ordered steps: (1) retain explicit UNVERIFIED currentness and classify docs; (2) archive only reference-free historical plans; (3) run the existing PPO check, browser link check, ZIP integrity/member check, and scoped diff/privacy check; (4) submit the accepted local change through `ship-post`.

Acceptance: `python3 docs/ppo/build_all.py && python3 docs/ppo/check_ppo.py --lidy` exits 0 and reports `итого: ошибок 0`; the browser reports six index links, two maps opened, and zero page errors; the ZIP check reports `AC3 members=2 exact=1 unsafe-members=0 originals-left=0 crc=PASS`; `git diff --check`, `git diff --cached --check`, and the scoped privacy scan exit 0 with zero tracked private paths. These checks prove a safe interim artifact, not semantic currency.

Completion: one successful `ship-post --submit` local commit and closure receipt for Beads atom `eurosteklo-re3`. Remote push, PR, CI, and merge require separate courier evidence.

Rollback: revert this scoped commit to restore the two plans and remove the ZIP and interim changes.
