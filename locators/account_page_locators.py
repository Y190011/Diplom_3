from selenium.webdriver.common.by import By

class AccountPageLocators:

    ACCOUNT_EXIT_BUTTON        = By.XPATH, ".//button[text() = 'Выход']"
    ACCOUNT_ORDER_HISTORY_URL  = By.XPATH, "//a[text()       = 'История заказов']"
    ACCOUNT_FIRST_HISTORY_ITEM = By.XPATH, "//ul[contains(@class,'OrderHistory')]/li[1]/a/p[text()='Выполнен']"
    ACCOUNT_HIST_ORDER_NUMBER_LOCATOR = By.XPATH, ".//div[contains(@class,'OrderHistory')]/p[contains(text(), '{}')]"
    ACCOUNT_HIST_ORDER_STATUS_LOCATOR = (By.XPATH,
                        ".//div[contains(@class,'OrderHistory')]/p[contains(text(), '{}')]/parent::div/parent::a/p")