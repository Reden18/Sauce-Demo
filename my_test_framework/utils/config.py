# This file loads the configurations from config.yaml
import yaml
# The selenium libraries components are imported
# By is a class used to locate elements in the DOM
from selenium.webdriver.common.by import By
# TimeoutException is an exception use for error handling in tests.
from selenium.common.exceptions import TimeoutException
# WebDriverWait is used to implement explicit waits
from selenium.webdriver.support.ui import WebDriverWait
# The expected_conditions is used with WebDriverWait to check conditions
from selenium.webdriver.support import expected_conditions as EC

# Function for accessingthe config.yaml file
def load_config():
    with open('utils/config.yaml', 'r') as file:
        config = yaml.safe_load(file)
    return config

# Loading the configurations
config = load_config()

# Assigning the base url, credentials and browser settings to their respective variables
# These variables contains strings
BASE_URL             = config['base_url']
USERNAME             = config['credentials']['username']
PASSWORD             = config['credentials']['password']
WRONG_USERNAME       = config['credentials']['wrong_username']
WRONG_PASSWORD       = config['credentials']['wrong_password']
BROWSER_TYPE         = config['browser']['type']
DRIVERS              = config['browser']['drivers']
LOGIN_ERROR_MESSAGES = config['error_messages']['login_page']
INVENTORY_URL        = config['inventory_url']

# Function to convert the locator type from string to By class
def get_locator(locator_dict):
    # Fetching the locator type and format it to uppercase
    locator_type = locator_dict['type'].upper()
    # Condition for locator type ID
    if locator_type == 'ID':
        return (By.ID, locator_dict['value'])
    # Condition for locator type CSS Path
    elif locator_type == 'CSS':
        return (By.CSS_SELECTOR, locator_dict['value'])
    # Condition for locator type Class
    elif locator_type == 'CLASS':
        return (By.CLASS_NAME, locator_dict['value'])
    # We can add more locator types here such as xpath or tag name
    else:
        # A value error is raised if locator type from config.yaml file is not supported (for now, I used ID, CLASS and CSS selector only)
        raise ValueError(f"Unsupported locator type: {locator_type}")
    
# Function for waiting for an element to be visible before a certain action can be performed
# Since the waiting can be used by several tests, I just set it up here
# The tests can just call this function if needed
def wait_for_element(driver, value, timeout=10, condition='visible'):
    wait = WebDriverWait(driver, timeout)
    try: 
        # Condition if the element is visible
        if condition == 'visible':
            return wait.until(EC.visibility_of_element_located((value)))
        # Condition if the element is clickable
        elif condition == 'clickable':
            return wait.until(EC.element_to_be_clickable((value)))
        # Condition if the element is present
        elif condition == 'presence':
            return wait.until(EC.presence_of_element_located((value)))
        # If none of the conditions are met, a value error is raised
        else:
            raise ValueError("Invalid condition specified.")
    # Return None if the element is not found in the specified time
    except TimeoutException:
        return None  