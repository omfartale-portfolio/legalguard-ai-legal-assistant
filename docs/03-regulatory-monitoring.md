# Regulatory monitoring and compliance deadlines

LegalGuard is described as including a regulatory watcher, a compliance calendar and deadline alerts. This page explains how those functions can be discussed without claiming a particular jurisdiction, source feed, update schedule or production result. None of those implementation details were supplied.

## Monitoring workflow

1. **Define scope.** Record the jurisdiction, regulator, topic, entity type and obligation that matter. A watcher without a defined scope can surface irrelevant or incomplete changes. Supported scope and configuration are **to be documented**.
2. **Identify an authoritative public source.** For any future demo or real use, link to the official publisher and the specific instrument or notice. Record jurisdiction, title, publication/effective dates and the date checked. The actual sources in LegalGuard’s watcher are **to be documented**.
3. **Compare a new item with the prior known version.** State what changed, where it changed and whether the comparison is complete. The product’s change-detection method, polling or alert cadence and version history are **to be documented**.
4. **Summarize with uncertainty visible.** Separate the source’s text from a plain-language summary, possible impact and questions for counsel. Do not convert an ambiguous effective date or applicability rule into a definitive obligation without review.
5. **Route to an owner.** A human confirms relevance, applicability, action and responsible owner. Escalate uncertain or material items. Assignment and approval behavior are **to be documented**.
6. **Track follow-up.** If a confirmed item creates a deadline, capture its source, rationale, owner, due date, time zone, status and next review date. The described calendar and alerts may support follow-through; exact fields and alert behavior are **to be documented**.

## Calendar and alert quality

A deadline is only useful if its origin and assumptions can be checked. A future portfolio demo should show the source text, the event that starts the clock, any calculation assumptions, the responsible reviewer and a way to correct or dismiss the item. If the deadline cannot be established from the cited source and known facts, mark it **unresolved** and ask for review instead of guessing.

The contract risk dashboard and compliance calendar are separate described capabilities. Any relationship between them, including shared records or common prioritization, is **to be documented**.

## Synthetic scenario

A fictional public notice appears to change a reporting date. The watcher summary flags the relevant passage and links to a fictional official notice. A reviewer checks the effective date, applicability and any transition language, then confirms or rejects the proposed calendar item. If the source page does not establish when the obligation applies, no definite due date is recorded.

This scenario is illustrative only. It uses no real law, regulator, customer or deadline and reports no actual monitoring result.

## Details to confirm

- Supported jurisdictions, regulators, topics and entity scopes.
- Exact public source inventory, curation process and update cadence.
- How changes are detected, compared, dated and linked to prior versions.
- How applicability and effective dates are summarized and reviewed.
- Calendar fields, time zone behavior, reminders, ownership and escalation.
- Handling of missed updates, unavailable sources, conflicting texts and false alerts.
- Whether items are tracked through completion and who approves closure.
- Feature status and any user-visible limits.
