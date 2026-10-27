# Goal brief — claude-5a83 — Eurosteklo source integrity and structure (TZ in Word deferred)

<goal>Within this session, prove with labeled checks that every Eurosteklo input is preserved inside the project, registered and hash-verified; the two 04.10 transcripts match their recordings by method (identity, duration, coverage, untouched text); client documents are cross-checked character-level against the owner's Word sources with every deviation logged and corrected; Codex's finished work (aea6d2f) is regression-checked; rarely used files are archived inside the project with zero loss.</goal>

<context>
- FACT owner needs trustworthy inputs before the new TZ (owner msgs this session). The Word TZ itself is deferred by the owner ("Пока что мы уходим от формирования документа Word").
- FACT otvety-klienta.md claims "дословно" but 5 of 18 answers differ from Word hsX (diff output this session: answers 3, 8, 12, 15, 18; meaning unchanged).
- FACT root docx Евростекло-уточнение-процесса.docx = blank form, 18 empty answer cells (awk output this session); untracked, outside private/.
- FACT transcripts: GR8 audio_duration 3882 s, 6342 words; Hkb 6605 s, 9123 words; confidence 0.789 (jq on full.json); semantic acceptance not done (private/INVENTORY.md:13,49-50); speakers unassigned (2026-10-04-dialogue/INVENTORY.md:15).
- FACT Codex closed eurosteklo-l07 with commit aea6d2f (bd show; git log). Its review cites a "private claim ledger" and "private goal evidence log" (aea6d2f:docs/review/2026-10-13-source-certification.md); find for *claim* in project and its worktree returns nothing → INFERENCE: deleted by its cleanup (owner-pasted log: "GOAL_FILES_REMOVED=86", via python Path.unlink after rm deny).
- FACT Codex commit 762af7e removed 2 plans; both listed in docs/archive/2026-10-13-history.zip (unzip -l). Byte equality UNVERIFIED.
</context>

<inputs>Private sources under client-materials/private/ (INVENTORY.md); 4 owner links fetched to /tmp/claude-es-examples: hsX filled answers (sha 04a72425…), 8uH original old TZ docx (7fd5ed31…), 52X and 9x2 analyst examples (12e77a85…, ec5b240d…). Tools: sha256sum, ffprobe/ffmpeg, jq, unzip, diff, git, bd, safe-delete, code-channel, docs/ppo/build_all.py + check_ppo.py, tmux-send.</inputs>

<deliverables>
1. client-materials/private/2026-10-13-owner-links/ with the 4 files + INVENTORY rows (sha256).
2. client-materials/private/2026-10-13-verification/: registry-check.md, transcripts-check.md, docs-crosscheck.md, codex-check.md (private, not in git).
3. otvety-klienta.md corrected to Word bytes (or "дословно" claim removed) with change note; root blank docx moved into private/ (nothing deleted).
4. docs/archive/ additions + archive manifest (path, sha256, reason); project tree slimmer, nothing lost.
5. .goal/claude-5a83-evidence.log with AC lines.
</deliverables>

<constraints>In: clients/eurosteklo only. Out: Word TZ, portal/1C/Miro writes, publishing, push (ship-post courier only). No deletions: moves into archive only; any removal only via safe-delete with copy. Do not edit Codex's closed atom or branch; findings go as new bd issues. Originals' bytes never edited. Laws: no python -c/heredoc, code via code-channel.</constraints>

<user_touchpoints>None planned. No L2 installs (AssemblyAI is the only transcriber, owner decision). Archive moves are reversible (git/zip) → covered by owner standing authorization. Delivery to GitHub = courier, outside this session.</user_touchpoints>

<unknowns>
- Whether Codex claim ledger is recoverable (check .worktrees, refs/safe-delete, Trash) → step 4; if not, log as lost evidence, its 20 decisions re-derivable from source-status.md.
- Which files are "rarely used" → rule: not linked from docs/ppo/index.html, README, PROJECT-STRUCTURE, AGENTS.md and not touched since 01.10 → candidate; list before move.
- Old TZ docx vs sanitized-tz.md: diff expected only in removed phones/emails → step 3.
</unknowns>

<methods>
- Steps 2-3: Definition of Done + Given/When/Then (methodology SKILL.md:70,72) — each check has a labeled pass line.
- Step 4: 5 Whys (SKILL.md:48) on the deleted ledger — root cause in Codex cleanup procedure.
- Step 5: ADR (SKILL.md:60) — archive selection rule as a bd line.
</methods>

