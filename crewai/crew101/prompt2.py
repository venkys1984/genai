from crewai import Agent, Task, Crew

# 🧠 Define a simple agent
agent = Agent(
    role="Smart Assistant",
    goal="Answer any user prompt as clearly as possible",
    backstory="You're a helpful and knowledgeable assistant.",
    verbose=True
)

# 📝 Create a task with your prompt
task = Task(
    description="Answer the user's question: What are the benefits of meditation?",
    agent=agent,
    expected_output='Give a correct response'
)

# 🚀 Assemble the crew and run it
crew = Crew(
    agents=[agent],
    tasks=[task],
    verbose=True
)

result = crew.kickoff()
print("\n✅ Final Answer:\n", result)
