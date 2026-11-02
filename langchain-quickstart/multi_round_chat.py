import os
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

load_dotenv()  # Load the API key and OpenAI-compatible endpoint from .env.
api_key = os.getenv("SILICON_API_KEY")
base_url = os.getenv("SILICON_API_BASE")

#Qwen/Qwen3-8B
#tencent/Hunyuan-MT-7B: does not support tool/function calling
#Qwen/Qwen2.5-7B-Instruct
#deepseek-ai/DeepSeek-R1-0528-Qwen3-8B
#Qwen/Qwen3.5-4B
model = init_chat_model(
    "Qwen/Qwen3.5-4B",
    model_provider="openai",
    base_url=base_url,
    api_key=api_key
)

#multiple round of question
messages = [
    SystemMessage(content="""You are a professional
    python coding assistant, and you are good at
    explaining the concept. """)
]

print("""Multiple rounds of conversation
example(Input 'quit' to quit) \n""")

while True:
  user_input = input("You: ")
  if user_input.lower() == 'quit':
    break

  # add a user message
  messages.append(HumanMessage(content=user_input))

  #invoke the model
  response = model.invoke(messages)

  #adding model response to the history
  messages.append(AIMessage(content=response.content))

  print(f"AI: {response.content}\n")




