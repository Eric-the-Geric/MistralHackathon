from selenium.webdriver.remote.webdriver import WebDriver

def retrieve_possible_actions(driver: WebDriver) -> str:
    script = """
        function isElementHidden(element) {
            var style = window.getComputedStyle(element);
            if (!style) {
                return true; // If style is null or undefined, consider the element hidden
            }
            if (style.display === 'none' || style.visibility === 'hidden' || style.opacity === '0') {
                return true;
            }
            if (element.offsetWidth === 0 && element.offsetHeight === 0) {
                return true;
            }
            var rect = element.getBoundingClientRect();
            if (rect.top >= window.innerHeight || rect.left >= window.innerWidth) {
                return true;
            }
            return false;
        }

        var actions = [];

        var landedElement = document.getElementById('landed');
        if (landedElement) {
            var buyButton = landedElement.querySelector('input[type="button"]');
            if (buyButton && !isElementHidden(buyButton) && buyButton.style.display !== 'none') {
                actions.push({
                    id: 'buy-button',
                    value: buyButton.value
                });
            }
        }
        
        // Roll Dice button
        var rollDiceButton = document.getElementById('nextbutton');
        if (rollDiceButton) {
            actions.push({
                id: rollDiceButton.id,
                value: rollDiceButton.value
            });
        }
        var popupTextElement = document.getElementById('popuptext');
        console.log(popupTextElement)
        if (popupTextElement) {
            var okButton = popupTextElement.querySelector('input[type="button"]');
            if (okButton && !isElementHidden(okButton) && okButton.style.display !== 'none') {
                actions.push({
                    id: okButton.id,
                    value: okButton.value
                });
            }
        }
        return actions;
    """
    actions_content = driver.execute_script(script)
    return actions_content
