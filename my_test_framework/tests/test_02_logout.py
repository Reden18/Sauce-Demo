# Importing pytest for the fixture
# Importing LoginPage class
# Importing HomePage class
# Importing values from config.py
import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from utils.config import USERNAME, PASSWORD, BASE_URL
from utils.conftest import setup

# Uses the fixture created on the conftest.py that initializes the webdriver
@pytest.mark.usefixtures("setup")
class TestLogout:
    # This function tests logging out after logging in as a user
    def test_successful_logout(self):
        # Log in is performed first
        login_page = LoginPage(self.driver)
        # Entering a valid username
        login_page.enter_username(USERNAME)
        # Entering a valid password
        login_page.enter_password(PASSWORD)
        # Clicking the login button after inputting valid username and password
        login_page.click_login()

        # Then, logout is tested
        home_page = HomePage(self.driver)
        home_page.logout()
        ## This assertion validates if the current url contains the same url used during the webdriver initialization
        assert BASE_URL == self.driver.current_url