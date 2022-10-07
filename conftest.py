import pytest
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    return driver

@pytest.fixture()
def registration_email():
    registration_email = f"baymakova{random.randint(1000, 9999)}@yandex.ru"
    return registration_email

@pytest.fixture()
def auth_for_transition(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, "//p[text()='Личный Кабинет']").click()
    driver.find_element(By.XPATH, "//input[@class='text input__textfield text_type_main-default']").send_keys("baymakova03@yandex.ru")
    driver.find_element(By.NAME, "Пароль").send_keys("123456")
    driver.find_element(By.XPATH,"//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h1[text()='Соберите бургер']")))

