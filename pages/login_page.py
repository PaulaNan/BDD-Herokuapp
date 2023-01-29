from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    USER_NAME_INPUT = (By.ID, 'username')
    PASSWORD = (By.ID, 'password')
    LOGIN_BUTTON = (By.XPATH, '//button[@type="submit"]')
    EMAIL_MESSAGE = (By.XPATH, '//div[@id="flash"]')

    def set_username(self):
        self.driver.find_element(*self.USER_NAME_INPUT).send_keys('tomsmith')

    def set_password(self):
        self.driver.find_element(*self.PASSWORD).send_keys('SuperSecretPassword!')

    def click_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    # def user_login(self, email, password):
    #     self.set_username(email)
    #     self.set_password(password)
    #     self.click_login_button()

    def verify_correct_login(self):
        actual = self.driver.find_element(*self.EMAIL_MESSAGE).text
        expected = 'You logged into a secure area!\n×'
        self.assertEqual(actual, expected, 'error message is incorrect')
