from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from pages.base_page import Page

from pages.header_page import HeaderPage
from pages.main_page import MainPage
from pages.search_page import SearchPage


class Application:
    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.header_page = HeaderPage(self.driver)
        self.search_page = SearchPage(self.driver)