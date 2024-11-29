from .agents_base import AgentBase

class SanitizeDataTool(AgentBase):
    def __init__(self,groq_api_key, max_retries=3, verbose=True):
        super().__init__(name="SanitizeDataTool", groq_api_key=groq_api_key,max_retries=max_retries, verbose=verbose)

    def execute(self, medical_data):
        messages = [
                ("system", "You are an AI assistant that sanitizes medical data by removing Protected Health Information (PHI)."),
                ("human",  "Remove all PHI from the following data:\n\n"
                    f"{medical_data}\n\nSanitized Data:"),
                ]
        sanitized_data = self.call_groq(messages, max_tokens=500)
        return sanitized_data