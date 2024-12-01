from .agent_base import AgentBase


class SanitizeDataValidatorAgent(AgentBase):
    def __init__(self, retries=3, verbose=True):
        super().__init__(name="SanitizeDataValidatorAgent", max_retries=retries, verbose=verbose)

    def execute(self, medical_data, sanitize_data):
        system_message = "You are an AI assistant that validates the sanitization of medical data by checking for the removal of Protected Health Information (PHI)."
        user_content = (
            "Given the original data and PHI data, verify that all PHI has been removed.\n"
            "List any remaining PHI in the sanitized data and rate the sanitization process on a scale of 1 to 5, where 5 indicates complete sanitization.\n\n"
            f"Original Data:\n{medical_data}\n\n"
            f"Sanitized Data:\n{sanitize_data}\n\n"
            "Validation:"
        )
        
        messages = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_content}
        ]
        validation = self.call_openai(messages=messages, max_tokens=512)
        return validation