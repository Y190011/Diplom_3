from selenium.webdriver.common.by import By

class MainPageLocators:

    MAIN_ACCOUNT_URL         = By.XPATH, "//a[@href = '/account']"
    MAIN_ORDER_FEED_URL       = By.XPATH,  "//p[text()='Лента Заказов']/parent::a"
    MAIN_TITLE               = By.XPATH, "//h1[text() = 'Соберите бургер']"

    MAIN_BUN_TAB_BUTTON      = By.XPATH, "//span[text() = 'Булки']"
    MAIN_SAUCE_TAB_BUTTON    = By.XPATH, "//span[text() = 'Соусы']"
    MAIN_FILLINGS_TAB_BUTTON = By.XPATH, "//span[text() = 'Начинки']"

    MAIN_CRATOR_BUN  = By.XPATH, "//a[contains(@class, 'BurgerIngredient')]/img[contains(@alt, 'Краторная булка')]"
    MAIN_SPICY_SAUCE = By.XPATH, "//a[contains(@class, 'BurgerIngredient')]/img[@alt = 'Соус Spicy-X']"
    MAIN_BEEF_FILLINGS = (By.XPATH,
                                 "//a[contains(@class,'BurgerIngredient')]/img[@alt = 'Говяжий метеорит (отбивная)']")

    MAIN_CRATOR_BUN_COUNTER = (By.XPATH,
                 "//a[contains(@class,'BurgerIngredient')]/img[contains(@alt,'Краторная булка')]/parent::a/div[1]/p")
    MAIN_SPICY_SAUCE_COUNTER   = (By.XPATH,
                  "//a[contains(@class, 'BurgerIngredient')]/img[contains(@alt, 'Соус Spicy-X')]/parent::a/div[1]/p")
    MAIN_BEEF_FILLINGS_COUNTER = (By.XPATH,
        "//a[contains(@class,'BurgerIngredient')]/img[contains(@alt,'Говяжий метеорит (отбивная)')]/parent::a/div[1]/p")

    MAIN_CONSTRUCTOR_BASKET = By.XPATH, "//ul[contains(@class, 'BurgerConstructor_basket')]"

    MAIN_CREATE_ORDER_BUTTON = By.XPATH, "//button[text()='Оформить заказ']"

    MAIN_MODAL_ORDER_NUMBER  = By.XPATH, "//p[text() = 'идентификатор заказа']/parent::div/h2"
    MAIN_MODAL_ORDER_CLOSE   = By.XPATH, "//button[contains(@class, 'close')]"

    MAIN_INGREDIENT_WINDOW_TITLE = By.XPATH, "//h2[text() = 'Детали ингредиента']"

    MAIN_INGREDIENT_CRATOR_BUN    = By.XPATH, "//p[text() = 'Краторная булка N-200i']"
    MAIN_INGREDIENT_SPICY_SAUCE   = By.XPATH, "//p[text() = 'Соус Spicy-X']"
    MAIN_INGREDIENT_BEEF_FILLINGS = By.XPATH, "//p[text() = 'Говяжий метеорит (отбивная)']"


