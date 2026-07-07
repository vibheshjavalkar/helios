from services.gemini_client import generate

class ModelExecutor:

    def execute(self, model_name, task_name, prompt, context, mode):

        if model_name == "gemini":
            return generate(prompt)

        elif model_name in ["gpt4o_sim", "claude_sim", "perplexity_sim"]:
            simulation_prompt = f"""
            You are simulating the behavior of {model_name}.
            TASK: {task_name}
            CONTEXT: {context}
            Respond realistically to:
            {prompt}
            """
            return generate(simulation_prompt)

        elif model_name in ["ollama_llama3", "mistral_local"]:
            return self._simulate_local_model(model_name, prompt)

        else:
            return "ERROR: Unknown model"

    def _simulate_local_model(self, model_name, prompt):
        return f"[SIMULATED LOCAL {model_name}] processed: {prompt[:200]}"
