# The BasePage is imported
# The config and get_locator function is also imported
from pages.base_page import BasePage
from utils.config import config, get_locator

# This class contains methods for interacting with the login page
class LoginPage(BasePage):
    # The get locator function is called and assign the locator values to their corresponding variables
    # Variable for the username input
    USERNAME_INPUT = get_locator(config['locators']['login_page']['username_input'])
    # Variable for the password input
    PASSWORD_INPUT = get_locator(config['locators']['login_page']['password_input'])
    # Variable for the login button
    LOGIN_BUTTON   = get_locator(config['locators']['login_page']['login_button'])
    # Variable for the error message
    ERROR_MESSAGE  = get_locator(config['locators']['login_page']['error_message'])
    # Variable for error button

    # The function for entering the username in the username text box
    def enter_username(self, username):
        self.enter_text(self.USERNAME_INPUT, username)

    # The function for entering the password in the password text box
    def enter_password(self, password):
        self.enter_text(self.PASSWORD_INPUT, password)
        
    # The function for clicking the login button
    def click_login(self):
        self.click_element(self.LOGIN_BUTTON)

    # The function for retrieving the error message
    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)
    
    # The function for refreshing the page
    # I added this fuction so I can run the test consecutively without relaunching the webdriver on each test
    # This function helps clears the texts entered on the previous tests so new input from next tests can be entered
    def refresh_page(self):
        self.driver.refresh()