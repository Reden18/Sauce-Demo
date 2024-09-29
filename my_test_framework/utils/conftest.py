# This file contains the setup and teardown functionality using pytest
import pytest
import time
from utils.browser import get_driver
from utils.config import BASE_URL

# Creating fixtures for setting up the webdriver
# This fixture will be instatiated foe every class
@pytest.fixture(scope="class")
def setup(request):
    # The get_driver() function is called from the browser.py module
    driver = get_driver()
    # Condition if the webdriver initialization fails
    if driver is None:
        pytest.fail("WebDriver failed to initialize")
    # Retrieving the base url
    driver.get(BASE_URL)
    # Accessing the attributes on the current class
    request.cls.driver = driver
    yield
    # Closing the webdriver
    driver.quit()
    
# This function is added to add delays between tests
@pytest.fixture(autouse=True)
def delay_between_tests():
    time.sleep(5)  # Wait for 2 seconds before each test