import json
import os

import backoff
from dotenv import load_dotenv
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage

load_dotenv()


system_prompt = """You are in the interface module.
The user will send you a instruction to run on the interface and a html code.

You must generate plain javascript code to run on the interface to perform the instruction.
You have to press buttons or use selectors to perform the action on the interface and NOT try to execute js functions directly.
"""

TOOL = {
    "type": "function",
    "function": {
        "name": "run_action_on_interface",
        "description": "Run an action on the interface using the provided HTML code.",
        "parameters": {
            "type": "object",
            "properties": {
                "javascript_code": {
                    "type": "string",
                    "description": "The JavaScript code to run on the interface.",
                },
            },
            "required": ["javascript_code"],
        },
    },
}


@backoff.on_exception(backoff.expo, Exception, max_tries=3, max_time=60)
def run_action_on_interface(html_code: str, action: str) -> str:
    api_key = os.environ["MISTRAL_API_KEY"]
    model = "mistral-large-latest"

    client = MistralClient(api_key=api_key)

    user_prompt = """
    The user wants to perform the following action on the interface:
    {action}

    The user has provided the following HTML code:
    {html_code}
    """.format(
        action=action, html_code=html_code
    )

    chat_response = client.chat(
        model=model,
        messages=[
            ChatMessage(role="system", content=system_prompt),
            ChatMessage(role="user", content=user_prompt),
        ],
        tools=[TOOL],
        tool_choice="any",
    )

    assert isinstance(chat_response.choices[0].message.tool_calls, list)

    function_arguments_parsed = json.loads(
        chat_response.choices[0].message.tool_calls[0].function.arguments
    )

    assert "javascript_code" in function_arguments_parsed

    print("javascript_code", function_arguments_parsed["javascript_code"])

    return function_arguments_parsed["javascript_code"]
