from base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep

login_button = (By.CLASS_NAME, 'login-button')
exercises_button = (By.XPATH, '//*[@id="top-menu"]/a[4]')


class HomePage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get('https://gymlog.ru/')

    def open_sign_in(self):
        self.find_element(login_button).click()

    def open_exercises_page(self):
        self.find_element(exercises_button).click()

