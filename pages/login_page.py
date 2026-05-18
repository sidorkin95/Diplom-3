import allure

from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage
from urls import Urls


class LoginPage(BasePage):

    @allure.step("Открыть страницу входа")
    def open_login_page(self):
        self.open_url(Urls.LOGIN_PAGE)
        self.wait_for_visible(LoginPageLocators.page_title)

    @allure.step("Перейти к восстановлению пароля")
    def go_to_password_recovery(self):
        self.click(LoginPageLocators.forgot_password_link)

    @allure.step("Дождаться загрузки страницы входа")
    def wait_login_page_loaded(self):
        self.wait_for_visible(LoginPageLocators.page_title)

    @allure.step("Страница входа открыта")
    def is_login_page_open(self):
        return self.is_current_url_startswith(Urls.LOGIN_PAGE)