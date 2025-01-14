import pytest
import allure
from urls import Urls
from pages.logon_page   import LogonPage
from pages.main_page    import MainPage
from pages.account_page import AccountPage
import data


@allure.title("Тестируем: создание бургера и окно ингредиента")
class TestMainPage:

    @allure.step("Выполняем проверку создания бургера")
    def test_main(self, driver):
        logon_page = LogonPage(driver)
        main_page = MainPage(driver)
        account_page = AccountPage(driver)
        logon_page.get_page(Urls.URL_LOGIN_PAGE)
        logon_page.logon_by_logon_button(data.my_email, data.my_password)
        assert main_page.check_main_page() != None
        order_num = main_page.create_order()
        assert order_num != None

    @allure.step("Выполняем проверку модальных окон ингредиентов")
    def test_ingredient_window(self, driver):
        logon_page = LogonPage(driver)
        main_page = MainPage(driver)
        logon_page.get_page(Urls.URL_LOGIN_PAGE)
        logon_page.logon_by_logon_button(data.my_email, data.my_password)
        assert main_page.check_main_page() != None
        main_page.ingredient_window()



