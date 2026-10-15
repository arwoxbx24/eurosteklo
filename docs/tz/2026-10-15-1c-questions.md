# TZ: Eurosteklo 1C developer question pack (atom eurosteklo-xeb, claude-7934)

## U1 — question pack for the client's 1C developer from the 1C call transcript

Goal: one Russian document `docs/meetings/2026-10-15-1c-call/voprosy-1c-razrabotchiku.md` for Vitaly (Eurosteklo-side developer) built from the 1C call transcript (owner link https://b244.ru/rvY, private copy `client-materials/private/2026-10-15-1c-call/transcript.txt`, git-ignored).

Sections: Цель диалога, Финиш диалога, Сага, Итоги, Участники, Порядок действий, Вопросы разработчику 1С (Dmitry's 8 questions expanded plus unanswered or weakly answered points; each with Цель, Где смотреть, Что прислать, Статус ответа), Документы, Согласованность (20 rows of `docs/meetings/2026-10-04-dialog/svod.tsv` that mention 1С: consistent / contradicts / new), Критика (owner's questions), Фиксация (last).

Method: three independent blocks written in parallel (eurosteklo CLAUDE.md, law of splitting), merged mechanically. Every answer, fact and verdict line carries PROVEN, INFERRED or UNVERIFIED (AGENTS.md:54) with a transcript time code.

Out of scope: full TZ (owner: not now), Bitrix portal access, edits of svod.tsv and closure.tsv, messages to the client.

Acceptance: section, question and label counts by `grep -c` as listed in atom eurosteklo-xeb.

## U2 — Word file per participant (atom eurosteklo-7ti)

Goal (owner 15.10: "формат Word, для каждого специалиста свой файл"): four `.docx` files in `docs/meetings/2026-10-15-1c-call/` built from the U1 document: Виталий (technical 1C questions В1–В6, В9–В12, В14, В15, В17, В19–В23), Роман (В7, В8, В13, В16, В18, В23), Дмитрий (work sheet, his questions В1–В8 and internal notes), Андрей (overview, own tasks, В3, В11, В23, consistency and critique).

Method: four parallel blocks write one Markdown file each, questions copied verbatim; `pandoc` 3.1.3 converts Markdown to `.docx`. Internal sections (critique, consistency) go only to the ARWOX files (Дмитрий, Андрей).

Acceptance: four `.docx` read back by `pandoc -t plain` with rc 0; every question В1–В23 present in at least one file; each file has the headings Кому and Цель.

## U3 — client files without internal assessment (atom eurosteklo-edm)

Defect of U2: the client files for Виталий and Роман carried internal "Статус ответа" lines (18 and 6), evidence labels PROVEN/INFERRED/UNVERIFIED (66 and 38) and one assessment of Roman's answer. Fix: drop those lines and labels from the two client files only, keep every question, purpose, where to look and what to send; ARWOX files (Дмитрий, Андрей) keep the labels and stay byte-identical.

Acceptance: both client `.docx` read back by `pandoc -t plain` show status=0, labels=0, questions 18 and 6; ARWOX `.docx` unchanged against commit 619f064.

## U4 — clean business text in all four Word files (atom eurosteklo-rdy)

Defect of U2/U3 (owner 15.10): all four `.docx` still carried time codes (40–86 per file), question prefixes В<n>, row codes D<n>, "Источник:" lines, labels, speaker numbers, paths and ids, plus "Где смотреть" hints that may mislead a 1C developer. Fix: rewrite all four files under the same names (no new links): plain-digit numbering, per question "Вопрос", "Что описать или прислать" and an empty "Ответ:" field; the Andrey critique says per point "прав / не прав / прав частично" and what to correct. The project rule is added to `CLAUDE.md`. Method: four parallel blocks, one file each; `pandoc` 3.1.3 converts Markdown to `.docx`.

Acceptance: `pandoc -t plain` of each `.docx` shows time codes=0, labels=0, "Источник"=0, "Спикер"=0, paths/ids=0, prefixes=0, "Где смотреть"=0; "Ответ:" fields 18/6/8/3 (Виталий/Роман/Дмитрий/Андрей); Andrey critique has ≥1 "прав".
