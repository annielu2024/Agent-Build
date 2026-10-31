from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()  # Load the API key and OpenAI-compatible endpoint from .env.

# DashScope exposes Qwen through its OpenAI-compatible chat completions API.
model = init_chat_model(
    "qwen3.7-flash",
    model_provider = "openai"
)

response = model.invoke("Hello, please introduce yourself.")
print(response.content)