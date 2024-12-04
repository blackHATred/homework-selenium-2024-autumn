import pytest
from selenium.webdriver.support import expected_conditions as EC

from hw.code.base import BaseCase
from hw.code.ui.locators.index import IndexLocators
from hw.code.fixtures import *


@pytest.mark.skip
class TestAuth(BaseCase):
    def test_need_authenticate(self, index_page):
        index_page.open_and_wait()
        # Если пользователь не авторизован, то откроется страница входа
        index_page.click(IndexLocators.GO_TO_CABINET_BUTTON)
        WebDriverWait(self.driver, 10).until(EC.url_contains(Config.VK_ID_URL))
        assert Config.VK_ID_URL in self.driver.current_url

    def test_already_authenticated(self, authorized_user):
        # Если пользователь авторизован, то происходит редирект с главной страницы на ЛК или регистрацию,
        # если ЛК не создан
        authorized_user.driver.get(Config.VK_ADS_URL)
        WebDriverWait(self.driver, 10).until(lambda driver: driver.current_url in (Config.VK_ADS_OVERVIEW_URL, Config.VK_ADS_REGISTER_URL))
        assert self.driver.current_url in (Config.VK_ADS_OVERVIEW_URL, Config.VK_ADS_REGISTER_URL)


