# Practice with locators: Create locators + search strategy

# Amazon logo, Search by Xpath, "//i[@class="a-icon a-icon-logo"]"
# Email field, Search by ID, "ap_email"
# Continue button, Search by ID, "continue"
# Conditions of use link, Search by Xpath, "gp/help/customer/display.html/ref=ap_signin_notification_condition_of_use?ie=UTF8&nodeId=508088"
# Privacy Notice link, Search by Xpath, "gp/help/customer/display.html/ref=ap_signin_notification_privacy_notice?ie=UTF8&amp;nodeId=468496"
# Need help link, Search by ID, "a-expander-prompt"
# Forgot your password link,Search by ID, "auth-fpp-link-bottom"
# Other issues with Sign-In link, Search by ID, "ap-other-signin-issues-link"
# Create your Amazon account button, Search by ID,  "createAccountSubmit"

# Test Case: Logged out user sees Sign in page when clicking Orders:

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

service = Service(executable_path=r'C:\Users\Admin\python-selenium-automation\chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get('https://www.amazon.com/')

driver.find_element(By.ID, 'nav-orders').click()
sleep(2)

expected_result = 'Sign in'
actual_result = driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
assert expected_result == actual_result, f'Expected {expected_result} instead got {actual_result}'

driver.find_element(By.ID, 'ap_email')

print('Test Passed')
driver.quit()
