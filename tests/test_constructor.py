import allure

from pages.feed_page import FeedPage
from pages.main_page import MainPage


@allure.story("Конструктор")
class TestConstructor:

    @allure.title("Переход в конструктор по кнопке в шапке")
    @allure.description("Из ленты заказов возвращаемся в конструктор")
    def test_navigate_to_constructor(self, open_main_page):
        main_page = MainPage(open_main_page)
        feed_page = FeedPage(open_main_page)

        main_page.go_to_order_feed()
        feed_page.wait_feed_loaded()
        main_page.go_to_constructor()

        assert main_page.is_constructor_open()

    @allure.title("Переход в ленту заказов по кнопке в шапке")
    @allure.description("По кнопке «Лента заказов» открывается страница ленты")
    def test_navigate_to_order_feed(self, open_main_page):
        main_page = MainPage(open_main_page)
        feed_page = FeedPage(open_main_page)

        main_page.go_to_order_feed()
        feed_page.wait_feed_loaded()

        assert feed_page.is_feed_page_open()

    @allure.title("Клик по ингредиенту открывает модальное окно с деталями")
    @allure.description("При клике на ингредиент появляется окно «Детали ингредиента»")
    def test_ingredient_modal_opens(self, open_main_page):
        main_page = MainPage(open_main_page)
        main_page.click_ingredient()

        assert main_page.is_ingredient_modal_open()

    @allure.title("Модальное окно ингредиента закрывается по крестику")
    @allure.description("После клика по крестику окно деталей закрывается")
    def test_ingredient_modal_closes(self, open_main_page):
        main_page = MainPage(open_main_page)
        main_page.click_ingredient()
        main_page.close_modal()

        assert main_page.is_ingredient_modal_closed()

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
        