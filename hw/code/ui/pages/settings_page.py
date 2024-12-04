from hw.code.conftest import Config
from hw.code.ui.locators.settings import SettingsLocators
from hw.code.ui.pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SettingsPage(BasePage):
    url = Config.VK_ADS_SETTINGS_URL

    def delete_account(self):
        self.open()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(SettingsLocators.DELETE_ACCOUNT_BUTTON))
        self.click(SettingsLocators.DELETE_ACCOUNT_BUTTON)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(SettingsLocators.DELETE_ACCOUNT_CONFIRM_BUTTON))
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(SettingsLocators.DELETE_ACCOUNT_CONFIRM_BUTTON))
        self.click(SettingsLocators.DELETE_ACCOUNT_CONFIRM_BUTTON)

