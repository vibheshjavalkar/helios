from models.registry import MODEL_REGISTRY

def compute_verdict(total_cost, baseline_cost=10):
    savings = ((baseline_cost - total_cost) / baseline_cost) * 100
    savings = max(min(savings, 100), -100)  # clamp

    if savings > 50:
        label = "Highly Optimized System"
    elif savings > 0:
        label = "Moderately Optimized System"
    else:
        label = "Inefficient System"

    return {
        "verdict": label,
        "efficiency_score": round(savings, 2),
        "insight": "Computed from normalized cost baseline comparison"
    }

class SystemVerdict:
    def generate(self, dashboard):
        total_cost = sum(MODEL_REGISTRY.get(r.get("model"), {}).get("cost", 0.0) for r in dashboard)
        return compute_verdict(total_cost, baseline_cost=10)

