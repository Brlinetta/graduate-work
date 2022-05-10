from base_page import BasePage
from time import sleep
from my_profile_page import My_profile_page
from home_page import HomePage


def test_creating_raining_program(driver):
    base_page = BasePage(driver)
    home_page = HomePage(driver)
    profile_page = My_profile_page(driver)
    base_page.open_home_page()
    sleep(2)
    home_page.open_sign_in()
    base_page.open_my_profile_page()
    name_program, category_program = profile_page.creating_program()
    assert name_program == 'program1\nредактировать' and \
           category_program == '20 отжиманий, 20 приседаний, 20 отжиманий, банка протеина'



