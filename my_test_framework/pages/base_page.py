# This contains all the base class for all pages with the containing reusable methods
# The wait_for_element function has been imported and is used on the functions below
# This wait_for_element function makes sure that the element is located first before doing an action
from utils.config import wait_for_element

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # Function for finding an element
    def find_element(self, locator):
        return wait_for_element(self.driver, locator)

    # Function for clicking an element (button etc.)    
    def click_element(self, locator):
        element = wait_for_element(self.driver, locator)
        # Once the element has been found, the click action is called
        element.click()

    # Function for entering text in an element (input textbox, search box, etc.)
    def enter_text(self, locator, text):
        element = self.find_element(locator)
        # Once the element has been found, the text are inputted
        element.send_keys(text)

    # Function for retrieving texts on a web page for validating error messages, button text, etc.
    def get_text(self, locator):
        element = wait_for_element(self.driver, locator)
        # Once the element has been found, the value is returned
        if element:
            return element.text
        # If the element is not found, it will return None
        else:
            return None