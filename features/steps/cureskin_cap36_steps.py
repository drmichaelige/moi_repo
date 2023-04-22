from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select




@given("Open CureSkin page")
def open_cureskin_page(context):
    context.app.main_page.open_cureskin()

@when('Click on the search field')
def search_field(context):
    context.app.header_page.search_field()


@then('Input text {text}')
def input_search(context, text):
    context.app.header_page.input_text(text)

@then('Click to search')
def send_search(context):
    context.app.header_page.click_to_search()

@then('Verify the results have spf')
def verify_result(context):
    context.app.search_page.verify_result()

