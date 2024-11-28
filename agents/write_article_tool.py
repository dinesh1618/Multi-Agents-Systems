from .agent_base import AgentBase


class WriteArticleTool(AgentBase):
    def __init__(self, max_retries=3, verbose=True):
        super().__init__(name="WriteArticleTool", max_retries=max_retries, verbose=verbose)

    def execute(self, topic, outline=None):
        system_message = "You are an expert academic writer."
        user_message = f"Write a research article about the following topic:\n{topic}:\n\n"
        if outline:
            user_message += f"Outline:\n{outline}\n\n"
        user_message += "Article:\n"
        messages = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_message}
        ]
        article = self.call_openai(messages=messages, max_tokens=1024)
        return article