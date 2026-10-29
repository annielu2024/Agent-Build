import gradio as gr
import numpy as np
import cv2

def image_to_sketch(image):
    # Convert image to grayscale
    gray_image = image.convert('L')
    # Invert the grayscale image
    inverted_image = 255-np.array(gray_image)
    # Apply Gaussian blur
    blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
    inverted_blurred = 255 - blurred
    # Create the sketch
    pencil_sketch = cv2.divide(np.array(gray_image), inverted_blurred, scale=256.0)
    return pencil_sketch

demo = gr.Interface(
    fn=image_to_sketch,
    inputs=[gr.Image(label="Upload Image", type="pil")],
    outputs=[gr.Image(label="Pencil Sketch")],
    title="Image to Pencil Sketch",
    description="Upload an image to convert it into a pencil sketch."
)

demo.launch(share=True)