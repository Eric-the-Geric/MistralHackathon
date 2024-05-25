from selenium import webdriver


def get_and_remove_display_none_elements(driver: webdriver.Chrome) -> str:
    return driver.execute_script(
        """
        var clone = document.body.cloneNode(true);
        var elementsToRemove = [];

        var elementsDisplayNone = clone.querySelectorAll('[style*="display: none"]');
        elementsDisplayNone.forEach(function(element) {
            elementsToRemove.push(element);
        });

        var allElements = clone.querySelectorAll('*');
        allElements.forEach(function(element) {
            var originalElement = document.querySelector('*[data-xpath="' + element.getAttribute('data-xpath') + '"]');
            if (originalElement && window.getComputedStyle(originalElement).display === 'none') {
                elementsToRemove.push(element);
            }
        });

        elementsToRemove.forEach(function(element) {
            element.remove();
        });


        allElements.forEach(function(element) {
            element.removeAttribute('data-xpath');
        });

        var div = document.createElement('div');
        div.appendChild(clone);
        return div.innerHTML;
        """
    )


def get_cleaned_html(driver: webdriver.Chrome, url: str) -> str:
    driver.get(url)

    # Add unique xpath attributes to elements to map between original and cloned elements
    driver.execute_script(
        """
        function getXPath(element) {
            var paths = [];
            for (; element && element.nodeType == Node.ELEMENT_NODE; element = element.parentNode) {
                var index = 0;
                for (var sibling = element.previousSibling; sibling; sibling = sibling.previousSibling) {
                    if (sibling.nodeType == Node.DOCUMENT_TYPE_NODE)
                        continue;
                    if (sibling.nodeName == element.nodeName)
                        ++index;
                }
                var tagName = element.nodeName.toLowerCase();
                var pathIndex = (index ? "[" + (index + 1) + "]" : "");
                paths.splice(0, 0, tagName + pathIndex);
            }
            return paths.length ? "/" + paths.join("/") : null;
        }

        var allElements = document.querySelectorAll('*');
        allElements.forEach(function(element) {
            element.setAttribute('data-xpath', getXPath(element));
        });
        """
    )

    return get_and_remove_display_none_elements(driver)
