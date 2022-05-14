from home_page import HomePage
from selenium.webdriver.common.by import By
from base_page import BasePage
from time import sleep
from exercises_page import Exercise_Search

exercise_1 = (By.ID, 'exercise-197')
exercise_2 = (By.ID, 'exercise-199')
equipment_3 = (By.XPATH, '//*[@id="solar"]/div[2]/div[3]/section[2]/div[3]/div[1]/div[4]')


def test_without_equipment(driver):
    base_page = BasePage(driver)
    home_page = HomePage(driver)
    exercise_search = Exercise_Search(driver)
    base_page.open_home_page()
    home_page.open_sign_in()
    base_page.open_my_profile_page()
    home_page.open_exercises_page()
    sleep(2)
    exercise_search.dont_click_equipment()
    sleep(2)
    exercise_search.looking_element_exercises(exercise_1)
    sleep(5)
    equipment = exercise_search.check_level(equipment_3)
    assert equipment == 'Снаряжение: Собственное тело'


def test_equipment(driver):
    base_page = BasePage(driver)
    home_page = HomePage(driver)
    exercise_search = Exercise_Search(driver)
    base_page.open_home_page()
    home_page.open_sign_in()
    base_page.open_my_profile_page()
    home_page.open_exercises_page()
    exercise_search.click_equipment()
    exercise_search.looking_element_exercises(exercise_2)
    equipment = exercise_search.check_level(equipment_3)
    assert equipment == 'Снаряжение: Прочее'


