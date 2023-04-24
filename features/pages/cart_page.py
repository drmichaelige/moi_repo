import time
from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

class CartPage(Page):
    ADD_TO_CART = (By.XPATH, "//button[text()='Add to cart']")
    VIEW_CART = (By.XPATH,"//*[contains(text(),'View cart')]")
    DELETE_PRODUCT = (By.CSS_SELECTOR,'#Remove-1')
    CART_EMPTY = (By.CSS_SELECTOR,'.cart__empty-text')
    def add_to_cart(self):
        self.click(*self.ADD_TO_CART)
        time.sleep(1)

    def view_cart(self):
        self.click(*self.VIEW_CART)


    def delete_from_cart(self):
        self.click(*self.DELETE_PRODUCT)


    def verify_cart_empty(self):
        expected_result = 'Your cart is currently empty'
        actual_result = self.find_element(*self.CART_EMPTY).text
        print(expected_result)
        print(actual_result)
        assert expected_result != actual_result, f'Expected product name not found'