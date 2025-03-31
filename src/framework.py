"""
SimpleReActFramework implementation for material analysis.
"""
import traceback
from typing import List

from langchain.agents import Tool, AgentType, initialize_agent
from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI

from src.tools.material_tools import MaterialTools
from src.utils.logger import setup_logger
from config.settings import DEFAULT_BASE_URL, DEFAULT_MODEL_NAME, DEFAULT_TEMPERATURE, AGENT_TYPE, MEMORY_KEY

logger = setup_logger("material_analysis.framework")

class SimpleReActFramework:
    """Material analysis reaction framework for reading, predicting, matching, and saving material data."""
    
    def __init__(self, openai_api_key: str, base_url: str = DEFAULT_BASE_URL, 
                 model_name: str = DEFAULT_MODEL_NAME, temperature: float = DEFAULT_TEMPERATURE):
        """
        Initialize the reaction framework
        
        Args:
            openai_api_key: OpenAI API key
            base_url: API base URL
            model_name: Model name to use
            temperature: Model temperature parameter
        """
        logger.info("Initializing SimpleReActFramework...")
        
        # Initialize LLM
        self.llm = ChatOpenAI(
            openai_api_key=openai_api_key,
            base_url=base_url,
            temperature=temperature,
            model_name=model_name
        )
        
        # Initialize memory and tools
        self.memory = ConversationBufferMemory(memory_key=MEMORY_KEY)
        self.material_tools = MaterialTools()
        self.tools = self._setup_tools()
        
        # Initialize agent
        self.agent = self._setup_agent()
        
        logger.info("SimpleReActFramework initialization completed")
    
    def _setup_tools(self) -> List[Tool]:
        """Set up the tool list"""
        tools = [
            Tool(
                name="read_data",
                func=self.material_tools.read_data,
                description="Read material expressions. Parameter: file_path (str): Data file path."
            ),
            Tool(
                name="model_predict",
                func=self.material_tools.model_predict,
                description="Predict material properties. Parameter: model_path (str): Model file path"
            ),
            Tool(
                name="rule_match",
                func=self.material_tools.rule_match,
                description="Match materials containing specific elements. Parameter: rule_elements (string): A comma-separated list of element symbols to match (e.g. 'Fe,Co,Ni' or 'Sc,Y,La,Ce')."
            ),
            Tool(
                name="save_result",
                func=self.material_tools.save_result,
                description="Save the matched materials to a CSV file. Parameter: save_path (str): The file path to save the result."
            )
        ]
        return tools

    def _setup_agent(self):
        """Set up the agent"""
        agent = initialize_agent(
            tools=self.tools,
            llm=self.llm,
            agent=eval(f"AgentType.{AGENT_TYPE}"),
            memory=self.memory,
            verbose=True
        )
        return agent

    def run(self, query: str) -> str:
        """
        Run a query
        
        Args:
            query: User query string
            
        Returns:
            Query result
        """
        logger.info(f"Executing query: {query}")
        try:
            response = self.agent.run(query)
            logger.info("Query execution successful")
            return response
        except Exception as e:
            error_msg = f"Agent execution error: {str(e)}"
            logger.error(f"{error_msg}\n{traceback.format_exc()}")
            return error_msg 
        
