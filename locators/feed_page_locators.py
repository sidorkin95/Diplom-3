from selenium.webdriver.common.by import By


class FeedPageLocators:
    page_title = [By.XPATH, "//h1[text()='Лента заказов']"]
    order_link = [By.XPATH, "//a[contains(@class, 'OrderHistory_link')]"]
    first_order_link = [
        By.XPATH,
        "(//a[contains(@class, 'OrderHistory_link')][not(.//p[contains(., '9999')])])[1]",
    ]
    order_modal_number = [
        By.XPATH,
        "//section[contains(@class, 'Modal_modal')]//h2[contains(@class, 'Modal_modal__title')]",
    ]
    order_modal_composition = [
        By.XPATH,
        "//section[contains(@class, 'Modal_modal')]//ul/li",
    ]

    completed_all_time_value = [
        By.XPATH,
        "//p[text()='Выполнено за все время:']/following-sibling::p[1]",
    ]

    completed_today_value = [
        By.XPATH,
        "//p[text()='Выполнено за сегодня:']/following-sibling::p[1]",
    ]

    in_progress_orders = [
        By.XPATH,
        "//p[contains(text(), 'В работе')]/following-sibling::ul"
        "//li[contains(@class, 'text_type_digits-default')]",
    ]

    order_numbers_in_feed = [
        By.XPATH,
        "//a[contains(@class, 'OrderHistory_link')]"
        "//p[contains(@class, 'text_type_digits-default')]",
    ]
