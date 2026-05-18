from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


class DriverFactory:

    @classmethod
    def getWebdriver(cls, browser_name):
        browser = browser_name.lower()
        if browser == "chrome":
            options = ChromeOptions()
            options.add_argument("--disable-notifications")
            return webdriver.Chrome(options=options)
        if browser == "firefox":
            options = FirefoxOptions()
            options.set_preference("dom.webnotifications.enabled", False)
            return webdriver.Firefox(options=options)
        raise ValueError(f"Неподдерживаемый браузер: {browser_name}")