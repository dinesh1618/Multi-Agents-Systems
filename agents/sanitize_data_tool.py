from .agent_base import AgentBase

class SanitizeDataTool(AgentBase):
    def __init__(self, max_retries=3, verbose=True):
        super().__init__(name="SanitizeDataTool", max_retries=max_retries, verbose=verbose)

    def execute(self, medical_data):
        messages = [
            {"role": "system", "content": "You are an AI assistant that sanitize medical data by removing protexted health infomation (PHI)."},
            {
                "role": "user",
                "content": (
                    "Remove all PHI from following data:\n\n"
                    f"{medical_data}\n\nSantized Data:\n"
                )
            }
        ]
        sanized_data = self.call_openai(messages=messages, max_tokens=500)
        return sanized_data
