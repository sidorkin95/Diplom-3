import allure

from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage
from urls import Urls


class LoginPage(BasePage):

    @allure.step("Открыть страницу входа")
    def open_login_page(self):
        self.driver.get(Urls.LOGIN_PAGE)
        self.wait_for_visible(LoginPageLocators.page_title)

    @allure.step("Перейти к восстановлению пароля")
    def go_to_password_recovery(self):
        self.click(LoginPageLocators.forgot_password_link)

    @allure.step("Авторизация")
    def login(self, email, password):
        self.send_keys(LoginPageLocators.email_input, email)
        self.send_keys(LoginPageLocators.password_input, password)
        self.click(LoginPageLocators.login_button)
