import time

from dotenv import load_dotenv

from shared.actions import Action
from src.modules.interface.actions_to_prompt import ExtraAction
from src.modules.interface.retrieve_game_history import retrieve_game_history
from src.modules.interface.retrieve_player_cash import retrieve_player_cash
from src.modules.interface.start import execute_action, init_interface

load_dotenv()


if __name__ == "__main__":
    driver = init_interface()
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
