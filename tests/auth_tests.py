from tests_locators import TestLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
class TestAutorization:

    def test_auth_via_main_button_entrance_login_success(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        driver.find_element(*TestLocators.INPUT_FIELD).send_keys("baymakova03@yandex.ru")
        driver.find_element(*TestLocators.PASSWORD_FIELD).send_keys("123456")
        driver.find_element(*TestLocators.LOGIN_AUTH_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((TestLocators.COLLECT_BURGER_HEADER)))

        assert driver.find_element(*TestLocators.LOGIN_BUTTON).text == 'Оформить заказ'
        driver.quit()

    def test_auth_via_profile_link_login_success(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocators.PROFILE_TITLE).click()
        driver.find_element(*TestLocators.INPUT_FIELD).send_keys("baymakova03@yandex.ru")
        driver.find_element(*TestLocators.PASSWORD_FIELD).send_keys("123456")
        driver.find_element(*TestLocators.LOGIN_AUTH_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((TestLocators.COLLECT_BURGER_HEADER)))

        assert driver.find_element(*TestLocators.LOGIN_BUTTON).text == 'Оформить заказ'
        driver.quit()

    def test_auth_via_reg_form_login_success(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(*TestLocators.REG_FORM_AUTH_LINK).click()
        driver.find_element(*TestLocators.INPUT_FIELD).send_keys("baymakova03@yandex.ru")
        driver.find_element(*TestLocators.PASSWORD_FIELD).send_keys("123456")
        driver.find_element(*TestLocators.LOGIN_AUTH_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((TestLocators.COLLECT_BURGER_HEADER)))

        assert driver.find_element(*TestLocators.LOGIN_BUTTON).text == 'Оформить заказ'
        driver.quit()

    def test_auth_via_reset_password_form(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
        driver.find_element(*TestLocators.RESTORE_PASSWORD_LINK).click()
        driver.find_element(*TestLocators.INPUT_FIELD).send_keys("baymakova03@yandex.ru")
        driver.find_element(*TestLocators.PASSWORD_FIELD).send_keys("123456")
        driver.find_element(*TestLocators.LOGIN_AUTH_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((TestLocators.COLLECT_BURGER_HEADER)))

        assert driver.find_element(*TestLocators.LOGIN_BUTTON).text == 'Оформить заказ'
        driver.quit()