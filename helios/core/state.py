class StateManager:
    def __init__(self):
        self.state = {
            "goal": "",
            "tasks": [],
            "logs": [],
            "results": []
        }

    def set_goal(self, goal):
        self.state["goal"] = goal

    def set_tasks(self, tasks):
        self.state["tasks"] = tasks

    def add_log(self, message):
        self.state["logs"].append(message)

    def add_result(self, result):
        self.state["results"].append(result)

    def get_state(self):
        return self.state
