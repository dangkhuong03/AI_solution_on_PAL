# ProcurePilot — Source Audit and Bug-Fix Report

## Verdict

| Issue | Source/config bug? | Verdict |
|---|---|---|
| 1. Score discrepancy | **Yes — implementation drift** | Exact quote and supplier inputs match local fixture; live run did not use the exact local commercial-score formula |
| 2. Urgent 200 units appears early | **Yes — two source leaks** | Scenario was in `05_demo_case_context.md`, and calculator `__main__` printed the 800/200 split unconditionally |
| 3. Conversational approval accepted | **Yes — prompt enforcement bug** | Prompt stated the rule but did not define a strict full-message grammar or rejection response |
| 4. Draft PO fields omitted | **Yes — prompt/config bug** | Template lacked explicit Approver note; Desired Output did not require exact template fields; local existence cannot prove MindPal upload |

Prompt-injection handling was not changed.

## Issue 1 — Score discrepancy

### Definitive diagnosis

This is **not a data difference**:

- The three live quotes exactly match `demo_payload`.
- Supplier master and performance values match the local CSVs.
- The local calculator returns A=93.20, C=93.16, B=76.30.

It is an **implementation difference between the local calculator and the calculation
executed in MindPal**.

The current code uses only one relative normalization:

```text
cost_score = lowest eligible TCO / supplier TCO × 100
```

It does not use min-max normalization.

The live deltas are:

- A: +1.17
- C: +1.00
- B: -1.00

With commercial terms weighted at 5%, those deltas are explained almost exactly if
the live implementation used commercial scores near A=90, C=100, B=60, instead of
the local code's A=66.6667, C=80, B=80. The old `04_scoring_model.md` said only
"payment terms score up to 60 plus warranty score up to 40" and did not specify the
exact sub-formulas. MindPal therefore had room to reinterpret the calculation.

### Fix

- `04_scoring_model.md`: now contains every exact formula, prohibits min-max
  normalization, and includes a base-case regression table.
- `procurepilot_calculator.py`: now returns `algorithm_id` and per-criterion score
  contributions, and runs `assert_demo_regression()`.

### Deployment action

Replace the MindPal Execute Python code with the updated
`procurepilot_calculator.py`. Re-upload/relearn `04_scoring_model.md`. Do not ask the
LLM to recreate the scoring code from prose.

Expected base result:

```text
SUP-A 93.20
SUP-C 93.16
SUP-B 76.30
```

## Issue 2 — Adaptive scenario leakage

### Diagnosis

`05_demo_case_context.md` explicitly contained the urgent 200-unit scenario. Since
that file is a Knowledge Source, the agent correctly retrieved it too early.

The calculator also unconditionally ran and printed:

```python
calculate_split(demo_payload["quotes"], {"SUP-A": 800, "SUP-C": 200})
```

when the full script was executed. Either source was sufficient to leak the adaptive
answer. This was source leakage, not autonomous inference.

### Fix

The adaptive scenario has been removed from the KB. The calculator's base
`__main__` execution no longer calls `calculate_split`. The function remains
available and must be called only after the user explicitly introduces the urgent
quantity/allocation constraint.

The KB file now contains only the base PR and an explicit boundary: no urgent
quantity, earlier deadline, downtime cost or split award may be assumed unless the
user introduces it in the current conversation.

The demo script/blueprint may still describe the future user message because those
documents are builder instructions, not agent Knowledge Sources.

## Issue 3 — Strict approval

### Diagnosis

The old prompt said only APPROVE authorizes a Draft PO, but it did not define:

- entire trimmed message equality;
- case sensitivity;
- examples of rejected conversational affirmations;
- the required response when approval is ambiguous.

An LLM optimizing for user intent therefore treated “Looks good, go ahead and do it”
as approval.

### Fix

The System Prompt now defines approval as a strict literal-token protocol. Only an
entire trimmed, case-sensitive message equal to `APPROVE` changes state to APPROVED.
All other positive/ambiguous responses keep the state PENDING and trigger an explicit
instruction to use `APPROVE`, `REVISE: ...`, or `REJECT: ...`.

## Issue 4 — Draft PO completeness

### Diagnosis

- `06_draft_po_template.md` was listed in the blueprint as a required Knowledge
  Source, but a local file does not prove it was uploaded and assigned in MindPal.
- The template did not explicitly contain an `Approver note` field.
- Desired Output only said “Draft PO”, without requiring exact adherence to the
  template field list.

### Fix

- Added `Approver note` to the template.
- Added a MindPal upload manifest to the blueprint.
- Desired Output now requires the exact full field list, evidence references,
  `UNKNOWN` for unavailable fields, and a complete section per supplier in a split
  award.

## Paste-ready System Prompt replacement

Replace the existing `HUMAN CONTROL` block with:

```text
HUMAN CONTROL
Approval is a strict literal-token protocol, not an intent-classification task.
Create a Draft PO only when the user's entire trimmed message is exactly:
APPROVE

The token is case-sensitive. Any other message is NOT approval, including:
"Looks good", "go ahead", "do it", "yes", "approved", "proceed",
"APPROVE please", or a message that merely contains the word APPROVE.

For any positive or ambiguous conversational response that is not the exact token,
keep Human decision=PENDING, do not create or populate any Draft PO, and reply:
"To authorize Draft PO creation, reply with the exact token APPROVE.
Otherwise use REVISE: <instruction> or REJECT: <reason>."

REVISE: <instruction> requires re-analysis and a new recommendation.
REJECT: <reason> closes the recommendation without a Draft PO.
The Draft PO must say: FOR DEMONSTRATION ONLY — NOT SENT — NOT BINDING.
```

Replace the Draft PO portion of `Desired Output Format` with:

```text
11. Draft PO (only when Human decision=APPROVED after the exact token APPROVE)

When approved, follow the Knowledge Base file 06_draft_po_template.md exactly.
For every supplier PO, include every field below; do not omit a field:
- PR reference
- Supplier
- Item/specification
- Quantity
- Unit price
- Freight
- Total
- Delivery date
- Delivery location
- Payment terms
- Warranty
- Recommendation reference
- Human decision
- Approver note ("Exact APPROVE token received in the current chat")
- Evidence references, including relevant [KB: ...], [QUOTE: ...], and
  [PYTHON: MRO-SENSOR-V1] references

If any required PO field is unavailable, write UNKNOWN and keep the Draft PO
incomplete; never silently omit the field. For a split award, create one complete
Draft PO section per supplier and repeat the full field list for each.
```

## Consistency confirmation

- `05_demo_case_context.md` is now consistent with the base-case-first demo. No other
  agent Knowledge Source should contain the urgent 200-unit constraint.
- `06_draft_po_template.md` is consistent with the strengthened Desired Output.
- The blueprint's adaptive demo still works because the user supplies that constraint
  later in chat.
- Prompt-injection policy and quote content are unchanged.
