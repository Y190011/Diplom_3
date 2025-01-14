from pages.base_page import BasePage
import allure
from locators.order_feed_page_locators import OrderFeedPageLocators


class OrderFeedPage(BasePage):

    @allure.step("Проверяем переход на страницу Лента заказов")
    def check_order_feed_page(self):
        return self.find_element_with_wait(OrderFeedPageLocators.ORDER_FEED_PAGE_TITLE)

    @allure.step("Выполняем переход со страницы Лента заказов на страницу Конструктор (главную)")
    def go_to_main_page(self):
        assert self.click_to_element(OrderFeedPageLocators.ORDER_FEED_CONSTRUCTOR_URL) != None

    @allure.step("Получаем текущие показания счетчиков 'Выполнено за все время:' и 'Выполнено за сегодня:'")
    def get_burgers_numbers(self):
        burgers_all_element   = self.get_text_from_element(OrderFeedPageLocators.ORDER_FEED_BURGERS_ALL)
        burgers_today_element = self.get_text_from_element(OrderFeedPageLocators.ORDER_FEED_BURGERS_TODAY)
        return burgers_all_element, burgers_today_element

    @allure.step("Выполняем переход в Личный кабинет")
    def go_to_account_page(self):
        assert self.click_to_element(OrderFeedPageLocators.ORDER_FEED_ACCOUNT_URL) != None

    @allure.step("Получаем Status Box Ленты заказов")
    def get_status_box_list(self):
        return self.get_elements_with_wait(OrderFeedPageLocators.ORDER_FEED_STATUS_BOX)

    @allure.step("Проверяем наличие номера бургера в статусе 'В работе:' или 'Готовы:'")
    def check_current_order_in_status_box(self, order_number):
        status_box_list = self.get_status_box_list()
        for current_status_element in status_box_list:
            if current_status_element.text == '0' + order_number:
                return True
        return False

    @allure.step("Проверяем модальное окно заказа - текст 'Состав' и номер бургера, закрываем модальное окно")
    def check_order_in_order_feed_list(self, order_number):
        locator_num = self.format_locators_text(OrderFeedPageLocators.ORDER_FEED_FIND_ORDER_IN_FEED, order_number)
        self.scroll_to_element(locator_num)
        locator_click = self.format_locators_text(OrderFeedPageLocators.ORDER_FEED_CLICK_ORDER_IN_FEED, order_number)
        assert self.click_to_element(locator_click) != None
        self.find_element_with_wait(OrderFeedPageLocators.ORDER_FEED_BURGER_MODAL_TITLE)
        locator_burger_modal_number = (
            self.format_locators_text(OrderFeedPageLocators.ORDER_FEED_BURGER_MODAL_TITLE, order_number))
        self.find_element_with_wait(locator_burger_modal_number)
        assert self.click_to_element(OrderFeedPageLocators.ORDER_FEED_BURGER_MODAL_CLOSE) != None

