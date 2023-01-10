from selenium.webdriver.common.by import By

class TestLocators:
# Надпись "Вход"
    LOGIN_TITLE = (By.XPATH, "//div[@class ='Auth_login__3hAey']/h2[text()='Вход']")

# Поле ввода пароля
    PASSWORD_FIELD = (By.NAME, "Пароль")

# Кнопка "Зарегистрироваться"
    REG_BUTTON = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")

# Поле ввода имени и поле ввода email
    INPUT_FIELD = (By.XPATH, "//input[@class='text input__textfield text_type_main-default']")

# Надпись "Регистрация"
    REG_TITLE = (By.CLASS_NAME, "App_componentContainer__2JC2W")

# Заголовок "Регистрация"
    REG_HEADER = (By.XPATH, "//div[@class='Auth_login__3hAey']/h2")

# Ошибка
    REG_ERROR = (By.XPATH, "//p[@class='input__error text_type_main-default']")

# Кнопка "Войти в аккаунт"
    LOGIN_BUTTON = (By.XPATH, "//button[@class ='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")

# Кнопка "Войти" на форме авторизации
    LOGIN_AUTH_BUTTON = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")

# Надпись "Соберите бургер"
    COLLECT_BURGER_HEADER = (By.XPATH, "//h1[text()='Соберите бургер']")

# Ссылка "Личный кабинет"
    PROFILE_TITLE = (By.XPATH, "//p[text()='Личный Кабинет']")

# Ссылка "Войти" на форме регистрации
    REG_FORM_AUTH_LINK = (By.XPATH, "//a[@class='Auth_link__1fOlj']")

# Ссылка "Восстановить пароль"
    RESTORE_PASSWORD_LINK = (By.XPATH, "//a[@class='Auth_link__1fOlj']")

# Кнопка "Восстановить пароль"
    RESTORE_PASSWORD_BUTTON = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")

# Ссылка "Профиль"
    PROFILE_LINK = (By.LINK_TEXT, "Профиль")

# Текст профиля
    PROFILE_TEXT = (By.XPATH, "//p[@class='Account_text__fZAIn text text_type_main-default']")

# Ссылка "Конструктор"
    CONSTRUCTOR_LINK = (By.XPATH, "//p[@class='AppHeader_header__linkText__3q_va ml-2']")

# Кнопка "Выход" в личном кабинете
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")

# Лого
    LOGO_LINK = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']")

# Надпись "Булки"
    BREAD_TITLE = (By.XPATH, "//span[text()='Булки']")

# Надпись "Булки" в списке булок
    BREAD_HEADER = (By.XPATH, "//h2[text()='Булки']")

# Надпись "Соусы"
    SAUSES_TITLE = (By.XPATH, "//span[text()='Соусы']")

# Надпись "Соусы" в списке соусов
    SAUSES_HEADER = (By.XPATH, "//h2[text()='Соусы']")

# Список ингредиентов
    INGREDIENTS_UL = (By.XPATH, "//ul[@class='BurgerIngredients_ingredients__list__2A-mT']")

# Надпись "Начинки"
    STUFFS_TITLE = (By.XPATH, "//span[text()='Начинки']")

# Надпись "Начинки" в списке начинок
    STUFFS_HEADER = (By.XPATH, "//h2[text()='Начинки']")

