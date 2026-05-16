import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from urls import Urls


class MainPage(BasePage):

    @allure.step("Перейти в конструктор")
    def go_to_constructor(self):
        self.click(MainPageLocators.constructor_link)
        self.wait_for_visible(MainPageLocators.page_title)

    @allure.step("Перейти в ленту заказов")
    def go_to_order_feed(self):
        self.click(MainPageLocators.order_feed_link)

    @allure.step("Перейти в личный кабинет")
    def go_to_personal_account(self):
        self.click(MainPageLocators.personal_account_link)

    @allure.step("Открыть страницу входа")
    def click_login_button(self):
        self.click(MainPageLocators.login_button)

    @allure.step("Клик по ингредиенту")
    def click_ingredient(self):
        self.click(MainPageLocators.ingredient_fluorescent_bun)

    @allure.step("Закрыть модальное окно")
    def close_modal(self):
        self.click(MainPageLocators.modal_close_button)

    @allure.step("Добавить ингредиент в заказ")
    def add_ingredient_to_order(self):
        source = MainPageLocators.ingredient_fluorescent_bun
        target = MainPageLocators.burger_drop_zone_bottom
        if "firefox" in self.driver.name.lower():
            self.drag_and_drop_js(source, target)
        else:
            self.drag_and_drop(source, target)

    @allure.step("Получить счётчик ингредиента")
    def get_ingredient_counter(self):
        return int(self.get_text(MainPageLocators.ingredient_counter))

    @allure.step("Оформить заказ")
    def place_order(self):
        self.click(MainPageLocators.place_order_button)

    @allure.step("Закрыть окно оформленного заказа")
    def close_order_modal(self):
        self.wait_for_visible(MainPageLocators.order_modal_title)
        self.click(MainPageLocators.order_modal_close)

    @allure.step("Получить номер оформленного заказа")
    def get_order_number_from_modal(self):
        self.wait_for_visible(MainPageLocators.order_modal_title)
        order_number = self.get_text(MainPageLocators.order_modal_number).strip()
        while order_number == "9999":
            order_number = self.get_text(MainPageLocators.order_modal_number).strip()
        return order_number.lstrip("#")

    @allure.step("Проверить, что заказ оформлен")
    def is_order_placed(self):
        return (
            self.is_visible(MainPageLocators.order_modal_title)
            and self.is_visible(MainPageLocators.order_modal_status)
        )

    def is_on_main_page(self):
        return self.get_current_url().rstrip("/") == Urls.BASE_URL.rstrip("/")
