from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def browser_init(context):
    """
    :param context: Behave context
    """

    ############# FIREFOX #####################
    options = FirefoxOptions()
    # options.headless = True
    context.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
    #############################################
    #
    # ############## CHROME ######################
    # options = ChromeOptions()
    # options.headless = True
    # options.add_argument("--window-size=1920,1080")
    # context.driver = webdriver.Chrome(options=options, executable_path=ChromeDriverManager().install())
    # ############################################



    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()

