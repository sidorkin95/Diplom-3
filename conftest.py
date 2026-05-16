import os

import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from data.data_user import delete_user, register_user
from driver_factory import DriverFactory
from locators.main_page_locators import MainPageLocators
from urls import Urls


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default=None,
        help="chrome или firefox. Без параметра — оба браузера.",
    )


def pytest_generate_tests(metafunc):
    if "driver" not in metafunc.fixturenames:
        return
    browser_option = metafunc.config.getoption("--browser")
    if browser_option:
        metafunc.parametrize("driver", [browser_option.lower()], indirect=True)
    else:
        metafunc.parametrize("driver", ["chrome", "firefox"], indirect=True)


@pytest.fixture()
def driver(request):
    web_driver = DriverFactory.getWebdriver(request.param)
    web_driver.maximize_window()
    yield web_driver
    web_driver.quit()


@pytest.fixture()
def open_main_page(driver):
    driver.get(Urls.MAIN_PAGE)
    return driver


@pytest.fixture()
def registered_user():
    user = register_user()
    yield user
    delete_user(user["access_token"])


@pytest.fixture()
def logged_in_driver(driver, registered_user):
    driver.get(Urls.MAIN_PAGE)
    driver.execute_script(
        "window.localStorage.setItem('accessToken', arguments[0]);",
        registered_user["access_token"],
    )
    driver.execute_script(
        "window.localStorage.setItem('refreshToken', arguments[0]);",
        registered_user["refresh_token"],
    )
    driver.refresh()
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable(MainPageLocators.place_order_button)
    )
    return driver


def pytest_sessionfinish(session, exitstatus):
    try:
        alluredir = session.config.option.allure_report_dir
    except AttributeError:
        return
    if not alluredir:
        return
    os.makedirs(alluredir, exist_ok=True)
    env_path = os.path.join(alluredir, "environment.properties")
    with open(env_path, "w", encoding="utf-8") as file:
        file.write(f"BASE_URL={Urls.BASE_URL}\n")
