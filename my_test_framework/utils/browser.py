# This module provides the get_driver() function that initializes the WebDriver based on the browser type specified in config.yaml file
# The webdriver is imported
from selenium import webdriver
# Service is imported from the web driver one for each browser type
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
# The browsers and their corresponding webdrivers are imported
from utils.config import BROWSER_TYPE, DRIVERS

# The function for initializing the webdriver
def get_driver():
    try:
        # Initializes Chrome if chosen as browser from the config.yaml file
        if BROWSER_TYPE == "chrome":
            service = ChromeService(DRIVERS['chrome'])
            driver = webdriver.Chrome(service=service)

        # Initializes Firefox if chosen as browser from the config.yaml file
        elif BROWSER_TYPE == "firefox":
            service = FirefoxService(DRIVERS['firefox'])
            driver = webdriver.Firefox(service=service)

        # Initializes Edge if chosen as browser from the config.yaml file
        elif BROWSER_TYPE == "edge":
            service = EdgeService(DRIVERS['edge'])
            driver = webdriver.Edge(service=service)
        
        # An error will be raised if browser selected is not chrome, firefox, or edge
        else:
            raise ValueError(f"Unsupported browser: {BROWSER_TYPE}")

        # Window is maximized for better visualization
        driver.maximize_window()
        # Returns the webdriver
        return driver

    # Exception handling if error encounterd in initializing the webdriver
    except Exception as e:
        # Returns None
        return None
