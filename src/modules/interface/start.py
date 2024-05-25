import os
import time
from typing import Union

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

#from src.modules.interface.actions_to_prompt import get_action_prompt
from src.modules.interface.interface_agent import run_action_on_interface
from src.modules.interface.retrieve_game_history import retrieve_game_history
from src.modules.interface.retrieve_player_cash import retrieve_player_cash
from src.modules.interface.utils import get_cleaned_html
from src.shared.actions import Action, ExtraAction


actions_to_prompt: dict[Union[Action, ExtraAction], str] = {
    # Tabs:
    Action.MANAGE: "Go on the 'Manage' tab",
    Action.BUY: "Go to the 'Buy' tab",
    Action.TRADE: "Go to the 'Trade' tab",
    # Actions:
    Action.ROLL_AGAIN: "Roll the dice again",
    Action.BUY_PROPERTY: "Buy the property you landed on Buy ($Any)",
    Action.END_TURN: "End turn",
    Action.PASS: "Pass",
    Action.BID: "Enter an amount and press the 'Bid' button",
    Action.EXIT_AUCTION: "Exit the auction",
    Action.CANCEL_TRADE: "Cancel the trade",
    # Extra actions:
    ExtraAction.INITIALIZE: "Initialize the game for 2 players and start the game. Player 1 has to be human and Player 2 has to be AI (test).",
    ExtraAction.ROLL_DICE: "Roll the dice",
}


def get_action_prompt(action: Union[Action, ExtraAction]) -> str:
    #print((action))
    print(f"Action received: {action}")
    print(f"Type of action: {type(action)}")
    print(f"All Action members: {list(Action)}")
    print(f"All ExtraAction members: {list(ExtraAction)}")
    return actions_to_prompt[action]

def init_interface() -> WebDriver:
    repo_root = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..", "..")
    )
    print("repo_root>", repo_root)
    monopoly_web_index_path = os.path.join(
        repo_root, "monopoly-interface", "index.html"
    )
    print("monopoly_web_index_path>", monopoly_web_index_path)
    file_url = f"file://{monopoly_web_index_path}"

    driver = webdriver.Firefox()

    driver.get(file_url)

    driver.implicitly_wait(2)

    time.sleep(2)

    return driver


def execute_action(driver: WebDriver, action: Union[Action, ExtraAction]) -> None:
    print("[Performing action]", action)
    cleaned_html = get_cleaned_html(driver)

    js_code_for_action = run_action_on_interface(
        html_code=cleaned_html,
        action=get_action_prompt(action),
    )

    print("js_code_for_action>", js_code_for_action)

    driver.execute_script(js_code_for_action)


if __name__ == "__main__":
    driver = init_interface()
    print("Initialized interface", driver)
    time.sleep(1)

    try:
        actions_to_execute = [
            ExtraAction.INITIALIZE,
            ExtraAction.ROLL_DICE,
            Action.BUY,
            Action.BUY_PROPERTY,
            Action.END_TURN,
        ]

        for action in actions_to_execute:
            execute_action(driver, action)

            time.sleep(2)

        print("Player histories:", retrieve_game_history(driver))
        print("Player cash:", retrieve_player_cash(driver))

        time.sleep(200)
    finally:
        driver.quit()
