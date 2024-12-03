import os

import pytest
from dotenv import load_dotenv

from hw.code.base import BaseCase
from hw.code.conftest import Config
from hw.code.ui.locators.auth import AuthLocators
from hw.code.ui.locators.index import IndexLocators
from hw.code.ui.pages.base_page import BasePage


class AuthData:
    cookies: list[dict] = None


@pytest.fixture(scope='session')
def credentials() -> dict:
    load_dotenv()
    return {
        'login': os.getenv('LOGIN'),
        'password': os.getenv('PASSWORD')
    }


@pytest.fixture(scope='function')
def get_cookies(driver, credentials) -> list[dict]:
    if AuthData.cookies is None:
        current_page = BasePage(driver)
        current_page.open()
        current_page.click(IndexLocators.GO_TO_CABINET_BUTTON)
        current_page.click(AuthLocators.MAIL_RU_OAUTH_OPTION_BUTTON)
        current_page.fill_field(AuthLocators.EMAIL_INPUT, credentials['login'])
        current_page.click(AuthLocators.NEXT_BUTTON)
        current_page.click(AuthLocators.AUTH_PROBLEMS_BUTTON)
        current_page.click(AuthLocators.USE_PASSWORD_BUTTON)
        current_page.fill_field(AuthLocators.PASSWORD_INPUT, credentials['password'])
        current_page.click(AuthLocators.SUBMIT_BUTTON)
        current_page.is_opened(url=Config.VK_ADS_CABINET_URL)
        AuthData.cookies = driver.get_cookies()
    return AuthData.cookies


class TestAuth(BaseCase):
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.current_page = BasePage(self.driver)
        self.current_page.open()
        yield
        self.driver.delete_all_cookies()

    def test_need_authenticate(self):
        # Если пользователь не авторизован, то откроется страница входа
        self.current_page.click(IndexLocators.GO_TO_CABINET_BUTTON)
        assert self.current_page.is_opened(url=Config.VK_ID_URL)

    def test_already_authenticated(self, get_cookies):
        # Если пользователь авторизован, то происходит редирект с главной страницы на ЛК или регистрацию
        for cookie in get_cookies:
            self.driver.add_cookie(cookie)
        self.driver.get(Config.VK_ADS_URL)
        assert self.current_page.is_opened(url=Config.VK_ADS_CABINET_URL)


