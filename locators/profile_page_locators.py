from selenium.webdriver.common.by import By


class ProfilePageLocators:
    profile_tab = [By.LINK_TEXT, "Профиль"]
    order_history_tab = [By.LINK_TEXT, "История заказов"]
    order_history_tab_active = [
        By.XPATH,
        '//a[contains(@href, "order-history") and contains(@class, "Account_link_active")]',
    ]
    logout_button = [By.XPATH, "//button[text()='Выход']"]
    profile_hint = [By.XPATH, "//p[contains(text(), 'персональные данные')]"]
    order_numbers_in_history = [
        By.XPATH,
        "//*[contains(@class, 'OrderHistory')]//p[contains(@class, 'text_type_digits-default')]",
    ]