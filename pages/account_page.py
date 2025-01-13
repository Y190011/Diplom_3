from pages.base_page import BasePage
import allure
import data
from locators.logon_page_locators import LogonPageLocators
from locators.account_page_locators import AccountPageLocators

class AccountPage(BasePage):

    @allure.step("Проверяем переход на Историю заказов")
    def go_to_order_history(self):
        self.click_to_element(AccountPageLocators.ACCOUNT_ORDER_HISTORY_URL)

    @allure.step("Проверяем переход на страницу Личный кабинет")
    def check_account_page(self):
        self.find_element_with_wait(AccountPageLocators.ACCOUNT_ORDER_HISTORY_URL)

    @allure.step("Проверяем загрузку Истории заказов")
    def check_order_first_history_item(self):
        self.find_element_with_wait(AccountPageLocators.ACCOUNT_FIRST_HISTORY_ITEM)

    @allure.step("Выполняем выход из системы")
    def account_logout(self):
        self.click_to_element(AccountPageLocators.ACCOUNT_EXIT_BUTTON)

    @allure.step("Проверяем наличие созданного заказа в Истории заказов")
    def check_order_in_history(self, order_number):
        locator_number = self.format_locators_text(AccountPageLocators.ACCOUNT_HIST_ORDER_NUMBER_LOCATOR, order_number)
        locator_status = self.format_locators_text(AccountPageLocators.ACCOUNT_HIST_ORDER_STATUS_LOCATOR, order_number)
        self.check_order_first_history_item()
        self.find_element_by_locator(locator_number)
        assert self.find_element_by_locator(locator_status).text == data.STATUS_ORDER_COMPLETED


