from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep


email_field = (By.ID, 'email')
password_field = (By.ID, 'password')
login = 'User354'
password = 'VKfbdm'
login_button = (By.CLASS_NAME, 'btn-primary')
username = (By.CLASS_NAME, 'profile-username')
invalid_input = (By.CLASS_NAME, 'col-md-12')


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        #self.email_field = self.find_element(email_field)


    @property
    def email_field(self):
        return self.find_element(email_field)

    def tru_data_input(self,):
        self.email_field.send_keys(login)
        self.find_element(password_field).send_keys(password)
        self.find_element(login_button).click()

    def username_tru(self):
        return self.find_element(username)

    def invalid_login_input(self):
        self.email_field.send_keys('1350qwertyuiop')
        self.find_element(password_field).send_keys(password)
        self.find_element(login_button).click()

    def invalid_input_window(self):
        return self.find_element(invalid_input)

    def invalid_password_input(self):
        self.email_field.send_keys(login)
        self.find_element(password_field).send_keys('11111111')
        self.find_element(login_button).click()
