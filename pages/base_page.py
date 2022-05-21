from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from time import sleep


login = 'User354'
password = 'VKfbdm'
login_button1 = (By.CLASS_NAME, 'btn-primary')
email_field = (By.ID, 'email')
password_field = (By.ID, 'password')


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self):
        raise NotImplementedError

    def open_home_page(self):
        self.driver.get('https://gymlog.ru/')

    def find_element(self, *args):
        by, val = args[0]
        return self.driver.find_element(by, val)

    def open_my_profile_page(self):
        self.find_element(email_field).send_keys(login)
        self.find_element(password_field).send_keys(password)
        sleep(2)
        self.find_element(login_button1).click()
