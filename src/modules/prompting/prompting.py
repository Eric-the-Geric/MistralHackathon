from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
from dotenv import load_dotenv
import os
import json

ROOT_DIR = '.env'
load_dotenv(ROOT_DIR)
api_key = os.environ["MISTRAL_API_KEY"]
model = "mistral-large-latest"
def main():
    current_strategy = strategist()
    action, response = agent(current_strategy)
    function_result = names_to_functions[function_name](**function_params)
    function_result

    tool_call = response.choices[0].message.tool_calls[0]
    function_name = tool_call.function.name
    function_params = json.loads(tool_call.function.arguments)
    print("\nfunction_name: ", function_name, "\nfunction_params: ", function_params)


    [ChatMessage(role=x, content=y) for x, y in all_messages.items()]
def strategist():
    client = MistralClient(api_key=api_key)
    messages = [
            ChatMessage(role="system", content="You are an ai agent that was designed to be a master monopoly strategist"),
            ChatMessage(role="user", content="What is the best short term, medium term and long term strategies for the beginning of the game")
    ]
    # No streaming
    chat_response = client.chat(
        model=model,
        messages=messages,
    )
    return chat_response.choices[0].message.content

def agent(context):
    client = MistralClient(api_key=api_key)
    messages = [
            ChatMessage(role="system", content="You are an outstanding monopoly player. You only output functions given to you"),
            ChatMessage(role="user", content=context)
    ]
    # No streaming
    chat_response = client.chat(
        model=model,
        messages=messages,
        tools=TOOLS,
        tool_choice="any"
    )
    messages.append(response.choices[0].message)
    return chat_response.choices[0].message.content, messages, chat_reponse

if __name__ == "__main__":
    main()
