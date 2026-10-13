# Documentation directory guide

Placement rules: [Eurosteklo directory contract](../PROJECT-STRUCTURE.md). Current client-source locations and limits: [source locator](SOURCE-REGISTER.md). Archived members and restore route: [archive register](archive/README.md).

Inventory date: 2026-10-13. Source: `git ls-files docs`, the immediate directory names, and the project `AGENTS.md`. This guide describes where files are stored; it does not certify their process claims as current.

| Directory | Observed role | Currentness |
| --- | --- | --- |
| `archive/` | PROVEN: one ZIP containing two dated, one-off plans from 1 October 2026. See the archive decision below. | Historical; not a source of current process truth. |
| `as-is/` | PROVEN: five tracked notes and frame records (`git ls-files docs/as-is`). | UNVERIFIED for the latest client answers. |
| `idei/` | PROVEN: five tracked agent idea files (`git ls-files docs/idei`). | UNVERIFIED as client requirements. |
| `meetings/` | PROVEN: seventeen tracked meeting and variant files (`git ls-files docs/meetings`). | UNVERIFIED beyond each dated source. |
| `package/` | PROVEN: five numbered Markdown files (`git ls-files docs/package`). | Client approval UNVERIFIED. |
| `plans/` | PROVEN: ten tracked plans after the archive move (`git ls-files docs/plans`). | UNVERIFIED as completed work. |
| `ppo/` | PROVEN: seventy tracked source, HTML, map, and build files (`git ls-files docs/ppo`). Start at [the HTML index](ppo/index.html). | Map claim verification against both recordings is UNVERIFIED. |
| `process/` | PROVEN: twenty-five tracked notes, parts, work files, and BPMN assets (`git ls-files docs/process`). | Process truth UNVERIFIED. |
| `research/` | PROVEN: eight tracked research records (`git ls-files docs/research`). | Client approval UNVERIFIED. |
| `review/` | PROVEN: fifty-eight tracked review records (`git ls-files docs/review`). | Currentness UNVERIFIED. |
| `solutions/` | PROVEN: one tracked workflow issue record (`git ls-files docs/solutions`). | Process relevance UNVERIFIED. |
| `specifications/` | PROVEN: three tracked specifications (`git ls-files docs/specifications`). | Client process truth UNVERIFIED. |
| `tz/` | PROVEN: task specifications including the interim release and directory-contract passports. | Implementation acceptance UNVERIFIED. |

The launch checkout also has an empty, untracked `business-processes/` directory. No tracked `packet/`, `is/`, or singular `meeting/` directory exists. The requested “packet” is most likely the observed `package/`; “is” most likely refers to `as-is/`, but those name interpretations are INFERRED from the directory list. No rename is justified by the supplied files.

The standalone [`ppo-eurosteklo.html`](ppo/ppo-eurosteklo.html) is a 28 September 2026 edition and is outside the current generator. The HTML index points to the lead and deal working maps. [Source status](ppo/source-status.md) records why their overall currentness is UNVERIFIED. Neither page age nor a generated link establishes current client approval.

## Archive decision

The two one-off plans `2026-10-01-0859-chore-soobshchenie-agentam-vypolnenie-plan.md` and `2026-10-01-1544-chore-aktualizatsiya-hvosty-plan.md` were moved from `plans/` into [`2026-10-13-history.zip`](archive/2026-10-13-history.zip). Both had zero inbound path and basename references in tracked `docs/`; a bounded scan found no email address, phone number, secret assignment, or private-material path. `unzip -t` reported no errors before the source copies were removed. Other dated review folders and a dated plan have inbound references from tracked specifications (`git grep -l` counts: 41, 3, and 2 respectively), so they remain at their referenced paths. No zero-byte or byte-identical duplicate tracked `docs/` file was found in the bounded inventory.
