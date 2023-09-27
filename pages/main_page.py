from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page
from support.logger import logger


class MainPage(Page):

    def open_main(self):
        self.open_url()


