from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


@given("Open godaddy page")
def open_godaddy_page(context):
    context.app.main_page.open_godaddy()

@when("Maximize browser window")
def godaddy_winsize(context):
    context.app.main_page.maximize_window()

@then("Close browser")
def close_browser(context):
    context.app.main_page.close_godaddy()

@then("Get Title of page and print it")
def title_page(context):
    context.app.header_page.godaddy_title_page()

@then("Get URL of current page and print it")
def page_url(context):
    context.app.header_page.godaddy_page_url()

@then("Get Title of page and validate it with expected value")
def title_page(context):
    context.app.header_page.validate_title_page()

@then("Get URL of current page and validate it with expected value")
def url_current_page(context):
    context.app.header_page.validate_current_url()

@then("Get Page source of web page")
def page_source(context):
    context.app.header_page.get_page_source()

@then("Validate that page title is present in page source")
def page_title_source(context):
    context.app.header_page.page_title_source()