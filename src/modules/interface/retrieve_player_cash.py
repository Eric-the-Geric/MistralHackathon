from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


def retrieve_player_cash(driver: WebDriver) -> dict:
    """Example return value: Player cash: {'Player 1': 1400, 'AI Test 1': 1500}"""
    player_cash = {}

    for i in range(1, 4):  # Adjust range if there are more or fewer players
        try:
            # Construct IDs for the player name and cash elements
            name_id = f"p{i}moneyname"
            cash_id = f"p{i}money"

            # Locate elements using the constructed IDs
            player_name_element = driver.find_element(By.ID, name_id)
            player_cash_element = driver.find_element(By.ID, cash_id)

            # Extract text from the elements
            player_name = player_name_element.text
            player_cash_value = player_cash_element.text

            # Convert cash value to an integer
            player_cash[player_name] = int(player_cash_value)
        except Exception as e:
            # Handle case where element is not found or other errors
            print(f"Error processing player {i}: {e}")

    return player_cash
