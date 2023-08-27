from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_BTN = (By.ID, 'nav-search-submit-button')
CART_ICON = (By.CSS_SELECTOR, '#nav-cart')
ORDERS_BTN = (By.ID, 'nav-orders')
HEADER_LINKS = (By.CSS_SELECTOR, '#zg_header a')
BESTSELLER_BTN = (By.CSS_SELECTOR, "[href='/gp/bestsellers/?ref_=nav_cs_bestsellers']")
#PRODUCT_NAME = (By.CSS_SELECTOR, 'h2 span.a-text-normal')
PRODUCT_NAME = (By.CSS_SELECTOR, '#productTitle')
CLICK_FIRST_ITEM = (By.CSS_SELECTOR, ' .a-price-whole')
CLICK_ADD_TO_CART = (By.ID, 'add-to-cart-button')
SIGNIN_BTN = (By.CSS_SELECTOR, '#nav-signin-tooltip .nav-action-signin-button')


@given('open Amazon page')
def open_amazon(context):
    # context.driver.get('https://www.amazon.com/')
    context.app.main_page.open_main()


@when('Search for {product}')
def search_on_amazon(context, product):
    context.app.header.search_product(product)
    #context.driver.find_element(*SEARCH_FIELD).send_keys(product)
    #context.driver.find_element(*SEARCH_BTN).click()


@when('click Cart Icon')
def click_cart_icon(context):
    context.driver.find_element(*CART_ICON).click()


@when('click Orders')
def click_orders(context):
    # context.driver.find_element(*ORDERS_BTN).click()
    context.app.header.click_orders()


@when('click on first product')
def click_on_first_product(context):
    context.driver.find_element(*CLICK_FIRST_ITEM).click()


@when('Store product name')
def store_product_name(context):
    context.product_name = context.driver.find_element(*PRODUCT_NAME).text
    print(f'Current product: {context.product_name}')


@when('Click BestSellers button')
def click_bestsellers_button(context):
    context.driver.find_element(*BESTSELLER_BTN).click()


@when('Click add to Cart Icon')
def click_add_to_cart(context):
    context.driver.find_element(*CLICK_ADD_TO_CART).click()


@when('Open cart page')
def open_cart_page(context):
    context.driver.get('https://www.amazon.com/gp/cart/view.html?ref_=nav_cart')


@when('Click on button from Signin popup')
def click_from_signin_popup(context):
    context.driver.wait.until(EC.element_to_be_clickable(SIGNIN_BTN)).click()
    assert "signin" in context.driver.current_url, "Sign In page not opened"


@then('Verify BestSellers page has 5 header links')
def verify_link_amount(context):
    links = context.driver.find_elements(*HEADER_LINKS)
    print(links)
    print(f'Total links: {len(links)}')
    assert len(links) == 5, f'Error, expected 5 did not match actual {len(links)}'
