import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

# Initialize the Chrome driver
driver = webdriver.Chrome()


# Get the absolute path to the repository's root
repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

# Construct the absolute path to the index.html file
monopoly_web_index_path = os.path.join(repo_root, 'monopoly-interface', 'index.html')

# Open the web page
driver.get("file://"+monopoly_web_index_path)


# Wait for the page to load completely
time.sleep(2)

driver.execute_script("console.log('Hello from the console!')")

time.sleep(20)

# TODO
# Interact with the page