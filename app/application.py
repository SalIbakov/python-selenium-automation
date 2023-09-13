from pages.main_page import MainPage
from pages.header import Header
from pages.privacy_notice_page import PrivacyNoticePage
from pages.search_result_page import SearchResultPage
from pages.signin_page import SignInPage
from pages.cart import Cart

class Application:

    def __init__(self, driver):
        self.main_page = MainPage(driver)
        self.header = Header(driver)
        self.privacy_notice_page = PrivacyNoticePage(driver)
        self.search_result_page = SearchResultPage(driver)
        self.signin_page = SignInPage(driver)
        self.cart = Cart(driver)



