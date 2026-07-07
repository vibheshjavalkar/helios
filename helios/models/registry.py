MODEL_REGISTRY = {
    "gemini": {
        "type": "real",
        "provider": "google",
        "cost": 1,
        "latency": 1,
        "quality": 9
    },
    "gpt4o_sim": {
        "type": "simulated",
        "provider": "openai",
        "cost": 8,
        "latency": 3,
        "quality": 10
    },
    "claude_sim": {
        "type": "simulated",
        "provider": "anthropic",
        "cost": 7,
        "latency": 2,
        "quality": 10
    },
    "perplexity_sim": {
        "type": "simulated",
        "provider": "perplexity",
        "cost": 5,
        "latency": 2,
        "quality": 8
    },
    "ollama_llama3": {
        "type": "simulated_connector",
        "provider": "ollama",
        "cost": 2,
        "latency": 2,
        "quality": 7
    },
    "mistral_local": {
        "type": "simulated_connector",
        "provider": "huggingface",
        "cost": 2,
        "latency": 2,
        "quality": 8
    }
}
