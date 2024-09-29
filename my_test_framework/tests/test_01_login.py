# Importing pytest for the fixture
# Importing LoginPage class
# Importing values from config.py
# LOGIN_ERROR_MESSAGES contains all the expected error messages for the login page
import pytest
from pages.login_page import LoginPage
from utils.config import USERNAME, PASSWORD, WRONG_USERNAME, WRONG_PASSWORD, LOGIN_ERROR_MESSAGES, INVENTORY_URL
from utils.conftest import setup

# Uses the fixture created on the conftest.py that initializes the webdriver
@pytest.mark.usefixtures("setup")
class TestLogin:
    # Test for leaving the username input box empty and clicking login button
    def test_username_required(self):
        login_page = LoginPage(self.driver)
        # Only password input box is filled out
        login_page.enter_password(WRONG_PASSWORD)
        # The login button is clicked after entering texts in the password input box
        login_page.click_login()
        # Retrieving the error message displayed in the login page after leaving the username empty
        error_message = login_page.get_error_message()
        # Validating the error message through assertion
        # This compares the error message retrieved from the login page and the one specified in the config.yaml file
        assert error_message == LOGIN_ERROR_MESSAGES['username_required']

    # Test for leaving the password input box empty and clicking login button
    def test_password_required(self):
        login_page = LoginPage(self.driver)
        # The login page is refreshed to remove the texts inputted from the previous test
        login_page.refresh_page()
        # Only username input box is filled out
        login_page.enter_username(WRONG_USERNAME)
        # The login button is clicked after entering texts in the username input box
        login_page.click_login()
        # Retrieving the error message displayed in the login page after leaving the password empty
        error_message = login_page.get_error_message()
        # Validating the error message through assertion
        # This compares the error message retrieved from the login page and the one specified in the config.yaml file
        assert error_message == LOGIN_ERROR_MESSAGES['password_required']

    # Test for leaving both the username and password input box empty and clicking login button
    def test_both_username_and_password_required(self):
        login_page = LoginPage(self.driver)
        # The login page is refreshed to remove the texts inputted from the previous test
        login_page.refresh_page()
        # Login button is clicked without entering username and password
        login_page.click_login()
        # Retrieving the error message displayed in the login page after leaving the username and password empty
        error_message = login_page.get_error_message()
        # Validating the error message through assertion
        # This compares the error message retrieved from the login page and the one specified in the config.yaml file
        assert error_message == LOGIN_ERROR_MESSAGES['username_required']

    # Test for inputting invalid username and password and clicking login button
    def test_invalid_credentials(self):
        login_page = LoginPage(self.driver)
        # The login page is refreshed to remove the texts inputted from the previous test
        login_page.refresh_page()
        # Username input box is supplied with an invalid username
        login_page.enter_username(WRONG_USERNAME)
        # Password input box is supplied with an invalid password
        login_page.enter_password(WRONG_PASSWORD)
        # The login button is clicked after entering texts in the username and password input box
        login_page.click_login()
        # Retrieving the error message displayed in the login page after inputting invalid credentials
        error_message = login_page.get_error_message()
        # Validating the error message through assertion
        # This compares the error message retrieved from the login page and the one specified in the config.yaml file
        assert error_message == LOGIN_ERROR_MESSAGES['invalid_credentials']

    # Test for inputting valid username and password and clicking the login button
    def test_successful_login(self):
        login_page = LoginPage(self.driver)
        # The login page is refreshed to remove the texts inputted from the previous test
        login_page.refresh_page()
        # Username input box is supplied with valid username
        login_page.enter_username(USERNAME)
        # Password input box is supplied with valid password
        login_page.enter_password(PASSWORD)
        # The login button is clicked after entering texts in the username and password input box
        login_page.click_login()
        # The assumption here is that if the user successfully logs in, they will be taken to a URL that contains the base_url plus the plus the url for this homepage
        assert INVENTORY_URL in self.driver.current_url