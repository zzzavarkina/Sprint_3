from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestAutorization:

    def test_auth_via_main_button_entrance_login_success(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']").click()
        driver.find_element(By.XPATH, "//input[@class='text input__textfield text_type_main-default']").send_keys("baymakova03@yandex.ru")
        driver.find_element(By.NAME, "Пароль").send_keys("123456")
        driver.find_element(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h1[text()='Соберите бургер']")))

        assert driver.find_element(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']").text == 'Оформить заказ'
        driver.quit()

    def test_auth_via_profile_link_login_success(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(By.XPATH, "//p[text()='Личный Кабинет']").click()
        driver.find_element(By.XPATH, "//input[@class='text input__textfield text_type_main-default']").send_keys("baymakova03@yandex.ru")
        driver.find_element(By.NAME, "Пароль").send_keys("123456")
        driver.find_element(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h1[text()='Соберите бургер']")))

        assert driver.find_element(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']").text == 'Оформить заказ'
        driver.quit()

    def test_auth_via_reg_form_login_success(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(By.XPATH, "//a[@class='Auth_link__1fOlj']").click()
        driver.find_element(By.XPATH, "//input[@class='text input__textfield text_type_main-default']").send_keys("baymakova03@yandex.ru")
        driver.find_element(By.NAME, "Пароль").send_keys("123456")
        driver.find_element(By.XPATH,"//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h1[text()='Соберите бургер']")))

        assert driver.find_element(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']").text == 'Оформить заказ'
        driver.quit()

    def test_auth_via_reset_password_form(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
        driver.find_element(By.XPATH, "//a[@class='Auth_link__1fOlj']").click()
        driver.find_element(By.XPATH, "//input[@class='text input__textfield text_type_main-default']").send_keys("baymakova03@yandex.ru")
        driver.find_element(By.NAME, "Пароль").send_keys("123456")
        driver.find_element(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h1[text()='Соберите бургер']")))

        assert driver.find_element(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']").text == 'Оформить заказ'
        driver.quit()