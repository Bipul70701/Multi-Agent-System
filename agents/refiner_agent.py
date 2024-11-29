from .agents_base import AgentBase

class RefinerAgent(AgentBase):
    def __init__(self,groq_api_key, max_retries=2, verbose=True):
        super().__init__(name="RefinerAgent", groq_api_key=groq_api_key,max_retries=max_retries, verbose=verbose)

    def execute(self, draft):
        messages = [
                ("system", "You are an expert editor who refines and enhances research articles for clarity, coherence, and academic quality."),
                ("human",  "Please refine the following research article draft to improve its language, coherence, and overall quality:\n\n"
                            f"{draft}\n\nRefined Article:"),
                ]
        refined_article = self.call_groq(
            messages=messages,
            temperature=0.5,
            max_tokens=2048
        )
        return refined_article