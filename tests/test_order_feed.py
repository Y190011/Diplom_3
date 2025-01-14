import pytest
import allure
from urls import Urls
from pages.order_feed_page import OrderFeedPage
from pages.logon_page      import LogonPage
from pages.main_page       import MainPage
from pages.account_page    import AccountPage
import data


@allure.title("Тестируем: Вход, создание бургера, сравнение счетчиков, проверка номера бургера в 'Готовы/В работе'"
              " проверка модального окна для данного бургера, переход в ЛК, проверка наличия бургера в истории")
class TestOrderFeedPage:

    def test_create_order_and_check_history_and_tape_feed(self, driver):

        main_page = MainPage(driver)
        account_page = AccountPage(driver)
        order_feed_page = OrderFeedPage(driver)

        logon_page = LogonPage(driver)
        logon_page.get_page(Urls.URL_LOGIN_PAGE)
        assert logon_page.check_logon_page() != None
        logon_page.logon_by_logon_button(data.my_email, data.my_password)

        assert main_page.check_main_page() != None
        main_page.go_to_order_feed_page()

        assert order_feed_page.check_order_feed_page() != None
        completed_all_before, completed_today_before = (order_feed_page.get_burgers_numbers())
        order_feed_page.go_to_main_page()

        assert main_page.check_main_page() != None
        order_number = main_page.create_order()
        main_page.go_to_order_feed_page()

        assert order_feed_page.check_order_feed_page() != None
        completed_all_after, completed_today_after = order_feed_page.get_burgers_numbers()
        order_feed_page.check_order_in_order_feed_list(order_number)
        order_in_status_box = order_feed_page.check_current_order_in_status_box(order_number)
        assert order_in_status_box == True and completed_all_after > completed_all_before and \
               completed_today_after > completed_today_before, \
               (f"order in Status Box {order_in_status_box}, completed_all_before {completed_all_before}, \
               completed_today_before {completed_today_before}, completed_all_after {completed_all_after}, \
               completed_today_after {completed_today_after} ")
        order_feed_page.go_to_account_page()

        account_page.check_account_page()
        account_page.go_to_order_history()
        account_page.check_order_in_history(order_number)
        account_page.account_logout()

