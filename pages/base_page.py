import allure
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Найти элемент")
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step("Найти все элементы")
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step("Кликнуть на элемент")
    def click(self, locator):
        element = self.wait.until(expected_conditions.element_to_be_clickable(locator))
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center', inline: 'center'});", element
        )
        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Заполнить поле")
    def send_keys(self, locator, text):
        element = self.wait.until(expected_conditions.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    @allure.step("Получить текст элемента")
    def get_text(self, locator):
        element = self.wait.until(expected_conditions.visibility_of_element_located(locator))
        return element.text

    @allure.step("Ожидать видимость элемента")
    def wait_for_visible(self, locator):
        return self.wait.until(expected_conditions.visibility_of_element_located(locator))

    @allure.step("Ожидать невидимость элемента")
    def wait_for_invisible(self, locator):
        return self.wait.until(expected_conditions.invisibility_of_element_located(locator))

    @allure.step("Ожидать кликабельность элемента")
    def wait_for_clickable(self, locator):
        return self.wait.until(expected_conditions.element_to_be_clickable(locator))

    @allure.step("Проверить видимость элемента")
    def is_visible(self, locator):
        try:
            return self.wait_for_visible(locator).is_displayed()
        except Exception:
            return False

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Перетащить элемент")
    def drag_and_drop(self, source_locator, target_locator):
        source = self.wait.until(
            expected_conditions.visibility_of_element_located(source_locator)
        )
        target = self.wait.until(
            expected_conditions.visibility_of_element_located(target_locator)
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center', inline: 'center'});", source
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center', inline: 'center'});", target
        )
        actions = ActionChains(self.driver)
        (
            actions.click_and_hold(source)
            .pause(0.3)
            .move_to_element(target)
            .pause(0.3)
            .release()
            .perform()
        )

    @allure.step("Перетащить элемент через JavaScript")
    def drag_and_drop_js(self, source_locator, target_locator):
        source = self.wait.until(
            expected_conditions.visibility_of_element_located(source_locator)
        )
        target = self.wait.until(
            expected_conditions.visibility_of_element_located(target_locator)
        )
        self.driver.execute_script(
            """
            const source = arguments[0];
            const target = arguments[1];
            const dataTransfer = new DataTransfer();
            const dragStart = new DragEvent('dragstart', {
                bubbles: true, cancelable: true, dataTransfer,
            });
            source.dispatchEvent(dragStart);
            const dragOver = new DragEvent('dragover', {
                bubbles: true, cancelable: true, dataTransfer,
            });
            target.dispatchEvent(dragOver);
            const drop = new DragEvent('drop', {
                bubbles: true, cancelable: true, dataTransfer,
            });
            target.dispatchEvent(drop);
            const dragEnd = new DragEvent('dragend', {
                bubbles: true, cancelable: true, dataTransfer,
            });
            source.dispatchEvent(dragEnd);
            """,
            source,
            target,
        )
