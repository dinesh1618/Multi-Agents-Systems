from .summarize_tool import SummarizeTool
from .summarize_validator_agent import SummarizeValidatorAgent
from .write_article_tool import WriteArticleTool
from .write_article_validator_agent import WriteArticleValidatorAgent
from .sanitize_data_tool import SanitizeDataTool
from .sanitize_data_validator_agent import SanitizeDataValidatorAgent
from .refiner_agent import RefinerAgent
from .validator_agent import ValidatorAgent

class AgentManager:
    def __init__(self, max_retries=2, verbose=True):
        self.agent = {
            "summarize": SummarizeTool(max_retries=max_retries, verbose=verbose),
            "summarize_validator": SummarizeValidatorAgent(retries=max_retries, verbose=verbose),
            "write_article": WriteArticleTool(max_retries=max_retries, verbose=verbose),
            "write_article_validator": WriteArticleValidatorAgent(retries=max_retries, verbose=verbose),
            "sanitize": SanitizeDataTool(max_retries=max_retries, verbose=verbose),
            "sanitize_validator": SanitizeDataValidatorAgent(retries=max_retries, verbose=verbose),
            "refiner": RefinerAgent(retries=max_retries, verbose=verbose),
            "validator": ValidatorAgent(max_retries=max_retries, verbose=verbose)
        }

    def get_agent(self, agent_name):
        agent = self.agent.get(agent_name)
        if not agent:
            raise ValueError(f"Agent {agent_name} not found.")
        return agent