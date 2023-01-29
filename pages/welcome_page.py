from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class WelcomePage(BasePage):
    FORM_AUTH_LINK = (By.XPATH, '//a[@href="/login"]')
    JAVA_SCRIPT_BUTTON = (By.XPATH, '//a[text()="JavaScript Alerts"]')

    def navigate_welcome_page(self):
        self.driver.get('https://the-internet.herokuapp.com/')

    def click_form_auth_link(self):
        self.driver.find_element(*self.FORM_AUTH_LINK).click()

    def click_java_script_link(self):
        self.driver.find_element(*self.JAVA_SCRIPT_BUTTON).click()
