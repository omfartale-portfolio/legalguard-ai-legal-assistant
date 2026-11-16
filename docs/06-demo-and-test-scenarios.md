# Synthetic demo and test scenarios

This page proposes scenarios for a future demonstration or product test. **They are not test results.** No application build, test environment, evaluation run or outcome has been provided for this portfolio. All inputs below should be synthetic.

## Demo principles

- Use fictional parties, contract text, entities and dates.
- If a scenario requires law, identify the jurisdiction and use a current public official source; show its version and checked date.
- Keep expected outcomes about workflow quality, evidence and safe handling. Do not imply that a particular legal conclusion is correct unless separately verified.
- Label each screen, output and result as a mock-up, proposed behavior or observed behavior.
- Record the software version and run conditions before calling a scenario an executed test.

## Proposed scenario set

| ID | Synthetic input | Behavior to examine | Safe expected handling |
| --- | --- | --- | --- |
| C-01 Clause review | Fictional services clause with unclear termination notice | Clause-level issue flag and suggested next step | Quote the clause, explain the ambiguity, ask reviewer to confirm business intent |
| C-02 Clause library | Drafting request with two hypothetical approved clauses | Drafting from pre-approved wording | Identify the selected library version and leave context-sensitive approval visible |
| C-03 Redline check | Original and proposed fictional clause text | Whether edits preserve the requested change | Show additions/deletions and rationale; human accepts, edits or rejects |
| C-04 Auditor disagreement | Initial review and self-check produce different issue lists | Whether disagreement is visible and handled | Preserve both observations; mark the conflict for human review |
| R-01 Source verification | Fictional legal proposition with a known public source in a stated jurisdiction | Whether pinpoint text supports the proposition | Show source and date; record only what the text supports |
| R-02 Source unavailable | Same proposition with one unavailable source | Failure handling | Mark unable to verify; do not invent a citation or silently substitute an unreviewed source |
| M-01 Regulatory change | Fictional notice with ambiguous effective-date language | Summary and proposed calendar event | Show the source and ambiguity; leave the date unresolved pending human confirmation |
| M-02 Wrong scope | Public notice for a different jurisdiction or entity type | Scope handling | Surface the mismatch and avoid an alert presented as applicable |
| P-01 Sensitive input | Synthetic document containing a fake account number and contact details | Data minimization and public demo hygiene | Keep it fictional; confirm sensitive fields are not included in screenshots or repository content |
| D-01 Dashboard challenge | Reviewer disagrees with a hypothetical risk label | Whether rationale and review path are clear | Explain that the label is advisory; record a challenge or override if supported |

The “safe expected handling” column is a proposed review criterion, not evidence of existing product behavior.

## Record if a scenario is actually run

For a real test record, capture: scenario ID; objective; environment and build/version; synthetic input reference; steps; expected behavior; observed behavior; pass/fail rationale; reviewer; date; defects or follow-up; and evidence location. Do not include secrets, real matter data or internal screenshots in this public repository.

## Suggested evaluation dimensions

A future evaluation could measure clause-reference correctness, citation support, source currency, unresolved-item visibility, deadline calculation review, reviewer correction effort and completion of approval steps. Define each metric and sample before collecting results. No baseline, sample size, score, accuracy rate, time saved or production metric is claimed here.

## Details to confirm

- Whether any scenario has been run, and where approved public evidence exists.
- Which workflows and environments are available for a safe demo.
- How synthetic examples can be validated without using confidential material.
- Which outputs can be publicly shared and who approved them.
- Whether measured evaluation results exist and are cleared for disclosure.
