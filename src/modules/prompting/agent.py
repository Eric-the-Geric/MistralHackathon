from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
from dotenv import load_dotenv
import os
import json
#from src.shared.actions import Action
from src.modules.prompting.tools import STARTER_TOOLS, ACTIONS

#print(history)
def main():
    ROOT_DIR = '.env'
    load_dotenv(ROOT_DIR)
    api_key = os.environ["MISTRAL_API_KEY"]
    model = "mistral-large-latest"
    with open('./src/modules/prompting/history.txt', 'r') as f:
        history = f.read()

    strategy = strategist(model, api_key)
    #print(strategy)
    response = agent(strategy + '\n\n' + history, model, api_key)
    tool_call = response.choices[0].message.tool_calls[0]
    function_name = tool_call.function.name
    function_params = json.loads(tool_call.function.arguments)
    print("\nfunction_name: ", function_name, "\nfunction_params: ", function_params)

def agent(current_status, model, api_key):
#    if menu == auction:
    client = MistralClient(api_key=api_key)
    messages = [
            ChatMessage(role="system", content="You are an outstanding monopoly player. Given the a general strategy and the history of the game so far, you need to choose an action that would most likely lead to winning the game."), 
            ChatMessage(role="user", content=current_status)
    ]
    chat_response = client.chat(
        model=model,
        messages=messages,
        tools=ACTIONS,
        tool_choice="any"
    )
    #messages.append(chat_response.choices[0].message)
    #how to see which function it called print(chat_response.choices[0].message.tool_calls[0].function)
    return chat_response

def strategist(model, api_key):
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

if __name__ == "__main__":
    main()
