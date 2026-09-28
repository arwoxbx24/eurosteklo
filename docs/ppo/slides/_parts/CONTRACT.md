# Контракт разметки слайда (образец ППО простым языком)
Слайд 16:9, одна страница = одна мысль. Язык — простой, без PROVEN/INFERRED на лицевой стороне; статус — словом-чипом, источник — мелко в конце пункта.
```
<section class="slide" id="p1">
  <header><span class="num">1</span><h2>Заголовок-вывод</h2><p class="lead">одна фраза</p></header>
  <ol class="flow"><li class="step"><b>Шаг</b><span>кто</span></li> ... (3–5 шагов; стрелки рисует CSS)</ol>
  <div class="zones">
    <div class="zone see"><h3>Что видим</h3><ul><li>факт <span class="st st-board">на доске</span> <small class="src">источник: файл/узел</small></li></ul></div>
    <div class="zone ask"><h3>Что спросить</h3><ol><li>вопрос <em class="show">Покажите: …</em></li></ol></div>
    <div class="zone unk"><h3>Чего не знаем</h3><ul><li>пробел <span class="st st-unk">не знаем</span></li></ul></div>
  </div>
  <footer>Источники: … </footer>
</section>
```
Статус-чипы: st-board «на доске» (есть в источнике клиента), st-said «со слов», st-unk «не знаем». Не больше 5 пунктов в «Что спросить», не больше 4 в остальных зонах, каждая фраза ≤ 14 слов.
Слайд блокеров: `<section class="slide slide-blockers" id="p2">` c header как выше и `<table class="blk"><thead><tr><th>№</th><th>Не знаем</th><th>Кого спросить</th><th>Что без этого стоит</th></tr></thead><tbody>…</tbody></table>`.
Правило AGENTS.md: нет источника — «Информации нет», ничего не выдумывать. Работа только чтение репозитория, кроме своего файла.
