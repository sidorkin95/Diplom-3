import allure

from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage


@allure.story("Восстановление пароля")
class TestPasswordRecovery:

    @allure.title("Переход на страницу восстановления пароля по ссылке")
    @allure.description("На странице входа нажимаем «Восстановить пароль» и проверяем URL")
    def test_navigate_to_forgot_password_page(self, driver):
        login_page = LoginPage(driver)
        forgot_page = ForgotPasswordPage(driver)

        login_page.open_login_page()
        login_page.go_to_password_recovery()

        assert forgot_page.is_forgot_password_page_open()

    @allure.title("Ввод email открывает страницу сброса пароля")
    @allure.description("Вводим почту зарегистрированного пользователя и нажимаем «Восстановить»")
    def test_submit_email_opens_reset_password_page(self, driver, registered_user):
        forgot_page = ForgotPasswordPage(driver)
        forgot_page.open_forgot_password_page()
        forgot_page.submit_email(registered_user["email"])

        assert forgot_page.is_reset_password_page_open()

    @allure.title("Кнопка показать/скрыть пароль подсвечивает поле")
    @allure.description("После перехода на сброс пароля клик по иконке делает поле активным")
    def test_show_password_highlights_field(self, driver, registered_user):
        forgot_page = ForgotPasswordPage(driver)
        forgot_page.open_forgot_password_page()
        forgot_page.submit_email(registered_user["email"])
        forgot_page.toggle_password_visibility()

        assert forgot_page.is_password_field_active()
        