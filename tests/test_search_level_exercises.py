from home_page import HomePage
from selenium.webdriver.common.by import By
from base_page import BasePage
from time import sleep
from exercises_page import Exercise_Search

exercise_1 = (By.ID, 'exercise-198')
exercise_2 = (By.ID, 'exercise-197')
level_1 = (By.XPATH, '//*[@id="solar"]/div[2]/div[3]/section[2]/div[3]/div[1]/div[3]')


def test_level_professional(driver):
    base_page = BasePage(driver)
    home_page = HomePage(driver)
    exercise_search = Exercise_Search(driver)
    base_page.open_home_page()
    home_page.open_sign_in()
    base_page.open_my_profile_page()
    sleep(3)
    home_page.open_exercises_page()
    exercise_search.dont_click_level_beginners()
    sleep(1)
    exercise_search.looking_element_exercises(exercise_1)
    level = exercise_search.check_level(level_1)
    assert level == 'Уровень: Продвинутым'


def test_level_beginners(driver):
    base_page = BasePage(driver)
    home_page = HomePage(driver)
    exercise_search = Exercise_Search(driver)
    base_page.open_home_page()
    home_page.open_sign_in()
    base_page.open_my_profile_page()
    sleep(3)
    home_page.open_exercises_page()
    exercise_search.dont_click_level_professional()
    exercise_search.looking_element_exercises(exercise_2)
    level = exercise_search.check_level(level_1)
    assert level == 'Уровень: Начинающим'



