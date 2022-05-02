from base_page import BasePage
from my_measurements import Measurements
from home_page import HomePage


def test_create_measurements(driver):
    base_page = BasePage(driver)
    home_page = HomePage(driver)
    base_page.open_home_page()
    home_page.open_sign_in()
    base_page.open_my_profile_page()
    measurements = Measurements(driver)
    measurements.open_measurements()
    measurements.create_measurements()


