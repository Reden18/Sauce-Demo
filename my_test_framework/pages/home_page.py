# The wait_for_element function has been imported and is used on the functions below
# This wait_for_element function makes sure that the element is located first before doing an action
# The BasePage is imported
# The config and get_locator function is also imported
from utils.config import wait_for_element
from utils.config import config, get_locator
from pages.base_page import BasePage

# This class contains methods for interacting with the home page
class HomePage(BasePage):
    # The get locator function is called and assign the values to their corresponding variables
    MENU_BUTTON = get_locator(config['locators']['home_page']['menu_button'])
    LOGOUT_BUTTON = get_locator(config['locators']['home_page']['logout_button'])

    # The function clicking the hamburger main menu
    def open_menu(self):
        self.click_element(self.MENU_BUTTON)

    # The function for clicking the logout button
    def logout(self):
        # The open_menu function is called since the logout option is hidden on the hamburger menu
        self.open_menu()
        wait_for_element(self.driver, self.LOGOUT_BUTTON)
        self.click_element(self.LOGOUT_BUTTON)

class AddToCart(BasePage):
    ADD_TO_CART_BUTTON = get_locator(config['locators']['home_page']['add_to_cart_button'])

    def add_to_cart(self):
        self.click_element(self.ADD_TO_CART_BUTTON)