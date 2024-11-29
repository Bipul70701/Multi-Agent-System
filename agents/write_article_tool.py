from .agents_base import AgentBase

class WriteArticleTool(AgentBase):
    def __init__(self, groq_api_key,max_retries=2, verbose=True):
        super().__init__(name="WriteArticleTool",groq_api_key=groq_api_key, max_retries=max_retries, verbose=verbose)

    def execute(self, topic, outline=None):
        system_message = "You are an expert academic writer."
        user_content = f"Write a research article on the following topic:\nTopic: {topic}\n\n"
        if outline:
            user_content += f"Outline:\n{outline}\n\n"
        user_content += "Article:\n"
        messages = [
                ("system", system_message),
                ("human",  user_content),
                ]
        article = self.call_groq(messages, max_tokens=1000)
        return article