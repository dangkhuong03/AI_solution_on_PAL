from datetime import date
from typing import Any

MODEL_VERSION = "MRO-SENSOR-V1"
ALGORITHM_ID = (
    "cost-ratio|delivery-minus-8-per-day|risk-100-65-20|"
    "commercial-linear-60-40|weighted-v1"
)
WEIGHTS = {
    "cost": 0.30,
    "delivery": 0.20,
    "quality": 0.15,
    "reliability": 0.15,
    "risk": 0.10,
    "esg": 0.05,
    "commercial": 0.05,
}
RISK_SCORE = {"LOW": 100.0, "MEDIUM": 65.0, "HIGH": 20.0}


def _days_late(delivery_date: str, required_date: str) -> int:
    delivery = date.fromisoformat(delivery_date)
    required = date.fromisoformat(required_date)
    return max(0, (delivery - required).days)


def _commercial_score(payment_days: int, warranty_months: int) -> float:
    payment = min(60.0, payment_days / 45.0 * 60.0)
    warranty = min(40.0, warranty_months / 36.0 * 40.0)
    return payment + warranty


def calculate(payload: dict[str, Any]) -> dict[str, Any]:
    quantity = int(payload["quantity"])
    required_date = payload["required_date"]
    suppliers = {row["supplier_id"]: row for row in payload["suppliers"]}
    performance = {row["supplier_id"]: row for row in payload["performance"]}

    rows = []
    excluded = []
    for quote in payload["quotes"]:
        supplier_id = quote["supplier_id"]
        supplier = suppliers[supplier_id]
        perf = performance[supplier_id]

        failed_gates = []
        if supplier["status"] != "APPROVED":
            failed_gates.append("SUPPLIER_NOT_APPROVED")
        if supplier["compliance_status"] != "PASS":
            failed_gates.append("COMPLIANCE_NOT_PASS")
        if quote["spec_compliance"] != "FULL":
            failed_gates.append("SPEC_NOT_FULLY_COMPLIANT")

        tco = round(
            float(quote["unit_price"]) * quantity + float(quote["freight"]), 2
        )
        late_days = _days_late(quote["delivery_date"], required_date)
        row = {
            "supplier_id": supplier_id,
            "eligible": not failed_gates,
            "failed_gates": failed_gates,
            "landed_tco": tco,
            "late_days": late_days,
            "delivery_score": max(0.0, 100.0 - late_days * 8.0),
            "quality_score": float(perf["quality_score"]),
            "reliability_score": float(perf["on_time_delivery_pct"]),
            "risk_score": RISK_SCORE[supplier["financial_risk"]],
            "esg_score": float(perf["esg_score"]),
            "commercial_score": _commercial_score(
                int(quote["payment_terms_days"]), int(quote["warranty_months"])
            ),
        }
        rows.append(row)
        if failed_gates:
            excluded.append({"supplier_id": supplier_id, "reasons": failed_gates})

    eligible_rows = [row for row in rows if row["eligible"]]
    if not eligible_rows:
        raise ValueError("No eligible suppliers after hard gates.")

    minimum_tco = min(row["landed_tco"] for row in eligible_rows)
    for row in eligible_rows:
        row["cost_score"] = round(minimum_tco / row["landed_tco"] * 100.0, 2)
        row["score_contributions"] = {
            "cost": round(row["cost_score"] * WEIGHTS["cost"], 4),
            "delivery": round(row["delivery_score"] * WEIGHTS["delivery"], 4),
            "quality": round(row["quality_score"] * WEIGHTS["quality"], 4),
            "reliability": round(
                row["reliability_score"] * WEIGHTS["reliability"], 4
            ),
            "risk": round(row["risk_score"] * WEIGHTS["risk"], 4),
            "esg": round(row["esg_score"] * WEIGHTS["esg"], 4),
            "commercial": round(
                row["commercial_score"] * WEIGHTS["commercial"], 4
            ),
        }
        row["weighted_score"] = round(
            sum(row["score_contributions"].values()),
            2,
        )

    ranked = sorted(
        eligible_rows, key=lambda row: row["weighted_score"], reverse=True
    )
    return {
        "model_version": MODEL_VERSION,
        "algorithm_id": ALGORITHM_ID,
        "ranked_suppliers": ranked,
        "excluded_suppliers": excluded,
        "recommended_by_score": ranked[0]["supplier_id"],
        "calculation_assumptions": [
            "TCO includes quoted unit price and freight only.",
            "All prices are USD; no FX conversion is required.",
            "Missing values must be resolved before this function is called.",
        ],
    }


