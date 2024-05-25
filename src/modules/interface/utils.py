from selenium import webdriver


def get_and_remove_display_none_elements(driver: webdriver.Chrome) -> None:
    driver.execute_script("""
        var elements = document.querySelectorAll('[style*="display: none"]');
        elements.forEach(function(element) {
            element.parentNode.removeChild(element);
        });
    """)

    driver.execute_script("""
        var elementsToRemove = [];
        var elements = document.querySelectorAll('*');
        elements.forEach(function(element) {
            if (window.getComputedStyle(element).display === 'none') {
                elementsToRemove.push(element);
            }
        });
        elementsToRemove.forEach(function(element) {
            element.remove();
        });
    """)

def get_cleaned_html(driver: webdriver.Chrome, url: str) -> str:
    driver.get(url)
    
    # Remove elements with display: none;
    get_and_remove_display_none_elements(driver)
    
    # Return the cleaned HTML
    return driver.page_source
