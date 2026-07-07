from agents.planner import PlannerAgent
from agents.router import RouterAgent
from agents.security import SecurityAgent
from tools.mcp import MCPClient
from agents.explainability import ExplainabilityAgent
from core.verdict import SystemVerdict
from core.execution import ExecutionEngine

class Orchestrator:
    def __init__(self, state):
        self.state = state
        self.planner = PlannerAgent()
        self.router = RouterAgent()
        self.security = SecurityAgent()
        self.mcp = MCPClient()
        self.explainer = ExplainabilityAgent()
        self.verdict_engine = SystemVerdict()
        self.executor = ExecutionEngine()

    def run(self, goal, mode="SAFE", ui_callback=None):
        import os

        if mode == "DEMO":
            if not os.environ.get("GEMINI_API_KEY"):
                raise Exception("DEMO MODE REQUIRES GEMINI API KEY")

        # STEP 1: security check
        if ui_callback: ui_callback("▶ Running Security Check...")
        security_result = self.security.check(goal, mode)

        if not security_result["allow"]:
            if ui_callback: ui_callback(f"❌ Security Blocked: {security_result['category']}")
            return {
                "final_output": "Blocked by security agent.",
                "security_report": security_result
            }
            
        self.state.set_goal(goal)
        self.state.add_log(f"SECURITY → {security_result['category']} | {security_result['risk']}")
        if ui_callback: ui_callback("✔ Security Check Passed")

        # STEP 2: planning
        if ui_callback: ui_callback("▶ Planning Tasks...")
        tasks = self.planner.run(goal, mode=mode)
        self.state.set_tasks(tasks)
        
        if mode == "DEMO":
            self.state.add_log("Execution workflow generated dynamically.")
        else:
            self.state.add_log("Using development planner.")

        outputs = []

        # STEP 3: task execution loop
        for task in tasks:
            task_name = task["name"]
            
            if ui_callback: ui_callback(f"▶ Executing `{task_name}`...")

            # Use LLM-based router
            decision = self.router.route(task_name, mode=mode)
            routed_model = decision.get("selected_model", "gemini-flash")
            reason = decision.get("reason", "No reason provided")

            self.state.add_log(f"[ROUTER] {task_name} → {routed_model}")
            self.state.add_log(f"↳ Reason: {reason}")

            instruction = task.get("instruction", "Follow standard procedures.")
            context = self.mcp.get_context(task_name, mode)
            
            # Actual or Simulated Execution
            execution_response = self.executor.run(task_name, instruction, context, routed_model, mode)
            execution_result = execution_response["output"]
            self.state.add_log(f"[EXECUTION] Completed using {routed_model}")
            
            if ui_callback: ui_callback(f"✔ `{task_name}` completed ({routed_model})")

            outputs.append({
                "task": task_name,
                "model": routed_model,
                "reason": reason,
                "context": context,
                "result": execution_result
            })

        for out in outputs:
            self.state.add_result(out)

        if ui_callback: ui_callback("▶ Generating AI Audit Report...")
        explanation = self.explainer.explain(
            self.state.get_state(),
            mode
        )
        if ui_callback: ui_callback("✔ Mission Complete!")

        verdict = self.verdict_engine.generate(
            self.state.get_state()["results"]
        )

        return {
            "goal": goal,
            "tasks": tasks,
            "outputs": outputs,
            "logs": self.state.get_state()["logs"],
            "explanation": explanation,
            "verdict": verdict
        }
