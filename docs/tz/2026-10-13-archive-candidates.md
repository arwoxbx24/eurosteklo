# TZ: Eurosteklo archive candidates (atom eurosteklo-2o0.5, claude-5a83)

## U1 — read-only audit: list rarely used tracked files

Goal: produce a ranked list of tracked files in `/root/workspaces/projects/clients/eurosteklo` that can move into `docs/archive/` without breaking anything. Read-only: do not edit, move or delete any file.

Exploration: repowise / codebase-memory first, then `git` and `grep -n` on named files.

Scope: `git ls-files` only. Never candidates: `AGENTS.md`, `CLAUDE.md`, `README.md`, `PROJECT-STRUCTURE.md`, `.gitignore`, `.claude/**`, `.specify/**`, `client-materials/**`, `docs/archive/**`, `docs/ppo/index.html`, `docs/ppo/lidy/**`, `docs/ppo/sdelki/**`, `docs/ppo/_common/**`, `docs/ppo/build_all.py`, `docs/ppo/check_ppo.py`, `docs/meetings/variants/LINKS.md` and every file it lists, `docs/SOURCE-REGISTER.md`, `docs/README.md`, `docs/tz/**`, `specs/**/spec.md` of open work.

Rule: a file is a candidate only if ALL hold:
1. Its path (or file name) is referenced by no other tracked file outside `docs/archive/` (`git grep -n -F <name>`), and not by `docs/ppo/build_all.py` or any `_parts/*.py`.
2. Last commit touching it is before 2026-10-05 (`git log -1 --format=%ad --date=short -- <path>`).
3. It is not a client source and not a published link.

Output (stdout, Markdown table, max 80 rows): path | last commit date | inbound refs (0) | size bytes | reason it is low value (one phrase). Then one line: `candidates=<n> total_bytes=<n>`. Also list separately up to 10 files that fail only rule 1 because they are referenced solely from other candidates.

Principles: KISS, YAGNI; no code changes. Facts only from command output; unknown = UNVERIFIED.
