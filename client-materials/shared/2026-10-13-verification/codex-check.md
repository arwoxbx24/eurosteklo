# Codex regression check (read-only), 2026-10-13

| # | Check | Command | Result | Verdict |
|---|---|---|---|---|
| 1 | Archive byte equality | blob id `git rev-parse 762af7e^:<path>` vs `git hash-object` of `unzip -p` output | plan 0859: 888e8c59...=888e8c59...; plan 1544: 549804de...=549804de... Equal 2/2. Note: the planned `git show > file` + sha256sum route gave an empty file for the git side (e3b0c442..., empty hash), so blob-id comparison was used instead (blob id = hash of exact bytes). | PASS |
| 2 | build_all.py change | `git show 762af7e -- docs/ppo/build_all.py` | Removed: (a) old per-process badges and descriptions in BLOCKS (replaced by BADGE "UNVERIFIED - source review pending"); (b) section "Лид и сделка - где граница" (7 bullets); (c) section "Основания и правила" (4 bullets). Replaced by one paragraph "Map source review ... incomplete". Removed text referenced `docs/ppo/00-resheniya-vladeltsa.md` and `client-materials/sanitized-*.md`: both still exist (ls). No code dependency removed, only HTML text. | PASS |
| 3a | Checker main | `python3 docs/ppo/check_ppo.py` | rc 1. errors 3, warnings 1. K9 errors: lidy/karta-lidy.html, obsledovanie-lidy-podrobno.html, obsledovanie-lidy.html "changed vs 21125b3 without --lidy". K5 warning 1 (layer A). | FAIL |
| 3b | Checker l07 worktree | `python3 /root/workspaces/projects/.worktrees/codex/eurosteklo-l07/docs/ppo/check_ppo.py` (script uses its own ROOT) | Identical: errors 3, warnings 1. | same as main |
| 4 | aea6d2f in main | `git merge-base --is-ancestor aea6d2f main` | exit 1 = not in main. Only on branch codex/eurosteklo-l07-source-cert (also worktree eurosteklo-l07). `git diff --stat 277a349 aea6d2f`: 11 files, 57+/29-. | info |
| 5 | Ledger recovery | `git for-each-ref refs/safe-delete`; `find .worktrees/codex -name '*claim*'`; `find /tmp -maxdepth 3 -name '*01a134e5*'`; `find ... -name 'codex-01a134e5*'` | safe-delete refs: none. `*claim*` hits belong to unrelated dcfg-* worktrees (claim_ledger.py, tz docs), none is codex-01a134e5-claims.json. /tmp hit: dir /tmp/hook_outputs/01a134e5-c247-7790-86a1-1801d5768d1e with 3 hook-output .txt files (18465 bytes each); not the ledger/evidence log (content not opened). `codex-01a134e5*` search in codex worktrees and eurosteklo: 0 files. | no copy found |
| 7 | Codex reply | `ls client-materials/private/2026-10-13-verification` | contains registry-check.md, transcripts-check.md; no codex-deleted-files.md. Codex reply: pending | pending |

Notes on check 3: K9 compares lidy pages to base 21125b3. Lidy pages were already changed after that base by merged PRs (`git log 21125b3..main -- docs/ppo/lidy/karta-lidy.html`: 70adbef #39, f8aca37 #37, 0de477d #21). So the 3 errors are not shown to originate from Codex commit 762af7e; the stale base in docs/CHECKPOINTS.md is the likely cause (inference, base update not tested). Criterion as set by contract still fails: errors 3 on main.

## 5 Whys (ledger loss, facts only)

1. Why is the private claim ledger / evidence log absent? No file codex-01a134e5-* found in worktrees, project or /tmp, and no refs/safe-delete ref.
2. Why no copy? Per brief, Codex deleted 86 .goal files with Path.unlink; safe-delete refs (the sanctioned backup route) are absent, so deletion did not go through safe-delete. (Brief fact; the unlink call itself not observed here.)
3. Why did it use Path.unlink? Per brief, `rm` was denied; Codex chose another form of the same goal (permission-routes.md: second form = bypass) instead of `tools/bin/safe-delete`.
4. Why was the ledger cited in a review without being in git? docs/review/2026-10-13-source-certification.md (aea6d2f) cites private files under client-materials/private, which is not tracked in git (project CLAUDE.md), so no git history to restore from.
5. Why no safeguard? No gate verified that a cited evidence artifact exists or is backed up before deletion (not verified in code; hypothesis).

Codex reply: pending

Codex regression: FAIL archive_equal=2/2 checker_errors=3 ledger_recovered=no
