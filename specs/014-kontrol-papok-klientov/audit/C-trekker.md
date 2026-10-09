# Блок C — трекер и история (аудит 09.10, только чтение)

## Вердикты

| ID | вердикт | доказательство |
|---|---|---|
| H1 | РЕАЛИЗОВАНО (причина найдена; правила/исправления нет) | Причина: переменная окружения `BEADS_DIR` в процессе агента. `bd where` (cwd=clients/eurosteklo) → `/root/workspaces/projects/.beads` (database …/.beads/dolt). `bd -C …/clients/eurosteklo where` → prefix eurosteklo, `…/eurosteklo/.beads/embeddeddolt`. `BEADS_DIR="" bd where` (cwd=eurosteklo) → `…/clients/eurosteklo/.beads`, prefix eurosteklo (локальная база). `bd context` → `BEADS_DIR points to unsafe location: /root/workspaces/projects/.beads` (подтверждает, что переменная задана). Источник задания переменной не найден: grep BEADS в `/root/.claude/settings.json`, `projects/.claude/settings.local.json`, `eurosteklo/.claude/settings*.json` — пусто (settings.json в projects и eurosteklo отсутствуют); BEADS_DIR нет в `/root/CLAUDE.md`, `projects/CLAUDE.md`, `LAWS-PROCEDURES.md`, `CONTOUR-PASSPORT.md`, `TOOLS-REGISTRY.md`. Единственное место в tools: `bin/ship:3` `export BEADS_DIR=${BEADS_DIR:-/root/workspaces/projects/.beads}`. Откуда переменная в сессии — НЕ ПРОВЕРЕНО (env читать запрещено). Конфиги: projects/.beads: `metadata.json` dolt_mode=server, dolt_database=dcfg, `config.yaml` dolt.port 36211; eurosteklo/.beads: dolt_mode=embedded, dolt_database=eurosteklo; файла redirect в обеих .beads нет (`ls -la`). `bd where --help`: «Show the active beads database location, including redirect information»; порядок поиска базы в `bd --help`/`bd where --help` не описан (флаг `--db`: «default: auto-discover .beads/*.db»). Правила про BEADS_DIR для вложенных репо в законах нет (grep пусто). |
| H2 | РЕАЛИЗОВАНО (источник найден); правила «автор = агент» НЕ НАЙДЕНО в этом блоке | `git -C clients/eurosteklo config --show-origin user.name` → `file:.git/config	Codex CLI`; `git -C projects …` → `file:.git/config	Claude Code`; `git -C tools …` → `file:/root/.gitconfig	Claude Code`. Т.е. в репо Евростекла имя задано локально в его `.git/config` (Codex CLI), в projects — локально Claude Code, в tools — глобально. bd `--actor` по умолчанию: `$BEADS_ACTOR, git user.name, $USER` (`bd --help`) — поэтому `eurosteklo-426` создан «Codex CLI». Правило поиска по законам — блок A. |
| H4 | ЧАСТИЧНО | `bd search err:ctx` → «No issues found». `err:ctx` выдаёт `tools/bin/git-sync:33` (`ga_ctx "$name" … || emit "$name" err:ctx`), когда имя репо не найдено в реестре `ga_roots`; для вложенного репо имя в реестре = относительный путь (`git-auto-lib:30-32` `rel=${g#"$p"/}` → `clients/eurosteklo`), а не basename `eurosteklo`. Причина зафиксирована в `tools/docs/tz/2026-10-09-dcfg-6namg-ship-post-live-sync.md:9` и в `dcfg-ta2r0` («:284 live sync берёт basename вместо имени ga_roots»). Исправление влито: `ship-post:307` `if ! name=$(ga_repo_of "$repo"); then name=$(basename "$repo"); fi`, `ship-post:129` `name=$(ga_repo_of …)`; `dcfg-ta2r0` CLOSED, PR tools#157 (6d7f77c), `dcfg-6namg` CLOSED, PR #149. Отдельной задачи на `err:ctx` в Евростекле нет. Поддержка локальной `.beads` вложенного репо в ship-post: `grep -n "err:ctx\|BEADS_DIR\|\.beads" bin/ship-post` → пусто (ship-post не упоминает ни BEADS_DIR, ни .beads); ship ставит `BEADS_DIR` по умолчанию на общую базу (`bin/ship:3`). Фактическое воспроизведение err:ctx на Евростекле после #157 — НЕ ПРОВЕРЕНО (ship-post не запускался). Замечание: `dcfg-ta2r0` отмечает, что в clients/eurosteklo нет CI pull_request (ci_pr_workflows=0) → ADR v4: скан пишет wait-owner no-ci и ship не вызывает. |
| H12 | ЧАСТИЧНО | `dcfg-bqocd` (рекурсия code-channel формы 2) — CLOSED 09.10: PR tools#154 (adf673a), `code-channel-test PASS 21/21`, прогон формы 2 дал непустой git diff 2 files +3/-2; повтор 09.10 в `dcfg-fl9er.5.3` учтён. `eurosteklo-426` — НЕ про рекурсию: «code-channel: перерасход Bitrix GPT не ловится» (P0, OPEN, создан 05.10, Codex CLI; discovered-from `eurosteklo-ds6`); критерии: канал читает usage/limit Bitrix, audit с пустым stdout → rc≠0 и переход к форме 3, замер при исчерпанной квоте. Ни одно из трёх не подтверждено закрытием в этой задаче. Ограничение формулировки H12: ТЗ ссылается на 426 как на рекурсию — факт иной. Частичная реализация H5 в tools: `d1aad1f feat(code-channel): денежный стоп формы 3 по usage_daily/OR_DAILY_STOP (spec:098) (#88)` (форма 3, не Bitrix форма 1). Воспроизводимость рекурсии после #154 — НЕ ПРОВЕРЕНО (code-channel не запускался). |

## Найденные задачи bd

| id | статус | заголовок | тема |
|---|---|---|---|
| dcfg-bqocd | closed | code-channel форма 2: codex вызывает code-channel рекурсивно | H12 |
| dcfg-fl9er.5.3 | closed | [CLAUDE-config-69bb] U3 --help: safe-delete code-channel place-files … (блокирует/связан с bqocd) | H12 |
| eurosteklo-426 | open (P0) | [CLAUDE-config-68f3] code-channel: перерасход Bitrix GPT не ловится… (локальная база eurosteklo) | H12/H5 |
| dcfg-ta2r0 | closed | ship-post: вложенные репо — --submit принимает, --watch не сканирует; live sync берёт basename | H4 |
| dcfg-6namg | closed | ship-post: после слияния основные папки tools/projects не обновляются (ga_live_sync) | H4 |
| dcfg-8yqv4.14 | open (P0) | spec:099 v4 U12 — ship-post: конечные состояния атома в квитанции и bd (blocked by ta2r0) | H4 |
| dcfg-9uhb3 | open (P2) | ship и ship-post: --help выполняет команду | H4 (смежно) |
| dcfg-8rtt0 | open (P2) | [ship-post] delivery failure projects exit 24 | H4 (смежно) |
| dcfg-dtl8p | open (P2) | [ship-post] delivery failure tools exit 40 | H4 (смежно) |
| dcfg-5zcr3 | open (P2) | [ship-post] отказ ship 80: dcfg-o88tx | H4 (смежно) |
| dcfg-m2lzu | closed | ship-post delivery failure dcfg-gured.2 (ТЗ: конфликт PR = отказ 50, tools#158) | H4 (смежно) |
| dcfg-sw0b3.1 | closed | ship-post и git-sync: одна открытая задача на причину | H4 (смежно) |
| dcfg-vzy6r | closed | ship-post: bd close от точного assignee атома | H2 (смежно: actor) |
| (поиск `err:ctx`) | — | совпадений в bd нет | H4 |
| (поиск BEADS_DIR / вложенная база) | — | задач не искалось в bd отдельно; в законах упоминаний нет | H1 |

Открытые в локальной базе eurosteklo (`bd -C … list --status open,in_progress`): eurosteklo-426 (open P0), eurosteklo-37m (in_progress P1, hooks), eurosteklo-ds6 (in_progress P1), eurosteklo-ds6.8 (open P2), eurosteklo-71o (open P2, safe-delete отказывает на сегменте clients), eurosteklo-ia1 (open P2, GIT-SYNC rescued refs). Всего 6 (4 open, 2 in_progress). Предупреждение bd: `beads.role not configured (GH#2950)`.

## История за 7 дней (по запрошенным путям)

`git -C /root/workspaces/tools log --since=7.days --oneline -- bin/ship-post bin/code-channel` — 15 коммитов; затрагивающие темы: 87b1d0d (#158 dcfg-m2lzu), 6d7f77c (#157 dcfg-ta2r0 — доставка из всех репо ga_roots; H4), aab17d5 (#155 dcfg-fl9er.5.3), adf673a (#154 dcfg-bqocd; H12), d5ebdfe (#149 dcfg-6namg; H4), 7b4479b (#148 dcfg-vzy6r; actor), ccb001b (#146), 3cad975 (#142 dcfg-bjch1), c3ee082 (#122), aabdd6d (#118), 6e6d57d (#117), 5f0312e (#116), 4be760b (#115), 8bfce7f (#114), d1aad1f (#88 денежный стоп формы 3).

`git -C /root/workspaces/projects log --since=7.days --oneline -- CLAUDE.md docs/LAWS-PROCEDURES.md clients/CLAUDE.md` — 24 коммита (40b5e1eb7 … 85f1985ca); по темам H1/H2/H4/H12 (BEADS_DIR, git user.name, err:ctx, рекурсия code-channel) совпадающих по заголовку коммитов нет. Ближайшие по смыслу: aaadb2a0e (#311 spec:099 v4 CR — доставка), 60094126a (#309 CLAUDE.md:22). Содержимое диффов не читалось. Примечание: список включает коммиты старше 7 дней по смыслу номеров PR; даты в выводе не запрашивались.
