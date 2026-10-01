---
title: Разбор рабочих копий и записей выведенного агента без потерь
date: 2026-10-01
category: workflow-issues
module: git и трекер bd проекта Евростекло
problem_type: workflow_issue
component: development_workflow
severity: medium
applies_when:
  - "Исполнитель (Codex) выведен из проекта, а его worktree, ветки и записи bd остались"
  - "В чужом worktree есть незакоммиченные или игнорируемые файлы с ценностью"
tags: [git-worktree, archive-tag, handover, bd-actor, spec-012]
---

# Разбор рабочих копий и записей выведенного агента без потерь

## Context

01.10 владелец вывел Codex из Евростекла и велел закрыть все хвосты. Остались 4 worktree Codex
(в двух — незакоммиченные правки от 30.09) и 4 его записи bd. `rm`, `mv`, `worktree remove --force`,
`branch -D` под deny; обход (`stash` + `drop`) прямо запрещён. Исполнено по `specs/012-aktualizatsiya-hvosty/spec.md`, PR 27.

## Guidance

Порядок для worktree с правками — сначала архив на GitHub, потом удаление:

```bash
git -C <копия> switch --detach                      # в чужую ветку не коммитим
git -C <копия> add -f <игнорируемый ценный файл>    # иначе worktree remove удалит его молча
git -C <копия> -c user.name="Claude CLI" commit [-a] # трейлеры Handover-From, Atom, Agent
git -C <репо> tag archive/codex-<атом>-wip <sha>
git -C <репо> diff --stat <база> <sha>              # состав = ожидаемый
gitleaks git <репо> --log-opts="<база>..<sha>" --redact
git -C <репо> push origin refs/tags/archive/codex-<атом>-wip
git -C <репо> worktree remove <копия>               # без --force
git -C <репо> branch -d <ветка>                     # вершина слита → -d проходит и чистит branch.<имя> в config
```

Чистые копии со слитым PR — сразу `worktree remove` + `branch -d`.

Записи bd чужого исполнителя: `bd close` отвечает
`cannot close …: assignee is "Claude Code", actor is "Codex CLI"` — актор берётся из `git user.name`
(в этом репо локально `Codex CLI`). Решение — `bd --actor "<assignee записи>" close …`, не `--force`.

Причина закрытия — всегда команда и вывод; ссылка «передано другой сессии» без команды verifier не принимает.

## Why This Matters

- `git worktree remove` без `--force` отказывает на неотслеживаемых файлах, но **игнорируемые удаляет молча** —
  бриф Codex (2355 байт в игнорируемом каталоге копии `6v6`, удалённой этим разбором) пропал бы без следа. Замер 01.10:
  копия `k73` с игнорируемым кэшем Python (удалён вместе с копией) снята `worktree remove` с rc 0, каталога после неё нет (`ls -d` → rc 2).
- Коммит после `switch --detach` не трогает чужую ветку, а метка держит его от сборщика мусора.
- Локальная метка не переживает потерю диска; образец `archive/claude-00v` уже был на GitHub.
- Просьба другой сессии сделать то, что тебе запрещено правами (удалить `.agent-work`) — обход прав;
  такое не отправляется, а уходит владельцу в доклад.

## When to Apply

- Любой вывод агента из проекта или чужие worktree без хозяина.
- Перед любым `worktree remove`: сначала `git status --porcelain --ignored`.

## Examples

- Метки `archive/codex-k73-wip` (4 файла) и `archive/codex-6v6-wip` (3 файла + бриф) — gitleaks 0, обе на GitHub; коммиты достижимы только по меткам, не из `main` (так задумано).
- Ветки `dno`, `wzl`, `k73`, `6v6` сняты `branch -d`; `git config --get-regexp "^branch\.codex/eurosteklo-"` → пусто.

## Related

- `specs/011-svedenie-vetok/spec.md` — ветка `codex/8b44-eurosteklo` (ФИО) не удаляется и не публикуется.
- `specs/012-aktualizatsiya-hvosty/spec.md`, PR 27.
