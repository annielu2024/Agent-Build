import os
from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()  # Load the API key and OpenAI-compatible endpoint from .env.
api_key = os.getenv("SILICON_API_KEY")
base_url = os.getenv("SILICON_API_BASE")

# Initialize a model that supports tool calling
tool_model = init_chat_model(
    "Qwen/Qwen2.5-7B-Instruct",
    model_provider="openai",
    base_url=base_url,
    api_key=api_key
)

@tool
def get_weather(city: str) -> str:
  """Get the weather for a given city."""
  return f"The weather for {city} is sunny."

agent = create_agent(
    model=tool_model,
    tools=[get_weather],
    system_prompt="You are an AI Weather assistant"
)

result = agent.invoke({
    "messages": [{"role": "user", "content": "How is the weather in San Diego?"}]
})
#print(result)
print(result["messages"][-1].content)  # Print the last message from the agent's response