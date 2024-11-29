from .agents_base import AgentBase

class ValidatorAgent(AgentBase):
    def __init__(self,groq_api_key, max_retries=2, verbose=True):
        super().__init__(name="ValidatorAgent",groq_api_key=groq_api_key, max_retries=max_retries, verbose=verbose)

    def execute(self, topic, article):

        system_message = "You are an AI assistant that validates research articles for accuracy, completeness, and adherence to academic standards."
        
        user_content = ("Given the topic and the research article below, assess whether the article comprehensively covers the topic, follows a logical structure, and maintains academic standards.\n"
                            "Provide a brief analysis and rate the article on a scale of 1 to 5, where 5 indicates excellent quality.\n\n"
                            f"Topic: {topic}\n\n"
                            f"Article:\n{article}\n\n"
                            "Validation:"
                        )
        
        messages = [
                ("system", system_message),
                ("human",  user_content),
                ]
        
        validation = self.call_groq(
            messages=messages,
            temperature=0.3,         # Lower temperature for more deterministic output
            max_tokens=500
        )
        return validation