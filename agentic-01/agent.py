from langchain.tools import Tool
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent,AgentType


def tool_calc(someinput: str) -> str:
    return str(eval(someinput))


calculator = Tool(
    name="mini_calc",
    func=tool_calc,
    description="Mini Calculator Tool"
)

# Initialize ChatOpenAI with supported arguments
llm = ChatOpenAI(temperature=0)

agent = initialize_agent(
    tools =[calculator],
    llm=llm,
    agent_type= AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

print("Welcome to the Mini Calculator!")
print("You can use the calculator to perform basic arithmetic operations.")
userQuery = input("Entery your query: ")
response = agent.run(userQuery)
print(response)