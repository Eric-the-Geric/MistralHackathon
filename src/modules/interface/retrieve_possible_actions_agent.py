import os

import backoff
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
from selenium.webdriver.remote.webdriver import WebDriver

from src.modules.interface.utils import get_cleaned_html

RETRIEVE_POSSIBLE_ACTIONS_AGENT_TOOL = {
    "type": "function",
    "function": {
        "name": "retrieve_possible_actions_agent",
        "description": "Retrieve possible actions for the agent to take using html code.",
        "parameters": {
            "type": "object",
            "properties": {
                "possible_actions": {
                    "type": "array",
                    "description": "The possible actions for the agent to take.",
                    "items": {
                        "type": "string",
                        "description": "The possible action for the agent to take.",
                    },
                },
                "extra_useful_info": {
                    "type": "string",
                    "description": "Extra useful information for the agent to take action. (Ex. current amount of money, current player, minimal required amount to bid, etc.)",
                },
            },
            "required": ["possible_actions"],
        },
    },
}

system_prompt = """You are in the interface agent.
The user will send you a instruction to run on the interface and a html code.
The html code represent a monopoly game interface.

Example actions:
- Press the 'Roll Dice' button.
- Enter an amount to bid (the minimum bid is $10).
- Go to the 'Trade' tab.

You might want to give extra info in the response, like the current amount of money, the current player, the minimal required amount to bid, etc.

You do not need to mention directly any html code in your response.

The main interface has 3 tabs (Buy, Manage, Trade). Tabs will give access to different actions.

Output only the results, be concise and clear.
"""


@backoff.on_exception(backoff.expo, Exception, max_tries=3, max_time=60)
def retrieve_possible_actions_agent(html_code: str) -> str:
    api_key = os.environ["MISTRAL_API_KEY"]
    model = "mistral-large-latest"

    client = MistralClient(api_key=api_key)

    user_prompt = """
    I to retrieve possible actions for the agent to take using the following HTML code:
    {html_code}
    """.format(
        html_code=html_code
    )

    chat_response = client.chat(
        model=model,
        messages=[
            ChatMessage(role="system", content=system_prompt),
            ChatMessage(role="user", content=user_prompt),
        ],
        # tools=[RETRIEVE_POSSIBLE_ACTIONS_AGENT_TOOL],
        # tool_choice="any",
    )

    result = chat_response.choices[0].message.content
    if isinstance(result, list):
        result = ", ".join(result)

    # assert isinstance(chat_response.choices[0].message.tool_calls, list)

    # function_arguments_parsed = json.loads(
    #     chat_response.choices[0].message.tool_calls[0].function.arguments
    # )

    # assert "possible_actions" in function_arguments_parsed

    # if "extra_useful_info" in function_arguments_parsed:
    #     actions = function_arguments_parsed["possible_actions"]
    #     extra_info = function_arguments_parsed["extra_useful_info"]
    #     result = f"{', '.join(actions)} - {extra_info}"
    # else:
    #     result = ", ".join(function_arguments_parsed["possible_actions"])

    return result


def retrieve_possible_actions_agent_from_driver(driver: WebDriver) -> str:
    html_code = get_cleaned_html(driver)
    return retrieve_possible_actions_agent(html_code)
