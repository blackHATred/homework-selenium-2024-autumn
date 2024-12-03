import pytest

from hw.code.base import BaseCase
from hw.code.conftest import Config
from hw.code.ui.pages.base_page import BasePage
from hw.code.ui.pages.register_page import RegisterPage

from hw.code.ui.pages.settings_page import SettingsPage
from hw.code.test_auth import get_cookies, credentials


class RegisterData:
    registered: bool = None


class TestRegistration(BaseCase):
    @pytest.fixture(autouse=True)
    def setup(self, driver, get_cookies):
        self.driver = driver
        # Для регистрации нужно сначала войти через VK ID
        for cookie in get_cookies:
            self.driver.add_cookie(cookie)
        self.index_page = BasePage(self.driver)
        self.register_page = RegisterPage(self.driver)
        yield
        self.driver.delete_all_cookies()

    def test_redirect(self):
        # При открытии главной страницы при наличии авторизации происходит редирект на регистрацию, либо ЛК
        self.index_page.open_and_wait()
        # Для идемпотентности тестов удаляем аккаунт, если он зарегистрирован (произошел редирект в ЛК)
        if Config.VK_ADS_OVERVIEW_URL in self.driver.current_url:
            settings_page = SettingsPage(self.driver)
            settings_page.open_and_wait()
            settings_page.delete_account()
            RegisterData.registered = False
            # Теперь пользователь точно не зарегистрирован. Должен произойти редирект на регистрацию
            self.index_page.open_and_wait()

        assert Config.VK_ADS_REGISTER_URL in self.driver.current_url

    def test_switch_language(self):
        pass

    def test_new_cabinet_option(self):
        pass

    def test_checkboxes(self):
        pass

    def test_email_validation(self):
        pass

    def test_phone_number_validation(self):
        pass

    def test_registration(self):
        pass
