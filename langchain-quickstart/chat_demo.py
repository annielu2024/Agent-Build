import os
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()  # Load the API key and OpenAI-compatible endpoint from .env.
api_key = os.getenv("SILICON_API_KEY")
base_url = os.getenv("SILICON_API_BASE")

#Qwen/Qwen3-8B
#tencent/Hunyuan-MT-7B: does not support tool/function calling
#Qwen/Qwen2.5-7B-Instruct
#deepseek-ai/DeepSeek-R1-0528-Qwen3-8B
#Qwen/Qwen3.5-4B
model = init_chat_model(
    "Qwen/Qwen3-8B",
    model_provider="openai",
    base_url=base_url,
    api_key=api_key
)

# single simple question
print("\n " + model.invoke("Why sky is blue?").content) 





