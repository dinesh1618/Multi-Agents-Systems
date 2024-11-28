from .agent_base import AgentBase


class SummarizeValidatorAgent(AgentBase):
    def __init__(self, retries=3, verbose=True):
        super().__init__(name="SummarizeValidatorAgent", max_retries=retries, verbose=verbose)

    def execute(self, original_text, summary):
        system_message = "You are an AI assistant that validates summaries of medical texts."
        user_content = (
            "Given the original text and its summary, assess whether the summary accurately and concisely capture the key points of the original text.\n"
            "Provide a brief analysis and rate the summary on a scale of 1 to 5. where 5 indicate the excellent quality.\n\n"
            f"Original Text:\n{original_text}\n\n"
            f"Summary:\n{summary}\n\n"
            "Validation:"
        )
        messages = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_content}
        ]
        validation = self.call_openai(messages=messages, max_tokens=512)
        return validation