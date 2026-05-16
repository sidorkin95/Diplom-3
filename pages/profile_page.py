import allure
from selenium.webdriver.support.wait import WebDriverWait

from locators.profile_page_locators import ProfilePageLocators
from pages.base_page import BasePage


def _normalize_order_number(order_number: str) -> str:
    return order_number.strip().lstrip("#").lstrip("0") or "0"


class ProfilePage(BasePage):

    @allure.step("Дождаться загрузки профиля")
    def wait_profile_loaded(self):
        self.wait_for_visible(ProfilePageLocators.profile_hint)

    @allure.step("Перейти в историю заказов")
    def open_order_history(self):
        self.click(ProfilePageLocators.order_history_tab)
        self.wait_for_visible(ProfilePageLocators.order_history_tab_active)

    @allure.step("Выйти из аккаунта")
    def logout(self):
        self.click(ProfilePageLocators.logout_button)

    def get_order_numbers_in_history(self):
        return [
            element.text.strip().lstrip("#")
            for element in self.find_elements(ProfilePageLocators.order_numbers_in_history)
        ]

    @allure.step("Заказ {order_number} есть в истории")
    def is_order_in_history(self, order_number):
        target = _normalize_order_number(order_number)
        return any(
            _normalize_order_number(number) == target
            for number in self.get_order_numbers_in_history()
        )

    @allure.step("Дождаться заказа {order_number} в истории")
    def wait_order_in_history(self, order_number, timeout=15):
        target = _normalize_order_number(order_number)
        WebDriverWait(self.driver, timeout).until(
            lambda _: any(
                _normalize_order_number(number) == target
                for number in self.get_order_numbers_in_history()
            ),
            message=f"Заказ {order_number} не появился в истории",
        )
