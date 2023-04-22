from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchPage(Page):
    SEARCH_RESULT = (By.ID,'ProductCount')
    # NO_RESULTS = (By. XPATH,"//*[contains(text(), 'No results found')]")
    NO_RESULTS = (By.CSS_SELECTOR,'.title.title--primary')

    # def verify_no_result(self):
    #     expected_text = 'No results found for “Baby Oil” \n Check the spelling or use a different word or phrase'
    #     actual_text = self.find_element(*self.NO_RESULTS).text
    #     # print("|" + expected_text + "|")
    #     # print("|" + actual_text + "|")
    #     assert expected_text == actual_text, f'Expected text not found'

    def verify_no_results(self):
        # expected_result = self.find_element(*self.SEARCH_RESULT).text

        expected_result = 'No results found'
        actual_result = self.find_element(*self.NO_RESULTS).text
        print(expected_result)
        print(actual_result)
        assert expected_result != actual_result, f'Expected product name not found'