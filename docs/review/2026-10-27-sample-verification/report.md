# Выборочная проверка записей и расшифровок — 2026-10-27 (dcfg-kv8b5)

## Метод

ISO 2859-1, general inspection level II, single sampling. Lot = 32 files with a recorded SHA-256 in the private register `client-materials/private/INVENTORY.md`. Level II sample for lot 26–50 = 8 (source: https://qualityinspection.org/inspection-level/ — secondary summary; the standard table itself was not read). Selection: every 4th file in register order (positions 1, 5, 9, 13, 17, 21, 25, 29). Check = file exists; size equals the register where the register gives a size. No byte or hash re-check (the owner's request: no full re-check). Acceptance number: 0 failures.

## Записи встреч

| Запись | Файл | Размер, байт | Итог |
|---|---|---|---|
| Лиды (04.10) | 2026-10-04-dialogue/GR8/sharex-7tKKjc.webm | 114 344 595 | OK |
| Сделки (04.10) | 2026-10-04-dialogue/Hkb/sharex-KqTiK6.webm | 303 194 845 | OK |
| 1С (22.10) | Это наш диалог/sharex-usECm0.mp4 | 306 588 515 | OK |

Лиды = GR8, Сделки = Hkb — вывод по содержанию: слово «лид» 40 раз в GR8 и 3 раза в Hkb.

## Выборка из реестра

| № | Файл | Размер по реестру | Размер на диске | Итог |
|---|---|---|---|---|
| 1 | sharex-miOIdC.rar | 3 191 907 | 3 191 907 | OK |
| 5 | mindmaps/Евростекло (3).jpg | 73 148 | 73 148 | OK |
| 9 | transcription/eurosteklo-source.mp3 | 163 732 | 163 732 | OK |
| 13 | 2026-10-04-dialogue/transcripts/GR8/dialogue.txt | — | 80 094 | OK |
| 17 | 2026-10-13-owner-links/sharex-gBfNyB.docx | — | 1 669 402 | OK |
| 21 | analysis/codex-hooks-handoff-2026-10-06.md | — | 26 645 | OK |
| 25 | 2026-10-04-dialogue/delivery.html | — | 6 916 | OK |
| 29 | 2026-10-08-client-answers/blank-form-2026-10-06.docx | — | 39 707 | OK |

## Расшифровки

| Запись | Расшифровка | Движок | Объём | Покрытие | Итог |
|---|---|---|---|---|---|
| Лиды | transcripts/GR8/dialogue.txt | AssemblyAI (job completed) | 6 930 слов | длительность совпадает с записью в пределах 2 с (реестр, запись SRC05) | OK |
| Сделки | transcripts/Hkb/dialogue.txt | AssemblyAI (job completed) | 10 287 слов | в пределах 2 с (реестр, запись SRC06) | OK |
| 1С | assemblyai-7nd.json | AssemblyAI | 116 фрагментов | последний фрагмент 3 662 с при длительности видео 01:01:09 (3 669 с) | OK |
| Встреча 27.10 (ссылка b244.ru/cc5) | assemblyai-cc5.json | AssemblyAI (universal-3-5-pro) | 68 фрагментов, 3 говорящих, 1 549 слов | последний фрагмент 897 с при длительности медиа 903 с (замер инструмента транскрибации) | OK |

Расшифровка встречи 27.10 сделана 27.10. Видео (101 934 567 байт) и расшифровка сохранены в закрытой папке проекта вне Git и внесены в закрытый реестр. В Git — только итоги встречи.

TOTAL sample=8/32 files_ok=8 recordings_ok=3 transcripts_ok=4 FAIL=0
