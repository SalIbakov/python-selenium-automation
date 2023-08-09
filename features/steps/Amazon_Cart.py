from behave import given, when, then
from selenium.webdriver.common.by import By



@when('click Cart Icon')
def click_Cart_Icon(context):
    context.driver.find_element(By.CSS_SELECTOR, '#nav-cart').click()


@then('Amazon Cart page is empty')
def Amazon_Cart_page_is_empty(context):
    expected_result = 'Your Amazon Cart is empty'
