from models.registry import MODEL_REGISTRY

class OptimizationAgent:

    def score_task_complexity(self, task_name):
        if "generate" in task_name:
            return 3  # high complexity
        elif "analyze" in task_name:
            return 1  # low complexity
        else:
            return 2  # medium

    def evaluate_model(self, model, complexity):
        m = MODEL_REGISTRY[model]
        
        quality = m.get("quality", 5)
        cost = m.get("cost", 0.0)
        latency = m.get("latency", 0.0)

        return (
            quality * complexity
            - cost * 2
            - latency * 1
        )

    def select_model(self, task_name):

        complexity = self.score_task_complexity(task_name)

        best_model = None
        best_score = -999

        for model in MODEL_REGISTRY:
            score = self.evaluate_model(model, complexity)

            if score > best_score:
                best_score = score
                best_model = model

        return best_model
