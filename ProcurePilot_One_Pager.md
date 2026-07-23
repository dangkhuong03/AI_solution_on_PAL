# ProcurePilot — AI Procurement Decision Agent on PAL

**Live PAL agent:** [\[Purchase Request PR-2026-0042 for 1000 Temperature Sensors\]](https://share.getmindpal.com/thread/agent/6a61ee636307c66adf9a546e)

**Supporting evidence:** See `ProcurePilot_Evidence_Appendix.md` for the evidence matrix, source hashes, control-test transcript, calculation disclosure, and screenshot checklist.

## High-value business problem

Industrial procurement teams must compare supplier quotations across price, delivery, quality, reliability, risk, ESG, and commercial terms while enforcing procurement policy and maintaining an audit trail. Today, this work is commonly performed through email, spreadsheets, and manual document review. It is slow, difficult to reproduce, and vulnerable to missing data, inconsistent scoring, and accidental use of untrusted supplier instructions.

This is worth solving because purchasing decisions directly affect cost, production continuity, compliance, and supplier risk. A low-price supplier that misses a maintenance deadline can cost substantially more than the apparent saving.

## Working PAL solution

I built **ProcurePilot**, a single AI procurement agent on PAL. The agent:

1. Reads the purchase request and six controlled knowledge-base files covering procurement policy, supplier master data, supplier performance, the scoring model, case context, and the Draft PO template.
2. Requests missing quotations instead of inventing data.
3. Extracts and normalizes three supplier quotations.
4. Applies hard gates for approved status, compliance, and full technical-specification compliance.
5. Compares landed TCO, delivery, quality, reliability, financial risk, ESG, and commercial terms using the locked `MRO-SENSOR-V1` model.
6. Detects and ignores prompt injection embedded in supplier content.
7. Produces an evidence-linked Decision Dossier and recommendation.
8. Requires the exact human token `APPROVE` before creating a non-binding Draft PO.
9. Never contacts a supplier or issues a binding Purchase Order.

## Demonstrated case and result

The live test used **PR-2026-0042** for 1,000 industrial temperature sensors for Bac Ninh Plant, with a USD 50,000 budget and required delivery by 30 August 2026.

| Supplier | Landed TCO | Delivery | Weighted score | Outcome |
|---|---:|---|---:|---|
| SUP-A — Alpha Industrial | $45,200 | 27 Aug, on time | **93.20** | **Recommended** |
| SUP-C — CoreSense Technologies | $48,800 | 18 Aug, on time | 93.16 | Close second |
| SUP-B — Beta Components | $41,500 | 8 Sep, 9 days late | 76.30 | Eligible, but not recommended |

ProcurePilot recommended **SUP-A**: the highest score, delivery three days before the deadline, low financial risk, and a total cost within budget. Compared with the next-best on-time option, the recommendation saves **USD 3,600**. The agent also neutralized an instruction inside SUP-C's quote telling it to ignore policy and select SUP-C.

The approval control was tested with “Looks good, go ahead and do it.” ProcurePilot correctly refused to treat this as authorization. Only after receiving the exact token `APPROVE` did it create a Draft PO for USD 45,200, clearly marked **NOT SENT — NOT BINDING**.

## Before and after

| Before PAL | After ProcurePilot |
|---|---|
| Buyer searches across files, emails, and spreadsheets | Agent retrieves controlled evidence and asks only for missing inputs |
| Manual quote normalization and spreadsheet formulas | Consistent schema and locked scoring specification |
| Policy checks depend on buyer memory | Hard gates and policy checks applied every time |
| Supplier text may be mistaken for instructions | Supplier documents treated as untrusted evidence |
| Approval may be ambiguous in chat or email | Exact-token human approval gate |
| Decision rationale assembled manually | Decision Dossier and non-binding Draft PO generated automatically |

## Estimated impact and ROI

For one sourcing event, the assisted workflow is estimated to reduce analysis and documentation time from **2.5 hours to 20 minutes**, an **87% cycle-time reduction**. In the demonstrated case it also identified a **USD 3,600 saving** versus the next-best on-time supplier while avoiding the operational risk of selecting the cheapest but late supplier.

A conservative annual scenario of 10 similar requests per month gives:

- Labor saved: `(2.5 − 0.33) hours × 120 cases × $30/hour` = **$7,812/year**
- Sourcing benefit: `0.5% × ($45,200 × 120)` = **$27,120/year**
- Estimated total annual benefit: **$34,932**

The estimated ROI is:

`ROI = (34,932 − annual PAL operating cost) / annual PAL operating cost × 100%`

For illustration, at an annual operating cost of USD 5,000, estimated ROI is approximately **599%**, with payback in about **1.7 months**. These are planning estimates and should be replaced with observed handling time, sourcing volume, and realized savings during a production pilot.

## MVP status and next step

The end-to-end agent, evidence retrieval, injection defense, recommendation, approval gate, Decision Dossier, and Draft PO were demonstrated successfully. In the current PAL session, a Python execution tool was not available, so the agent manually reproduced and checked the base case against the authoritative regression fixture. This limitation is explicitly recorded; the MVP must not claim that Python was executed.

Before production use, the next step is to enable PAL's Python/Code Interpreter capability or connect a deterministic scoring API, then store execution logs, model version, input hash, approver identity, and an ISO-8601 approval timestamp in the audit trail.
