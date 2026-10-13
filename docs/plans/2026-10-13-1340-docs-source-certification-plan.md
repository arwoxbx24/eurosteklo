---
title: Eurosteklo Source Certification - Plan
type: docs
date: 2026-10-13
---

# Eurosteklo Source Certification - Plan

## Goal Capsule

**Objective:** A developer can distinguish every current lead and deal process assertion in the owner-facing HTML maps from an unresolved question, with each asserted fact traceable to the supplied client material and the maps accessible through the existing links.

**Authority:** The owner requested a separate verification goal after the 2026-10-13 structure release. `AGENTS.md`, `PROJECT-STRUCTURE.md`, the private inventory, and the client's actual sources govern the work. A source file's presence, a citation token, or an earlier `PROVEN` label does not certify its meaning.

**Stop condition:** Never report map-wide source certification while a material, unsupported process assertion remains on a current map. If the supplied sources do not settle a point, mark it `UNVERIFIED` or `CONTRADICTED`, move it to the relevant question/survey area, and omit it from the certified process. Request only the specific missing evidence if that point must remain in the current process.

## Product Contract

### Problem and scope

The 2026-10-13 release made the HTML navigation, directory guide, and archive available. It did not establish semantic agreement between the two maps and the latest dated Miro export, two recordings and transcripts, or Roman's answer file. `docs/ppo/source-status.md` records 20 passport rows as unverified for meaning and explicitly says the row ledger does not cover every process statement. This plan covers the full visible claim set, not just those rows.

### Requirements

**Source integrity**

- R1. Use the locally present `client-materials/private/miro-2026-10-08/board.svg`, both 2026-10-04 recording/transcript pairs, `client-materials/private/2026-10-08-client-answers/otvety-klienta.md`, the original CSV and five JPGs, and their inventories. Check exact paths, dates, and checksums before treating a version as current. Do not ask for a file until this search shows it is actually absent.
- R2. Preserve client originals and private evidence outside Git. The current transcript validation has two `semantic_acceptance=false` results; do not rewrite that receipt or claim the silent videos prove spoken words. A transcript can identify a passage, but a process claim needs corroborated client evidence.

**Claim classification**

- R3. Enumerate every visible process assertion in `docs/ppo/lidy/karta-lidy.html`, `docs/ppo/sdelki/karta-sdelki.html`, and process labels in `docs/ppo/index.html`, with a stable page anchor or locator. For each, record the exact supporting client source and Miro node, answer ID, transcript locator, or visual timecode where applicable. Record conflicts rather than choosing a convenient source.
- R4. Assign `PROVEN`, `INFERRED`, `UNVERIFIED`, or `CONTRADICTED` under `AGENTS.md`. A current-process statement may remain asserted only if its evidence passes review; an unresolved statement remains visibly uncertain or moves to a question, with no invented Bitrix24 or 1C behavior. The owner-reported Bitrix24 cloud Professional context does not establish the exact 1C application or connector behavior.

**Owner and developer result**

- R5. Correct maintained PPO parts, rebuild the existing pages, and preserve the lead, deal, index, and historical PPO URLs. A reader must be able to reach the two current HTML maps and their question pages without treating the 28 September standalone page as current.
- R6. Publish only a source-safe certification summary and the corrected HTML. Keep verbatim confidential answers, recordings, transcripts, CRM data, and personal data in `client-materials/private/`. The developer handoff states what is certified, what remains unresolved, and which client evidence would resolve it.

### Acceptance examples

- AE1. A claim supported by the dated board and a client answer has both locators and a reviewed status; the map statement matches the support.
- AE2. A claim supported only by an unaccepted transcript is not presented as `PROVEN`.
- AE3. A conflict between an older screenshot and a later client answer is documented with both sources; the map does not silently pick one.
- AE4. A genuinely absent answer becomes one precise question; other verified process points can still be delivered.

## Planning Contract

- KTD1. Treat the existing private inventory and `docs/SOURCE-REGISTER.md` as the source locator; use the actual private files in the canonical project for review. Do not copy private originals into the isolated Git worktree.
- KTD2. Keep a private evidence ledger containing necessary source excerpts and a publishable `docs/ppo/source-status.md` with claim IDs, status, and safe locators only. A machine count checks coverage; independent source review checks meaning. Neither substitutes for the other.
- KTD3. Edit the maintained `docs/ppo/lidy/_parts/`, `docs/ppo/sdelki/_parts/`, and shared PPO parts, then use `docs/ppo/build_all.py`; do not hand-edit generated HTML. Preserve existing public paths and linked question pages.
- KTD4. The existing `docs/ppo/check_ppo.py --lidy`, a local browser pass, ZIP integrity check, scoped Git diff, and private-path scan are the verification tools. Do not add an integration, custom parser, or Bitrix24 write to perform a documentation audit.

