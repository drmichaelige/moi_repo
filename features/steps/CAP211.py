from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


@then('Input non-existent product name:{product} to search')
def product_search(context, product):
    context.app.header_page.product_search(product)


    @then('Verify no results found')
    def verify_no_results(context):
        context.app.search_page.verify_no_results()


