from crewai_tools import PDFSearchTool
from crewai import Agent, Task, Crew

pdf_tool = PDFSearchTool(pdf='/home/venky/Downloads/treasure_island.pdf', verbose=True)

research_agent = Agent(
    role = 'Research Agent',
    goal = 'Search the PDF and find the relevant answer to the question: What kind of a person was Long John Silver',
    allow_delegation=False,
    verbose=True,
    backstory=(
        """The agent is good at searching documents and providing answers to the questions based on the document"""
    ),
    tools=[pdf_tool],
)

test_task = Task(
    description="Understand the question and give the correct response",
    agent=research_agent,
    expected_output='Give a correct response'
)

crew = Crew(
    agents=[research_agent],
    tasks=[test_task],
    verbose = True
)

output = crew.kickoff()

print(output)

