"""
Langchain 1.0 Agent Example: AI Translator Assistant
Function:
- Auto detect language
- Multiple style translation
- Terminology Translation
"""
import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv()  # Load the API key and OpenAI-compatible endpoint from .env.
api_key = os.getenv("SILICON_API_KEY")
base_url = os.getenv("SILICON_API_BASE")

class SmartTranslator:
  def __init__(self):
    # Vv1.0: use init_chat_model
    # Use the API_KEY from notebook variable if SILICON_API_KEY is not in env
    api_key = os.getenv("SILICON_API_KEY") or API_KEY
    self.model = init_chat_model(
        "Qwen/Qwen3-8B",
        model_provider="openai",
        base_url=base_url,
        api_key=api_key,
        temperature = 0.3 # translator should use low temperature
    )

  def translate(self, text: str, target_lang: str = "Chinese", style: str = "official"):
    """
    Translate Text

    Args:
        text: the source text
        target_lang: destination language (Chinese/English/Japanese etc)
        style: translation sytle (Official/Verbal/Literature)
    """
    system_prompt = f"""You are a professional translator assistant.
      Task:
      1. Auto-detect input text language
      2. Translate the input text to {target_lang}
      3. Apply {style} style
      4. If there is terminology, please use () to mark source text

      Output format:
      【Source text】: XXX
      【Traslated】: XXX
      【Terminology】: (if there is any)
    """

    messages = [
        SystemMessage(content = system_prompt),
        HumanMessage(content = text)
    ]

    response = self.model.invoke(messages)
    return response.content

def main():
  translator = SmartTranslator()
  print(" Smart Translator Assistant (Langchian 1.0)")
  print("=" * 50)

  #Example 1: Translate English to Chinese (technical doc)
  text1 = "Langchain is a framework for developing applications powered by large language models."
  print(f"\n 原文: {text1} ")
  print(f"\n 翻译结果: {translator.translate(text1, 'Chinese', 'Official')}")

  print("\n" + "="*50)

  #Example 2: Translate Chinese to English (verbal)
  text2 = "这个框架真的很好用， 强烈推荐。"
  print(f"\n Source: {text2} ")
  print(f"\n Translated: {translator.translate(text2, 'English', 'Verbal')}")

  print("\n" + "="*50)

  #Interactive Mode
  print("\n Interactive Mode (type 'quit' to quit) \n")
  while True:
    text = input("Please input source text: ")
    if text.lower() == 'quit':
      break

    target = input("Target language (default is Chinese): ") or "Chinese"
    style = input("Style (Official/Verbal/Literature, default is Official): ") or "Official"

    print("\n Translating...... \n")
    result = translator.translate(text, target, style)
    print(f"\n Source: {text} ")
    print(f"\n Translated: {result} ")
    print("="*50)

if __name__ == "__main__":
  main()
