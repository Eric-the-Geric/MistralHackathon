import time

from dotenv import load_dotenv

from src.modules.interface.retrieve_game_history import retrieve_game_history
from src.modules.interface.retrieve_player_cash import retrieve_player_cash
from src.modules.interface.retrieve_possible_actions_agent import (
    retrieve_possible_actions_agent_from_driver,
)
from src.modules.interface.start import execute_action, init_interface
from src.modules.prompting.agent import agent

load_dotenv()


if __name__ == "__main__":
    driver = init_interface()
    time.sleep(1)

    try:
        history = ""

        initial_prompt = "initialize the game"
        first_roll = "roll the dice"
        first_move = agent(initial_prompt)
        execute_action(driver, first_move)
        first_roll_action = agent(first_roll)
        execute_action(driver, first_roll_action)
        while True:
            possible_actions = retrieve_possible_actions_agent_from_driver(driver)
            print("possible_actions > ", possible_actions)
            # buttons_available = str(retrieve_possible_actions(driver))
            # print(buttons_available)
            history = (
                retrieve_game_history(driver)
                + "\n\n"
                + f"your bank balance: [{retrieve_player_cash(driver)}] and the options available to you are: {possible_actions}."
            )
            action = agent(history)
            execute_action(driver, action)
            time.sleep(2)

            print("Player histories:", retrieve_game_history(driver))
            print("Player cash:", retrieve_player_cash(driver))

        time.sleep(200)
    finally:
        driver.quit()
