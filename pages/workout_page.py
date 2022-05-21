from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep


workout_button = (By.CLASS_NAME, 'bg-yellow')
create_button = (By.CLASS_NAME, 'btn-success')
program = (By.ID, 'select2-program_id-container')
input_name_program = (By.CLASS_NAME, 'select2-search__field')
save_button = (By.CLASS_NAME, 'btn-primary')


class Workout_Page(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def creating_workout(self):
        self.find_element(workout_button).click()
        self.find_element(create_button).click()
        self.find_element(program).click()
        self.find_element(input_name_program).send_keys('program\n')
        sleep(5)
        self.find_element(save_button).click()
        sleep(7)
