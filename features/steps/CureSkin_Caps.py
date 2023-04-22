from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


@then('Search for {product}')
def product_search(context, product):
    context.app.header_page.product_search(product)

@then('Verify search results are shown')
def verify_result(context):
    context.app.search_page.verify_result()