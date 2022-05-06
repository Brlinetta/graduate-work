from base_page import BasePage
from my_measurements import Measurements
from home_page import HomePage
category = 'Вес'
data = '03.05.2022'
kg = '80\n'


def test_create_measurements(driver):
    base_page = BasePage(driver)
    home_page = HomePage(driver)
    base_page.open_home_page()
    home_page.open_sign_in()
    base_page.open_my_profile_page()
    measurements = Measurements(driver)
    measurements.open__measurements()
    measurements.create_measurements(category, data, kg)
    data_measurements = measurements.check_measurements()
    measurements.delete_measurements()
    assert data_measurements == ('Вес', '80', '3.5.2022')


def test_redact_measurements(driver):
    base_page = BasePage(driver)
    home_page = HomePage(driver)
    base_page.open_home_page()
    home_page.open_sign_in()
    base_page.open_my_profile_page()
    measurements = Measurements(driver)
    measurements.open__measurements()
    measurements.create_measurements(category, data, kg)
    measurements.redact_measurements()
    assert True





