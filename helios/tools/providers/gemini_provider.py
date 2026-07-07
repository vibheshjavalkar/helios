import json
from services.gemini_client import generate
from tools.providers.base_provider import ContextProvider

class GeminiProvider(ContextProvider):
    def get_context(self, task: str, mode: str = "SAFE") -> dict:
        if mode == "DEMO":
            return self._llm_context(task)
        return self._safe_context(task)

    def _safe_context(self, task: str) -> dict:
        return {
            "task": task,
            "key_concepts": ["basic processing"],
            "constraints": ["low compute usage"],
            "recommended_approach": "simple step execution",
            "risk_factors": ["unknown complexity"],
            "tooling_suggestions": ["standard LLM call"],
            "complexity_hint": "low"
        }

    def _llm_context(self, task: str) -> dict:
        prompt = f"""
You are a CONTEXT INTELLIGENCE LAYER inside a multi-agent system.

Your job is to generate structured execution context for a task.

TASK:
{task}

Return ONLY valid JSON:

{{
  "task": "{task}",
  "key_concepts": [],
  "constraints": [],
  "recommended_approach": "",
  "risk_factors": [],
  "tooling_suggestions": [],
  "complexity_hint": "low | medium | high"
}}
"""
        response = generate(prompt, is_json=True)
        return json.loads(response)
