from pages.base_page import BasePage
import allure
from locators.main_page_locators import MainPageLocators
import data

class MainPage(BasePage):

    @allure.step("Выполняем переход из Конструктор в Личный кабинет")
    def go_to_personal_account(self):
        self.click_to_element(MainPageLocators.MAIN_ACCOUNT_URL)

    @allure.step("Проверяем переход на страницу Конструктор (главную)")
    def check_main_page(self):
        self.find_element_with_wait(MainPageLocators.MAIN_TITLE)

    @allure.step("Перетаскиваем ингредиенты, проверяем счетчики ингредиентов")
    def create_burger_1_in_basket(self):
        bun_counter_before = self.get_text_from_element(MainPageLocators.MAIN_CRATOR_BUN_COUNTER)
        self.drag_and_drop(MainPageLocators.MAIN_CRATOR_BUN,
                           MainPageLocators.MAIN_CONSTRUCTOR_BASKET, "Bun")
        bun_counter_after    = self.get_text_from_element(MainPageLocators.MAIN_CRATOR_BUN_COUNTER)
        sauce_counter_before = self.get_text_from_element(MainPageLocators.MAIN_SPICY_SAUCE_COUNTER)
        self.drag_and_drop(MainPageLocators.MAIN_SPICY_SAUCE,
                           MainPageLocators.MAIN_CONSTRUCTOR_BASKET,   "Spicy")
        sauce_counter_after = self.get_text_from_element(MainPageLocators.MAIN_SPICY_SAUCE_COUNTER)
        fillings_counter_before = self.get_text_from_element(MainPageLocators.MAIN_BEEF_FILLINGS_COUNTER)
        self.drag_and_drop(MainPageLocators.MAIN_BEEF_FILLINGS,
                           MainPageLocators.MAIN_CONSTRUCTOR_BASKET,"Fillings")
        fillings_counter_after = self.get_text_from_element(MainPageLocators.MAIN_BEEF_FILLINGS_COUNTER)
        assert bun_counter_before < bun_counter_after and sauce_counter_before < sauce_counter_after and \
               fillings_counter_before < fillings_counter_after, \
               (f"bun_counter_before      {bun_counter_before}-bun_counter_after {bun_counter_after},"
                f"sauce_counter_before    {sauce_counter_before}-sauce_counter_after {sauce_counter_after},"
                f"fillings_counter_before {fillings_counter_before}-fillings_counter_before {fillings_counter_before}")

    @allure.step("Формируем бургер, создаем заказ, получаем номер заказа, закрываем окно заказа")
    def create_order(self):
        self.create_burger_1_in_basket()
        self.create_order_for_burger_in_basket()
        order_number = self.get_order_num_not_equal_n9()
        self.close_order_modal_window()
        return order_number

    @allure.step("Нажимаем кнопку 'Создание заказа'")
    def create_order_for_burger_in_basket(self):
        self.click_to_element(MainPageLocators.MAIN_CREATE_ORDER_BUTTON)

    @allure.step("Ожидаем и получаем номер созданного заказа")
    def get_order_num_not_equal_n9(self):
        return self.wait_change_value(MainPageLocators.MAIN_MODAL_ORDER_NUMBER, '9999')

    @allure.step("Закрываем модальное окно кликом по крестику")
    def close_order_modal_window(self):
        self.click_to_element(MainPageLocators.MAIN_MODAL_ORDER_CLOSE)

    @allure.step("Перетаскиваем ингредиент - {ingredient_name}")
    def drag_and_drop(self, locator_from, locator_to, ingredient_name):
        if data.DRIVER_NAME == 'firefox':
           self.drag_and_drop_firefox(locator_from, locator_to)
        else:
           self.drag_and_drop_chrome(locator_from, locator_to)

    @allure.step("Тестируем модальные окна деталей ингредиентов - булка, соус, начинка")
    def ingredient_window(self):
        self.click_to_element(MainPageLocators.MAIN_BUN_TAB_BUTTON)
        self.click_to_element(MainPageLocators.MAIN_CRATOR_BUN)
        self.find_element_with_wait(MainPageLocators.MAIN_INGREDIENT_WINDOW_TITLE)
        self.find_element_with_wait(MainPageLocators.MAIN_INGREDIENT_CRATOR_BUN)
        self.click_to_element(MainPageLocators.MAIN_MODAL_ORDER_CLOSE)

        self.click_to_element(MainPageLocators.MAIN_SAUCE_TAB_BUTTON)
        self.click_to_element(MainPageLocators.MAIN_SPICY_SAUCE)
        self.find_element_with_wait(MainPageLocators.MAIN_INGREDIENT_WINDOW_TITLE)
        self.find_element_with_wait(MainPageLocators.MAIN_INGREDIENT_SPICY_SAUCE)
        self.click_to_element(MainPageLocators.MAIN_MODAL_ORDER_CLOSE)

        self.click_to_element(MainPageLocators.MAIN_FILLINGS_TAB_BUTTON)
        self.click_to_element(MainPageLocators.MAIN_BEEF_FILLINGS)
        self.find_element_with_wait(MainPageLocators.MAIN_INGREDIENT_WINDOW_TITLE)
        self.find_element_with_wait(MainPageLocators.MAIN_INGREDIENT_BEEF_FILLINGS)
        self.click_to_element(MainPageLocators.MAIN_MODAL_ORDER_CLOSE)

    @allure.step("Тестируем переход cо страницы Конструктор на страницу Лента заказов")
    def go_to_order_feed_page(self):
        self.click_to_element(MainPageLocators.MAIN_ORDER_FEED_URL)
