from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# create a new Chrome browser instance
service = Service(executable_path=r'C:\Users\Admin\python-selenium-automation\chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# By ID - #


# By Class(es) - .
driver.find_element(By.CSS_SELECTOR, '.nav-search-submit-button')
#mult classes using '.' to join
driver.find_element(By.CSS_SELECTOR, ('.nav-input.nav-progressive-attribute')

# By ID + Class # - . or any comb
driver.find_element(By.CSS_SELECTOR, '#nanv-input.nav-progressive-attribute')

# By Name "[]"
driver.find_element(By.CSS_SELECTOR, "[placeholder='Search Amazon'][aria-label='Search Amazon']")

# By ID suing tag - tag#
driver.find_element(By.CSS_SELECTOR, 'input#nanv-input.nav-progressive-attribute')

# By partial attribute *
driver.find_element(By.CSS_SELECTOR, "[placeholder*='Search Amazon'][aria-label='Search Amazon']")

# By parent/ child element
