from agents import Agent
from src.agent.my_config.gemini_config import MODEL

agent = Agent(
    name = "assistant", 
    instructions= "you are a helpfull assistant.",
    model= MODEL
    )
