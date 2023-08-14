from behave import given, when, then
from selenium.webdriver.common.by import By

SEARCH_RESULT = (By.CSS_SELECTOR, '.a-color-state.a-text-bold')
CART_EMPTY_SIGN = (By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']")

@then('verify Amazon Cart page is empty')
def verify_amazon_cart_page_is_empty(context):
    actual_result = context.driver.find_element(*CART_EMPTY_SIGN).text
    assert actual_result == 'Your Amazon Cart is empty', f'Expected Your Amazon Cart is empty instead got {actual_result}'


@then('verify search result is {expected_result}')
def verify_search_result(context, expected_result):
    actual_result = context.driver.find_element(*SEARCH_RESULT).text
    assert expected_result == actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'
