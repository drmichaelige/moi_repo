from selenium.webdriver.common.by import By
from pages.base_page import Page

class MainPage(Page):


    def open_cureskin(self):
         self.open_cureskin_page()

    def open_godaddy(self):
         self.open_godaddy_page()


    def maximize_window(self):
        position = self.driver.get_window_size()
        maximize_window = self.driver.maximize_window()
        # maximize_window = self.driver.window().maximize()
        print(position)
        # print(max_window)
        print(maximize_window)
        # assert position == max_window, f'window size is not maximized'

    def close_godaddy(self):
         self.driver.close()