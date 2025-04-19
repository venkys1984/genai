from langchain.agents import initialize_agent, AgentType
from langchain_openai import ChatOpenAI
from langchain.tools import tool
import os
import datetime

# 🛠️ Define custom tools using @tool decorator

@tool
def get_current_time(unused: str) -> str:
    """Returns the current system time."""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

@tool
def calculate(expression: str) -> str:
    """Evaluates a math expression like '5 * (3 + 2)'."""
    try:
        return str(eval(expression))
    except Exception as e:
        return f"Error: {e}"

# 🧰 Bundle tools
tools = [get_current_time, calculate]

# 🔮 Use GPT-4 Turbo (or 3.5)
llm = ChatOpenAI(
    model="gpt-4-turbo",  # Or use "gpt-3.5-turbo-1106"
    temperature=0
)

# 🤖 Create the agent using function-calling behavior
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.OPENAI_FUNCTIONS,
    verbose=True
)

# 🗨️ Ask a question — the agent will pick the right tool!
response = agent.invoke("What time is it right now and what is 12 * 8 + 5?")
print("\n✅ Final Answer:", response)
