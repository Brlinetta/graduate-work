from base_page import BasePage
from my_exercises_page import Exercises
from home_page import HomePage


def test_create_exercises(driver):
    base_page = BasePage(driver)
    home_page = HomePage(driver)
    base_page.open_home_page()
    home_page.open_sign_in()
    base_page.open_my_profile_page()
    exercises = Exercises(driver)
    id_exercises = exercises.create_exercises()
    exercises_1 = exercises.open_exercises(id_exercises)
    assert exercises_1.is_displayed()


def test_redact_exercises(driver):
    base_page = BasePage(driver)
    home_page = HomePage(driver)
    base_page.open_home_page()


