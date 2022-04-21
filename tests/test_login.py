from pages.home_page import HomePage
from pages.login_gage import LoginPage
from time import sleep

login = 'User354'
password = 'VKfbdm'


def test_login_correct_data(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.open_sign_in()
    login_page = LoginPage(driver)
    login_page.tru_data_input()
    sleep(6)
    assert login_page.username_tru().text == login


def test_login_invalid_login(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.open_sign_in()
    login_page = LoginPage(driver)
    login_page.invalid_login_input()
    sleep(4)
    assert login_page.invalid_input_window().is_displayed()


def test_password_invalid_login(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.open_sign_in()
    login_page = LoginPage(driver)
    login_page.invalid_password_input()
    sleep(4)
    assert login_page.invalid_input_window().is_displayed()



    #assert login_page.email_field.is_displayed()


