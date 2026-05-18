import allure
import time
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:

    DEFAULT_TIMEOUT = 10

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, self.DEFAULT_TIMEOUT)

    @allure.step("Открыть URL")
    def open_url(self, url):
        self.driver.get(url)

    @allure.step("Обновить страницу")
    def refresh_page(self):
        self.driver.refresh()

    @allure.step("Установить значение в localStorage")
    def set_local_storage_item(self, key, value):
        self.driver.execute_script(
            "window.localStorage.setItem(arguments[0], arguments[1]);",
            key,
            value,
        )

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

    @allure.step("Получить атрибут элемента")
    def get_attribute(self, locator, attribute_name):
        element = self.find_element(locator)
        return element.get_attribute(attribute_name)

    @allure.step("Ожидать видимость элемента")
    def wait_for_visible(self, locator, timeout=None):
        wait = self._get_wait(timeout)
        return wait.until(expected_conditions.visibility_of_element_located(locator))

    @allure.step("Ожидать невидимость элемента")
    def wait_for_invisible(self, locator, timeout=None):
        wait = self._get_wait(timeout)
        return wait.until(expected_conditions.invisibility_of_element_located(locator))

    @allure.step("Ожидать кликабельность элемента")
    def wait_for_clickable(self, locator, timeout=None):
        wait = self._get_wait(timeout)
        return wait.until(expected_conditions.element_to_be_clickable(locator))

    @allure.step("Ожидать выполнения условия")
    def wait_until(self, condition, timeout=None, message=None):
        wait = self._get_wait(timeout)
        return wait.until(condition, message=message)

    @allure.step("Проверить видимость элемента")
    def is_visible(self, locator, timeout=None):
        try:
            return self.wait_for_visible(locator, timeout=timeout).is_displayed()
        except TimeoutException:
            return False

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    def is_current_url(self, expected_url):
        return self.get_current_url() == expected_url

    def is_current_url_startswith(self, prefix):
        return self.get_current_url().startswith(prefix)

    def is_current_url_contains(self, fragment):
        return fragment in self.get_current_url()

    def is_firefox(self):
        return "firefox" in self.driver.name.lower()

    def _get_wait(self, timeout):
        if timeout is None:
            return self.wait
        return WebDriverWait(self.driver, timeout)

    @allure.step("Перетащить элемент")
    def drag_and_drop(self, source_locator, target_locator):
        source = self.wait.until(
            expected_conditions.visibility_of_element_located(source_locator)
        )
        target = self.wait.until(
            expected_conditions.visibility_of_element_located(target_locator)
        )

        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", source)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", target)

        if self.is_firefox():
            self.drag_and_drop_js(source_locator, target_locator)
        else:
            actions = ActionChains(self.driver)
            actions.click_and_hold(source).pause(0.3).move_to_element(target).pause(0.3).release().perform()

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
            
            const sourceRect = source.getBoundingClientRect();
            const targetRect = target.getBoundingClientRect();
            const sourceX = sourceRect.left + sourceRect.width / 2;
            const sourceY = sourceRect.top + sourceRect.height / 2;
            const targetX = targetRect.left + targetRect.width / 2;
            const targetY = targetRect.top + targetRect.height / 2;
            
            const dataTransfer = new DataTransfer();
            
            const dragStartEvent = new DragEvent('dragstart', {
                bubbles: true, cancelable: true,
                clientX: sourceX, clientY: sourceY,
                dataTransfer: dataTransfer
            });
            source.dispatchEvent(dragStartEvent);
            
            const dragOverEvent = new DragEvent('dragover', {
                bubbles: true, cancelable: true,
                clientX: targetX, clientY: targetY,
                dataTransfer: dataTransfer
            });
            target.dispatchEvent(dragOverEvent);
            
            const dropEvent = new DragEvent('drop', {
                bubbles: true, cancelable: true,
                clientX: targetX, clientY: targetY,
                dataTransfer: dataTransfer
            });
            target.dispatchEvent(dropEvent);
            
            const dragEndEvent = new DragEvent('dragend', {
                bubbles: true, cancelable: true,
                clientX: targetX, clientY: targetY,
                dataTransfer: dataTransfer
            });
            source.dispatchEvent(dragEndEvent);
            """,
            source,
            target,
        )
        time.sleep(1)
        