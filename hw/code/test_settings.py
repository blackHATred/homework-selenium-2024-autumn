import pytest

from hw.code.base import BaseCase
from hw.code.ui.pages.settings_page import SettingsPage


class TestMainTab(BaseCase):
    @pytest.fixture(autouse=True)
    def setup_settings_page(self, driver):
        self.settings_page = SettingsPage(self.driver)
        self.settings_page.open()

    def test_cancel_button(self):
        # Нажатие кнопки "Отмена" приводит к возвращению всех полей в исходное состояние
        # Сначала введем что-нибудь
        previous_value = self.settings_page.get_field_value('Телефон')
        self.settings_page.clear_field('Телефон')
        self.settings_page.fill_field('Телефон', '+79005553535')
        # Нажимаем "Отмена"
        self.settings_page.click_button('Отмена')
        # Проверяем, что поле вернулось в прошлое состояние
        assert self.settings_page.get_field_value('Телефон') == previous_value

