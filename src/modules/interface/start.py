import os
import time

from selenium import webdriver

from src.modules.interface.actions_to_prompt import ExtraAction, get_action_prompt
from src.modules.interface.interface_agent import run_action_on_interface
from src.modules.interface.retrieve_game_history import retrieve_game_history
from src.modules.interface.retrieve_player_cash import retrieve_player_cash
from src.modules.interface.utils import get_cleaned_html
from src.shared.actions import Action


def start_interface() -> None:
    repo_root = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..", "..")
    )
    monopoly_web_index_path = os.path.join(
        repo_root, "monopoly-interface", "index.html"
    )
    file_url = f"file://{monopoly_web_index_path}"

    driver = webdriver.Chrome()

    driver.get(file_url)

    driver.implicitly_wait(2)
    time.sleep(3)

    try:
        actions_to_execute = [
            ExtraAction.INITIALIZE,
            ExtraAction.ROLL_DICE,
            Action.BUY,
            Action.BUY_PROPERTY,
            Action.END_TURN,
        ]

        for action in actions_to_execute:
            print("[Performing action]", action)
            cleaned_html = get_cleaned_html(driver)

            js_code_for_action = run_action_on_interface(
                html_code=cleaned_html,
                action=get_action_prompt(action),
            )

            print("js_code_for_action>", js_code_for_action)

            driver.execute_script(js_code_for_action)

            time.sleep(2)

        print("Player histories:", retrieve_game_history(driver))
        print("Player cash:", retrieve_player_cash(driver))

        time.sleep(200)
    finally:
        driver.quit()


if __name__ == "__main__":
    start_interface()
