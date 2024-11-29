from .agents_base import AgentBase

class SummarizeTool(AgentBase):
    def __init__(self,groq_api_key,max_retries,verbose=True):
        super().__init__(name="summarizeTool",groq_api_key=groq_api_key,max_retries=max_retries,verbose=verbose)
    
    def execute(self,text):
        messages = [
                ("system", "You are an AI assistant that summarize Medical Text."),
                ("human",  "Please provide a concise summary of the following medical text:\n\n"
                    f"{text}\n\nSummary:"),
                ]
        
        summary = self.call_groq(messages, max_tokens=300)
        return summary