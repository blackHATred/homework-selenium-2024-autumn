from hw.code.conftest import Config
from hw.code.ui.locators.settings import SettingsLocators
from hw.code.ui.pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SettingsPage(BasePage):
    url = Config.VK_ADS_SETTINGS_URL
    valid_test_data = {
        'tel': '+9999999999111',
        'email': 'smailcmail@gmail.com',
        'full_name': 'Батовкин Александр Егорович',
        'inn': '744918114973'
    }

    def delete_account(self):
        self.open()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(SettingsLocators.DELETE_ACCOUNT_BUTTON))
        self.click(SettingsLocators.DELETE_ACCOUNT_BUTTON)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(SettingsLocators.DELETE_ACCOUNT_CONFIRM_BUTTON))
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(SettingsLocators.DELETE_ACCOUNT_CONFIRM_BUTTON))
        self.click(SettingsLocators.DELETE_ACCOUNT_CONFIRM_BUTTON)

    def type_valid_data_on_main_tab(self):
        self.clear_field(SettingsLocators.TEL_INPUT)
        self.fill_field(SettingsLocators.TEL_INPUT, SettingsPage.valid_test_data['tel'])
        self.click(SettingsLocators.ADD_EMAIL_BUTTON)
        self.clear_field(SettingsLocators.EMAIL_INPUT_0)
        self.fill_field(SettingsLocators.EMAIL_INPUT_0, SettingsPage.valid_test_data['email'])
        self.clear_field(SettingsLocators.FULL_NAME_INPUT)
        self.fill_field(SettingsLocators.FULL_NAME_INPUT, SettingsPage.valid_test_data['full_name'])
        self.clear_field(SettingsLocators.TIN_INPUT)
        self.fill_field(SettingsLocators.TIN_INPUT, SettingsPage.valid_test_data['inn'])

    def save_settings(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(SettingsLocators.SAVE_BUTTON))
        self.click(SettingsLocators.SAVE_BUTTON)

    def cancel_settings(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(SettingsLocators.CANCEL_BUTTON))
        self.click(SettingsLocators.CANCEL_BUTTON)

