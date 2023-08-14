from behave import given, when, then
from selenium.webdriver.common.by import By


@then('verify Sign In page opens')
def sig_in_page_opens(context):
    expected_result = 'Sign in'
    actual_result = context.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
    assert expected_result == actual_result, f'Expected {expected_result} instead got {actual_result}'

    context.driver.find_element(By.ID, 'ap_email')