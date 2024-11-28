from .agent_base import AgentBase


class WriteArticleValidatorAgent(AgentBase):
    def __init__(self, retries=3, verbose=True):
        super().__init__(name="WriteArticleValidatorAgent", max_retries=retries, verbose=verbose)

    def execute(self, topic, article):
        system_message = "You are an AI assistant that validate research articles."
        user_content = (
            "Given the topic and the aticles, access wether the aticle comprehensively covers the topic, follows a logical structure, and maintain the academic standards.\n"
            "Provide a brief analysis and rate the aticle on a scale of 1 to 5. where 5 indicates the excellent quality.\n\n"
            f"Topic:\n{topic}\n\n"
            f"Article:\n{article}\n\n"
            "Validation:"
        )
        messages = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_content}
        ]
        validation = self.call_openai(messages=messages, max_tokens=512)
        return validation