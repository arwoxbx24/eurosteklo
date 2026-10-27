# Реестр входного пакета

- Получено: 2026-09-28
- Источник: `https://b244.ru/Npe`
- Режим: конфиденциально, Git и публикация запрещены
- Проверка архива: `unrar` — `All OK`
- Содержание не анализировалось
- Дополнительный источник (этап агрегации): выгрузка Битрикс24 интегратора (`b24-export/`), 2026-09-28
- Дополнительные источники (этап агрегации), получены 2026-09-28, конфиденциально: `miro/` (доска Miro, read-only), `video-portal/` (запись экрана портала: mp4, srt, кадры)

| Файл | Тип | Размер | SHA-256 |
|---|---|---:|---|
| `sharex-miOIdC.rar` | RAR v4 | 3 191 907 | `130e4002fc9cbf8cece02981e39d5f85837a188260d9d2d84d01db631432cb77` |
| `mindmaps/sharex-win-ifBLjU.mp4` | MP4 | 3 030 057 | `31e9834a729b077e1430e33db8fbc3d10c3b8f25bd4c913406ab021e07bab6cb` |
| `mindmaps/Евростекло (1).jpg` | JPEG | 79 254 | `888a59eefd237a9ae801ea26c6d73f233b604c967e81b5cba2b96dbeaffe7bac` |
| `mindmaps/Евростекло (2).jpg` | JPEG | 94 320 | `a96ced8b846766806d84c8d2116f962ab6a20c56d4b49345f42ba250b9a5c5ee` |
| `mindmaps/Евростекло (3).jpg` | JPEG | 73 148 | `b5153f9e2974563432e59a7236ad41bedfd457c011bc2474e27555841496d798` |
| `mindmaps/Евростекло (4).jpg` | JPEG | 85 897 | `e2e4d1c3ee9ea579fdb1626a2518f0d0b72a583a0532ece8060a6f1050d7a63f` |
| `mindmaps/Евростекло.csv` | UTF-8 CSV | 5 299 | `669e70136e232b65f096d6c9dce4fa995fe9c40a63db4ed79d929b364b1a8843` |
| `mindmaps/Евростекло.jpg` | JPEG | 77 398 | `c78853771af3e36b80e3450988557cd0ddd35504019a426e2cf685b59c3ccbdc` |
| `transcription/eurosteklo-source.mp3` | MP3, без слышимого сигнала | 163 732 | `5bd5636e651d927bc2c1caa5296b3032abb71b5b4a64ca86c2996d60e80da383` |
| `transcription/eurosteklo-transcript.txt` | UTF-8, пустой результат AssemblyAI | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `b24-export/` (каталог) | Выгрузка Б24 интегратора; получено 2026-09-28, источник: выгрузка Б24 интегратора, конфиденциально | 26 файлов (фактический счёт на 28.09.2026) | — |
| `transcription/STATUS.md` | Статус транскрибации (речь отсутствует) | — | — |
| `miro/` (каталог) | Выгрузка доски Miro read-only: nodes.csv (73 узла), edges.csv (25 связей), comments.json (31 комментарий), board.svg, README.md; получено 2026-09-28, источник: доска Miro, конфиденциально | 5 файлов | — |
| `video-portal/` (каталог) | Запись экрана портала: sharex-xDNm1l.mp4 (20,9 МБ), sharex-xDNm1l.srt; получено 2026-09-28, источник: клиентская запись экрана портала, конфиденциально | 2 файла (mp4 и srt) | — |
| `2026-10-08-client-answers/otvety-klienta.md` | Ответы клиента на 18 вопросов формы уточнения процесса (`docs/review/2026-10-05-consistency/utochneniya.html`); получено 2026-10-08 от владельца, конфиденциально | 18 ответов | — |
| `video-portal/frames/` (каталог) | Кадры записи экрана: frame_0001…frame_0035.png, index.csv, README.md; получено 2026-09-28, источник: клиентская запись экрана портала, конфиденциально | 37 файлов (35 кадров) | — |

## Observed source hashes for semantic review (2026-10-13)

These SHA-256 values identify the local bytes observed on 2026-10-13; they do not establish client approval or an unrecorded receipt date. All entries are confidential.

