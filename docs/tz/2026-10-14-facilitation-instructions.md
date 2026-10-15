# U1. Договор фасилитации для агентов проекта

Поручение владельца от 14.10.2026: рецензировать `docs/process/facilitation-contract.md` из дерева Claude и сделать его обязательным для Claude и Codex через инструкции проекта. Источник скопирован без правки исходного файла; к копии добавлен § 7 для согласования с действующими поручениями.

Архитектура: `AGENTS.md` — общая точка входа; `CLAUDE.md` направляет Claude к ней; `docs/process/facilitation-contract.md` хранит полное правило. Прямое поручение владельца уже является решением по своему объёму. Оно не ждёт второго согласия и не отправляется в парковку.

Файлы: `AGENTS.md`, `CLAUDE.md`, `docs/process/facilitation-contract.md`, `docs/tz/2026-10-14-facilitation-instructions.md`.

Порядок: проверить источник и цепочку инструкций; исправить устаревшее ограничение исполнителя; добавить общую ссылку и § 7; проверить точный состав изменений, ссылки, отсутствие закрытых данных и `git diff --check`; записать рецензию и результат в свой атом; выполнить локальную сдачу через `ship-post`.

Проверка: `git diff --check` и проверка наличия ссылки из `AGENTS.md`, указания читать его в `CLAUDE.md`, ключевых правил одного блока, ORID и парковки в договоре, а также ровно четырёх заявленных файлов в изменениях. Ожидаемый результат: проверки проходят; `ship-post --submit` создаёт локальный коммит и закрывает `eurosteklo-8ha` с SHA. Доставка в `main` и загрузка новых правил уже работающими сессиями проверяются отдельно.

Откат: `git revert` коммита этого атома через штатный маршрут. Исходный файл в дереве Claude не изменять.

Рецензия `rule-author`: исходные § 3–6 требовали повторного решения владельца и парковали любую его новую тему; это противоречило текущему прямому поручению. Обязательный заголовок также мог конфликтовать с более приоритетным форматом ответа. § 7 сохраняет один блок, ORID и парковку, но устраняет эти конфликты. В § 2 снята фиксированная роль Codex как исполнителя; § 5 теперь приглашает владельца к формату, не навязывая ему инструкцию агента. В `CLAUDE.md` исправлены устаревшая роль единственного исполнителя, требование второго «да» и смешение диалогового блока с параллельными подзадачами. Дополнительные остановки, повторные проверки, XML, новые настройки и уровень рассуждения не вводились.

Основание приоритета: прямое поручение владельца 14.10.2026 в текущей задаче. OpenAI предупреждает, что модель «can be more sensitive to instructions contained in skills and other files, such as AGENTS.md» и лишний вопрос «can cause it to stop when the user may expect it to make reasonable assumptions and persist» — https://developers.openai.com/api/docs/guides/prompt-guidance#instruction-following и https://developers.openai.com/api/docs/guides/prompt-guidance#initiative-and-follow-through. Для Codex: «Codex builds an instruction chain when it starts (once per run; in the TUI this usually means once per launched session)» — https://learn.chatgpt.com/docs/agent-configuration/agents-md#how-codex-discovers-guidance. Путь Claude к `AGENTS.md` задан первой строкой проектного `CLAUDE.md`.
