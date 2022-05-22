from pages.base_page import BasePage
from time import sleep
from selenium.webdriver.common.by import By


category_neck = (By.XPATH, '//*[@id="solar"]/div[2]/div[3]/section[2]/div[3]/div[1]/div[1]')
category_shoulders_button = (By.XPATH, '//*[@id="solar"]/div[2]/div[3]/section[2]/div[2]/div[1]/div[2]/a[2]')
category_back_exercises = (By.XPATH, '//*[@id="solar"]/div[2]/div[3]/section[2]/div[2]/div[1]/div[2]/a[3]')
category_breast_exercises = (By.XPATH, '//*[@id="solar"]/div[2]/div[3]/section[2]/div[2]/div[1]/div[2]/a[4]')
category_triceps_exercises = (By.XPATH, '//*[@id="solar"]/div[2]/div[3]/section[2]/div[2]/div[1]/div[2]/a[5]')
category_biceps_exercises = (By.XPATH, '//*[@id="solar"]/div[2]/div[3]/section[2]/div[2]/div[1]/div[2]/a[6]')
category_forearm_exercises = (By.XPATH, '//*[@id="solar"]/div[2]/div[3]/section[2]/div[2]/div[1]/div[2]/a[7]')
category_press_exercises = (By.XPATH, '//*[@id="solar"]/div[2]/div[3]/section[2]/div[2]/div[1]/div[2]/a[8]')
category_femur_exercises = (By.XPATH, '//*[@id="solar"]/div[2]/div[3]/section[2]/div[2]/div[1]/div[2]/a[9]')
category_shin_exercises = (By.XPATH, '//*[@id="solar"]/div[2]/div[3]/section[2]/div[2]/div[1]/div[2]/a[10]')

beginners_dont_click_button = (By.XPATH, '//*[@id="solar"]/div[2]/div[3]/section[2]/div[2]/div[2]/fieldset[2]/div[1]')

professional_dont_click_button = (By.XPATH, '//*[@id="solar"]/div[2]/div[3]/section[2]/div[2]/div[2]/fieldset[2]/div[2]')

equipment_dont_click = (By.XPATH, '//*[@id="solar"]/div[2]/div[3]/section[2]/div[2]/div[2]/fieldset[4]/div[11]/label')

equipment_click = (By.XPATH, '//*[@id="solar"]/div[2]/div[3]/section[2]/div[2]/div[2]/fieldset[4]/div[12]')


class Exercise_Search (BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def looking_element_exercises(self, exercises):
        window_before = self.driver.window_handles[0]
        sleep(5)
        self.find_element(exercises).click()
        window_after = self.driver.window_handles[1]
        sleep(5)
        self.driver.switch_to.window(window_after)
        sleep(5)

    def check_category(self):
        return self.find_element(category_neck).text

    def click_category_shoulders(self):
        self.find_element(category_shoulders_button).click()

    def click_category_back(self):
        self.find_element(category_back_exercises).click()

    def click_category_breast(self):
        self.find_element(category_breast_exercises).click()

    def click_category_(self):
        self.find_element(category_breast_exercises).click()

    def click_category_triceps(self):
        self.find_element(category_triceps_exercises).click()

    def click_category_biceps(self):
        self.find_element(category_biceps_exercises).click()

    def click_category_forearm(self):
        self.find_element(category_forearm_exercises).click()

    def click_category_press(self):
        self.find_element(category_press_exercises).click()

    def click_category_femur(self):
        self.find_element(category_femur_exercises).click()

    def click_category_shin(self):
        self.find_element(category_shin_exercises).click()

    def dont_click_level_beginners(self):
        self.find_element(beginners_dont_click_button).click()

    def dont_click_level_professional(self):
        self.find_element(professional_dont_click_button).click()

    def check_level(self, level):
        return self.find_element(level).text

    def dont_click_equipment(self):
        self.find_element(equipment_dont_click).click()

    def click_equipment(self):
        self.find_element(equipment_click).click()


