import time
from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


class HeaderPage(Page):

    SEARCH_ICON = (By.CSS_SELECTOR, '.icon-search.modal__toggle-open')
    SEARCH_INPUT = (By.ID, 'Search-In-Modal')
    SEND_SEARCH =(By.CSS_SELECTOR, "button[type ='submit']")
    POPUP_CLOSE = (By.CSS_SELECTOR,'.popup-close')
    def search_field(self):
        self.click(*self.SEARCH_ICON)
        # time.sleep(3)

    def input_search(self, text):
        self.input_text(text, *self.SEARCH_INPUT)

    def product_search(self, product):
        self.input_text(product, *self.SEARCH_INPUT)



    def click_to_search(self):
        self.click(*self.SEND_SEARCH)
        # time.sleep(2)

    # def input_text(self):
    #     search_text = self.find_element(*self.SEARCH_INPUT)
    #     click_search = self.find_element(*self.SEND_SEARCH)
    #     close_popup = self.find_element(*self.POPUP_CLOSE)
    #
    #
    #     action = ActionChains(self.driver)
    #     action.click(close_popup).perform()
    #     time.sleep(3)
    #     action.send_keys_to_element(click_search).perform()
    #     time.sleep(3)
    #     action.click(search_text).perform()
    #     time.sleep(3)
    #
    #



    # def input_search(self, text):
    #     input_text = self.find_element(text,self.SEARCH_INPUT)
    #     click_search = self.find_element(*self.SEARCH_INPUT)
    #
    #     action = ActionChains(self.driver)
    #     action.send_keys(input_text).perform()
    #     time.sleep(1)
    #     action.click(click_search).perform()