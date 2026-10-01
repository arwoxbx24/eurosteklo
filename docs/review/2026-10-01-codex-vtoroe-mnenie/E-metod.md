# E — способ запуска Codex для этого аудита

Дата проверки: 01.10.2026. Срез задания: `9690df60bfecfdd5839946f0ca12d9392a2359f3`. Версия установленного CLI: `codex-cli 0.159.3`, фактическая строка 2 в `E-codex-help.txt`.

skills: `openai-docs` → этот файл, разделы официальных источников и проверочных команд (SKILL.md прочитан; официальный поиск и последующее чтение страниц выполнены). Общую оркестрацию и остальные навыки ведёт родительский агент.

Сравниваются возможности способов запуска, а не действующие настройки конкретного профиля. Запуск рабочих сессий, установка плагинов, чтение конфигурации или авторизации, операции tmux и испытание восстановления здесь не выполнялись.

## Сравнение по пяти измерениям

| Измерение | Что лучше | Дословная цитата | Источник |
|---|---|---|---|
| 1. Загрузка навыков и плагинов CE, Spec Kit, CSB | Для ручной проверки наличия удобнее интерактивный интерфейс: документация описывает меню навыков и плагинов. Превосходство самого механизма загрузки над `exec` **НЕ ПРОВЕРЕНО**. Документация не подтверждает, что `exec` лишён навыков. Фактическая загрузка именно CE, Spec Kit и CSB в двух новых сессиях не испытывалась. | **D3:** Browse and use skills. **D4:** Browse installed and discoverable plugins. **D2:** Skills are loaded and visible to the agent (at least their metadata), so Codex can discover and choose them implicitly. | D2–D4 ниже: официальные страницы навыков и команд. **H3:** `E-codex-help.txt:21` — Manage Codex plugins. |
| 2. Видимость работы владельцу | Интерактивный Codex в выделенном терминальном окне предпочтителен для непосредственного наблюдения и вмешательства — **INFERRED**, рекомендация по форме интерфейса. `exec` тоже показывает ход работы: stderr и, при выборе JSONL, события. Реальная доступность окна tmux владельцу **НЕ ПРОВЕРЕНА**. | **H2:** If no subcommand is specified, options will be forwarded to the interactive CLI. **D5:** While `codex exec` runs, Codex streams progress to `stderr` and prints only the final agent message to `stdout`. | `E-codex-help.txt:9`; D5, официальная страница non-interactive-mode. |
| 3. Сохранение результата в файл и автоматизация | `codex exec`: **PROVEN** наличие объявленных CLI возможностей JSONL и сохранения последнего сообщения; документация прямо описывает скриптовый запуск. Это поддерживает воспроизводимый запуск фиксированного аудита. Возможность `-o` не означает, что все требуемые A–E автоматически созданы. | **H10:** Print events to stdout as JSONL. **H12:** Specifies file where the last message from the agent should be written. | `E-codex-help.txt:249`, `:252`; D5 и описание non-interactive-mode ниже. |
| 4. Одобрения и песочница | Ни один способ запуска сам по себе не доказан безопаснее. **PROVEN**: обе справки объявляют профиль и выбор песочницы; верхний CLI объявляет политику одобрений. **НЕ ПРОВЕРЕНО**: эффективные права и настройки рабочих сессий. Автоматизация требует заранее заданных разрешений; режим интерфейса не является свидетельством их применения. | **H6:** `--profile <CONFIG_PROFILE_V2>`; **H7:** `--sandbox <SANDBOX_MODE>`; **D6:** Run with explicit, pre-set sandbox and approval settings. | `E-codex-help.txt:90,196` и `:93,199`; политика H8–H9: строки `118`, `123`; D6, non-interactive-mode. |
| 5. Продолжение после обрыва | Оба имеют продолжение сохранённой сессии: **PROVEN** объявленные команды. `exec` поддерживает выбор ID или последней сессии; интерактивный режим — выбор сохранённой интерактивной сессии. Успешное восстановление после конкретного сбоя, сохранение процесса tmux и автоматический перезапуск **НЕ ПРОВЕРЕНЫ**. | **H4:** Resume a previous interactive session. **H5:** Resume a previous session by id or pick the most recent with --last. **D7:** You can also target a specific session ID with `codex exec resume <SESSION_ID>`. | `E-codex-help.txt:31`, `:153`; D7, non-interactive-mode; D8, страница команд. H13 (`:231`) отдельно предупреждает, что непостоянный режим не сохраняет файлы сессии. |

## Официальные источники и точные фрагменты

