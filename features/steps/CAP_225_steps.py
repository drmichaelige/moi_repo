from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


@when('Click on Shop All section')
def search_a_product(context):
    context.app.header_page.click_shop_all()


@then('Adjust Price Filter to change products number')
def price_filter(context):
    context.app.search_page.price_filter()


@then('Verify that number of products changes')
def verify_products(context):
    context.app.search_page.verify_products()


@then('Verify that products displayed are within the Price filter')
def verify_price_filter(context):
    context.app.search_page.verify_price_filter()