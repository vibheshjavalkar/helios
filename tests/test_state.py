import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../helios')))

import pytest
from core.state import StateManager

def test_state_management():
    manager = StateManager()
    manager.set_goal("Test Goal")
    manager.set_tasks([{"name": "task1"}])
    manager.add_log("Log 1")
    manager.add_result({"task": "task1", "model": "gemini", "result": "done"})

    state = manager.get_state()
    assert state["goal"] == "Test Goal"
    assert len(state["tasks"]) == 1
    assert state["tasks"][0]["name"] == "task1"
    assert len(state["logs"]) == 1
    assert state["logs"][0] == "Log 1"
    assert len(state["results"]) == 1
    assert state["results"][0]["model"] == "gemini"
