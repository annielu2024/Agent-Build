import gradio as gr

def reverse_text(text):
    return text[::-1]

def helloToPerson(name):
    return f"Hello {name}!"

def reverse_and_count(text):
    reversed_text = reverse_text(text)
    count = len(text)
    return reversed_text, count

demo = gr.Interface(
    fn = reverse_and_count,
    inputs="text",
    outputs = ["text", "number"],
    title = "Reverse and Count",
    description = "Enter text to see it reversed and counted.",
    examples=[
        ["Hello, world!"],
        ["Gradio is awesome!"],
        ["Python programming is fun!"]
    ]
)

demo.launch(share=True)

