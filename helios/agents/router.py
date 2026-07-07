import json
from services.gemini_client import generate

class RouterAgent:
    def __init__(self):
        pass

    def route(self, task_name, mode="SAFE"):
        if mode == "DEMO":
            prompt = f"""
You are a compute orchestration engine.

You must choose the best model from this list:

REAL MODELS:
- gemini

CONNECTOR/SIMULATED LOCAL:
- ollama_llama3
- mistral_local

SIMULATED MODELS:
- gpt4o_sim
- claude_sim
- perplexity_sim

TASK:
{task_name}

Return STRICT JSON:
{{
  "selected_model": "",
  "reason": "",
  "confidence": 0.0
}}
"""
            response_text = generate(prompt, is_json=True)
            decision = json.loads(response_text)
            
            if decision.get("selected_model") != "gemini":
                decision["execution_type"] = "simulated"
            else:
                decision["execution_type"] = "real"
                
            return decision
            
        else:
            # SAFE MODE: Fallback routing
            from agents.scoring_fallback import OptimizationAgent
            fallback = OptimizationAgent()
            model_fallback = fallback.select_model(task_name) or "gemini"
            return {
                "selected_model": model_fallback,
                "reason": "SAFE MODE: Rule-based scoring fallback used.",
                "confidence": 1.0
            }
