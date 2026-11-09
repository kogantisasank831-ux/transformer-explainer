# Project Logic — AI and Data Science Interview Cheat Sheets

**Last reviewed:** 9 November 2026  
**Owner:** repository owner  
**Audience:** AI/ML interview candidates with beginner-to-senior depth requirements  
**Review triggers:** a new batch; a material framework/model change; a reported technical error; or six months since the last review

## Scope

This component maintains concise, independent revision sheets and a master interview syllabus. It does not change the transformer explainer application or its build/runtime behavior.

## Documentation rules

| ID | Rule | Acceptance evidence |
|---|---|---|
| CHEAT-001 | Each sheet must support quick revision and deeper interview discussion. | Thirty-second revision, core sections, rapid Q&A, lead case, final checklist |
| CHEAT-002 | Explain intuition, essential math/code, use, trade-offs, and failure modes. | Topic review against the master index |
| CHEAT-003 | Keep Markdown as the canonical source. | Combined PDF/DOCX are generated from the same Markdown set |
| CHEAT-004 | Prefer official documentation and primary papers for unstable claims. | Primary references section in technical sheets |
| CHEAT-005 | Validate executable-looking Python examples at least for syntax. | `VALIDATION.md` records block count and result |
| CHEAT-006 | Verify combined documents structurally and visually. | DOCX archive check, PDF metadata/text check, representative-page render review |
| CHEAT-007 | Avoid unqualified tool recommendations. | Library maps explain purpose and require workload/version/license checks |
| CHEAT-008 | Keep batch and active-work state explicit. | Root README plus `WORK_PROGRESS.md` |

## Content pattern

Use the following pattern where it helps the topic:

1. target role and boundary;
2. thirty-second revision;
3. definitions and mental model;
4. formulas, shapes, syntax, or pseudocode;
5. decision/trade-off tables;
6. failure modes and debugging;
7. production or lead-level case;
8. rapid questions and answers;
9. final checklist;
10. primary references.

The pattern is guidance rather than a reason to repeat low-value sections.

## Generation and update flow

1. Select a bounded batch from `MASTER_INDEX.md`.
2. Draft each Markdown sheet against its role expectations.
3. Check topic coverage, internal consistency, code fences, and Python syntax.
4. Generate combined DOCX and A4 PDF from the ordered Markdown sources.
5. Inspect the cover, every section start, representative dense pages, and final page.
6. Record validation evidence and publish Markdown plus combined download links.

## Evidence boundary

Passing syntax and document checks does not prove framework runtime compatibility, benchmark performance, model quality, or production safety. Those require a pinned environment and workload-specific tests.

