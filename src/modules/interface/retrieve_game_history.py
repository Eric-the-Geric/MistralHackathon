from selenium.webdriver.remote.webdriver import WebDriver


def retrieve_game_history(driver: WebDriver) -> str:
    script = """
    const alertDiv = document.querySelector('#alert');
    const childDivs = alertDiv.querySelectorAll('div');
    const alertText = Array.from(childDivs).map(div => div.textContent).join('\\n');
    return alertText;
    """
    history_element_content = driver.execute_script(script)
    return history_element_content
