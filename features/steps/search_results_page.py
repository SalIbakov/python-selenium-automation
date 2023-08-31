from behave import given, when, then
from selenium.webdriver.common.by import By

SEARCH_RESULT = (By.CSS_SELECTOR, '.a-color-state.a-text-bold')
SIGNIN_HEADER = (By.XPATH, "//h1[@class='a-spacing-small']")
EMAIL_INPUT = (By.ID, 'ap_email')
CART_EMPTY_SIGN = (By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']")
PRODUCT_NAME = (By.ID, 'productTitle')
PRODUCT_NAME1 = (By.CSS_SELECTOR, '#productTitle')
PRODUCT_TITLE = (By.CSS_SELECTOR, 'h2 span.a-text-normal')
SEARCH_RESULTS = (By.CSS_SELECTOR, "[data-component-type='a-search-result']")
PRODUCT_IMG = (By.CSS_SELECTOR, " .a-image[data-image-latency='s-product-image']")


@then('verify Amazon Cart page is empty')
def verify_amazon_cart_page_is_empty(context):
    context.app.cart.verify_amazon_cart_page_is_empty()
    #actual_result = context.driver.find_element(*CART_EMPTY_SIGN).text
    #assert actual_result == 'Your Amazon Cart is empty', f'Expected Your Amazon Cart is empty instead got {actual_result}'


@then('verify search result is {expected_result}')
def verify_search_result(context, expected_result):
    context.app.search_result_page.verify_search_result(expected_result)


@then('verify cart has correct product')
def verify_correct_product(context):
    context.app.cart.verify_correct_product()
    #context.driver.get('https://www.amazon.com/gp/cart/view.html?ref_=nav_cart')
    #actual_name = context.driver.find_element(*PRODUCT_NAME).text
    #assert context.product_name == actual_name, f'Expected {context.product_name} but got {actual_name}'


@then('Verify Sign In page opened')
def signin_page_opened(context):
    # 1 context.driver.get('https://www.amazon.com/')
    # 2 actual_text = context.driver.find_element(*SIGNIN_HEADER).text
    # assert actual_text == 'Sign In', f'Expected Sign In but got {actual_text}'
    # context.driver.find_element(*EMAIL_INPUT)
    context.app.signin_page.signin_page_opened()


@then('Verify every product has name and image')
def verify_product_name_image(context):
    all_products = context.driver.find_elements(*SEARCH_RESULTS)

    for product in all_products:
        product_title = product.find_element(*PRODUCT_TITLE).text
        print(product_title)
        assert product_title, 'Product title not shown'
        product.find_element(*PRODUCT_IMG)

