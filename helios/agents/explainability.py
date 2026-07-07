import json
from services.gemini_client import generate

class ExplainabilityAgent:
    def explain(self, state, mode="SAFE"):
        if mode == "SAFE":
            logs = state.get("logs", [])
            tasks = state.get("tasks", [])
            results = state.get("results", [])

            explanation = []
            explanation.append("SYSTEM DECISION BREAKDOWN\n")
            for task in tasks:
                explanation.append(
                    f"Task: {task.get('name', 'unknown')} → executed using optimization-based routing"
                )
            explanation.append("\nMODEL SELECTION REASONING:\n")
            for r in results:
                model = r.get("model", "unknown")
                task_name = r.get("task", "unknown")
                explanation.append(
                    f"{task_name} used {model} because it balanced cost, latency, and quality constraints."
                )
            explanation.append("\nSYSTEM BEHAVIOR SUMMARY:")
            explanation.append("- Lower complexity tasks routed to efficient models")
            explanation.append("- Higher complexity tasks routed to higher reasoning capacity models")
            explanation.append("- Optimization engine dynamically selected best trade-off")
            return "\n".join(explanation)

        # DEMO Mode
        goal = state.get("goal", "")
        tasks_json = json.dumps(state.get("tasks", []), indent=2)
        results_json = json.dumps(state.get("results", []), indent=2)
        logs_json = json.dumps(state.get("logs", []), indent=2)

        prompt = f"""
Generate a concise execution audit in EXACT format:

EXECUTION SUMMARY (max 3 lines)
ROUTING DECISION (max 5 bullets)
COST VS QUALITY (max 3 bullets)
SYSTEM ISSUES (max 3 bullets)
RECOMMENDATION (max 3 bullets)

Do NOT exceed limits.
Do NOT write paragraphs.

Context:
User Goal: {goal}
Planned Tasks: {tasks_json}
Routing Decisions & Execution Logs & Dashboard Metrics: {results_json}
Execution Timeline Logs: {logs_json}
"""
        return generate(prompt)

