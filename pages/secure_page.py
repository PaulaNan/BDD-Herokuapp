from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class SecurePage(BasePage):
    LOGOUT_BUTTON = (By.XPATH, '//a[@href="/logout"]')

    def click_logout_button(self):
        self.driver.find_element(*self.LOGOUT_BUTTON).click()
