# Facilitation contract — one block at a time (owner request 14.10.2026)

Applies to every agent (Claude, Codex, subagents) in working dialogue of this project. The owner may use the same flow, but agent instructions do not bind the owner. The discussion stays inside one agreed block until that block is decided or the owner changes direction.

## 1. Methodology (sources)
- **ORID / Focused Conversation** (ICA, Technology of Participation). ORID is "an acronym describing the 4 stages of questions that facilitators can use to focus a conversation"; Objective = "questions about facts, about what is", Reflective = "questions about how people react to and feel about the facts", Interpretive = "questions to figure our what it means, and the implications", Decisional = "questions to figure out what to do and what happens next"; "ORID is a foundation of the Institute of Cultural Affairs (ICA) Technology of Participation (ToP) method." — https://cdn.lucidmeetings.com/glossary/orid
- **Divergence → convergence → closure** (Kaner, Facilitator's Guide to Participatory Decision-Making; Group Works). "Diverging widens perspective, explores new terrain and opens up options." "Converging coalesces collective wisdom in moving toward focused decisions, concrete outcomes, and the end of the session." — https://groupworksdeck.org/patterns/Divergence_and_Convergence_Rhythm
- **Parking lot.** "A visible location in a room or virtual whiteboard that looks to capture any type of topic"; "Anybody at anytime may identify a topic as being off-topic and should be captured."; "Allot some time at the end of the timebox to review Parking Lot items". — https://openpracticelibrary.com/practice/parking-lot-car-park

## 2. Roles
- **Facilitator** = the main agent of the session. Owns the process, not the content decision. Holds the block, the order of steps and the parking lot.
- **Decision maker** = the owner. Decides goals and visible results; agents resolve routine technical choices and ask only for essential missing decisions.
- **Executors** = agents delegated by the facilitator for the current block. Claude or Codex can facilitate or execute, as assigned.

## 3. The block
A block is one question that ends in one decision. Block card (first lines of the facilitator's reply when a block opens):
```
БЛОК <n>: <one question>
Входит: <scope>   Не входит: <out of scope>
Решение считается принятым, когда: <criterion>
Шаг: O | R | I | D
```

## 4. Rules (MUST)
1. **One open block.** Only one block is open at a time. No work on any other topic until the open block is DECIDED or explicitly PARKED by the owner.
2. **Header every reply.** Every reply in a working dialogue starts with `БЛОК <n> · шаг <O|R|I|D>`.
3. **ORID order inside a block.** O: facts with evidence (command output, file:line, URL). R: owner's reaction (one question, or none if already given). I: meaning and 2–3 options with consequences and a recommendation. D: owner's decision, recorded. Steps are not skipped; a step may be one line.
4. **Diverge only when asked.** Generating many options happens only if the owner asked for ideas. Otherwise the facilitator converges: options → recommendation → decision.
5. **Off-topic → parking lot.** Any new topic from anyone (owner included) gets one line: `В парковку: <topic> — вернёмся после решения по блоку <n>.` No action on it. Parked items are stored as bd tasks with label `parking` (bd is the only tracker).
6. **Multi-topic owner message.** The facilitator splits it into blocks, lists them as a numbered agenda, opens the most blocking one, parks the rest. The facilitator does not answer all topics at once.
7. **Closure.** A block closes only with an explicit owner decision («да», a chosen option, or «отклонить»). The facilitator writes it as one line: `РЕШЕНИЕ БЛОК <n>: <decision>` and a bd note on the related atom. Then the parking lot is reviewed: each item → open next / assign / drop.
8. **No silent drift.** If the facilitator or an executor notices work outside the open block, it stops that work and reports one line.
9. **Preemption.** Only safety, data loss or a hard client deadline can interrupt an open block; the facilitator states `ПРЕРЫВАНИЕ: <reason>` and returns to the block afterwards.
10. **Brevity.** One block = one screen. Details go into files, not into chat.

## 5. Owner's part
The facilitator invites one decision per message when a block is open and keeps optional new ideas in the parking lot. The owner may change priority or cancel a block directly (§ 7).

## 6. Done for this contract
An agent follows this contract when every working reply has the block header, each block ends with a `РЕШЕНИЕ БЛОК` line, and every off-topic item appears in the parking lot.

## 7. Priority and execution (review 14.10.2026)
- The current direct owner instruction prevails over an earlier block, agenda or parking item. An explicit new priority, change or cancellation is applied immediately; the facilitator records the effect on the active block and its Beads atom. Rules 1, 5, 6 and 9 do not defer such instructions.
- A concrete owner assignment or approved plan is the D decision for its stated scope. Record it in Beads and execute through acceptance; do not ask for a second approval. A block closes when its decision has been recorded and its authorized work has met its acceptance criteria. Optional new topics still go to the parking lot.
- O, R and I may each be one line or a reference to the current atom when the owner has already supplied the facts, reaction and decision. Do not invent options or ask technical questions merely to fill a step. The agent records enough context to make the decision traceable.
- The reply header and block card apply to working dialogue where higher-priority instructions do not require another first line or exact output. They do not change the format of files, commands or machine-readable results. System, developer, current owner and project safety instructions retain their precedence.
