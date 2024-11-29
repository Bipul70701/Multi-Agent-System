from .agents_base import AgentBase

class SummarizeValidatorAgent(AgentBase):
    def __init__(self, groq_api_key,max_retries=2, verbose=True):
        super().__init__(name="SummarizeValidatorAgent", groq_api_key=groq_api_key,max_retries=max_retries, verbose=verbose)

    def execute(self, original_text, summary):
        system_message = "You are an AI assistant that validates summaries of medical texts."
        user_content = (
            "Given the original text and its summary, assess whether the summary accurately and concisely captures the key points of the original text.\n"
            "Provide a brief analysis and rate the summary on a scale of 1 to 5, where 5 indicates excellent quality.\n\n"
            f"Original Text:\n{original_text}\n\n"
            f"Summary:\n{summary}\n\n"
            "Validation:"
        )
        messages = [
                ("system", system_message),
                ("human",  user_content),
                ]
        validation = self.call_groq(messages, max_tokens=512)
        return validation