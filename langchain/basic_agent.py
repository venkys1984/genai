from langchain.agents import Tool, initialize_agent
from langchain.agents.agent_types import AgentType
from langchain_openai import ChatOpenAI

# Set your OpenAI key
import os


# Define a simple tool (calculator)
def simple_calculator(input_text: str) -> str:
    print('**************my calci got called*************')
    return str(eval(input_text))

# Wrap it as a LangChain Tool
calculator_tool = Tool(
    name="Calculator",
    func=simple_calculator,
    description="Useful for doing simple math. Input should be a math expression like '2 + 2'"
)

# Use latest OpenAI model
llm = ChatOpenAI(model_name="gpt-4-turbo", temperature=0)

# Initialize the agent with the tool and LLM
agent = initialize_agent(
    tools=[calculator_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Ask the agent a question
response = agent.run("What is 9 multiplied by 11 minus 4?")
print(response)
