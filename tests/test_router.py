import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../helios')))

import pytest
from unittest.mock import patch
from agents.router import RouterAgent

def test_router_safe():
    router = RouterAgent()
    decision = router.route("generate_solution", mode="SAFE")
    assert decision["selected_model"] in ["gemini", "mistral_local", "gpt4o_sim", "claude_sim", "perplexity_sim", "ollama_llama3"]
    assert "reason" in decision

@patch("agents.router.generate")
def test_router_demo(mock_generate):
    mock_generate.return_value = '{"selected_model": "claude_sim", "reason": "high quality", "confidence": 0.9}'
    router = RouterAgent()
    decision = router.route("analyze_request", mode="DEMO")
    assert decision["selected_model"] == "claude_sim"
    assert decision["execution_type"] == "simulated"
