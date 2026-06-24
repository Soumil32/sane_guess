import ollama

class LLM:

    def __init__(self, api_key, base_url, model, system_prompt):
        self.api_key = api_key
        self.base_url = base_url
        self.model = model
        self.system_prompt = system_prompt

    def chat(self, message: str, response_format):
        response: ollama.ChatResponse = ollama.chat(model=self.model, messages=[
            {
                'role': 'system',
                'content': self.system_prompt,
            },
            {
                'role': 'user',
                'content': message,
            },
        ])

        return response.message.content