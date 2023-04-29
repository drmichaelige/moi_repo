import time
from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


class SearchPage(Page):
    SEARCH_RESULT = (By.ID,'ProductCount')
    NO_RESULTS = (By.CSS_SELECTOR,'.title.title--primary')
    ADJUST_SLIDER = (By.XPATH,"//div[@role='slider']")
    FILTER_PRICE_RANGE = (By.XPATH, "//div[contains(text(),'Price: Rs. 0 — Rs. 725')]")
    # PRICE = (By.CSS_SELECTOR,'.price--on-sale')
    PRICE =(By.XPATH,'//*[@id="product-grid"]/li[1]/div/div/div[2]/div[2]/dl/div[2]/dd[2]/span/price-money/bdi/text()')

    def verify_no_results(self):
        expected_result = 'No results found'
        actual_result = self.driver.find_element(*self.NO_RESULTS).text
        print(expected_result)
        print(actual_result)
        assert expected_result != actual_result, f'Expected product name not found'


    def price_filter(self):
        slider_start = self.driver.find_element(*self.ADJUST_SLIDER)
        actions = ActionChains(self.driver)
        actions.click_and_hold(slider_start).pause(1)
        actions.move_by_offset(341,0).release()
        time.sleep(3)

    def verify_products(self):
        expected_result = '10 of 18 products'
        actual_result = self.driver.find_element(*self.SEARCH_RESULT).text
        print("Number of Products now equals to:" + expected_result)
        print("Number of Total Products equals to:" + actual_result)
        assert expected_result != actual_result, f'Expected product number not changed'

    # def verify_price_filter(self):
    #     displayed_price_range = "Price: Rs. 341 — Rs. 725"
    #     filter_price_range = self.driver.find_element(*self.FILTER_PRICE_RANGE).text
    #     print("Displayed products price range:" + str(displayed_price_range))
    #     print("Filter price range:" + str(filter_price_range))
    #     assert displayed_price_range [10:12] <  filter_price_range[:3], f'Displayed product prices not within Price Filter'


    def verify_price_filter(self):
        # displayed_price_range = "Price: Rs. 341 — Rs. 725"
        prices = self.driver.find_elements(*self.PRICE)
        price_list_text = [price.text for price in prices]
        for el in price_list_text:
            assert int(el) > 341 and int(el) < 725



