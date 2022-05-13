from home_page import HomePage
from selenium.webdriver.common.by import By
from base_page import BasePage
from time import sleep
from exercises_page import Exercise_Search

neck_exercises_1 = (By.ID, 'exercise-197')

shoulders_exercises_1 = (By.ID, 'exercise-36406')

back_exercises_1 = (By.ID, 'exercise-149')

breast_exercises_1 = (By.ID, 'exercise-29')

triceps_exercises_1 = (By.ID, 'exercise-175')

biceps_exercises_1 = (By.ID, 'exercise-1')

forearm_exercises_1 = (By.ID, 'exercise-113')

press_exercises_1 = (By.ID, 'exercise-137')

femur_exercises_1 = (By.ID, 'exercise-44')

shin_exercises_1 = (By.ID, 'exercise-49')


def test_exercise_search_category_neck(driver):
    base_page = BasePage(driver)
    home_page = HomePage(driver)
    exercise_search = Exercise_Search(driver)
    base_page.open_home_page()
    home_page.open_sign_in()
    base_page.open_my_profile_page()
    sleep(3)
    home_page.open_exercises_page()
    exercise_search.looking_element_exercises(neck_exercises_1)
    sleep(2)
    category = exercise_search.check_category()
    assert category == 'Категория: Шея'


def test_exercise_search_category_shoulders(driver):
    base_page = BasePage(driver)
    home_page = HomePage(driver)
    exercise_search = Exercise_Search(driver)
    base_page.open_home_page()
    home_page.open_sign_in()
    base_page.open_my_profile_page()
    home_page.open_exercises_page()
    exercise_search.click_category_shoulders()
    exercise_search.looking_element_exercises(shoulders_exercises_1)
    category = exercise_search.check_category()
    assert category == 'Категория: Плечи'


def test_exercise_search_category_back(driver):
    base_page = BasePage(driver)
    home_page = HomePage(driver)
    exercise_search = Exercise_Search(driver)
    base_page.open_home_page()
    home_page.open_sign_in()
    base_page.open_my_profile_page()
    home_page.open_exercises_page()
    exercise_search.click_category_back()
    exercise_search.looking_element_exercises(back_exercises_1)
    category = exercise_search.check_category()
    assert category == 'Категория: Спина'


def test_exercise_search_category_breast(driver):
    base_page = BasePage(driver)
    home_page = HomePage(driver)
    exercise_search = Exercise_Search(driver)
    base_page.open_home_page()
    home_page.open_sign_in()
    base_page.open_my_profile_page()
    home_page.open_exercises_page()
    exercise_search.click_category_breast()
    exercise_search.looking_element_exercises(breast_exercises_1)
    category = exercise_search.check_category()
    assert category == 'Категория: Грудь'


def test_exercise_search_category_triceps(driver):
    base_page = BasePage(driver)
    home_page = HomePage(driver)
    exercise_search = Exercise_Search(driver)
    base_page.open_home_page()
    home_page.open_sign_in()
    base_page.open_my_profile_page()
    home_page.open_exercises_page()
    exercise_search.click_category_triceps()
    exercise_search.looking_element_exercises(triceps_exercises_1)
    category = exercise_search.check_category()
    assert category == 'Категория: Трицепс'


def test_exercise_search_category_biceps(driver):
    base_page = BasePage(driver)
    home_page = HomePage(driver)
    exercise_search = Exercise_Search(driver)
    base_page.open_home_page()
    home_page.open_sign_in()
    base_page.open_my_profile_page()
    home_page.open_exercises_page()
    exercise_search.click_category_biceps()
    exercise_search.looking_element_exercises(biceps_exercises_1)
    category = exercise_search.check_category()
    assert category == 'Категория: Бицепс'


def test_exercise_search_category_forearm(driver):
    base_page = BasePage(driver)
    home_page = HomePage(driver)
    exercise_search = Exercise_Search(driver)
    base_page.open_home_page()
    home_page.open_sign_in()
    base_page.open_my_profile_page()
    home_page.open_exercises_page()
    exercise_search.click_category_forearm()
    exercise_search.looking_element_exercises(forearm_exercises_1)
    category = exercise_search.check_category()
    assert category == 'Категория: Предплечье'


def test_exercise_search_category_press(driver):
    base_page = BasePage(driver)
    home_page = HomePage(driver)
    exercise_search = Exercise_Search(driver)
    base_page.open_home_page()
    home_page.open_sign_in()
    base_page.open_my_profile_page()
    home_page.open_exercises_page()
    exercise_search.click_category_press()
    exercise_search.looking_element_exercises(press_exercises_1)
    category = exercise_search.check_category()
    assert category == 'Категория: Пресс'


def test_exercise_search_category_femur(driver):
    base_page = BasePage(driver)
    home_page = HomePage(driver)
    exercise_search = Exercise_Search(driver)
    base_page.open_home_page()
    home_page.open_sign_in()
    base_page.open_my_profile_page()
    home_page.open_exercises_page()
    exercise_search.click_category_femur()
    exercise_search.looking_element_exercises(femur_exercises_1)
    category = exercise_search.check_category()
    assert category == 'Категория: Бедра'


def test_exercise_search_category_shin(driver):
    base_page = BasePage(driver)
    home_page = HomePage(driver)
    exercise_search = Exercise_Search(driver)
    base_page.open_home_page()
    home_page.open_sign_in()
    base_page.open_my_profile_page()
    home_page.open_exercises_page()
    exercise_search.click_category_shin()
    exercise_search.looking_element_exercises(shin_exercises_1)
    category = exercise_search.check_category()
    assert category == 'Категория: Голень'


