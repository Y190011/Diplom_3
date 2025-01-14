from selenium.webdriver.common.by import By

class LogonPageLocators:

    RECOVERY_TITLE          = By.XPATH, "//h2[text() = 'Восстановление пароля']"
    RECOVERY_EMAIL          = By.XPATH, "//input[@name = 'name']"
    RECOVERY_BUTTON         = By.XPATH, "//button[text() = 'Восстановить']"
    RECOVERY_CODE_INPUT     = By.XPATH, "//label[text()='Введите код из письма']"
    RECOVERY_PASSWORD       = By.XPATH, "//input[@type='password']"
    RECOVERY_LOGIN_URL      = By.XPATH, "//a[@href = '/login']"
    RECOVERY_SAVE_BUTTON    = By.XPATH, "//button[text() = 'Сохранить']"

    ENTRANCE_TITLE                  = By.XPATH, ".//h2[text() ='Вход']"
    ENTRANCE_EMAIL                  = By.XPATH, ".//input[@type = 'text']"
    ENTRANCE_PASSWORD               = By.XPATH, ".//input[@type = 'password']"
    ENTRANCE_BUTTON                 = By.XPATH, ".//button[text() = 'Войти']"
    ENTRANCE_FORGOT_PASSWORD_URL    = By.XPATH, ".//a[@href = '/forgot-password']"
    ENTRANCE_PASSWORD_VIEW_ICON     = By.XPATH, "//input[@name = 'Пароль']/parent::div/div"

    ENTRANCE_PASSWORD_PARENT_DIV    = By.XPATH, "//input[@name='Пароль']/parent::div"
