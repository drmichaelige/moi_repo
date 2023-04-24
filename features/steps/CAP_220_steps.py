from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select



@when('Click on a product')
def search_a_product(context):
    context.app.header_page.click_a_product()


@then('Add items to the cart')
def add_to_cart(context):
    context.app.cart_page.add_to_cart()


@then('View cart')
def view_cart(context):
    context.app.cart_page.view_cart()

@then('Delete product from cart')
def delete_cart(context):
    context.app.cart_page.delete_from_cart()

@then('Verify cart is empty')
def verify_empty_cart(context):
    context.app.cart_page.verify_cart_empty()