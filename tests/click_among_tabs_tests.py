from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests_locators import TestLocators

class TestClickAmongTabs:

    def test_constructor_click_on_sauses_tab_scroll_success(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((TestLocators.COLLECT_BURGER_HEADER)))
        driver.find_element(*TestLocators.SAUSES_TITLE).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((TestLocators.SAUSES_HEADER)))

        assert driver.find_elements(*TestLocators.INGREDIENTS_UL)[1].is_displayed()
        driver.quit()

    def test_constructor_click_on_stuffs_tab_scroll_success(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((TestLocators.COLLECT_BURGER_HEADER)))
        driver.find_element(*TestLocators.STUFFS_TITLE).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((TestLocators.STUFFS_HEADER)))

        assert driver.find_elements(*TestLocators.INGREDIENTS_UL)[2].is_displayed()
        driver.quit()

    def test_constructor_click_on_bread_tab_scroll_success(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((TestLocators.COLLECT_BURGER_HEADER)))
        driver.find_element(*TestLocators.STUFFS_TITLE).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((TestLocators.STUFFS_HEADER)))
        driver.find_element(*TestLocators.BREAD_TITLE).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((TestLocators.BREAD_HEADER)))

        assert driver.find_elements(*TestLocators.INGREDIENTS_UL)[0].is_displayed()
        driver.quit()