import pytest

from hw.code.base import BaseCase
from hw.code.ui.pages.settings_page import SettingsPage


@pytest.mark.skip
class TestMainTab(BaseCase):
    @pytest.fixture(autouse=True)
    def setup_settings_page(self, driver):
        self.settings_page = SettingsPage(self.driver)
        self.settings_page.open()

    def test_cancel_button(self):
        pass


class TestNotificationTab(BaseCase):
    pass


class TestAccessListTab(BaseCase):
    pass


class TestChangesHistoryTab(BaseCase):
    pass

