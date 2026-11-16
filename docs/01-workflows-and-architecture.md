# Workflows and conceptual architecture

This document describes the LegalGuard capabilities provided for this portfolio and a clear way to explain their relationship. The flow below is a **documentation model**, not a verified diagram of the software’s internal architecture. No language, model, database, service, integration or deployment platform has been confirmed.

## Confirmed description

LegalGuard is described as an AI-powered legal automation tool used in a legal/compliance context. The described capabilities are contract review with clause-level suggestions, drafting from a pre-approved clause library, redlining workflows, an auditor pass/self-check, a regulatory watcher, compliance calendar and deadline alerts, a contract risk dashboard, and a verification layer checked against 30–40 curated legal sources. Human review and risk controls are also part of the brief.

These are user-described capabilities, not claims of current availability, adoption, accuracy or production status.

## Conceptual workflow

1. **Work item enters a workflow.** A reviewer starts from a contract, a drafting request, a regulatory item or a compliance obligation. Actual supported file types, intake steps and access permissions are **to be documented**.
2. **Relevant material is identified.** Contract work is organized at clause level; legal research is related to a curated source set. The actual extraction, search and retrieval methods are **to be documented**.
3. **The tool proposes a result.** Examples include issue flags, clause-level suggestions, a draft based on pre-approved language, a redline, or an obligation/deadline item. The exact behavior and limits of each feature are **to be documented**.
4. **Checks and verification are applied.** The described auditor pass/self-check and legal-source verification are intended quality steps. Their rules, coverage and handling of a failed check are **to be documented**.
5. **A human reviews and decides.** A qualified reviewer checks the relevant text, context and evidence, then accepts, edits, rejects or escalates the proposal. The user’s authority and the audit trail are **to be documented**.
6. **Operational follow-through is tracked.** A described risk dashboard, regulatory watcher, compliance calendar and deadline alerts help surface matters for attention. How items are assigned, updated and closed is **to be documented**.

## Capability map

| Workflow | Described output | Important unknowns |
| --- | --- | --- |
| Contract review | Clause-level analysis and suggestions; risk dashboard | Contract types, scoring logic, review rubric |
| Drafting/redlining | Proposed language from an approved clause library; proposed edits | Approval and versioning of clause library; compare format |
| Research verification | Checks against 30–40 curated legal sources | Source inventory, jurisdiction and version controls, evidence format |
| Regulatory operations | Watcher, calendar entries and deadline alerts | Monitored sources, update cadence, deadline rules and ownership |
| Quality and oversight | Auditor pass/self-check and human review | Check criteria, exceptions, approval gates and audit records |

## Data and trust boundaries to document

A useful architecture account should identify what information enters the system, what is stored, who can access it, what is sent to any external service, how long information is retained, and how deletion works. It should distinguish public legal material from confidential contract content. These details were not supplied and must not be inferred.

The portfolio uses synthetic scenarios only. It contains no real contract, internal policy or legal matter.

## Details to confirm

- Product status and the time period in which each capability was used.
- The author’s role and ownership of design, workflow or implementation.
- Actual architecture, components, models, languages, integrations and deployment.
- Intake formats, access control, retention and data-handling rules.
- Reviewer roles, exception paths, audit trail and approval points.
- Which capabilities are live, experimental, manual or planned.

Until confirmed, treat the sequence above as a conceptual explanation only.
