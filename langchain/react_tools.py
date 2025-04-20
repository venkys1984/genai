from langchain.agents import tool
from langchain.prompts import PromptTemplate
from langchain.tools.render import render_text_description
from langchain_openai import ChatOpenAI

@tool
def get_text_length(text:str)->int:
    """
    Returns the length of a text by counting the characters
    """
    text = text.strip("\n ")
    return len(text)

def main():
    # n = get_text_length.invoke(input = {
    #     "text": "leopard"
    # })

    # print(n)

    tools = [get_text_length]


    template = """
    
    Answer the following questions as best you can. You have access to the following tools:

    {tools}

    Use the following format:

    Question: the input question you must answer
    Thought: you should always think about what to do
    Action: the action to take, should be one of [{tool_names}]
    Action Input: the input to the action
    Observation: the result of the action
    ... (this Thought/Action/Action Input/Observation can repeat N times)
    Thought: I now know the final answer
    Final Answer: the final answer to the original input question

    Begin!

    Question: {input}
    Thought:
    
    """

    prompt = PromptTemplate.from_template(template=template).partial(tools=render_text_description(tools), tool_names = ','.join([ t.name for t in tools]))

    llm =    ChatOpenAI(model="gpt-4o", temperature=0,stop = ["\nObservation", "Observation"])


main()
