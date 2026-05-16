import allure

from locators.login_page_locators import LoginPageLocators
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from urls import Urls


@allure.story("Личный кабинет")
class TestPersonalAccount:

    @allure.title("Переход в личный кабинет по кнопке в шапке")
    @allure.description("Авторизованный пользователь переходит в профиль по кнопке «Личный кабинет»")
    def test_open_personal_account(self, logged_in_driver):
        driver = logged_in_driver
        main_page = MainPage(driver)
        profile_page = ProfilePage(driver)

        main_page.go_to_personal_account()
        profile_page.wait_profile_loaded()

        assert driver.current_url.startswith(Urls.PROFILE_PAGE)

    @allure.title("Переход в раздел «История заказов»")
    @allure.description("В личном кабинете открываем вкладку «История заказов»")
    def test_open_order_history(self, logged_in_driver):
        driver = logged_in_driver
        main_page = MainPage(driver)
        profile_page = ProfilePage(driver)

        main_page.go_to_personal_account()
        profile_page.wait_profile_loaded()
        profile_page.open_order_history()

        assert driver.current_url.startswith(Urls.ORDER_HISTORY_PAGE)

    @allure.title("Выход из аккаунта")
    @allure.description("После выхода открывается страница входа")
    def test_logout(self, logged_in_driver):
        driver = logged_in_driver
        main_page = MainPage(driver)
        profile_page = ProfilePage(driver)
        login_page = LoginPage(driver)

        main_page.go_to_personal_account()
        profile_page.wait_profile_loaded()
        profile_page.logout()

        login_page.wait_for_visible(LoginPageLocators.page_title)
        assert driver.current_url.startswith(Urls.LOGIN_PAGE)
