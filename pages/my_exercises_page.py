from pages.base_page import BasePage
from time import sleep
from selenium.webdriver.common.by import By

my_exercises_button = (By.CLASS_NAME, 'bg-green')
create_exercises_button = (By.CLASS_NAME, 'btn-success')
exercise_name = (By.ID, 'field_name_u')
category = (By.ID,'select2-field_category_id-container')
category_input = (By.CLASS_NAME, 'select2-search__field')
measure1 = (By.ID, 'select2-field_measure_1_id-container')
measure1_input = (By.CLASS_NAME, 'select2-search__field')
measure2 = (By.ID, 'select2-field_measure_2_id-container')
measure2_input = (By.CLASS_NAME, 'select2-search__field')
description = (By.ID, 'field_content_u')
save = (By.CLASS_NAME, 'pull-right')
elem_id = (By.XPATH, '//*[@id="object-form"]/input[1]')

my_profile = (By.CLASS_NAME, 'user-image')
exercises1 = (By.ID, 'select2-field_category_id-container')
name_exercises = (By.CLASS_NAME, 'content-header')
category_exercises = (By.CLASS_NAME, 'params')

redact_exercises_button = (By.CLASS_NAME, 'btn-primary')


class Exercises (BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def create_exercises(self):
        self.find_element(my_exercises_button).click()
        self.find_element(create_exercises_button).click()
        self.find_element(exercise_name).send_keys('exercise 1')
        self.find_element(category).click()
        self.find_element(category_input).send_keys('спина\n')
        self.find_element(measure1).click()
        self.find_element(category_input).send_keys('кг\n')
        self.find_element(measure2).click()
        self.find_element(category_input).send_keys('время\n')
        self.find_element(description).send_keys('становая тяга 100 кг')
        self.find_element(save).click()
        sleep(2)
        id_exercises = self.find_element(elem_id).get_attribute('value')
        return id_exercises

    def open_exercises(self, id_exercises):
        self.find_element(my_profile).click()
        self.find_element(my_exercises_button).click()
        id_1 = 'exercise_' + id_exercises
        self.driver.find_element(By.XPATH, '//*[@id=' + '"' + id_1 + '"' + ']/td[1]/a').click()
        return self.find_element(name_exercises).text,\
               self.find_element(category_exercises).text

    def redact_exercises(self):
        self.find_element(redact_exercises_button).click()
        self.find_element(exercise_name).clear()
        self.find_element(exercise_name).send_keys('exercise 1 redact')
        self.find_element(category).click()
        self.find_element(category_input).send_keys('ше\n')
        self.find_element(description).clear()
        self.find_element(description).send_keys('Наклон головы назад и вбок')
        self.find_element(save).click()
        sleep(2)
        id_exercises = self.find_element(elem_id).get_attribute('value')
        return id_exercises











