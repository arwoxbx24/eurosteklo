# Client documents cross-check — 2026-10-13 (claude-5a83, atom eurosteklo-2o0.3)

Confidential. Sources of truth: client Word files received by the owner's links (INVENTORY § "Owner links received 2026-10-13").

## 1. Client answers: Word hsX vs otvety-klienta.md

Method: Word table cells (`unzip -p … word/document.xml`, cells split by `</w:tc>`, rows by `</w:tr>`) vs the answer column of the md table; `diff` of 18 rows each side (`wc -l` 18 / 18).

| Result | Rows |
| --- | --- |
| Identical characters | 13 of 18 (1, 2, 4, 5, 6, 7, 9, 10, 11, 13, 14, 16, 17) |
| Different characters, same meaning | 5 of 18 |

Differences (md vs Word):
- No. 3: Word "100 000" uses a no-break space (bytes `302 240`); md uses a normal space.
- No. 8: Word list items start with "-"; md uses "—" and adds ";".
- No. 12: md adds a space after "Сервиса.".
- No. 15: md adds ". " between "монтаж" and "По условиям".
- No. 18: md adds ";", "—" and "." between list items.
- Limit: Word paragraphs inside one cell are joined without a separator by this extraction, so part of the spacing differences in No. 8, 15 and 18 can come from the extraction; the added "—", ";" and "." cannot.

No figure, role, term or deadline differs. Falsification finding: the md header claimed "Ответы записаны дословно"; this is false at character level.

Correction: the md header is rewritten to state the real status and to name the Word file as the source of truth. The previous bytes are kept as `2026-10-08-client-answers/otvety-klienta.v1-2026-10-08.md` (sha256 8e758c6a…, equal to the registered SRC02 hash). New md hash: b8fa343c…. The answer table itself is unchanged.

## 2. Old TZ: Word 8uH vs client-materials/sanitized-tz.md

Method: Word `document.xml` text (tags and XML entities removed) and sanitized-tz.md lines 6–42, both with all whitespace removed; `wc -m` 7539 / 7539; `cmp` — no difference.

- The text is identical character for character (ignoring whitespace and line breaks).
- The 7 diagrams (word/media/image1–7.png) are not in the md, as its header says.
- Finding: the md header says "телефоны и e-mail удалены", but the Word text contains no phone or e-mail (grep for e-mail and phone patterns: no match; the docx has no header or footer parts). The statement is unsupported; nothing was removed.
- Date: docx part timestamps are 2025-06-19 (`unzip -l`). This is an INFERENCE for the document date, not proof of authorship date.

## 3. Root blank form

`Евростекло-уточнение-процесса.docx` (sha256 1d6e32b0…, 18 empty answer cells) was untracked in the project root. Moved without change into `2026-10-08-client-answers/blank-form-2026-10-06.docx`.

Result: docs_crosscheck PASS — 18/18 answers compared, 5 deviations logged and corrected in the header, old TZ text identical.
