
import pytest
import allure
from urls import Urls
from pages.logon_page import LogonPage
from pages.main_page import MainPage
from pages.account_page import AccountPage
import data


@allure.title("Тестируем функциональность Личного кабинета")
class TestAccount:

    @allure.step("Выполнение тестирования Личного кабинета")
    def test_personal_account(self, driver):
        logon_page = LogonPage(driver)
        main_page  = MainPage(driver)
        account_page = AccountPage(driver)
        logon_page.get_page(Urls.URL_LOGIN_PAGE)
        logon_page.logon_by_logon_button(data.my_email, data.my_password)
        assert main_page.check_main_page() != None
        main_page.go_to_personal_account()
        assert account_page.check_account_page() != None
        account_page.go_to_order_history()
        assert account_page.check_order_first_history_item() != None
        account_page.account_logout()
        assert logon_page.check_logon_page() != None