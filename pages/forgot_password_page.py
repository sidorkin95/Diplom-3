import allure

from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from pages.base_page import BasePage
from urls import Urls


class ForgotPasswordPage(BasePage):

    @allure.step("Открыть восстановление пароля")
    def open_forgot_password_page(self):
        self.open_url(Urls.FORGOT_PASSWORD_PAGE)

    @allure.step("Ввести email и нажать Восстановить")
    def submit_email(self, email):
        self.send_keys(ForgotPasswordPageLocators.email_input, email)
        self.click(ForgotPasswordPageLocators.restore_button)
        self.wait_for_visible(ForgotPasswordPageLocators.save_button)

    @allure.step("Переключить видимость пароля")
    def toggle_password_visibility(self):
        self.click(ForgotPasswordPageLocators.show_hide_password_button)
        self.wait_for_visible(ForgotPasswordPageLocators.password_input_active)

    @allure.step("Страница восстановления пароля открыта")
    def is_forgot_password_page_open(self):
        return self.is_current_url(Urls.FORGOT_PASSWORD_PAGE)

    @allure.step("Страница сброса пароля открыта")
    def is_reset_password_page_open(self):
        return self.is_current_url_contains(Urls.RESET_PASSWORD_PAGE)

    @allure.step("Форма восстановления пароля отображается")
    def is_restore_form_visible(self):
        return self.is_visible(ForgotPasswordPageLocators.restore_button)

    @allure.step("Форма сброса пароля отображается")
    def is_reset_form_visible(self):
        return self.is_visible(ForgotPasswordPageLocators.save_button)

    @allure.step("Поле пароля в активном состоянии")
    def is_password_field_active(self):
        return (
            self.get_attribute(ForgotPasswordPageLocators.password_input, "type") == "text"
            and self.is_visible(ForgotPasswordPageLocators.password_input_active)
        )
    