| Source ID | Private relative path | Observed SHA-256 | Receipt date |
| --- | --- | --- | --- |
| SRC01 | miro-2026-10-08/board.svg | 74fa7e3d92986681668ba6c9280905f10f0a6942d1667039273ad75baa1d92d5 | UNVERIFIED in existing inventory |
| SRC02 | 2026-10-08-client-answers/otvety-klienta.v1-2026-10-08.md (these bytes were at otvety-klienta.md until the 2026-10-13 header correction; current file hash in "Registry reconciliation" below) | 8e758c6af8309f3e7590b28323f5334bcaf635223b0e148160f286472742ed73 | UNVERIFIED in existing inventory |
| SRC05 | 2026-10-04-dialogue/transcripts/GR8/dialogue.txt | 30c39ad8a81bf56e9bee46135f5569da7e4227f39966425260d04a075b44f0f3 | UNVERIFIED in existing inventory |
| SRC06 | 2026-10-04-dialogue/transcripts/Hkb/dialogue.txt | 1e33302469b51636b91f6140a7470f6a2c1fda7d894cbffa13e903c9d5f31611 | UNVERIFIED in existing inventory |

## Provenance correction for observed source hashes (2026-10-13)

This correction supersedes the blanket receipt-date label in the preceding observed-hash table. It certifies local version linkage only, not client approval of process meaning.

| Source ID | Local provenance | Limit |
| --- | --- | --- |
| SRC01 | Dated 2026-10-08 Miro export and source URL in miro-2026-10-08/DIFF.md; local file timestamps agree. | Client approval and exact receipt event remain UNVERIFIED. |
| SRC02 | Existing private inventory entry for the answer file contains 2026-10-08; local file timestamps agree. | The answers still require claim-by-claim review. |
| SRC05 | GR8 transcript job ID matches its full result; audio duration matches the inventoried recording within two seconds. | Transcript semantic acceptance remains false; it is a derived locator. |
| SRC06 | Hkb transcript job ID matches its full result; audio duration matches the inventoried recording within two seconds. | Transcript semantic acceptance remains false; it is a derived locator. |

## Owner links received 2026-10-13 (claude-5a83)

Fetched with `tools/scripts/pm2/b244-fetch.sh` into `2026-10-13-owner-links/`; SHA-256 equals an independent earlier fetch the same day. Confidential.

| Link | File | Content | SHA-256 |
| --- | --- | --- | --- |
| https://b244.ru/hsX | sharex-Eirzsk.docx | Client-filled form "Евростекло — уточнение процесса", 18 answers | 04a72425f494d2deb31e715eb153996dddf93c0e7a12b7182817e68317793094 |
| https://b244.ru/8uH | sharex-QmZYdE.docx | Original old Eurosteklo TZ (Word, with diagrams) | 7fd5ed31d0cfbbeeb1465a2c5ada39175c0d6d0406757017322ce5d71016e94b |
| https://b244.ru/52X | sharex-gBfNyB.docx | Analyst TZ example (hotel booking), format reference for the deferred Word TZ | 12e77a85af3c3becabd5e595c7cf49a3116eea09576de725b0eba5f1d13cef85 |
| https://b244.ru/9x2 | sharex-2J1imH.docx | Analyst TZ example (employee hiring), format reference for the deferred Word TZ | ec5b240d2aac626db453a112513cad036c6fa13fedeab32b1d9f6323dea4d45a |

## Registry reconciliation 2026-10-13 (claude-5a83)

All 15 hashed entries above (RAR, 7 mindmap files, 2 transcription files, SRC01, SRC02, SRC05, SRC06, sct) match the disk. Items found on disk without a register row are registered here. Class: SOURCE = client-originated; DERIVED = produced by agents from sources (not evidence by itself).

