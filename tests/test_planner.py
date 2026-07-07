import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../helios')))

import pytest
from unittest.mock import patch
from agents.planner import PlannerAgent

def test_planner_safe():
    planner = PlannerAgent()
    dag = planner.run("Test Goal", mode="SAFE")
    assert isinstance(dag, list)
    assert len(dag) == 4
    assert dag[0]["name"] == "analyze_request"

@patch("agents.planner.generate")
def test_planner_demo(mock_generate):
    mock_generate.return_value = '[{"name": "task1", "instruction": "do something"}]'
    planner = PlannerAgent()
    dag = planner.run("Test Goal", mode="DEMO")
    assert isinstance(dag, list)
    assert len(dag) == 1
    assert dag[0]["name"] == "task1"
    mock_generate.assert_called_once()
