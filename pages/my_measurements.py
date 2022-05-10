from base_page import BasePage
from time import sleep
from selenium.webdriver.common.by import By
import pyautogui

measurements_button = (By.CLASS_NAME, 'bg-aqua')
create_measurements_button = (By.CLASS_NAME, 'pull-right')
category_measurement = (By.CLASS_NAME, 'select2-selection__arrow')
input_category = (By.CLASS_NAME, 'select2-search__field')
weight_kg = (By.ID, 'measurement_value')
time_measurement = (By.ID, 'measurement_create_time')
save_measurement = (By.ID, 'btn-primary')

measurement = (By.XPATH, '//*[@class="highcharts-markers highcharts-series-0 highcharts-tracker"]//*[name()="path"]')

created_weight = (By.CLASS_NAME, 'select2-selection__rendered')
data_1 = (By.CLASS_NAME, 'form-control')

delete_button = (By.XPATH, '//*[@id="measurement-value-form"]/div[2]/a')

'measurement_create_time'
'self.find_element()'


class Measurements (BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open__measurements(self):
        self.find_element(measurements_button).click()

    def create_measurements(self, category, data, kg):
        self.find_element(create_measurements_button).click()
        self.find_element(category_measurement).click()
        self.find_element(input_category).send_keys(category)
        self.find_element(time_measurement).clear()
        self.find_element(time_measurement).send_keys(data)
        self.find_element(weight_kg).send_keys(kg)

        sleep(7)

    def check_measurements(self):
        sleep(3)
        self.find_element(measurement).click()
        self.find_element(measurement).click()
        return self.find_element(created_weight).text, \
               self.find_element(weight_kg).get_attribute("value"),\
               self.find_element(time_measurement).get_attribute("value")

    def redact_measurements(self):
        sleep(3)
        self.find_element(measurement).click()
        self.find_element(measurement).click()
        self.find_element(weight_kg).click()
        self.find_element(weight_kg).clear()
        self.find_element(weight_kg).send_keys('70\n')

    def delete_measurements(self):
        sleep(2)
        self.find_element(delete_button).click()
        pyautogui.press('enter')
        sleep(5)

