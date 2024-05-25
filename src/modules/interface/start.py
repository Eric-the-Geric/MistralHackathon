import os
import time

from selenium import webdriver

from src.modules.interface.actions_to_prompt import ExtraAction, extra_actions_to_prompt
from src.modules.interface.interface_agent import run_action_on_interface
from src.modules.interface.retrieve_game_history import retrieve_game_history
from src.modules.interface.utils import get_cleaned_html


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
        cleaned_html = get_cleaned_html(driver, file_url)
        print("Got cleaned html", cleaned_html)

        js_code_for_action = run_action_on_interface(
            html_code=cleaned_html,
            action=extra_actions_to_prompt[ExtraAction.INITIALIZE],
        )

        driver.execute_script(js_code_for_action)

        time.sleep(6)
        print(retrieve_game_history(driver))

        time.sleep(200)
    finally:
        driver.quit()


if __name__ == "__main__":
    start_interface()
