from .agent_base import AgentBase


class RefinerAgent(AgentBase):
    def __init__(self, retries=3, verbose=True):
        super().__init__(name="RefinerAgent", max_retries=retries, verbose=verbose)

    def execute(self, draft):
        messages = [
            {
                "role": "system",
                "content": [
                    {
                        "type": "text",
                        "text": "You are an expert editor who refines and enhances research articles for clarity, coherence, and academic quality."
                    },

                ]
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": (
                            "Please refine the following research artical draft to improve its language, coherence, and overall quality:\n\n"
                            f"{draft}\n\nRefined Artical:\n"
                        )
                        
                    }
                ]
            }
        ]
        refined_article = self.call_openai(messages=messages, temperature=0.5, max_tokens=2048)
        return refined_article