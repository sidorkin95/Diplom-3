import os

import pytest

from data.data_user import delete_user, register_user
from driver_factory import DriverFactory
from pages.main_page import MainPage
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
    main_page = MainPage(driver)
    main_page.open_main_page()
    return driver


@pytest.fixture()
def registered_user():
    user = register_user()
    if user is None:
        pytest.fail("Не удалось создать пользователя через API")
    yield user
    delete_user(user["access_token"])


@pytest.fixture()
def logged_in_driver(driver, registered_user):
    main_page = MainPage(driver)
    main_page.open_main_page()
    main_page.authorize_with_tokens(
        registered_user["access_token"],
        registered_user["refresh_token"],
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
        