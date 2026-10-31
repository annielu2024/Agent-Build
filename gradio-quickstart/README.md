 

# Gradio Quickstart

## Basic demo

Create and activate a virtual environment, install Gradio in it, then run the
demo with `python3` while the environment is active. Run these commands from
the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate
cd gradio-quickstart
python3 -m pip install -r requirements.txt
python3 demo.py
```

Check out the demo by copying the local URL http://127.0.0.1:7860 (local) or the public URL https://\*\*\*.gradio.live and pasting into the browser.

## Image converting demo

The image demo converts an uploaded image into a pencil sketch. After setting
up and activating the virtual environment above, run this from the
`gradio-quickstart` directory:

```bash
python3 image.py
```

Open the local URL printed in the terminal to use the demo. This script also
creates a public Gradio share URL https://\*\*\*.gradio.live.

## LLM API example

The Qwen chat example in `apidemo.py` uses the OpenAI Python
client with an OpenAI-compatible API endpoint. Before running it:

1. Create or copy an API key in the Alibaba Cloud Model Studio / DashScope
   console. Keep the key private; do not put it in your source code or commit it
   to Git.
2. Set the `DASHSCOPE_API_KEY` environment variable using the instructions for
   your operating system below. Replace `your-api-key` with your actual key.
3. Run the app from the `gradio-quickstart` directory. If you have not
   installed the dependencies yet, follow the Gradio quickstart setup above
   first.

### macOS

For the current Terminal session:

```bash
export DASHSCOPE_API_KEY="your-api-key"
python3 apidemo.py
```

To set it for future Terminal sessions, add the `export` line to your shell
profile (usually `~/.zshrc` on current macOS), then open a new Terminal window.
The profile stores the key as plain text, so keep that file private.

### Windows

In PowerShell, for the current window:

```powershell
$env:DASHSCOPE_API_KEY = "your-api-key"
python apidemo.py
```

To save the variable for future processes, run this in PowerShell:

```powershell
[Environment]::SetEnvironmentVariable("DASHSCOPE_API_KEY", "your-api-key", "User")
```

Then open a new PowerShell window and run:

```powershell
python apidemo.py
```

### Linux

For the current terminal session:

```bash
export DASHSCOPE_API_KEY="your-api-key"
python3 apidemo.py
```

To set it for future sessions, add the `export` line to your shell profile
(commonly `~/.bashrc` or `~/.zshrc`), then open a new terminal. The profile
stores the key as plain text, so ensure it is not publicly readable or
committed to Git.

The app uses the `qwen3.7-flash` model and prints a local Gradio URL in the
terminal. It also creates a public share URL https://\*\*\*.gradio.live; anyone with that link may be able
to access the demo while it is running.
