from .summarize_tool import SummarizeTool
from .write_article_tool import WriteArticleTool
from .sanatize_data_tool import SanitizeDataTool
from .summary_validator_agent import SummarizeValidatorAgent
from .write_article_validator_agent import WriteArticleValidatorAgent
from .sanatize_data_validator_agent import SanitizeDataValidatorAgent
from .refiner_agent import RefinerAgent
from .validator_agent import ValidatorAgent 

class AgentManager:
    def __init__(self,groq_api_key, max_retries=2, verbose=True):
        self.agents = {
            "summarize": SummarizeTool(groq_api_key,max_retries=max_retries, verbose=verbose),
            "write_article": WriteArticleTool(groq_api_key,max_retries=max_retries, verbose=verbose),
            "sanitize_data": SanitizeDataTool(groq_api_key,max_retries=max_retries, verbose=verbose),
            "summarize_validator": SummarizeValidatorAgent(groq_api_key,max_retries=max_retries, verbose=verbose),
            "write_article_validator": WriteArticleValidatorAgent(groq_api_key,max_retries=max_retries, verbose=verbose),
            "sanitize_data_validator": SanitizeDataValidatorAgent(groq_api_key,max_retries=max_retries, verbose=verbose),
            "refiner": RefinerAgent(groq_api_key,max_retries=max_retries, verbose=verbose),    
            "validator": ValidatorAgent(groq_api_key,max_retries=max_retries, verbose=verbose) 
        }
        self.groq_api_key=groq_api_key

    def get_agent(self, agent_name):
        agent = self.agents.get(agent_name)
        if not agent:
            raise ValueError(f"Agent '{agent_name}' not found.")
        return agent