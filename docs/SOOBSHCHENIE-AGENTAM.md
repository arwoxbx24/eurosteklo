# Разовое сообщение агентам (Codex CLI, Claude CLI, Claude Web) — от Claude Web, 30.09.2026

Прочитай, выполни свою часть, затем УДАЛИ этот файл и строку-ссылку на него в `docs/ppo/HANDOFF.md` (отдельный PR `<агент>/<дата>-soobshchenie-prochitano`). Работе не мешает.

## Что изменилось 30.09 (всё в `main`, ветка по умолчанию)
- Ствол — `main`. `codex/8b44-eurosteklo` — архив, в неё не писать.
- Имена веток: `<агент>/<ГГГГ-ММ-ДД>-<этап>-<суть>` (codex / claude-cli / claude-web); этап → PR → merge-коммит → строка в `docs/CHECKPOINTS.md`. Автор коммитов — своё имя (`git config user.name "Codex CLI"` / `"Claude CLI"`).
- Сделано: e1 (PR №6, карта сделок исправлена, точки С25–С29), e3 (PR №5, движок: чекбоксы, статусы, роли слева, `check_ppo.py`), e2 (PR №7, лиды/сделки без дублей, «А если…» по источникам, повестка встречи по лидам).
- Перед любым PR: `python3 docs/ppo/build_all.py && python3 docs/ppo/check_ppo.py` — ошибок 0.
- Документы: `specs/006-ispravlenie-kart/spec.md`, реестр требований `specs/006-ispravlenie-kart/REESTR-trebovanij.md`, журнал `docs/ppo/00-resheniya-vladeltsa.md`.

## Сделать (CLI-агент, по поручению владельца)
1. `git status` → `git fetch origin` → работать от `origin/main`. Старую копию с историей до 29.09 не пушить (П9: локальная backup-ветка).
2. Поставить метки отката (облако не может):
   `git tag -a checkpoint/2026-09-30-e3-dvizhok -m "e3" 09437d4f530d9d4e8c54305ef23a0ee556a268f9`
   `git tag -a checkpoint/2026-09-30-e1-sdelki -m "e1" 3898d95a76402934b64529d3a44ddec7293f0a3e`
   `git tag -a checkpoint/2026-09-30-e2-lidy-sdelki -m "e2" 71ea516d915f5d6f0e4a4765531a5410722d89c0`
   `git tag -a checkpoint/2026-09-30-e4-karta -m "e4" 97bc3cba6a14a6d131bd181f84e3c58a5364b6ef`
   затем `git push origin --tags`.
3. Удалить пустую ветку `claude/wonderful-pasteur-7tzxeu` (= `575a157`, содержимое в `main`): `git push origin --delete claude/wonderful-pasteur-7tzxeu` — облаку запрещено.
4. PR №4 (Codex, аудит сессии) — не сливать без «да» владельца.

## Ждём от владельца
- Транскрипт видео встречи 29.09 (~1,5 ч) — внести ответы, разблокировать точки.
- Дата следующей встречи (по лидам): страница `docs/ppo/lidy/obsledovanie-lidy.html`, лист владельцу `docs/ppo/lidy/_parts/povestka-vladeltsu.md`.
