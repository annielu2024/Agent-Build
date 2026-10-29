 

# Agent-Build

## Gradio quickstart

Create and activate a virtual environment, install Gradio in it, then run the
demo with `python3` while the environment is active:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r gradio-quickstart/requirements.txt
python3 gradio-quickstart/demo.py
```

Check out the demo by copying the local URL http://127.0.0.1:7860 (local) or the public URL https://\*\*\*.gradio.live and pasting into the browser.

## Image converting demo

The image demo converts an uploaded image into a pencil sketch. After setting
up and activating the virtual environment above, run:

```bash
python3 gradio-quickstart/image.py
```

Open the local URL printed in the terminal to use the demo. This script also
creates a public Gradio share URL https://\*\*\*.gradio.live.
