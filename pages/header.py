from selenium.webdriver.common.by import By
from pages.base_page import Page


class Header(Page):
    SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_BTN = (By.ID, 'nav-search-submit-button')
    ORDERS_BTN = (By.ID, 'nav-orders')
    SIGNIN_BTN = (By.CSS_SELECTOR, '#nav-signin-tooltip .nav-action-signin-button')
    CART_ICON = (By.CSS_SELECTOR, '#nav-cart')

    def click_cart_icon(self):
        self.click(*self.CART_ICON)

    def search_product(self, product):
        self.input_text(product, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)

    def click_orders(self, *locator):
        # self.driver.find_element(*locator).click()
        self.click(*self.ORDERS_BTN)

        # StaleElementException

        # e = self.find_element(*self.ORDERS_BTN)
        # print("ORDERS_BTN: ", e)
        # self.refresh()
        # e = self.find_element(*self.SEARCH_BTN)
        # print("After refresh, ORDERS_BTN: ", e)
        # e.click()

    def click_from_signin_popup(self):
        self.wait_for_element_clickable_click(*self.SIGNIN_BTN)

    def verify_signin_btn_clickable(self):
        self.wait_for_element_clickable(*self.SIGNIN_BTN)

    def verify_signin_btn_disappears(self):
        self.wait_for_element_disappear(*self.SIGNIN_BTN)

