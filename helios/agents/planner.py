import json
from services.gemini_client import generate

class PlannerAgent:
    def run(self, goal, mode="SAFE"):
        if mode == "DEMO":
            prompt = f"""
You are the Planner Agent inside the Helios multi-agent orchestration system.

Your only responsibility is to convert a user's goal into an execution plan.

Rules:

- Break the request into logical execution tasks.
- Keep each task atomic.
- Preserve execution order.
- Do not solve the problem.
- Do not generate answers.
- Do not recommend models.
- Return JSON only.

Required format:

[
  {{
    "name":"...",
    "instruction":"..."
  }}
]

User Goal:

{goal}
"""
            response = generate(prompt, is_json=True)
            return json.loads(response)

        return [
            {"name": "analyze_request", "instruction": "Analyze user intent"},
            {"name": "retrieve_context", "instruction": "Gather data"},
            {"name": "generate_solution", "instruction": "Formulate answer"},
            {"name": "validate_output", "instruction": "Verify quality"}
        ]
