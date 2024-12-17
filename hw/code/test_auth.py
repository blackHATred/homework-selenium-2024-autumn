import pytest

from hw.code.base import BaseCase
from hw.code.fixtures import *


class TestAuth(BaseCase):
    @pytest.fixture(autouse=True)
    def setup(self, index_page):
        index_page.open_and_wait()

    def test_need_authenticate(self, index_page):
        # Если пользователь не авторизован, то откроется страница входа
        index_page.click_go_to_cabinet_button()
        assert index_page.is_opened(Config.VK_ID_URL)

    def test_already_authenticated(self, authorized_user, driver):
        # Если пользователь авторизован, то происходит редирект с главной страницы на ЛК или регистрацию,
        # если ЛК не создан
        assert driver.current_url in (Config.VK_ADS_OVERVIEW_URL, Config.VK_ADS_REGISTER_URL)


