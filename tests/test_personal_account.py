import allure

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage


@allure.story("Личный кабинет")
class TestPersonalAccount:

    @allure.title("Переход в личный кабинет по кнопке в шапке")
    @allure.description("Авторизованный пользователь переходит в профиль по кнопке «Личный кабинет»")
    def test_open_personal_account(self, logged_in_driver):
        main_page = MainPage(logged_in_driver)
        profile_page = ProfilePage(logged_in_driver)

        main_page.go_to_personal_account()
        profile_page.wait_profile_loaded()

        assert profile_page.is_profile_page_open()

    @allure.title("Переход в раздел «История заказов»")
    @allure.description("В личном кабинете открываем вкладку «История заказов»")
    def test_open_order_history(self, logged_in_driver):
        main_page = MainPage(logged_in_driver)
        profile_page = ProfilePage(logged_in_driver)

        main_page.go_to_personal_account()
        profile_page.wait_profile_loaded()
        profile_page.open_order_history()

        assert profile_page.is_order_history_page_open()

    @allure.title("Выход из аккаунта")
    @allure.description("После выхода открывается страница входа")
    def test_logout(self, logged_in_driver):
        main_page = MainPage(logged_in_driver)
        profile_page = ProfilePage(logged_in_driver)
        login_page = LoginPage(logged_in_driver)

        main_page.go_to_personal_account()
        profile_page.wait_profile_loaded()
        profile_page.logout()
        login_page.wait_login_page_loaded()

        assert login_page.is_login_page_open()
        