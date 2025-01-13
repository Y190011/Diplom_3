import pytest
import allure
from urls import Urls
from pages.logon_page import LogonPage
import data


@allure.title("Тесты логина, восстановления пароля и проверки статуса активности поля password")
class TestRestorePassword:

    @allure.step("Тестируем авторизацию через кнопку Войти")
    def test_logon_via_entrance(self, driver):
        logon_page = LogonPage(driver)
        logon_page.get_page(Urls.URL_LOGIN_PAGE)
        logon_page.check_logon_page()
        logon_page.logon_by_logon_button(data.my_email, data.my_password)

    @allure.step("Тестируем восстановления пароля")
    def test_recovery_password_via_entrance(self, driver):
        logon_page = LogonPage(driver)
        logon_page.get_page(Urls.URL_LOGIN_PAGE)
        logon_page.check_logon_page()
        logon_page.recovery_password(data.my_email, data.my_password)

    @allure.step("Тестируем изменение статуса активности поля password при нажатии кнопки показать/скрыть пароль")
    def test_check_password_view(self, driver):
        logon_page = LogonPage(driver)
        logon_page.get_page(Urls.URL_LOGIN_PAGE)
        logon_page.check_logon_page()
        parent_tag_div_not_active_class_property, parent_tag_div_active_class_property = (
               logon_page.change_password_field_active_mode(data.my_email, data.my_password))
        assert data.password_parent_active_indicator not in parent_tag_div_not_active_class_property and \
               data.password_parent_active_indicator in parent_tag_div_active_class_property, \
               (f"Class with active {parent_tag_div_active_class_property}, \
                Class not active {parent_tag_div_not_active_class_property}")
