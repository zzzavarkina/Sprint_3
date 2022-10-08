import pytest
import random
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests_locators import TestLocators

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
    driver.find_element(*TestLocators.PROFILE_TITLE).click()
    driver.find_element(*TestLocators.INPUT_FIELD).send_keys("baymakova03@yandex.ru")
    driver.find_element(*TestLocators.PASSWORD_FIELD).send_keys("123456")
    driver.find_element(*TestLocators.LOGIN_AUTH_BUTTON).click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((TestLocators.COLLECT_BURGER_HEADER)))

