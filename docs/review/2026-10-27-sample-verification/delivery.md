# Опись доставки — 2026-10-27 (dcfg-kv8b5)

Опись перечисляет все ветки Claude, рабочие копии (worktree) и открытые PR репозитория arwoxbx24/eurosteklo и показывает, видит ли их веб-агент Claude на GitHub. Данные сняты 2026-10-27 командами: `gh pr list --state open`, `git fetch origin --prune`, `git branch -r --no-merged origin/main`, `git branch --no-merged origin/main --list claude/* claude-cli/*`, `git log <branch> --not --remotes`, `git worktree list`.

**Что не видно на GitHub по правилам:** папка `client-materials/private/` (записи и расшифровки) хранится вне Git по правилу проекта AGENTS.md:52 («Вне Git: client-materials/private/ … передаёт владелец отдельно»); веб-агент видит только тексты `docs/meetings/**`.

| Объект | Вид | Состояние | Причина / цифры |
|---|---|---|---|
| PR 33 `claude/clever-fermi-zek0uu` | открытый PR (Claude Web) | LISTED | на GitHub, не слит: клиентские документы сливаются только после «да» владельца (AGENTS.md:46) |
| PR 45 `codex/eurosteklo-lro.1-translate` | открытый PR (Codex) | LISTED | на GitHub, не слит: работа Codex, не Claude |
| `origin/claude/eurosteklo-abc-spec014` | удалённая ветка + рабочая копия | VISIBLE | на GitHub, не слита в main; локальных неотправленных коммитов 0 |
| `origin/claude/eurosteklo-qsn-lidy` | удалённая ветка | VISIBLE | на GitHub, не слита в main |
| `origin/claude/eurosteklo-v8r-otvety` | удалённая ветка | VISIBLE | на GitHub, не слита в main |
| `origin/codex/eurosteklo-a58-consistency-audit` | удалённая ветка (Codex) | LISTED | работа Codex, вне описи Claude |
| `origin/codex/eurosteklo-a58-consistency-v2` | удалённая ветка (Codex) | LISTED | работа Codex, вне описи Claude |
| `claude-cli/2026-10-13-tz-word` | рабочая копия | DELIVERED | ветка слита в main |
| `claude/ds6-dannye-faily` | рабочая копия | DELIVERED | ветка слита в main |
| `claude/eurosteklo-2o0.6-archive` | рабочая копия | DELIVERED | ветка слита в main |
| `claude/eurosteklo-7ti-word` | рабочая копия | DELIVERED | ветка слита в main |
| `claude/eurosteklo-edm-client-clean` | рабочая копия | DELIVERED | ветка слита в main |
| `claude/eurosteklo-ee2-by-addressee` | рабочая копия | DELIVERED | ветка слита в main |
| `claude/eurosteklo-rdy-clean-word` | рабочая копия | DELIVERED | ветка слита в main |
| `claude/eurosteklo-xeb-1c-questions` | рабочая копия | DELIVERED | ветка слита в main |
| `claude/eurosteklo-y3w-vitaly-prices` | рабочая копия | DELIVERED | ветка слита в main |
| Незакоммиченные файлы в рабочих копиях веток Claude из этой описи | рабочие копии других сессий | LISTED | не проверены: у ведущего агента нет разрешённой команды для чтения состояния чужих рабочих копий; коммитов вне GitHub 0 |
| `claude/dcfg-kv8b5-*` | ветки этой цели | DELIVERED | доставляются PR этой цели |

TOTAL items=18 delivered=10 visible=3 listed=5
UNLISTED=0
