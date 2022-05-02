from base_page import BasePage
from time import sleep
from selenium.webdriver.common.by import By

measurements_button = (By.CLASS_NAME, 'bg-aqua')
create_measurements_button = (By.CLASS_NAME, 'pull-right')
category_measurement = (By.CLASS_NAME, 'select2-selection__arrow')
input_category = (By.CLASS_NAME, 'select2-search__field')
weight_kg = (By.ID, 'measurement_value')
save_measurement = (By.ID, 'btn-primary')
'btn-primary'
'self.find_element()'


class Measurements (BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open_measurements(self):
        self.find_element(measurements_button).click()

    def create_measurements(self):
        self.find_element(create_measurements_button).click()
        self.find_element(category_measurement).click()
        self.find_element(input_category).send_keys('Вес')
        self.find_element(weight_kg).send_keys('80\n')
        sleep(7)

