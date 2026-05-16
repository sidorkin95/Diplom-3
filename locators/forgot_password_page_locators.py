from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:
    email_input = [By.XPATH, "//label[text()='Email']/following-sibling::input"]
    restore_button = [By.XPATH, "//button[text()='Восстановить']"]
    save_button = [By.XPATH, "//button[text()='Сохранить']"]
    password_input = [
        By.XPATH,
        "(//input[contains(@class, 'input__textfield')])[1]",
    ]
    password_input_active = [
        By.XPATH,
        "//motion.div[contains(@class, 'input') and contains(@class, 'input_status_active')]"
        " | //div[contains(@class, 'input') and contains(@class, 'input_status_active')]",
    ]
    show_hide_password_button = [
        By.XPATH,
        "(//input[contains(@class, 'input__textfield')])[1]/ancestor::div[contains(@class, 'input')]"
        "//div[contains(@class, 'icon-action')]",
    ]
