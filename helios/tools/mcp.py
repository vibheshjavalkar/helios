from tools.providers.gemini_provider import GeminiProvider

class MCPClient:
    def __init__(self, provider=None):
        self.provider = provider or GeminiProvider()

    def get_context(self, task: str, mode: str = "SAFE"):
        return self.provider.get_context(task, mode)

