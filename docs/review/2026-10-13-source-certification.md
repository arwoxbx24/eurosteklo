# Source decision review — 2026-10-13

Status: `PROVEN` for one written-answer row only; the lead and deal maps as complete current processes remain `UNVERIFIED`.

## Scope and source boundary

- Reviewed 114 visible map blocks in the private claim ledger: 20 current-process rows, 43 historical-source comparisons, and 51 navigation or nonprocess blocks.
- Compared current rows with the two 4 October recordings, their transcript locators, the 8 October written answers and Miro export, and the earlier CSV and five JPGs. The recordings' transcript validation remains `semantic_acceptance=false` for both; transcript text alone is not accepted as audio proof.
- Current-row decisions: 1 `PROVEN` from an exact written client answer, 1 `CONTRADICTED` between historical and later source material, and 18 `UNVERIFIED` composite rows. See `docs/ppo/source-status.md` for safe row IDs, locators, and limits. No unresolved row is certified as implemented portal behavior.
- Original client material and full claim text stay in `client-materials/private/`. This record contains no client answer text or personal data.

## Independent contradiction check

- The channel conflict remains visible in row `pasport-L2`; it is not resolved by selecting one source without client confirmation.
- The one `PROVEN` row, `pasport-L5`, is limited to the exact written answer. It does not certify configured CRM behavior.
- Composite stage, role, timing, and automation assertions retain `UNVERIFIED` labels where the supplied evidence does not settle the entire row.

## Acceptance boundary

The maintained passport parts and generated pages carry these decisions. `python3 docs/ppo/check_ppo.py --lidy` reported zero errors and one warning; local Chromium navigation opened both maps and their linked question pages with no page errors. The archive CRC check reported no errors. These checks prove build and navigation, not full process agreement. Source identity, claim coverage, and guarded local submission receipts are recorded separately in the private goal evidence log.
