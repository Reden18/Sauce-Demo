# Selenium WebDriver with Python Example

This repository contains the base setup of a UI testing project using Selenium WebDriver, Python and Page Object Model (POM) pattern.

The test site used for this project is [Sauce Demo](<https://www.saucedemo.com/>)

The tests includes the following:
1. Checking the username is required error
2. Checking the password is required error
3. Checking both username and password is required error
4. Logging in
5. Logging out

# Requirements

* Python 3.12.4
* pip (24.2)
* [venv](<https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/>) (recommended)

# Installation

1. Download or clone the repository 
2. Open a terminal
3. Go to the project root directory "/my_test_framework/".
4. Create a virtual environment: `py -m venv venv`
5. Activate the virtual environment executing the following script: `.\venv\Scripts\activate`
6. Execute the following command to download the necessary libraries:  `pip install -r requirements.txt`

# Test Execution

1. Open a terminal
2. From the project root directory run: `pytest -v --html=reports/test_report.html`

# Configuration

By default, tests will be executed in Chrome. Preferences can be changed in "/utils/config.yaml" file

# Results

To check the report, open the '/reports/test_report.html' file once the execution has finished.

# Links
   [Selenium - Python Documentation](<https://selenium-python.readthedocs.io/>)
   
   [Selenium Documentation](<https://www.selenium.dev/documentation/>)