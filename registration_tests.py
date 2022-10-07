import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestRegistration:

# Проверки имени

    def test_registration_input_russian_name_registration_complete(self, driver, registration_email):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "App_componentContainer__2JC2W")))
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[0].send_keys("Алеша")
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[1].send_keys(registration_email)
        driver.find_element(By.NAME, "Пароль").send_keys("123456")
        driver.find_element(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@class='Auth_login__3hAey']/h2[text()='Вход']")))

        assert '/login' in driver.current_url
        driver.quit()

    def test_registration_input_latin_name_registration_complete(self, driver, registration_email):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "App_componentContainer__2JC2W")))
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[0].send_keys("Alesha")
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[1].send_keys(registration_email)
        driver.find_element(By.NAME, "Пароль").send_keys("123456")
        driver.find_element(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@class='Auth_login__3hAey']/h2[text()='Вход']")))

        assert '/login' in driver.current_url
        driver.quit()

    def test_registration_input_russian_and_latin_name_registration_complete(self, driver, registration_email):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "App_componentContainer__2JC2W")))
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[0].send_keys("Алеsha")
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[1].send_keys(registration_email)
        driver.find_element(By.NAME, "Пароль").send_keys("123456")
        driver.find_element(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@class='Auth_login__3hAey']/h2[text()='Вход']")))

        assert '/login' in driver.current_url
        driver.quit()

    def test_registration_input_name_with_space_registration_complete(self, driver, registration_email):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "App_componentContainer__2JC2W")))
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[0].send_keys("Але ша")
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[1].send_keys(registration_email)
        driver.find_element(By.NAME, "Пароль").send_keys("123456")
        driver.find_element(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@class='Auth_login__3hAey']/h2[text()='Вход']")))

        assert '/login' in driver.current_url
        driver.quit()

    def test_registration_input_number_name_registration_complete(self, driver, registration_email):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "App_componentContainer__2JC2W")))
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[0].send_keys("999999")
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[1].send_keys(registration_email)
        driver.find_element(By.NAME, "Пароль").send_keys("123456")
        driver.find_element(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@class='Auth_login__3hAey']/h2[text()='Вход']")))

        assert '/login' in driver.current_url
        driver.quit()

    def test_registration_input_symbol_name_registration_complete(self, driver, registration_email):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "App_componentContainer__2JC2W")))
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[0].send_keys("!@#$%^&*()_+")
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[1].send_keys(registration_email)
        driver.find_element(By.NAME, "Пароль").send_keys("123456")
        driver.find_element(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@class='Auth_login__3hAey']/h2[text()='Вход']")))

        assert '/login' in driver.current_url
        driver.quit()

    def test_registration_input_name_with_first_space_registration_complete(self, driver, registration_email):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "App_componentContainer__2JC2W")))
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[0].send_keys(" Алеша")
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[1].send_keys(registration_email)
        driver.find_element(By.NAME, "Пароль").send_keys("123456")
        driver.find_element(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@class='Auth_login__3hAey']/h2[text()='Вход']")))

        assert '/login' in driver.current_url
        driver.quit()

    def test_registration_input_name_with_last_space_registration_complete(self, driver, registration_email):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "App_componentContainer__2JC2W")))
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[0].send_keys("Алеша ")
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[1].send_keys(registration_email)
        driver.find_element(By.NAME, "Пароль").send_keys("123456")
        driver.find_element(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@class='Auth_login__3hAey']/h2[text()='Вход']")))

        assert '/login' in driver.current_url
        driver.quit()

    def test_registration_input_hieroglyphs_name_registration_complete(self, driver, registration_email):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "App_componentContainer__2JC2W")))
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[0].send_keys("ਅਲੀਸ਼ਾ")
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[1].send_keys(registration_email)
        driver.find_element(By.NAME, "Пароль").send_keys("123456")
        driver.find_element(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@class='Auth_login__3hAey']/h2[text()='Вход']")))

        assert '/login' in driver.current_url
        driver.quit()

    def test_registration_input_empty_name_registration_failed(self, driver, registration_email):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "App_componentContainer__2JC2W")))
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[0].send_keys("")
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[1].send_keys(registration_email)
        driver.find_element(By.NAME, "Пароль").send_keys("123456")
        driver.find_element(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()

        assert driver.find_element(By.XPATH, "//div[@class='Auth_login__3hAey']/h2").text == 'Регистрация'
        driver.quit()

# Проверки email

    def test_registration_input_email_with_cyrillic_domain_registration_complete(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        registration_email = f"baymakova{random.randint(100, 999)}@яндекс.рф"
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "App_componentContainer__2JC2W")))
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[0].send_keys("ਅਲੀਸ਼ਾ")
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[1].send_keys(registration_email)
        driver.find_element(By.NAME, "Пароль").send_keys("123456")
        driver.find_element(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@class='Auth_login__3hAey']/h2[text()='Вход']")))

        assert '/login' in driver.current_url
        driver.quit()

    def test_registration_input_email_with_numeric_login_registration_complete(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        registration_email = f"{random.randint(10000, 99999)}@yandex.ru"
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "App_componentContainer__2JC2W")))
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[0].send_keys("ਅਲੀਸ਼ਾ")
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[1].send_keys(registration_email)
        driver.find_element(By.NAME, "Пароль").send_keys("123456")
        driver.find_element(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@class='Auth_login__3hAey']/h2[text()='Вход']")))

        assert '/login' in driver.current_url
        driver.quit()

    def test_registration_input_email_in_uppercase_registration_complete(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        registration_email = f"BAYMAKOVA{random.randint(10000, 99999)}@YANDEX.RU"
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "App_componentContainer__2JC2W")))
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[0].send_keys("ਅਲੀਸ਼ਾ")
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[1].send_keys(registration_email)
        driver.find_element(By.NAME, "Пароль").send_keys("123456")
        driver.find_element(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@class='Auth_login__3hAey']/h2[text()='Вход']")))

        assert '/login' in driver.current_url
        driver.quit()

    def test_registration_input_email_with_underlining_in_login_registration_complete(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        registration_email = f"_baymakova{random.randint(10000, 99999)}@yandex.ru"
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "App_componentContainer__2JC2W")))
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[0].send_keys("ਅਲੀਸ਼ਾ")
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[1].send_keys(registration_email)
        driver.find_element(By.NAME, "Пароль").send_keys("123456")
        driver.find_element(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@class='Auth_login__3hAey']/h2[text()='Вход']")))

        assert '/login' in driver.current_url
        driver.quit()

    def test_registration_input_email_with_hyphen_in_login_registration_complete(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        registration_email = f"bay-makova{random.randint(10000, 99999)}@yandex.ru"
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "App_componentContainer__2JC2W")))
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[0].send_keys("ਅਲੀਸ਼ਾ")
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[1].send_keys(registration_email)
        driver.find_element(By.NAME, "Пароль").send_keys("123456")
        driver.find_element(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@class='Auth_login__3hAey']/h2[text()='Вход']")))

        assert '/login' in driver.current_url
        driver.quit()

    def test_registration_input_email_with_underlining_in_domain_registration_complete(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        registration_email = f"baymakova{random.randint(10000, 99999)}@_yandex.ru"
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "App_componentContainer__2JC2W")))
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[0].send_keys("ਅਲੀਸ਼ਾ")
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[1].send_keys(registration_email)
        driver.find_element(By.NAME, "Пароль").send_keys("123456")
        driver.find_element(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@class='Auth_login__3hAey']/h2[text()='Вход']")))

        assert '/login' in driver.current_url
        driver.quit()

    def test_registration_input_email_with_hyphen_in_domain_registration_complete(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        registration_email = f"baymakova{random.randint(10000, 99999)}@yan-dex.ru"
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "App_componentContainer__2JC2W")))
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[0].send_keys("ਅਲੀਸ਼ਾ")
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[1].send_keys(registration_email)
        driver.find_element(By.NAME, "Пароль").send_keys("123456")
        driver.find_element(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@class='Auth_login__3hAey']/h2[text()='Вход']")))

        assert '/login' in driver.current_url
        driver.quit()

    def test_registration_input_email_with_dot_in_login_registration_complete(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        registration_email = f"bayma.kova{random.randint(10000, 99999)}@yandex.ru"
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "App_componentContainer__2JC2W")))
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[0].send_keys("ਅਲੀਸ਼ਾ")
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[1].send_keys(registration_email)
        driver.find_element(By.NAME, "Пароль").send_keys("123456")
        driver.find_element(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@class='Auth_login__3hAey']/h2[text()='Вход']")))

        assert '/login' in driver.current_url
        driver.quit()

    def test_registration_input_email_with_extra_dot_in_domain_registration_complete(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        registration_email = f"baymakova{random.randint(10000, 99999)}@yan.dex.ru"
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "App_componentContainer__2JC2W")))
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[0].send_keys("ਅਲੀਸ਼ਾ")
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[1].send_keys(registration_email)
        driver.find_element(By.NAME, "Пароль").send_keys("123456")
        driver.find_element(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@class='Auth_login__3hAey']/h2[text()='Вход']")))

        assert '/login' in driver.current_url
        driver.quit()

    def test_registration_input_not_unique_email_registration_failed(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        registration_email = f"baymakova{random.randint(10000, 99999)}@yandex.ru"
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "App_componentContainer__2JC2W")))
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[0].send_keys("ਅਲੀਸ਼ਾ")
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[1].send_keys(registration_email)
        driver.find_element(By.NAME, "Пароль").send_keys("123456")
        driver.find_element(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
        driver.get("https://stellarburgers.nomoreparties.site/register")
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "App_componentContainer__2JC2W")))
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[0].send_keys("ਅਲੀਸ਼ਾ")
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[1].send_keys(registration_email)
        driver.find_element(By.NAME, "Пароль").send_keys("123456")
        driver.find_element(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()

        assert driver.find_element(By.XPATH, "//div[@class='Auth_login__3hAey']/h2").text == 'Регистрация'
        driver.quit()

    def test_registration_input_email_without_dot_in_domain_registration_failed(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        registration_email = f"baymakova{random.randint(100, 999)}@yandexru"
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "App_componentContainer__2JC2W")))
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[0].send_keys("ਅਲੀਸ਼ਾ")
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[1].send_keys(registration_email)
        driver.find_element(By.NAME, "Пароль").send_keys("123456")
        driver.find_element(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()

        assert driver.find_element(By.XPATH, "//div[@class='Auth_login__3hAey']/h2").text == 'Регистрация'
        driver.quit()

    def test_registration_input_email_without_at_in_domain_registration_failed(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        registration_email = f"baymakova{random.randint(100, 999)}yandex.ru"
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "App_componentContainer__2JC2W")))
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[0].send_keys("ਅਲੀਸ਼ਾ")
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[1].send_keys(registration_email)
        driver.find_element(By.NAME, "Пароль").send_keys("123456")
        driver.find_element(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()

        assert driver.find_element(By.XPATH, "//div[@class='Auth_login__3hAey']/h2").text == 'Регистрация'
        driver.quit()

    def test_registration_input_email_with_space_in_login_registration_failed(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        registration_email = f"bay makova{random.randint(100, 999)}@yandex.ru"
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "App_componentContainer__2JC2W")))
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[0].send_keys("ਅਲੀਸ਼ਾ")
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[1].send_keys(registration_email)
        driver.find_element(By.NAME, "Пароль").send_keys("123456")
        driver.find_element(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()

        assert driver.find_element(By.XPATH, "//div[@class='Auth_login__3hAey']/h2").text == 'Регистрация'
        driver.quit()

    def test_registration_input_email_with_space_in_domain_registration_failed(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        registration_email = f"baymakova{random.randint(100, 999)}@yan dex.ru"
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "App_componentContainer__2JC2W")))
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[0].send_keys("ਅਲੀਸ਼ਾ")
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[1].send_keys(registration_email)
        driver.find_element(By.NAME, "Пароль").send_keys("123456")
        driver.find_element(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()

        assert driver.find_element(By.XPATH, "//div[@class='Auth_login__3hAey']/h2").text == 'Регистрация'
        driver.quit()

    def test_registration_input_email_without_login_registration_failed(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        registration_email = '@yandex.ru'
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "App_componentContainer__2JC2W")))
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[0].send_keys("ਅਲੀਸ਼ਾ")
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[1].send_keys(registration_email)
        driver.find_element(By.NAME, "Пароль").send_keys("123456")
        driver.find_element(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()

        assert driver.find_element(By.XPATH, "//div[@class='Auth_login__3hAey']/h2").text == 'Регистрация'
        driver.quit()

    def test_registration_input_email_without_domain_registration_failed(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        registration_email = f"baymakova{random.randint(100, 999)}"
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "App_componentContainer__2JC2W")))
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[0].send_keys("ਅਲੀਸ਼ਾ")
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[1].send_keys(registration_email)
        driver.find_element(By.NAME, "Пароль").send_keys("123456")
        driver.find_element(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()

        assert driver.find_element(By.XPATH, "//div[@class='Auth_login__3hAey']/h2").text == 'Регистрация'
        driver.quit()

    def test_registration_input_empty_email_registration_failed(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        registration_email = ''
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "App_componentContainer__2JC2W")))
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[0].send_keys("ਅਲੀਸ਼ਾ")
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[1].send_keys(registration_email)
        driver.find_element(By.NAME, "Пароль").send_keys("123456")
        driver.find_element(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()

        assert driver.find_element(By.XPATH, "//div[@class='Auth_login__3hAey']/h2").text == 'Регистрация'
        driver.quit()

# Проверки пароля

    def test_registration_input_7_symbols_password_registration_complete(self, driver, registration_email):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "App_componentContainer__2JC2W")))
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[0].send_keys("ਅਲੀਸ਼ਾ")
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[1].send_keys(registration_email)
        driver.find_element(By.NAME, "Пароль").send_keys("1234567")
        driver.find_element(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@class='Auth_login__3hAey']/h2[text()='Вход']")))

        assert '/login' in driver.current_url
        driver.quit()

    def test_registration_input_8_symbols_password_registration_complete(self, driver, registration_email):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "App_componentContainer__2JC2W")))
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[0].send_keys("ਅਲੀਸ਼ਾ")
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[1].send_keys(registration_email)
        driver.find_element(By.NAME, "Пароль").send_keys("12345678")
        driver.find_element(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@class='Auth_login__3hAey']/h2[text()='Вход']")))

        assert '/login' in driver.current_url
        driver.quit()

    def test_registration_input_24_symbols_password_registration_complete(self, driver, registration_email):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "App_componentContainer__2JC2W")))
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[0].send_keys("ਅਲੀਸ਼ਾ")
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[1].send_keys(registration_email)
        driver.find_element(By.NAME, "Пароль").send_keys("123456781234567812345678")
        driver.find_element(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@class='Auth_login__3hAey']/h2[text()='Вход']")))

        assert '/login' in driver.current_url
        driver.quit()

    def test_registration_input_204_symbols_password_registration_complete(self, driver, registration_email):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "App_componentContainer__2JC2W")))
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[0].send_keys("ਅਲੀਸ਼ਾ")
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[1].send_keys(registration_email)
        driver.find_element(By.NAME, "Пароль").send_keys("489465165646456846543165465465464646846545165515646546465456545654565465456545654565464565456465461654684568456545654565456545654565456554456545654654654565465498684968456854514468468468468846858485418454")
        driver.find_element(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@class='Auth_login__3hAey']/h2[text()='Вход']")))

        assert '/login' in driver.current_url
        driver.quit()

    def test_registration_input_latin_letters_password_registration_complete(self, driver, registration_email):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "App_componentContainer__2JC2W")))
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[0].send_keys("ਅਲੀਸ਼ਾ")
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[1].send_keys(registration_email)
        driver.find_element(By.NAME, "Пароль").send_keys("oighof")
        driver.find_element(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@class='Auth_login__3hAey']/h2[text()='Вход']")))

        assert '/login' in driver.current_url
        driver.quit()

    def test_registration_input_cyrillic_letters_password_registration_complete(self, driver, registration_email):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "App_componentContainer__2JC2W")))
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[0].send_keys("ਅਲੀਸ਼ਾ")
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[1].send_keys(registration_email)
        driver.find_element(By.NAME, "Пароль").send_keys("апрвап")
        driver.find_element(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@class='Auth_login__3hAey']/h2[text()='Вход']")))

        assert '/login' in driver.current_url
        driver.quit()

    def test_registration_input_symbol_password_registration_complete(self, driver, registration_email):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "App_componentContainer__2JC2W")))
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[0].send_keys("ਅਲੀਸ਼ਾ")
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[1].send_keys(registration_email)
        driver.find_element(By.NAME, "Пароль").send_keys("#$%^&*")
        driver.find_element(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@class='Auth_login__3hAey']/h2[text()='Вход']")))

        assert '/login' in driver.current_url
        driver.quit()

    def test_registration_input_spaces_in_password_registration_complete(self, driver, registration_email):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "App_componentContainer__2JC2W")))
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[0].send_keys("ਅਲੀਸ਼ਾ")
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[1].send_keys(registration_email)
        driver.find_element(By.NAME, "Пароль").send_keys("123 456")
        driver.find_element(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@class='Auth_login__3hAey']/h2[text()='Вход']")))

        assert '/login' in driver.current_url
        driver.quit()

    def test_registration_input_hieroglyph_password_registration_complete(self, driver, registration_email):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "App_componentContainer__2JC2W")))
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[0].send_keys("ਅਲੀਸ਼ਾ")
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[1].send_keys(registration_email)
        driver.find_element(By.NAME, "Пароль").send_keys("ਅਲੌਸ਼ਕਿੰਸ")
        driver.find_element(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@class='Auth_login__3hAey']/h2[text()='Вход']")))

        assert '/login' in driver.current_url
        driver.quit()

    def test_registration_input_empty_password_registration_failed(self, driver, registration_email):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "App_componentContainer__2JC2W")))
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[0].send_keys("ਅਲੀਸ਼ਾ")
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[1].send_keys(registration_email)
        driver.find_element(By.NAME, "Пароль").send_keys("")
        driver.find_element(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()

        assert driver.find_element(By.XPATH, "//div[@class='Auth_login__3hAey']/h2").text == 'Регистрация'
        driver.quit()

    def test_registration_input_1_symbol_password_registration_failed(self, driver, registration_email):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "App_componentContainer__2JC2W")))
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[0].send_keys("ਅਲੀਸ਼ਾ")
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[1].send_keys(registration_email)
        driver.find_element(By.NAME, "Пароль").send_keys("1")
        driver.find_element(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()

        assert driver.find_element(By.XPATH, "//div[@class='Auth_login__3hAey']/h2").text == 'Регистрация'
        assert driver.find_element(By.XPATH, "//p[@class='input__error text_type_main-default']").is_displayed()
        assert driver.find_element(By.XPATH, "//p[@class='input__error text_type_main-default']").text == 'Некорректный пароль'
        driver.quit()

    def test_registration_input_3_symbols_password_registration_failed(self, driver, registration_email):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "App_componentContainer__2JC2W")))
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[0].send_keys("ਅਲੀਸ਼ਾ")
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[1].send_keys(registration_email)
        driver.find_element(By.NAME, "Пароль").send_keys("123")
        driver.find_element(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()

        assert driver.find_element(By.XPATH, "//div[@class='Auth_login__3hAey']/h2").text == 'Регистрация'
        assert driver.find_element(By.XPATH, "//p[@class='input__error text_type_main-default']").is_displayed()
        assert driver.find_element(By.XPATH, "//p[@class='input__error text_type_main-default']").text == 'Некорректный пароль'
        driver.quit()

    def test_registration_input_4_symbols_password_registration_failed(self, driver, registration_email):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "App_componentContainer__2JC2W")))
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[0].send_keys("ਅਲੀਸ਼ਾ")
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[1].send_keys(registration_email)
        driver.find_element(By.NAME, "Пароль").send_keys("1234")
        driver.find_element(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()

        assert driver.find_element(By.XPATH, "//div[@class='Auth_login__3hAey']/h2").text == 'Регистрация'
        assert driver.find_element(By.XPATH, "//p[@class='input__error text_type_main-default']").is_displayed()
        assert driver.find_element(By.XPATH, "//p[@class='input__error text_type_main-default']").text == 'Некорректный пароль'
        driver.quit()

    def test_registration_input_5_symbols_password_registration_failed(self, driver, registration_email):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "App_componentContainer__2JC2W")))
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[0].send_keys("ਅਲੀਸ਼ਾ")
        driver.find_elements(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")[1].send_keys(registration_email)
        driver.find_element(By.NAME, "Пароль").send_keys("12345")
        driver.find_element(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()

        assert driver.find_element(By.XPATH, "//div[@class='Auth_login__3hAey']/h2").text == 'Регистрация'
        assert driver.find_element(By.XPATH, "//p[@class='input__error text_type_main-default']").is_displayed()
        assert driver.find_element(By.XPATH, "//p[@class='input__error text_type_main-default']").text == 'Некорректный пароль'
        driver.quit()