<plan>
1. Q1 Preserve owner links: place 4 files into private/2026-10-13-owner-links via tools/bin/place-files, add INVENTORY rows, verify sha256. L1. Me. ~5 calls.
2. Q1 [P track A] Registry + transcripts: hash every INVENTORY entry; list unregistered files; ffprobe duration vs audio_duration (±2 s); last utterance end vs duration; gaps >30 s with silencedetect; dialogue.txt rebuilt from full.json with jq and diff = 0. L1 (sha256sum, ffprobe, jq). Me. ~15 calls. Owns 2026-10-13-verification/registry-check.md, transcripts-check.md.
3. Q2 [P track B] Docs cross-check: Word hsX vs otvety-klienta.md (18 rows) → fix md to Word text; 8uH vs sanitized-tz.md; root blank docx → private/. L1 (unzip, diff, Edit for MD). Me. ~10 calls. Owns docs-crosscheck.md, otvety-klienta.md.
4. Q2 Codex check: build_all.py + check_ppo.py on main+aea6d2f state; history.zip members byte-equal to git blobs of 762af7e^; ledger-loss 5 Whys; bd issue (cross-contour, found-by:claude-5a83). Ask Codex via tmux-send only if its window is live. L1. Me. ~12 calls. Owns codex-check.md.
5. Q2 Archive: candidate list by rule, ADR line, move into docs/archive (git mv / zip with manifest), verify count+hash before = after. L1. Me (MD/moves) or code-channel if a script is needed. ~12 calls.
6. Q3 L1 Commit via ship-post --submit, then AC7 and final checks. ~4 calls.
Note: 52X and 9x2 are inputs for the deferred Word TZ; preserved only (AC1). Codex contact is a note in codex-check.md ("window live: Y/N, message sent: Y/N"), not an AC. md fix serves request (3), docx move serves request (5); Word sources never edited.
</plan>

<acceptance_criteria>
AC1 Given 4 owner links, When placed, Then 4 files in private/2026-10-13-owner-links with sha equal to fetched → `grep -c` → "AC1 links_preserved=4/4".
AC2 Given INVENTORY, When hashed, Then every mismatch or unregistered file is a row in registry-check.md and rows without reason=0 → "AC2 registry=PASS unexplained=0".
AC3 Given GR8,Hkb, When checked, Then |ffprobe−audio_duration|≤2 s, dialogue.txt rebuilt from full.json diff=0 (no additions), words/min logged and word counts equal INVENTORY (6342, 9123), every gap >30 s is a row with silencedetect result → "AC3 transcripts=PASS 2/2 unexplained_gaps=0".
AC4 Given hsX and 8uH, When diffed, Then md answers equal Word 18/18 (or "дословно" claim removed with note) and 8uH text minus phones/emails vs sanitized-tz.md diff empty → "AC4 docs_crosscheck=PASS 18/18".
AC5 Given aea6d2f/762af7e, When rebuilt and compared, Then check_ppo errors=0 and archive members byte-equal 2/2; ledger-loss bd issue id logged → "AC5 codex_check=PASS".
AC6 Given archive rule, When moved, Then files_before = files_live+files_archived and hash mismatches=0 → "AC6 archive_loss=0".
AC7 Given session end, When git status, Then no untracked client file outside private/ → "AC7 stray_client_files=0".
All final checks: grep -Fx '<line>' .goal/claude-5a83-evidence.log.
</acceptance_criteria>

<tests>Real runs on real private files only; 1 run per AC + 1 spare; total 14. No new test code.</tests>

<definition_of_done>All AC lines present in evidence log from real runs; nothing deleted (only moved/archived); own atom closed via ship-post; temp files in /tmp removed with safe-delete after copies verified.</definition_of_done>

<risks>
1. Archive moves break links in HTML maps → run check_ppo + link grep after step 5.
2. Codex ledger unrecoverable → logged as evidence loss, not hidden; affects trust in 18 UNVERIFIED rows only.
3. Webm hashes differ from INVENTORY (re-download) → log, do not overwrite.
Seen in other contour: Codex bypassed rm deny with python heredoc unlink (owner-pasted log) → bd issue in step 4.
</risks>
