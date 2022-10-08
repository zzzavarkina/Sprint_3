from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests_locators import TestLocators

class TestTransitionToAndOutOfProfile:

    def test_transition_to_profile_via_profile_link_transition_complete(self, driver, auth_for_transition):
        driver.find_element(*TestLocators.PROFILE_TITLE).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((TestLocators.PROFILE_LINK)))
        assert driver.find_element(*TestLocators.PROFILE_TEXT).text == 'В этом разделе вы можете изменить свои персональные данные'
        driver.quit()

    def test_transition_from_profile_to_constructor_via_header_link_transition_complete(self, driver, auth_for_transition):
        driver.find_element(*TestLocators.CONSTRUCTOR_LINK).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((TestLocators.COLLECT_BURGER_HEADER)))
        driver.quit()

    def test_transition_from_profile_to_constructor_via_logo_transition_complete(self, driver, auth_for_transition):
        driver.find_element(*TestLocators.LOGO_LINK).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((TestLocators.COLLECT_BURGER_HEADER)))
        driver.quit()

    def test_logout_via_button_logout_complete(self, driver, auth_for_transition):
        driver.find_element(*TestLocators.PROFILE_TITLE).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((TestLocators.PROFILE_LINK)))
        driver.find_element(*TestLocators.LOGOUT_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((TestLocators.LOGIN_TITLE)))
        driver.quit()