from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestTransitionToAndOutOfProfile:

    def test_transition_to_profile_via_profile_link_transition_complete(self, driver, auth_for_transition):
        driver.find_element(By.XPATH, "//p[text()='Личный Кабинет']").click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Профиль")))
        assert driver.find_element(By.XPATH, "//p[@class='Account_text__fZAIn text text_type_main-default']").text == 'В этом разделе вы можете изменить свои персональные данные'
        driver.quit()

    def test_transition_from_profile_to_constructor_via_header_link_transition_complete(self, driver, auth_for_transition):
        driver.find_element(By.XPATH, "//p[@class='AppHeader_header__linkText__3q_va ml-2']").click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h1[text()='Соберите бургер']")))
        driver.quit()

    def test_transition_from_profile_to_constructor_via_logo_transition_complete(self, driver, auth_for_transition):
        driver.find_element(By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']").click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h1[text()='Соберите бургер']")))
        driver.quit()

    def test_logout_via_button_logout_complete(self, driver, auth_for_transition):
        driver.find_element(By.XPATH, "//p[text()='Личный Кабинет']").click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Профиль")))
        driver.find_element(By.XPATH, "//button[text()='Выход']").click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h2[text()='Вход']")))
        driver.quit()