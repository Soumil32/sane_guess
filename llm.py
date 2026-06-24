import openai

class LLM:

    def __init__(self, api_key, base_url=None):
        self.api_key = api_key
        self.base_url = base_url or "https://api.openai.com/v1"
        