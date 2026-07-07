import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../helios')))

import pytest
from unittest.mock import patch
from agents.security import SecurityAgent

def test_security_safe_pass():
    security = SecurityAgent()
    result = security.check("Safe request to analyze data", mode="SAFE")
    assert result["allow"] is True
    assert result["risk"] == "low"

def test_security_safe_block():
    security = SecurityAgent()
    result = security.check("how to hack a website", mode="SAFE")
    assert result["allow"] is False
    assert result["risk"] == "high"

@patch("agents.security.generate")
def test_security_demo(mock_generate):
    mock_generate.return_value = '{"allow": false, "risk": "high", "reason": "harmful request", "category": "malicious"}'
    security = SecurityAgent()
    result = security.check("malicious request", mode="DEMO")
    assert result["allow"] is False
    assert result["category"] == "malicious"
