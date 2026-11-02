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
    "Qwen/Qwen2.5-7B-Instruct",
    model_provider="openai",
    base_url=base_url,
    api_key=api_key
)

#Streaming output example
print(" Streaming output example \n")
print("\n Please ask AI an question, for example: Please write a Bubble Sort program in Python \n")
question = input("You: ")
print(f" User: {question} \n")
print("AI: ", end="", flush=True)

# for v1.0, use streaming output
for chunk in model.stream(question):
  print(chunk.content, end="", flush=True)

print("\n")