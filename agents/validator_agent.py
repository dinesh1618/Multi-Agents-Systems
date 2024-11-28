from .agent_base import AgentBase

class ValidatorAgent(AgentBase):
    def __init__(self, max_retries=3, verbose=True):
        super().__init__(name="ValidatorAgent", max_retries=max_retries, verbose=verbose)

    def execute(self, topic, article):
        messages = [
            {
                "role": "system",
                "content": [
                    {
                        "type": "text",
                        "text": "You are an AI Assistant that validates research articles for accuracy, completeness, adherence to academic standards."
                    }
                ]
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": (
                            "Given the topic and research artcle below, assess wether the article comprehensively covers the topic, follows a logical structure, maintain the academic standards.\n"
                            "Provide a brief analysis and rate the aticle on a scale of 1 to 5. where 5 indicates the excellent quality.\n\n"
                            f"Topic:\n{topic}\n\n"
                            f"Article:\n{article}\n\n"
                            "Validation:"
                        )
                    }
                ]
            }
        ]

        validation = self.call_openai(messages=messages, temperature=0.3, max_tokens=300) # Low temperature for more deterministic output
        return validation