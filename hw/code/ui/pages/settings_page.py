from hw.code.conftest import Config
from hw.code.ui.locators.settings import SettingsLocators
from hw.code.ui.pages.base_page import BasePage


class SettingsPage(BasePage):
    url = Config.VK_ADS_SETTINGS_URL
    locators = SettingsLocators

    def delete_account(self):
        self.open()
        self.click(self.locators.DELETE_ACCOUNT_BUTTON)
        self.click(self.locators.DELETE_ACCOUNT_CONFIRM_BUTTON)

