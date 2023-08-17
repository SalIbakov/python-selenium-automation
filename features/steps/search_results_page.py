from behave import given, when, then
from selenium.webdriver.common.by import By

SEARCH_RESULT = (By.CSS_SELECTOR, '.a-color-state.a-text-bold')
CART_EMPTY_SIGN = (By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']")
PRODUCT_NAME = (By.CSS_SELECTOR, '#productTitle')

@then('verify Amazon Cart page is empty')
def verify_amazon_cart_page_is_empty(context):
    actual_result = context.driver.find_element(*CART_EMPTY_SIGN).text
    assert actual_result == 'Your Amazon Cart is empty', f'Expected Your Amazon Cart is empty instead got {actual_result}'


@then('verify search result is {expected_result}')
def verify_search_result(context, expected_result):
    actual_result = context.driver.find_element(*SEARCH_RESULT).text
    assert expected_result == actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'


@then('verify cart has correct product')
def verify_correct_product(context):
    actual_name = context.driver.find_element(*PRODUCT_NAME).text
    assert context.product_name == actual_name, f'Expected {context.product_name} but got {actual_name}'


@then('Verify Sign In page opened')
def signin_page_opened(context):
    context.driver.get('https://www.amazon.com/ap/signin')