def calculate_split(
    quotes: list[dict[str, Any]], allocation: dict[str, int]
) -> dict[str, Any]:
    quote_by_supplier = {quote["supplier_id"]: quote for quote in quotes}
    components = []
    total = 0.0
    for supplier_id, quantity in allocation.items():
        quote = quote_by_supplier[supplier_id]
        component = float(quote["unit_price"]) * quantity + float(quote["freight"])
        components.append(
            {
                "supplier_id": supplier_id,
                "quantity": quantity,
                "component_tco": round(component, 2),
            }
        )
        total += component
    return {
        "model_version": MODEL_VERSION,
        "algorithm_id": ALGORITHM_ID,
        "allocation": allocation,
        "components": components,
        "split_tco": round(total, 2),
        "assumption": "Each supplier charges its full quoted freight once.",
    }


demo_payload = {
    "quantity": 1000,
    "required_date": "2026-08-30",
    "suppliers": [
        {
            "supplier_id": "SUP-A",
            "status": "APPROVED",
            "compliance_status": "PASS",
            "financial_risk": "LOW",
        },
        {
            "supplier_id": "SUP-B",
            "status": "APPROVED",
            "compliance_status": "PASS",
            "financial_risk": "MEDIUM",
        },
        {
            "supplier_id": "SUP-C",
            "status": "APPROVED",
            "compliance_status": "PASS",
            "financial_risk": "LOW",
        },
    ],
    "performance": [
        {
            "supplier_id": "SUP-A",
            "on_time_delivery_pct": 96.5,
            "quality_score": 93,
            "esg_score": 78,
        },
        {
            "supplier_id": "SUP-B",
            "on_time_delivery_pct": 88.0,
            "quality_score": 90,
            "esg_score": 70,
        },
        {
            "supplier_id": "SUP-C",
            "on_time_delivery_pct": 98.0,
            "quality_score": 98,
            "esg_score": 85,
        },
    ],
    "quotes": [
        {
            "supplier_id": "SUP-A",
            "unit_price": 44.0,
            "freight": 1200,
            "delivery_date": "2026-08-27",
            "payment_terms_days": 30,
            "warranty_months": 24,
            "spec_compliance": "FULL",
        },
        {
            "supplier_id": "SUP-B",
            "unit_price": 40.0,
            "freight": 1500,
            "delivery_date": "2026-09-08",
            "payment_terms_days": 45,
            "warranty_months": 18,
            "spec_compliance": "FULL",
        },
        {
            "supplier_id": "SUP-C",
            "unit_price": 48.0,
            "freight": 800,
            "delivery_date": "2026-08-18",
            "payment_terms_days": 30,
            "warranty_months": 36,
            "spec_compliance": "FULL",
        },
    ],
}


def assert_demo_regression() -> None:
    expected = {"SUP-A": 93.20, "SUP-B": 76.30, "SUP-C": 93.16}
    result = calculate(demo_payload)
    actual = {
        row["supplier_id"]: row["weighted_score"]
        for row in result["ranked_suppliers"]
    }
    if actual != expected:
        raise AssertionError(
            f"CALCULATION_VERSION_MISMATCH: expected={expected}, actual={actual}"
        )


if __name__ == "__main__":
    assert_demo_regression()
    print(calculate(demo_payload))
