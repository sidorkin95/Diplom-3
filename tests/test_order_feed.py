import allure

from locators.feed_page_locators import FeedPageLocators
from pages.feed_page import FeedPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage


@allure.story("Лента заказов")
class TestOrderFeed:

    @allure.title("Клик по заказу открывает модальное окно с деталями")
    @allure.description("В ленте заказов открываем карточку и проверяем блок «Состав»")
    def test_order_modal_opens_from_feed(self, open_main_page):
        driver = open_main_page
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)

        main_page.go_to_order_feed()
        feed_page.wait_feed_loaded()
        feed_page.open_first_order()

        assert feed_page.is_visible(FeedPageLocators.order_modal_composition)

    @allure.title("Заказ из истории отображается в ленте заказов")
    @allure.description("Номер заказа есть в истории ЛК и в ленте")
    def test_order_from_history_visible_in_feed(self, logged_in_driver):
        driver = logged_in_driver
        main_page = MainPage(driver)
        profile_page = ProfilePage(driver)
        feed_page = FeedPage(driver)

        main_page.add_ingredient_to_order()
        main_page.place_order()
        order_number = main_page.get_order_number_from_modal()
        main_page.close_order_modal()

        main_page.go_to_personal_account()
        profile_page.wait_profile_loaded()
        profile_page.open_order_history()
        profile_page.wait_order_in_history(order_number)

        main_page.go_to_order_feed()
        feed_page.wait_feed_loaded()
        feed_page.wait_order_in_feed(order_number)

    @allure.title("Счётчик «Выполнено за всё время» увеличивается после заказа")
    @allure.description("Сравниваем счётчик до и после оформления заказа")
    def test_completed_all_time_counter_increases(self, logged_in_driver):
        driver = logged_in_driver
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)

        main_page.go_to_order_feed()
        feed_page.wait_feed_loaded()
        count_before = feed_page.get_completed_all_time_count()

        main_page.go_to_constructor()
        main_page.add_ingredient_to_order()
        main_page.place_order()
        main_page.close_order_modal()

        main_page.go_to_order_feed()
        feed_page.wait_feed_loaded()
        feed_page.wait_completed_all_time_increased(count_before)
        count_after = feed_page.get_completed_all_time_count()

        assert count_after > count_before

    @allure.title("Счётчик «Выполнено за сегодня» увеличивается после заказа")
    @allure.description("Сравниваем дневной счётчик до и после оформления заказа")
    def test_completed_today_counter_increases(self, logged_in_driver):
        driver = logged_in_driver
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)

        main_page.go_to_order_feed()
        feed_page.wait_feed_loaded()
        count_before = feed_page.get_completed_today_count()

        main_page.go_to_constructor()
        main_page.add_ingredient_to_order()
        main_page.place_order()
        main_page.close_order_modal()

        main_page.go_to_order_feed()
        feed_page.wait_feed_loaded()
        feed_page.wait_completed_today_increased(count_before)
        count_after = feed_page.get_completed_today_count()

        assert count_after > count_before

    @allure.title("Номер нового заказа появляется в разделе «В работе»")
    @allure.description("После оформления заказ отображается в колонке «В работе»")
    def test_new_order_in_progress_section(self, logged_in_driver):
        driver = logged_in_driver
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)

        main_page.go_to_order_feed()
        feed_page.wait_feed_loaded()

        main_page.go_to_constructor()
        main_page.add_ingredient_to_order()
        main_page.place_order()
        order_number = main_page.get_order_number_from_modal()
        main_page.close_order_modal()

        main_page.go_to_order_feed()
        feed_page.wait_feed_loaded()
        feed_page.wait_order_in_progress(order_number)
