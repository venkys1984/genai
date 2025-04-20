from crewai import Agent, Task, Crew

smart_ass = Agent(
    role='Joker',
    goal=f'Based on the context provided, answer the question - What is Natural Language Processing?',
    backstory='You are a smart assistant',
)

test_task = Task(
    description="Understand the question and give the correct response",
    agent=smart_ass,
    expected_output='Give a correct response'
)

crew = Crew(
    agents=[smart_ass],
    tasks=[test_task]
)

output = crew.kickoff()

print(output)
