import gradio as gr
import os
from openai import OpenAI

# Get DashScope API key from environment variable
# Make sure to set the environment variable DASHSCOPE_API_KEY before running
api_key = os.getenv("DASHSCOPE_API_KEY")
if not api_key:
    raise ValueError("DASHSCOPE_API_KEY environment variable not set.")

def call_qwen(message, history):
    client = OpenAI(
        api_key=api_key,
        #base_url="https://api.dashscope.com/v1",
        #base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
        base_url="https://ws-uh05o1itejeo8cxd.ap-southeast-1.maas.aliyuncs.com/compatible-mode/v1"
    )

    messages =[]

    if history:
        try:
            for msg in history:
                if isinstance(msg, dict) and "role" in msg and "content" in msg:
                    messages.append(msg)
                elif isinstance(msg, (list, tuple)) and len(msg) == 2:
                    user_msg, assistant_msg = msg
                    messages.append({"role": "user", "content": user_msg})
                    messages.append({"role": "assistant", "content": assistant_msg})
        except Exception as e:
            print(f"Error processing history: {e}")

    messages.append({"role": "user", "content": message})

    try:
        response = client.chat.completions.create(
            model="qwen3.7-flash",
            messages=messages,
            stream=False,
            temperature=0.7,
            max_tokens=512
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error calling Qwen API: {e}")
        return "Error: Unable to get response from Qwen API."

demo = gr.ChatInterface(
    fn=call_qwen,
    title="Qwen Chat Interface",
    description="Chat with Qwen model using DashScope API.",
    examples=[
        ["Hello, how are you?", []],
        ["Can you tell me a joke?", []],
        ["What's the weather like today?", []],
        ["Explain quantum computing in simple terms.", []],
        ["Write a short poem about the ocean.", []]
    ]
)

if __name__ == "__main__":
    demo.launch(theme=gr.themes.Soft(), share=True)


