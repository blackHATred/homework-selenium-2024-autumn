from hw.code.conftest import Config
from hw.code.ui.locators.settings import MainPage
from hw.code.ui.pages.base_page import BasePage


class SettingsPage(BasePage):
    url = Config.VK_ADS_SETTINGS_URL
    fields = {
        'Телефон': MainPage.TEL_INPUT,
    }
    buttons = {
        'Отмена': MainPage.CANCEL_BUTTON,
    }

    def fill_field(self, field_name: str, value: str):
        self.find(self.fields[field_name]).send_keys(value)

    def clear_field(self, field_name: str):
        self.find(self.fields[field_name]).clear()

    def click_button(self, button_name: str):
        self.click(self.buttons[button_name])

    def get_field_value(self, field_name: str):
        return self.find(self.fields[field_name]).get_attribute('value')


