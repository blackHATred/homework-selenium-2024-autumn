import pytest
from selenium.webdriver.support import expected_conditions as EC

from hw.code.base import BaseCase
from hw.code.ui.locators.index import IndexLocators
from hw.code.fixtures import *


class TestAuth(BaseCase):
    @pytest.fixture(autouse=True)
    def setup(self, index_page):
        index_page.open_and_wait()

    def test_need_authenticate(self, index_page, driver):
        # Если пользователь не авторизован, то откроется страница входа
        index_page.click(IndexLocators.GO_TO_CABINET_BUTTON)
        index_page.wait(10).until(EC.url_contains(Config.VK_ID_URL))
        assert Config.VK_ID_URL in driver.current_url

    def test_already_authenticated(self, authorized_user, driver):
        # Если пользователь авторизован, то происходит редирект с главной страницы на ЛК или регистрацию,
        # если ЛК не создан
        authorized_user.wait(10).until(lambda d: d.current_url in (Config.VK_ADS_OVERVIEW_URL, Config.VK_ADS_REGISTER_URL))
        assert driver.current_url in (Config.VK_ADS_OVERVIEW_URL, Config.VK_ADS_REGISTER_URL)