Источники получены через `mcp__openaiDeveloperDocs__search_openai_docs`, затем `mcp__openaiDeveloperDocs__fetch_openai_doc`. Первый поиск: `query="Codex exec interactive plugins resume sandbox", limit=8`; прочитан найденный раздел developer-commands. Последующие целевые поиски: `Codex skills discovery SKILL.md CLI`, `Codex CLI interactive progress resume sessions`. Сниппеты поиска не используются как доказательства: ниже только фрагменты фактически прочитанных страниц.

Дата обращения ко всем URL: **01.10.2026**. Страницы актуальной документации не закреплены за CLI **0.159.3**; они не являются архивной справкой этой версии. Конкретные доступные флаги и команды 0.159.3 сверены с локальным `--help`. Отдельной документации другого фиксированного номера версии для доказательства не использовано.

**D1 — плагины.** Вызов: `fetch_openai_doc(url="https://learn.chatgpt.com/docs/plugins", anchor="use-plugins-from-a-supported-surface")`.
URL: https://learn.chatgpt.com/docs/plugins#use-plugins-from-a-supported-surface
Фрагмент фактического ответа:

> for Codex, use the ChatGPT desktop app or Codex CLI.

Эта цитата подтверждает поддерживаемую поверхность CLI в целом. Она не разделяет поддержку по TUI и `exec` и не подтверждает установку конкретных трёх навыков.

**D2 — навыки.** Вызов: `fetch_openai_doc(url="https://learn.chatgpt.com/docs/customization/overview", anchor="skills")`.
URL: https://learn.chatgpt.com/docs/customization/overview#skills
Фрагмент фактического ответа:

> Skills are loaded and visible to the agent (at least their metadata), so Codex can discover and choose them implicitly.

Это описание механизма обнаружения, а не свидетельство выполнения навыка CE, Spec Kit или CSB.

**D3, D4 и D8 — интерактивные команды.** Вызов: `fetch_openai_doc(url="https://learn.chatgpt.com/docs/developer-commands", anchor="built-in-slash-commands")`.
URL: https://learn.chatgpt.com/docs/developer-commands#built-in-slash-commands
Фрагменты фактического ответа: для `/skills`, `/plugins` и `/resume` соответственно:

> Browse and use skills.

> Browse installed and discoverable plugins.

> Continue work from a previous CLI session without starting over.

**D5, D6 и D7 — неинтерактивный режим.** Вызов: `fetch_openai_doc(url="https://learn.chatgpt.com/docs/non-interactive-mode")`.
URL: https://learn.chatgpt.com/docs/non-interactive-mode
Фрагменты фактического ответа:

> Non-interactive mode lets you run Codex from scripts (for example, continuous integration (CI) jobs) without opening the interactive TUI.

> While `codex exec` runs, Codex streams progress to `stderr` and prints only the final agent message to `stdout`.

> Run with explicit, pre-set sandbox and approval settings.

> You can also target a specific session ID with `codex exec resume <SESSION_ID>`.

Не применялись советы документации о расширении прав, отключении конфигурации или правил. Паспорт разрешает анализ, а не перенастройку запуска.

## Фактическая справка CLI и самопроверка цитат

В `E-codex-help.txt` сохранены команды, stdout, stderr и коды возврата (stdout записан перед stderr для каждой команды). Реально выполнены:

```text
$ codex --version
codex-cli 0.159.3
exit_code=0
$ codex --help
exit_code=0
$ codex exec --help
exit_code=0
```

Во всех трёх случаях CLI дополнительно вывел предупреждение о невозможности создать PATH aliases в файловой системе только для чтения. Точный текст есть в исходном файле справки на строках 3, 143 и 259 и проверяется цитатой H14 ниже. Справка получена с кодом 0; это не доказательство успешного старта рабочей сессии.

Верхний CLI объявляет `--ask-for-approval`; отдельный раздел `exec --help` не перечисляет такой флаг. В отчёте не заявляется наличие отдельного флага `exec -a`, не даётся команда обхода настроек и не утверждается фактическое применение профиля.

Самопроверка: перепроверено 14 из 14 цитат H1–H14 по сохранённой справке. Все 18 найденных вхождений имеют заявленные номера строк, все коды возврата — 0. Совпадающие строки двух справок и три предупреждения учтены явно. Полный фактический вывод — ниже и в `E-grep.log`.

