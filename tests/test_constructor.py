import allure

from locators.feed_page_locators import FeedPageLocators
from locators.main_page_locators import MainPageLocators
from pages.feed_page import FeedPage
from pages.main_page import MainPage
from urls import Urls


@allure.story("Конструктор")
class TestConstructor:

    @allure.title("Переход в конструктор по кнопке в шапке")
    @allure.description("Из ленты заказов возвращаемся в конструктор")
    def test_navigate_to_constructor(self, open_main_page):
        driver = open_main_page
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)

        main_page.go_to_order_feed()
        feed_page.wait_feed_loaded()
        main_page.go_to_constructor()

        assert main_page.is_on_main_page()
        assert main_page.is_visible(MainPageLocators.page_title)

    @allure.title("Переход в ленту заказов по кнопке в шапке")
    @allure.description("По кнопке «Лента заказов» открывается страница ленты")
    def test_navigate_to_order_feed(self, open_main_page):
        driver = open_main_page
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)

        main_page.go_to_order_feed()
        feed_page.wait_feed_loaded()

        assert driver.current_url == Urls.FEED_PAGE
        assert feed_page.is_visible(FeedPageLocators.page_title)

    @allure.title("Клик по ингредиенту открывает модальное окно с деталями")
    @allure.description("При клике на ингредиент появляется окно «Детали ингредиента»")
    def test_ingredient_modal_opens(self, open_main_page):
        main_page = MainPage(open_main_page)
        main_page.click_ingredient()

        assert main_page.is_visible(MainPageLocators.ingredient_modal_title)

    @allure.title("Модальное окно ингредиента закрывается по крестику")
    @allure.description("После клика по крестику окно деталей закрывается")
    def test_ingredient_modal_closes(self, open_main_page):
        main_page = MainPage(open_main_page)
        main_page.click_ingredient()
        main_page.close_modal()
        main_page.wait_for_invisible(MainPageLocators.ingredient_modal_title)

        assert not main_page.is_visible(MainPageLocators.ingredient_modal_title)

    @allure.title("Счётчик ингредиента увеличивается при добавлении в заказ")
    @allure.description("После перетаскивания ингредиента счётчик становится больше")
    def test_ingredient_counter_increases(self, open_main_page):
        main_page = MainPage(open_main_page)
        counter_before = main_page.get_ingredient_counter()
        main_page.add_ingredient_to_order()
        counter_after = main_page.get_ingredient_counter()

        assert counter_after > counter_before

    @allure.title("Авторизованный пользователь может оформить заказ")
    @allure.description("Залогиненный пользователь оформляет заказ и видит подтверждение")
    def test_place_order_when_logged_in(self, logged_in_driver):
        main_page = MainPage(logged_in_driver)
        main_page.add_ingredient_to_order()
        main_page.place_order()

        assert main_page.is_order_placed()
