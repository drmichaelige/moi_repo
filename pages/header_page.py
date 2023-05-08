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
    # SHOP_BY_PRODUCT = (By.XPATH,"//a[contains(text(),'Shop by Product')]")
    CLICK_A_PRODUCT = (By.CSS_SELECTOR,"a[href='/products/sunscreen-spf-30']")
    SHOP_ALL = (By.XPATH,"//span[contains(text(),'Shop All')]")
    GODADDY_PAGE_TITLE = (By.CSS_SELECTOR,'#header .l16jx60o')
    PAGE_TITLE_SOURCE = (By.CSS_SELECTOR, '.line-content')
    def search_icon(self):
        self.wait_for_element_and_click(*self.POPUP_CLOSE)
        time.sleep(2)
        self.wait_for_element_and_click(*self.SEARCH_ICON)
        # time.sleep(3)

    # def input_search(self, text):
    #     self.input_text(text, *self.SEARCH_INPUT)

    def product_search(self, product):
        self.input_text(product, *self.SEARCH_INPUT)



    def click_to_search(self):
        self.click(*self.SEND_SEARCH)
        # time.sleep(2)

    def click_a_product(self):
        self.click(*self.CLICK_A_PRODUCT)


    def click_shop_all(self):
        self.click(*self.SHOP_ALL)


    def godaddy_title_page(self):
        title_page = self.driver.title
        print(title_page)
        #print(str(godaddy_title_page))

    def godaddy_page_url(self):
        current_url = self.driver.current_url
        print(current_url)


    def validate_title_page(self):
        title_page = self.driver.title
        expected_text = "Domain Names, Websites, Hosting & Online Marketing Tools - GoDaddy"
        print('Title page:' + title_page)
        print('Expected text:' + expected_text)
        assert  title_page == expected_text, f'Title page not validated'

    def validate_current_url(self):
        current_url = self.driver.current_url
        expected_url = 'https://www.godaddy.com/'
        print('Current Url:' + current_url)
        print('Expected_url:' + expected_url)
        assert current_url==expected_url, f'Expected URL is not Current URL '

    def get_page_source(self):
        page_source = self.driver.get('view-source:https://www.godaddy.com/')
        page_source_url = self.driver.current_url
        print(page_source_url)
       # page_source = self.driver.page_source

       # print(page_source)

    def page_title_source(self):
        page_title_source = self.driver.find_elements(*self.PAGE_TITLE_SOURCE)[14].text
        original_page_title = "Domain Names, Websites, Hosting & Online Marketing Tools - GoDaddy"
        print(page_title_source[7:73])
        print(original_page_title)
        assert original_page_title==page_title_source[7:73], f'Page title not present in page source'

    # def input_text(self):
    #     search_text = self.find_element(*self.SEARCH_INPUT)
    #     click_search = self.find_element(*self.SEND_SEARCH)
    #     close_popup = self.find_element(*self.POPUP_CLOSE)
    #
    #
        # action = ActionChains(self.driver)
        # action.click(close_popup).perform()
        # time.sleep(3)
        # action.send_keys_to_element(click_search).perform()
        # time.sleep(3)
        #   action.click(search_text).perform()
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