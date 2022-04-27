from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from base_page import BasePage
from home_page import HomePage
from time import sleep


program_button = (By.CLASS_NAME, 'inner')
create_program_button = (By.CLASS_NAME, 'btn-success')
program_name = (By.ID, 'field_name_u')
category = (By.CLASS_NAME, 'select2-selection--multiple')
detailed_description = (By.ID, 'field_content_u')
save_program = (By.CLASS_NAME, 'pull-right')
my_profile_button = (By.CLASS_NAME, 'user-image')
program_1 = (By.CLASS_NAME, 'odd')


class my_profile_page(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def creating_program(self):
        self.find_element(program_button).click()
        sleep(2)
        self.find_element(create_program_button).click()
        self.find_element(program_name).send_keys('program1')
        sleep(1)
        self.find_element(category).send_keys('мышечная масса\n')
        self.find_element(detailed_description).send_keys('20 отжиманий, 20 приседаний, 20 отжиманий, банка протеина')
        self.find_element(save_program).click()
        self.find_element(my_profile_button).click()
        self.find_element(program_button).click()
        return self.find_element(program_1)




