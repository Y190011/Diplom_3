from selenium.webdriver.common.by import By

class OrderFeedPageLocators:

    ORDER_FEED_PAGE_TITLE      = By.XPATH, "//h1[text() = 'Лента заказов']"

    ORDER_FEED_CONSTRUCTOR_URL = By.XPATH, "//p[text()  = 'Конструктор']/parent::a"
    ORDER_FEED_BURGERS_ALL     = By.XPATH, "//p[text()  = 'Выполнено за все время:']/parent::div/p[2]"
    ORDER_FEED_BURGERS_TODAY   = By.XPATH, "//p[text()  = 'Выполнено за сегодня:']/parent::div/p[2]"

    ORDER_FEED_ACCOUNT_URL = By.XPATH, "//a[@href = '/account']"

    ORDER_FEED_STATUS_BOX = By.XPATH, "//div[contains(@class, 'OrderFeed_orderStatusBox')]/ul/*"

    ORDER_FEED_FIND_ORDER_IN_FEED = By.XPATH, ".//ul[contains(@class,'OrderFeed_list')]//p[contains(text(), '{}')]"
    ORDER_FEED_CLICK_ORDER_IN_FEED = (By.XPATH,
                            ".//ul[contains(@class,'OrderFeed_list')]//p[contains(text(), '{}')]/parent::div/parent::a")
    ORDER_FEED_BURGER_MODAL_TITLE  = By.XPATH, "//p[text() = 'Cостав']"
    ORDER_FEED_BURGER_MODAL_NUMBER = By.XPATH, "//p[contains(text(),'{}')]"

    ORDER_FEED_BURGER_MODAL_CLOSE  = By.XPATH, "//section[2]//button[contains(@class, 'close')]"
