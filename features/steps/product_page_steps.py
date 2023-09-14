from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


COLOR_OPTIONS = (By.CSS_SELECTOR, '#variation_color_name li')
CURRENT_COLOR = (By.CSS_SELECTOR, '#variation_color_name .selection')


@given('Open Amazon product {product_id} page')
def open_amazon_product(context, product_id):
    context.driver.get(f'https://www.amazon.com/dp/{product_id}/')


@when('Hover over New Arrivals')
def hover_new_arrivals(context):
    context.app.header.hover_new_arrivals()


@then('Verify user can click through colors')
def verify_can_click_colors(context):
    expected_colors = ['Black', 'Blue Over Dye', 'Dark Blue Vintage']

    colors = context.driver.find_elements(*COLOR_OPTIONS)
    print(colors)
    print(len(colors))

    for color in colors:
        color.click()
        current_color = context.driver.find_element(*CURRENT_COLOR).text
        print(current_color)


@then('Verify user can click through selected colors')
def verify_can_click_colors(context):
    expected_colors = ['Black', 'Blue Over Dye', 'Dark Blue Vintage']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)

    for color in colors[:3]:
        color.click()
        current_color = context.driver.find_element(*CURRENT_COLOR).text

        actual_colors.append(current_color)

    assert actual_colors == expected_colors, f'Expected {expected_colors} did not match actual {actual_colors}'