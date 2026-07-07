from core.model_executor import ModelExecutor

class ExecutionEngine:

    def __init__(self):
        self.executor = ModelExecutor()

    # -------------------------
    # SAFE MODE (mock execution)
    # -------------------------
    def _safe_execute(self, task_name, instruction, context, model):

        mock_outputs = {
            "analyze_request": "Intent extracted: user wants optimized workflow generation.",
            "retrieve_context": "Context retrieved: multi-agent systems and optimization patterns.",
            "generate_solution": "Solution: stepwise agent-based pipeline with routing logic.",
            "validate_output": "Validation: output is consistent and complete."
        }

        return {
            "task": task_name,
            "model": model,
            "output": mock_outputs.get(task_name, "SAFE MODE OUTPUT"),
            "mode": "SAFE"
        }

    # -------------------------
    # DEMO MODE (REAL LLM execution)
    # -------------------------
    def _llm_execute(self, task_name, instruction, context, model):
        # We delegate strictly to the ModelExecutor for LLM interactions
        try:
            output = self.executor.execute(model, task_name, instruction, context, "DEMO")
            return {
                "task": task_name,
                "model": model,
                "output": output,
                "mode": "DEMO"
            }
        except Exception as e:
            return {
                "task": task_name,
                "model": model,
                "output": f"EXECUTION ERROR: {str(e)}",
                "mode": "DEMO_ERROR"
            }

    # -------------------------
    # PUBLIC METHOD
    # -------------------------
    def run(self, task_name, instruction, context, model, mode="SAFE"):
        if mode == "DEMO":
            return self._llm_execute(task_name, instruction, context, model)

        return self._safe_execute(task_name, instruction, context, model)
