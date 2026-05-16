import allure

from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from pages.base_page import BasePage
from urls import Urls


class ForgotPasswordPage(BasePage):

    @allure.step("Открыть восстановление пароля")
    def open_forgot_password_page(self):
        self.driver.get(Urls.FORGOT_PASSWORD_PAGE)

    @allure.step("Ввести email и нажать Восстановить")
    def submit_email(self, email):
        self.send_keys(ForgotPasswordPageLocators.email_input, email)
        self.click(ForgotPasswordPageLocators.restore_button)
        self.wait_for_visible(ForgotPasswordPageLocators.save_button)

    @allure.step("Переключить видимость пароля")
    def toggle_password_visibility(self):
        self.click(ForgotPasswordPageLocators.show_hide_password_button)
        self.wait_for_visible(ForgotPasswordPageLocators.password_input_active)

    @allure.step("Поле пароля в активном состоянии")
    def is_password_field_active(self):
        password_input = self.find_element(ForgotPasswordPageLocators.password_input)
        return (
            password_input.get_attribute("type") == "text"
            and self.is_visible(ForgotPasswordPageLocators.password_input_active)
        )
