import allure

from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage
from urls import Urls


@allure.story("Восстановление пароля")
class TestPasswordRecovery:

    @allure.title("Переход на страницу восстановления пароля по ссылке")
    @allure.description("На странице входа нажимаем «Восстановить пароль» и проверяем URL")
    def test_navigate_to_forgot_password_page(self, driver):
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.go_to_password_recovery()

        assert driver.current_url == Urls.FORGOT_PASSWORD_PAGE
        assert login_page.is_visible(ForgotPasswordPageLocators.restore_button)

    @allure.title("Ввод email и переход на страницу сброса пароля")
    @allure.description("Вводим почту зарегистрированного пользователя и нажимаем «Восстановить»")
    def test_submit_email_for_recovery(self, driver, registered_user):
        forgot_page = ForgotPasswordPage(driver)
        forgot_page.open_forgot_password_page()
        forgot_page.submit_email(registered_user["email"])

        assert Urls.RESET_PASSWORD_PAGE in driver.current_url
        assert forgot_page.is_visible(ForgotPasswordPageLocators.save_button)

    @allure.title("Кнопка показать/скрыть пароль подсвечивает поле")
    @allure.description("После перехода на сброс пароля клик по иконке делает поле активным")
    def test_show_password_highlights_field(self, driver, registered_user):
        forgot_page = ForgotPasswordPage(driver)
        forgot_page.open_forgot_password_page()
        forgot_page.submit_email(registered_user["email"])
        forgot_page.toggle_password_visibility()

        assert forgot_page.is_password_field_active()
