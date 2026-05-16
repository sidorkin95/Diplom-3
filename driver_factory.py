from selenium import webdriver


class DriverFactory:

    @classmethod
    def getWebdriver(cls, browser_name):
        browser = browser_name.lower()
        if browser == "chrome":
            return webdriver.Chrome(options=webdriver.ChromeOptions())
        if browser == "firefox":
            return webdriver.Firefox(options=webdriver.FirefoxOptions())
        
