from behave import given, when, then
from selenium.webdriver.common.by import By


@given('open Amazon page in Logged out mode')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('click Orders')
def click_orders(context):
    context.driver.find_element(By.ID, 'nav-orders').click()


@then('Sign In page opens')
def SignIn_page_opens(context):
    expected_result = 'Sign in'
    actual_result = context.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
    assert expected_result == actual_result, f'Expected {expected_result} instead got {actual_result}'

@then('Sign In header is visible, email input field is present')
def email_input_field_present(context):
    context.driver.find_element(By.ID, 'ap_email')
    print('Test Passed')
