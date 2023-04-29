from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

browserName = "chrome"

if browserName =="chrome":
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif browserName == "firefox":
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
elif browserName == "safari":
    driver = webdriver.Safari()
elif browserName == "edge":
    driver = webdriver.Edge(EdgeChromiumDriverManager().install())
else:
    print('please pass the correct browser name :' + browserName)



