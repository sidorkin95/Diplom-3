from selenium.webdriver.common.by import By


class MainPageLocators:
    page_title = [By.XPATH, "//h1[text()='Соберите бургер']"]
    place_order_button = [By.XPATH, "//button[text()='Оформить заказ']"]

    constructor_link = [By.XPATH, '//p[text()="Конструктор"]/parent::a']
    order_feed_link = [By.XPATH, '//p[text()="Лента Заказов"]/parent::a']
    personal_account_link = [By.XPATH, '//p[text()="Личный Кабинет"]/parent::a']

    ingredient_fluorescent_bun = [
        By.XPATH,
        '//a[contains(@href, "/ingredient/") and .//p[text()="Флюоресцентная булка R2-D3"]]',
    ]
    ingredient_counter = [
        By.XPATH,
        '//a[contains(@href, "/ingredient/") and .//p[text()="Флюоресцентная булка R2-D3"]]'
        '//p[contains(@class, "num")]',
    ]
    burger_drop_zone_bottom = [
        By.XPATH,
        "//span[contains(@class, 'constructor-element__text') and text()='Перетяните булочку сюда (низ)']",
    ]

    ingredient_modal_title = [By.XPATH, "//h2[text()='Детали ингредиента']"]
    modal_close_button = [By.XPATH, "//button[contains(@class, 'Modal_modal__close')]"]

    order_modal_title = [By.XPATH, "//p[text()='идентификатор заказа']"]
    order_modal_number = [By.XPATH, "//h2[contains(@class, 'Modal_modal__title')]"]
    order_modal_status = [By.XPATH, "//p[text()='Ваш заказ начали готовить']"]
    order_modal_close = [By.XPATH, "//button[contains(@class, 'Modal_modal__close')][1]"]
