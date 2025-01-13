from pages.base_page import BasePage
import allure
from locators.logon_page_locators import LogonPageLocators

class LogonPage(BasePage):

    @allure.step("Выполняем login по зарегистрированным email и паролю через кнопку 'Войти'")
    def logon_by_logon_button(self, email, password):
        self.add_text_to_element(LogonPageLocators.ENTRANCE_EMAIL, email)
        self.add_text_to_element(LogonPageLocators.ENTRANCE_PASSWORD, password)
        self.click_to_element(LogonPageLocators.ENTRANCE_BUTTON)

    @allure.step('Выполняем восстановление пароля')
    def recovery_password(self, email, password):
        self.click_to_element(LogonPageLocators.ENTRANCE_FORGOT_PASSWORD_URL)

        self.find_element_with_wait(LogonPageLocators.RECOVERY_TITLE)
        self.add_text_to_element(LogonPageLocators.RECOVERY_EMAIL, email)

        self.click_to_element(LogonPageLocators.RECOVERY_BUTTON)
        self.find_element_with_wait(LogonPageLocators.RECOVERY_CODE_INPUT)

        self.add_text_to_element(LogonPageLocators.RECOVERY_PASSWORD, password)
        self.click_to_element(LogonPageLocators.RECOVERY_SAVE_BUTTON)
        self.click_to_element(LogonPageLocators.RECOVERY_LOGIN_URL)
        self.find_element_with_wait(LogonPageLocators.ENTRANCE_TITLE)

    @allure.step('Изменяем режима отображения пароля, проверяем результат')
    def change_password_field_active_mode(self, email, password):
        self.add_text_to_element(LogonPageLocators.ENTRANCE_PASSWORD, password)
        self.add_text_to_element(LogonPageLocators.ENTRANCE_EMAIL, email)
        password_parent_not_active = self.find_element_by_locator(LogonPageLocators.ENTRANCE_PASSWORD_PARENT_DIV)
        parent_tag_div_not_active_class_property = password_parent_not_active.get_dom_attribute("class")
        self.click_to_element(LogonPageLocators.ENTRANCE_PASSWORD_VIEW_ICON)
        password_parent_active = self.find_element_by_locator(LogonPageLocators.ENTRANCE_PASSWORD_PARENT_DIV)
        parent_tag_div_active_class_property = password_parent_active.get_dom_attribute("class")
        return parent_tag_div_not_active_class_property, parent_tag_div_active_class_property

    @allure.step("Проверяем загрузку страницы авторизации")
    def check_logon_page(self):
        self.find_element_with_wait(LogonPageLocators.ENTRANCE_TITLE)


