from selenium.webdriver.common.by import By


class LoginPageLocators:
    page_title = [By.XPATH, "//h2[text()='Вход']"]
    forgot_password_link = [By.XPATH, '//a[contains(@href, "/forgot-password")]']