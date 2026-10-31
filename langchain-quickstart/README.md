# LangChain Quickstart

This example sends a prompt to the Qwen `qwen3.7-flash` model and prints the
response. It uses LangChain's OpenAI-compatible chat model integration with
Alibaba Cloud Model Studio (DashScope).

## 1. Create a virtual environment

Run these commands from the `langchain-quickstart` directory:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell, activate it with:

```powershell
.\.venv\Scripts\Activate.ps1
```

## 2. Install the required packages

With the virtual environment active, install the packages listed in
`requirements.txt`:

```bash
python -m pip install -r requirements.txt
```

## 3. Configure your API credentials

Create an API key in the Alibaba Cloud Model Studio / DashScope console. In
this directory, create a file named `.env` with the following settings:

```dotenv
OPENAI_API_KEY=your-dashscope-api-key
OPENAI_BASE_URL=https://dashscope-intl.aliyuncs.com/compatible-mode/v1
```

Replace the placeholder with your API key. Use the compatible-mode endpoint
for your DashScope region; for example, China accounts use
`https://dashscope.aliyuncs.com/compatible-mode/v1`. Keep `.env` private and
do not commit your API key.

## 4. Run the chat example

From the `langchain-quickstart` directory, with the virtual environment active
and `.env` configured, run:

```bash
python simple_chat.py
```

The script sends “Hello, please introduce yourself.” to the model and prints
the response in the terminal.
