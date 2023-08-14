from behave import given, when, then
from selenium.webdriver.common.by import By

SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_BTN = (By.ID, 'nav-search-submit-button')
CART_ICON = (By.CSS_SELECTOR, '#nav-cart')
ORDERS_BTN = (By.ID, 'nav-orders')
HEADER_LINKS = (By.CSS_SELECTOR, '#zg_header a')
BESTSELLER_BTN = (By.CSS_SELECTOR, "[href='/gp/bestsellers/?ref_=nav_cs_bestsellers']")
PRODUCT_NAME = (By.CSS_SELECTOR, 'h1 #productTitle')


@given('open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Search for {search_word}')
def search_on_amazon(context, search_word):
    context.driver.find_element(*SEARCH_FIELD).send_keys(search_word)
    context.driver.find_element(*SEARCH_BTN).click()


@when('click Cart Icon')
def click_cart_icon(context):
    context.driver.find_element(*CART_ICON).click()


@when('click Orders')
def click_orders(context):
    context.driver.find_element(*ORDERS_BTN).click()


@when('click on first product')
def click_on_first_product(context):
    context.driver.find_element(By.CSS_SELECTOR, ).click()


@when('Store product name')
def store_product_name(context):
    context.product_name = context.driver.find_element(*PRODUCT_NAME).text
    print(f'Current product: {context.product_name}')


@when('Click BestSellers button')
def click_bestsellers_button(context):
    context.driver.find_element(*BESTSELLER_BTN).click()


@then('Verify BestSellers page has 5 header links')
def verify_link_amount(context):
    links = context.driver.find_elements(*HEADER_LINKS)
    print(links)
    print(f'Total links: {len(links)}')
    assert len(links) == 5, f'Error, expected 5 did not match actual {len(links)}'
