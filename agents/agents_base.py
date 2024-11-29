from langchain_groq import ChatGroq
from abc import ABC,abstractmethod
from loguru import logger
import os

class AgentBase(ABC):
    def __init__(self,name,groq_api_key,max_retries=2,verbose=True):
        self.name=name
        self.max_retries=max_retries
        self.verbose=verbose
        self.groq_api_key=groq_api_key
    
    @abstractmethod
    def execute(self, *args, **kwargs):
        pass

    def call_groq(self,messages,temperature=0.7,max_tokens=150):
        retries=0
        while retries < self.max_retries:
            try:
                if self.verbose:
                    logger.info(f"{self.name}]Sending message to Chat Groq:")
                    for msg in messages:
                        logger.debug(f" msg['system']")
                llm=ChatGroq(
                    model="llama-3.2-90b-vision-preview",
                    temperature=temperature,
                    max_tokens=max_tokens,
                    groq_api_key=self.groq_api_key
                )
                response=llm.invoke(messages)
                reply=response.content
                if self.verbose:
                    logger.info(f"[{self.name}] Received Response: {reply}")
                return reply
            except Exception as e:
                retries+=1
                logger.error(f"[{self.name}] Error during CHATGROQ call: {e}. Retry {retries}/{self.max_retries}")
        raise Exception(f"[{self.name}] Failed to get response from ChatGROQ after {self.max_retries} retries.") 