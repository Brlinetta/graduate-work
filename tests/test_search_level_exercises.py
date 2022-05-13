from home_page import HomePage
from selenium.webdriver.common.by import By
from base_page import BasePage
from time import sleep
from exercises_page import Exercise_Search


def test_level_beginners (driver):
    base_page = BasePage(driver)
    home_page = HomePage(driver)
    exercise_search = Exercise_Search(driver)
    base_page.open_home_page()
    home_page.open_sign_in()
    base_page.open_my_profile_page()
    sleep(3)
    home_page.open_exercises_page()
    exercise_search.dont_click_level_beginners()
    sleep(5)
