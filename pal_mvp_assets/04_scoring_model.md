# Supplier Scoring Model — MRO-SENSOR-V1

This file is the authoritative scoring specification. MindPal must execute the exact
formulas below through Execute Python. The LLM must not invent, reinterpret, normalize,
or replace any formula.

## Hard gates

1. Supplier status must be APPROVED.
2. Compliance status must be PASS.
3. Technical specification compliance must be FULL.

## Weighted score

| Criterion | Weight |
|---|---:|
| Landed total cost | 30% |
| Delivery | 20% |
| Quality | 15% |
| On-time reliability | 15% |
| Financial/compliance risk | 10% |
| ESG | 5% |
| Commercial terms | 5% |

Python is the calculation authority. The LLM must not change weights or authoritative numeric results.

## Score conventions

- `landed_tco = unit_price × requested_quantity + freight`
- `cost_score = round(lowest_eligible_tco / supplier_tco × 100, 2)`
- `late_days = max(0, delivery_date - required_date)`
- `delivery_score = max(0, 100 - 8 × late_days)`
- `risk_score = {"LOW": 100, "MEDIUM": 65, "HIGH": 20}`
- `payment_score = min(60, payment_terms_days / 45 × 60)`
- `warranty_score = min(40, warranty_months / 36 × 40)`
- `commercial_score = payment_score + warranty_score`
- `weighted_score = round(cost_score×0.30 + delivery_score×0.20 + quality_score×0.15 + on_time_delivery_pct×0.15 + risk_score×0.10 + esg_score×0.05 + commercial_score×0.05, 2)`

All component scores are absolute except `cost_score`, which uses the ratio to the
lowest eligible TCO in the current comparison set. Do **not** use min-max
normalization for cost, risk, quality, delivery, ESG, or commercial terms.

## Base-case regression fixture

For PR quantity 1,000 and required date 2026-08-30, using the supplier and quote files
in this demo, Execute Python must return:

| Supplier | TCO | Cost score | Delivery score | Commercial score | Weighted score |
|---|---:|---:|---:|---:|---:|
| SUP-A | 45,200.00 | 91.81 | 100.00 | 66.6667 | **93.20** |
| SUP-B | 41,500.00 | 100.00 | 28.00 | 80.0000 | **76.30** |
| SUP-C | 48,800.00 | 85.04 | 100.00 | 80.0000 | **93.16** |

If the calculated scores differ from these values for the same inputs, return
`CALCULATION_VERSION_MISMATCH` and do not issue a recommendation.
