from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchPage(Page):
    SEARCH_RESULT = (By.ID,'ProductCount')


    def verify_result(self):
        expected_text = "2 results found for “SPF”"
        actual_text = self.find_element(*self.SEARCH_RESULT).text
        print("|" + expected_text + "|")
        print("|" + actual_text + "|")
        assert expected_text == actual_text, f'Expected text not found'