```text
H1
$ grep -n -F -e 'codex-cli 0.159.3' docs/review/2026-10-01-codex-vtoroe-mnenie/E-codex-help.txt
2:codex-cli 0.159.3
exit_code=0

H2
$ grep -n -F -e 'If no subcommand is specified, options will be forwarded to the interactive CLI.' docs/review/2026-10-01-codex-vtoroe-mnenie/E-codex-help.txt
9:If no subcommand is specified, options will be forwarded to the interactive CLI.
exit_code=0

H3
$ grep -n -F -e 'Manage Codex plugins' docs/review/2026-10-01-codex-vtoroe-mnenie/E-codex-help.txt
21:  plugin            Manage Codex plugins
exit_code=0

H4
$ grep -n -F -e 'Resume a previous interactive session' docs/review/2026-10-01-codex-vtoroe-mnenie/E-codex-help.txt
31:  resume            Resume a previous interactive session (picker by default; use --last to continue
exit_code=0

H5
$ grep -n -F -e 'Resume a previous session by id or pick the most recent with --last' docs/review/2026-10-01-codex-vtoroe-mnenie/E-codex-help.txt
153:  resume  Resume a previous session by id or pick the most recent with --last
exit_code=0

H6
$ grep -n -F -e '--profile <CONFIG_PROFILE_V2>' docs/review/2026-10-01-codex-vtoroe-mnenie/E-codex-help.txt
90:  -p, --profile <CONFIG_PROFILE_V2>
196:  -p, --profile <CONFIG_PROFILE_V2>
exit_code=0

H7
$ grep -n -F -e '--sandbox <SANDBOX_MODE>' docs/review/2026-10-01-codex-vtoroe-mnenie/E-codex-help.txt
93:  -s, --sandbox <SANDBOX_MODE>
199:  -s, --sandbox <SANDBOX_MODE>
exit_code=0

H8
$ grep -n -F -e '--ask-for-approval <APPROVAL_POLICY>' docs/review/2026-10-01-codex-vtoroe-mnenie/E-codex-help.txt
118:  -a, --ask-for-approval <APPROVAL_POLICY>
exit_code=0

H9
$ grep -n -F -e 'Never ask for user approval' docs/review/2026-10-01-codex-vtoroe-mnenie/E-codex-help.txt
123:          - never:      Never ask for user approval Execution failures are immediately returned to
exit_code=0

H10
$ grep -n -F -e 'Print events to stdout as JSONL' docs/review/2026-10-01-codex-vtoroe-mnenie/E-codex-help.txt
249:          Print events to stdout as JSONL
exit_code=0

H11
$ grep -n -F -e '--output-last-message <FILE>' docs/review/2026-10-01-codex-vtoroe-mnenie/E-codex-help.txt
251:  -o, --output-last-message <FILE>
exit_code=0

H12
$ grep -n -F -e 'Specifies file where the last message from the agent should be written' docs/review/2026-10-01-codex-vtoroe-mnenie/E-codex-help.txt
252:          Specifies file where the last message from the agent should be written
exit_code=0

H13
$ grep -n -F -e 'Run without persisting session files to disk' docs/review/2026-10-01-codex-vtoroe-mnenie/E-codex-help.txt
231:          Run without persisting session files to disk
exit_code=0

H14
$ grep -n -F -e 'WARNING: proceeding, even though we could not create PATH aliases: Read-only file system (os error 30)' docs/review/2026-10-01-codex-vtoroe-mnenie/E-codex-help.txt
3:WARNING: proceeding, even though we could not create PATH aliases: Read-only file system (os error 30)
143:WARNING: proceeding, even though we could not create PATH aliases: Read-only file system (os error 30)
259:WARNING: proceeding, even though we could not create PATH aliases: Read-only file system (os error 30)
exit_code=0

```

## Ограничения вывода

- Показаны объявленные возможности CLI и документированное поведение, а не испытание двух новых рабочих сессий. Гарантия выполнения полного аудита, загрузка конкретных навыков, эффективные права и восстановление после сбоя остаются **НЕ ПРОВЕРЕНЫ**.
- Документация подтверждает ручное возобновление сохранённой сессии. Она не является доказательством самозапуска процесса после завершения или постоянного видимого состояния работы.
- Для фиксированного задания с обязательными файлами автоматический запуск и машинный журнал полезнее интерфейса. Предпочтение интерфейса для постоянного наблюдения владельцем — отдельный критерий удобства, а не доказанное преимущество выполнения навыков.

Вердикт: для этого фиксированного файлового аудита предпочтителен `codex exec` с сохранением событий и результатов; интерактивный Codex в отдельном окне полезнее для непосредственного наблюдения, а превосходство загрузки CE, Spec Kit и CSB и восстановление tmux не проверены.