## Implementation Units

### U1. Establish the source passport

**Goal:** Confirm the exact version and integrity of every supplied input before interpreting it.

**Requirements:** R1, R2.

**Dependencies:** None.

**Files:** `client-materials/private/INVENTORY.md` (private ledger only), `docs/SOURCE-REGISTER.md` (safe locator only).

**Approach:** Compare inventory entries with file presence, checksum, and receipt date. Reconcile the 2026-10-08 Miro and transcript paths absent from the root private inventory. Preserve the existing false semantic-validation receipt. Record an absent file only after checking the canonical private directory and dated batch inventories.

**Verification:** Every source used later has an exact version and an inventory locator; no original bytes changed and no private file is tracked.

### U2. Certify each visible process claim

**Goal:** Produce a complete source-to-claim decision for the current lead and deal maps.

**Requirements:** R2, R3, R4. Covers AE1-AE4.

**Dependencies:** U1.

**Files:** `docs/ppo/source-status.md`, the private review ledger, `docs/ppo/lidy/karta-lidy.html`, `docs/ppo/sdelki/karta-sdelki.html`, `docs/ppo/index.html` (read-only inputs at this unit).

**Approach:** Inventory all visible assertions, not only `pasport-*` rows. Compare each with the latest board, answer file, original CSV/JPG, and relevant transcript/recording visual locator. Use the actual client wording in private review only; publish safe IDs and statuses. For a conflicting or unsupported assertion, state the exact gap and the decision to downgrade, relocate, or remove it from the current process.

**Verification:** The reviewer can follow every map assertion to a reviewed client source or a visible uncertainty label; no transcript-only or silent-video speech claim is upgraded to `PROVEN`.

### U3. Reconcile and rebuild the HTML maps

**Goal:** Make the owner-facing pages reflect the reviewed claim decisions.

**Requirements:** R4, R5, R6.

**Dependencies:** U2.

**Files:** Relevant `docs/ppo/lidy/_parts/`, `docs/ppo/sdelki/_parts/`, `docs/ppo/_common/` parts, generated `docs/ppo/index.html`, `docs/ppo/lidy/karta-lidy.html`, `docs/ppo/sdelki/karta-sdelki.html`, and `docs/ppo/source-status.md`.

**Approach:** Change only parts whose claim decision requires it, run the existing builder, and retain the historical notice on `docs/ppo/ppo-eurosteklo.html`. Keep unresolved items in their question/survey location rather than presenting them as accepted process.

**Verification:** The built pages show the reviewed statuses and retain existing links and page anchors.

### U4. Review, verify, and deliver

**Goal:** Provide an evidence-backed handoff without exposing client originals.

**Requirements:** R1-R6.

**Dependencies:** U3.

**Files:** `docs/ppo/source-status.md`, `docs/review/` dated review record, and the changed PPO files from U3.

**Approach:** Perform a separate source/contradiction review, run the existing PPO and browser checks on the actual local pages, inspect the exact Git diff for private content, then use the project's guarded `ship-post` submission and remote delivery path. Report unresolved points explicitly.

**Verification:** The review, build, navigation, privacy, and exact-head GitHub receipts agree with the delivered pages.

## Verification Contract

1. Source check: compare the inventory and actual private files by path and checksum; record a short `SOURCE_PASSPORT=PASS` line only after every used file matches. This is a real check on the supplied local material, not a synthetic fixture.
2. Claim check: independently verify every retained current-process assertion against its actual cited source, then verify that the claim inventory covers every visible process assertion. Record `CLAIM_COVERAGE=PASS` and `SOURCE_MEANING=PASS` separately; no row count alone proves meaning. Any unsupported current-process assertion makes `SOURCE_MEANING` fail until corrected or removed from the certified process.
3. Build and navigation: `python3 docs/ppo/build_all.py && python3 docs/ppo/check_ppo.py --lidy` must exit 0 and report `итого: ошибок 0`; open `docs/ppo/index.html` in a local browser and confirm the lead, deal, and linked question pages open without broken navigation or console errors.
4. Privacy and delivery: `git diff --check` exits 0; `git ls-files client-materials/private` prints nothing; the ZIP CRC still passes if the archive is touched; verify the submitted commit is reachable from remote `main` and the PR is merged before claiming GitHub delivery.

## Definition of Done

All supplied inputs needed by the retained current-process assertions have verified identity; every visible process assertion has a reviewed source decision; unsupported assertions are not represented as confirmed; HTML navigation and builder checks pass on the real pages; confidential originals remain untracked; the developer can access the exact delivered revision. If a material current-process assertion cannot be resolved from supplied evidence, do not claim full currentness: publish the precise unresolved item and keep source certification open until the owner supplies the needed source or approves its removal from the certified process.