| Path | Class | SHA-256 or file count |
| --- | --- | --- |
| sotrudniki-fio.md | SOURCE (client "сотрудники" file, names and roles; header states its origin) | 26e6921ba03a6c24407fadcf91c3c605ceef4fb8a5b6110151046c286edb0196 |
| opencode-audit.txt | DERIVED | 91b093af62c5a3331cab17587b72e25c0cf41f0e0d64df1412cda15e0a9251db |
| analysis/codex-hooks-handoff-2026-10-06.md | DERIVED | 27fefc81ddef187dbdae41d18ab21b6e42f6fc2d94f31c894e1bbde374e9c4ca |
| analysis/evidence-crv8.sqlite3 | DERIVED | 8bc5861926eca3a419856d96625760aacf4a34b42eed9006e2e86079fd3bd872 |
| analysis/delivery-crv10/ | DERIVED | 14 files |
| analysis/yandex-crv9/ | DERIVED | 4 files |
| miro-2026-10-08/TZ-codex-check.md | DERIVED | 80e3941144e6e67e1ee54145845eb329a9e006313df88c48084ef289be00da4c |
| 2026-10-04-dialogue/research.md | DERIVED | 6b43ecedb9c50a4946a1e4304670b9f1c839f691bf434cae4b6307524ccb8779 |
| 2026-10-04-dialogue/delivery.html | DERIVED | 7ed20abcbef97be0752ac4624da7f1474e56d31bb0cd1988233b073f707a5b81 |
| 2026-10-04-dialogue/inventory.json | DERIVED (batch register) | 8e1c485ecfcb54a4be50177e5fabcd151cc7cf4a4457485ef894ad692fe5c5c0 |
| 2026-10-04-dialogue/comparison/ | DERIVED | 2 files |
| 2026-10-04-dialogue/evidence/ | DERIVED | 16 files |
| 2026-10-04-dialogue/sverka/ | DERIVED | 16 files |
| 2026-10-04-dialogue/transcripts-tools/ | DERIVED | 4 files |
| 2026-10-13-verification/ | DERIVED (claude-5a83 checks) | check reports |
| 2026-10-08-client-answers/otvety-klienta.md | DERIVED (SRC02, header corrected 2026-10-13: not verbatim vs Word hsX) | b8fa343cd4db96163c4be5ade714957d9a493ccec854e00c7948b8c8882f7026 |
| 2026-10-08-client-answers/otvety-klienta.v1-2026-10-08.md | DERIVED (SRC02 bytes before correction) | 8e758c6af8309f3e7590b28323f5334bcaf635223b0e148160f286472742ed73 |
| 2026-10-08-client-answers/blank-form-2026-10-06.docx | DERIVED (our blank question form, moved from project root) | 1d6e32b0e7612e986370770feba82d11cbdfd8624f4cfe00c5c39ed8b8db4547 |
| Это наш диалог/sharex-082kvl.txt | SOURCE (https://b244.ru/mL3, 22.10; same bytes as 2026-10-15-1c-call/transcript.txt) | 067fb6b326942086bcddf5a3395940b9e99c16f2596753a415543c9e4ad9cdf8 |
| Это наш диалог/sharex-usECm0.mp4 | SOURCE (https://b244.ru/7nd, 22.10; 1C demo video, 01:01:09) | a391d1c87c7cf0f573aad9555c521293774067af30c7c85313227db501b20616 |
| Это наш диалог/assemblyai-7nd.json | DERIVED (AssemblyAI ru, speakers, of sharex-usECm0.mp4; 116 segments, 4 speakers, 5102 words) | 9416df7f22b166529f63f69d8f0e277c06c32d085ade40bf6a35ba1de207556e |
| Это наш диалог/INVENTORY.md | DERIVED (folder register) | — |

## Meeting 27.10.2026 (claude-3cb2, dcfg-kv8b5)

| Path | Class | SHA-256 |
| --- | --- | --- |
| `2026-10-27-dns/sharex-TEmZxf.mp4` | SOURCE (https://b244.ru/cc5, 27.10; meeting on 1С: Комплексная автоматизация) | fd6da57fd8372df63800d5fba9c286f73be0b847d892e80afc581d3deafa619e |
| `2026-10-27-dns/assemblyai-cc5.json` | DERIVED (AssemblyAI ru, speakers, of the video; 68 segments, 3 speakers) | 62067ee95217e4c008c040c89a1a22ff4e631118538a365a71ae621f1eba2145 |
