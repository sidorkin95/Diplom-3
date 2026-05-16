import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators.feed_page_locators import FeedPageLocators
from pages.base_page import BasePage


def _normalize_order_number(order_number: str) -> str:
    return order_number.strip().lstrip("#").lstrip("0") or "0"


class FeedPage(BasePage):

    @allure.step("Дождаться загрузки ленты заказов")
    def wait_feed_loaded(self):
        self.wait_for_visible(FeedPageLocators.page_title)
        self.wait.until(
            EC.visibility_of_element_located(FeedPageLocators.order_link)
        )

    @allure.step("Открыть первый заказ в ленте")
    def open_first_order(self):
        self.click(FeedPageLocators.first_order_link)
        self._wait_order_details_modal()

    @allure.step("Дождаться модального окна с деталями заказа")
    def _wait_order_details_modal(self):
        WebDriverWait(self.driver, 15).until(
            lambda _: self._is_order_details_page_open()
        )
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(FeedPageLocators.order_modal_composition)
        )

    def _is_order_details_page_open(self):
        url = self.driver.current_url.rstrip("/")
        return url.endswith("/feed") is False and "/feed/" in url

    def _get_visible_order_modal_number(self):
        for element in self.find_elements(FeedPageLocators.order_modal_number):
            if element.is_displayed():
                return element.text.strip().lstrip("#")
        return ""

    @allure.step("Получить счётчик «Выполнено за всё время»")
    def get_completed_all_time_count(self):
        return int(self.get_text(FeedPageLocators.completed_all_time_value))

    @allure.step("Получить счётчик «Выполнено за сегодня»")
    def get_completed_today_count(self):
        return int(self.get_text(FeedPageLocators.completed_today_value))

    def get_order_numbers_in_feed(self):
        return [
            element.text.strip().lstrip("#")
            for element in self.find_elements(FeedPageLocators.order_numbers_in_feed)
        ]

    def get_in_progress_order_numbers(self):
        return [
            element.text.strip().lstrip("#")
            for element in self.find_elements(FeedPageLocators.in_progress_orders)
        ]

    @allure.step("Заказ {order_number} есть в ленте")
    def is_order_in_feed(self, order_number):
        target = _normalize_order_number(order_number)
        return any(
            _normalize_order_number(number) == target
            for number in self.get_order_numbers_in_feed()
        )

    @allure.step("Заказ {order_number} в разделе «В работе»")
    def is_order_in_progress(self, order_number):
        target = _normalize_order_number(order_number)
        return any(
            _normalize_order_number(number) == target
            for number in self.get_in_progress_order_numbers()
        )

    @allure.step("Дождаться заказа {order_number} в ленте")
    def wait_order_in_feed(self, order_number, timeout=15):
        target = _normalize_order_number(order_number)
        WebDriverWait(self.driver, timeout).until(
            lambda _: any(
                _normalize_order_number(number) == target
                for number in self.get_order_numbers_in_feed()
            ),
            message=f"Заказ {order_number} не появился в ленте",
        )

    @allure.step("Дождаться заказа {order_number} в разделе «В работе»")
    def wait_order_in_progress(self, order_number, timeout=30):
        target = _normalize_order_number(order_number)
        self.wait_order_in_feed(order_number, timeout=timeout)
        WebDriverWait(self.driver, timeout).until(
            lambda _: any(
                _normalize_order_number(number) == target
                for number in self.get_in_progress_order_numbers()
            ),
            message=f"Заказ {order_number} не появился в разделе «В работе»",
        )

    @allure.step("Дождаться увеличения счётчика «Выполнено за всё время»")
    def wait_completed_all_time_increased(self, previous_count, timeout=30):
        WebDriverWait(self.driver, timeout).until(
            lambda _: self.get_completed_all_time_count() > previous_count,
            message="Счётчик «Выполнено за всё время» не увеличился",
        )

    @allure.step("Дождаться увеличения счётчика «Выполнено за сегодня»")
    def wait_completed_today_increased(self, previous_count, timeout=30):
        WebDriverWait(self.driver, timeout).until(
            lambda _: self.get_completed_today_count() > previous_count,
            message="Счётчик «Выполнено за сегодня» не увеличился",
        )
