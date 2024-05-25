from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
from dotenv import load_dotenv
import os
import json
from src.shared.actions import Action
from src.modules.prompting.tools import TOOLS

ROOT_DIR = '.env'
load_dotenv(ROOT_DIR)
api_key = os.environ["MISTRAL_API_KEY"]
model = "mistral-large-latest"

def agent():
    client = MistralClient(api_key=api_key)
    messages = [
            ChatMessage(role="system", content="You are an outstanding monopoly player. You only output a single choice of the options given to you"),
            ChatMessage(role="user", content="options are buy, sell or trade. What do you choose")
    ]
    chat_response = client.chat(
        model=model,
        messages=messages,
        tools=TOOLS,
        tool_choice="auto"
    )
    #messages.append(chat_response.choices[0].message)
    #how to see which function it called print(chat_response.choices[0].message.tool_calls[0].function)
    return chat_response

response = agent()
print(response.choices[0].message)
