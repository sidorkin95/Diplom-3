from selenium.webdriver.common.by import By


class LoginPageLocators:
    page_title = [By.XPATH, "//h2[text()='Вход']"]
    email_input = [By.XPATH, "//label[text()='Email']/following-sibling::input"]
    password_input = [By.CSS_SELECTOR, "input[type='password']"]
    login_button = [By.XPATH, "//button[text()='Войти']"]
    forgot_password_link = [By.XPATH, '//a[contains(@href, "/forgot-password")]']