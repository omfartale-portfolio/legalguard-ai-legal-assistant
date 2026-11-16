# Contract review and redlining

LegalGuard is described as supporting contract review with clause-level suggestions, redlining workflows, drafting from a pre-approved clause library, an auditor pass/self-check and a contract risk dashboard. This page turns those capabilities into a reviewable workflow. It does not assert that every step or control is implemented as written.

## Review flow

1. **Establish context.** Identify the document type, parties, business purpose, governing law and review instructions. The product’s supported intake fields and document types are **to be documented**.
2. **Review by clause.** Organize observations around the relevant provision. For each observation, a useful reviewer-facing record includes the clause reference, quoted text, issue, why it matters, proposed change, rationale and open question. Whether LegalGuard displays every field is **to be documented**.
3. **Offer a bounded suggestion.** A suggestion should be tied to the source text and stated review objective. It should distinguish a drafting preference from a legal requirement, identify assumptions, and preserve uncertainty for review. Actual generation and citation behavior are **to be documented**.
4. **Draft from approved language when appropriate.** The described clause library can be presented as a source of pre-approved wording. Library owners, approval authority, scope, versioning and fallback behavior are **to be documented**. Do not imply that a suggested clause is approved for every deal or jurisdiction.
5. **Prepare a redline for human review.** Show additions and deletions alongside the original clause, plus a concise reason. A human checks that the edit matches the instruction, preserves intended commercial meaning and does not introduce unsupported commitments. The actual redline format and editing interface are **to be documented**.
6. **Run checks, then decide.** An auditor pass/self-check is described. Its criteria, source material, limitations, and handling of a failed or inconclusive check are **to be documented**. A designated human reviewer accepts, edits, rejects or escalates each material suggestion before any external use.
7. **Record the disposition.** A useful review record distinguishes accepted, changed, rejected and unresolved suggestions. Whether the system records reviewer identity, rationale, versions or timestamps is **to be documented**.

## Synthetic illustration

**Fictional clause:** “Either party may terminate for convenience on 10 days’ notice.”

**Illustrative issue:** The notice period may be shorter than the business team expects. This is a negotiation or policy question, not a legal conclusion.

**Illustrative suggestion:** Ask the business owner to confirm the intended notice period. If an example redline is needed, use placeholder wording and label it as a proposal pending approval.

No real contract, party, company position or jurisdiction is represented here. The example demonstrates how to make an issue visible and actionable without claiming an outcome or a live product screen.

## Risk dashboard framing

The described contract risk dashboard should help a reviewer locate and prioritize open issues. To make the description auditable, document what a risk label means, which inputs affect it, how reviewers can challenge it, whether it is advisory, and how unresolved issues are shown. No scoring scale, weighting or measured risk reduction has been provided.

## Details to confirm

- Supported agreement types, formats and clause taxonomy.
- User role, review criteria and escalation path.
- Clause library governance, approved jurisdictions and version history.
- Redline and comment outputs, review state and audit trail.
- Auditor/self-check rules and known limitations.
- Dashboard labels, logic, intended users and meaning.
- Which parts are live, manual, experimental or planned.
