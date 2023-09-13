from behave import *
from time import sleep


@given('Open Amazon T&C page')
def open_amazon_tc_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')
    sleep(2)
    context.driver.refresh()


@when('Store original windows')
def store_original_window(context):
    context.original_window = context.app.privacy_notice_page.store_original_window()


@when('Click on Amazon Privacy Notice link')
def click_privacy_notice_link(context):
    context.app.privacy_notice_page.click_privacy_notice_link()


@when('Switch to the newly opened window')
def switch_window(context):
    context.app.privacy_notice_page.switch_to_new_window()


@then('Verify Amazon Privacy Notice page opened')
def verify_privacy_notice_page_opened(context):
    context.app.privacy_notice_page.verify_opened()


@then('User can close new window')
def close_page(context):
    context.app.privacy_notice_page.close_page()


@then('Switch back to original window')
def return_to_original_window(context):
    context.app.privacy_notice_page.switch_to_window(context.original_window)

