from base_page import BasePage
from time import sleep
from my_profile_page import My_profile_page
from home_page import HomePage
from workout_page import Workout_Page


def test_creating_workout(driver):
    base_page = BasePage(driver)
    home_page = HomePage(driver)
    profile_page = My_profile_page(driver)
    workout_page = Workout_Page(driver)
    base_page.open_home_page()
    home_page.open_sign_in()
    base_page.open_my_profile_page()
    workout_page.creating_workout()
    assert True
