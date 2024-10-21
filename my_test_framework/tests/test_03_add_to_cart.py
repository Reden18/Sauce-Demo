import pytest
from pages.home_page import AddToCart
from pages.login_page import LoginPage
from utils.config import USERNAME, PASSWORD
from utils.conftest import setup

@pytest.mark.usefixtures("setup")
class TestAddToCart:
    def test_add_to_cart(self):
        # Log in is performed first
        login_page = LoginPage(self.driver)
        # Entering a valid username
        login_page.enter_username(USERNAME)
        # Entering a valid password
        login_page.enter_password(PASSWORD)
        # Clicking the login button after inputting valid username and password
        login_page.click_login()

        add_to_cart_button = AddToCart(self.driver)
        add_to_cart_button.add_to_cart()