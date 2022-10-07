from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestClickAmongTabs:

    def test_constructor_click_on_sauses_tab_scroll_success(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h1[text()='Соберите бургер']")))
        driver.find_element(By.XPATH, "//span[text()='Соусы']").click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h2[text()='Соусы']")))

        assert driver.find_elements(By.XPATH, "//ul[@class='BurgerIngredients_ingredients__list__2A-mT']")[1].is_displayed()
        driver.quit()

    def test_constructor_click_on_stuffs_tab_scroll_success(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h1[text()='Соберите бургер']")))
        driver.find_element(By.XPATH, "//span[text()='Начинки']").click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h2[text()='Начинки']")))

        assert driver.find_elements(By.XPATH, "//ul[@class='BurgerIngredients_ingredients__list__2A-mT']")[2].is_displayed()
        driver.quit()

    def test_constructor_click_on_bread_tab_scroll_success(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h1[text()='Соберите бургер']")))
        driver.find_element(By.XPATH, "//span[text()='Начинки']").click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h2[text()='Начинки']")))
        driver.find_element(By.XPATH, "//span[text()='Булки']").click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h2[text()='Булки']")))

        assert driver.find_elements(By.XPATH, "//ul[@class='BurgerIngredients_ingredients__list__2A-mT']")[0].is_displayed()
        driver.quit()