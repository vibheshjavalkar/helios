import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../helios')))

import pytest
from unittest.mock import patch
from core.execution import ExecutionEngine

def test_execution_safe():
    engine = ExecutionEngine()
    res = engine.run("analyze_request", "Analyze intent", {}, "gemini", mode="SAFE")
    assert res["output"] == "Intent extracted: user wants optimized workflow generation."
    assert res["mode"] == "SAFE"

@patch("core.model_executor.generate")
def test_execution_demo_gemini(mock_generate):
    mock_generate.return_value = "Gemini response text"
    engine = ExecutionEngine()
    res = engine.run("task1", "do text", {}, "gemini", mode="DEMO")
    assert res["output"] == "Gemini response text"
    assert res["mode"] == "DEMO"

@patch("core.model_executor.generate")
def test_execution_demo_simulated(mock_generate):
    mock_generate.return_value = "Simulated response"
    engine = ExecutionEngine()
    res = engine.run("task1", "do text", {}, "gpt4o_sim", mode="DEMO")
    assert res["output"] == "Simulated response"
    assert res["mode"] == "DEMO"

def test_execution_demo_connector():
    engine = ExecutionEngine()
    res = engine.run("task1", "do text", {}, "ollama_llama3", mode="DEMO")
    assert "[SIMULATED LOCAL ollama_llama3]" in res["output"]
    assert res["mode"] == "DEMO"
