from hw.code.base import BaseCase
from selenium.webdriver.support import expected_conditions as EC

from hw.code.fixtures import *
from hw.code.ui.locators.settings import SettingsLocators


class TestMainTab(BaseCase):

    def test_settings_aside_button(self, settings_page, driver):
        # Можно перейти в настройки из любого места в ЛК, где доступно боковое меню
        driver.get(Config.VK_ADS_OVERVIEW_URL)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(SettingsLocators.SETTINGS_BUTTON))
        settings_page.click(SettingsLocators.SETTINGS_BUTTON)
        assert settings_page.is_opened()

    def test_cancel_button(self, settings_page):
        # Вносим изменения в любые поля, чтобы появились кнопки "Сохранить" и "Отмена"
        settings_page.open_and_wait()
        settings_page.type_valid_data_on_main_tab()  # Вносим валидные изменения
        settings_page.fill_field(SettingsLocators.FULL_NAME_INPUT, 'test')
        current_name = settings_page.get_field_value(SettingsLocators.FULL_NAME_INPUT)  # Запоминаем текущее значение
        settings_page.cancel_settings()  # Нажимаем на кнопку "Отмена"
        assert settings_page.get_field_value(SettingsLocators.FULL_NAME_INPUT) != current_name

    def test_save_button(self, settings_page):
        # Вносим изменения в любые поля, чтобы появились кнопки "Сохранить" и "Отмена"
        # Для сохранения данные должны быть валидными
        settings_page.open_and_wait()
        settings_page.type_valid_data_on_main_tab()
        settings_page.save_settings()
        # Обновляем страницу и проверяем, что сохранения прошли успешно
        settings_page.open()
        assert settings_page.get_field_value(SettingsLocators.TEL_INPUT) == SettingsPage.valid_test_data['tel']

    def test_tel_validation(self, settings_page):
        settings_page.open_and_wait()
        # Сначала заполним валидными данными
        settings_page.type_valid_data_on_main_tab()
        # Попробуем перезаписать валидный номер на невалидные варианты
        invalid_cases = [
            '+7(900)5553535',  # Содержит символы помимо цифр и +
            '79005553535',     # Начинается не с +
            '+9999999999',     # Слишком короткий (< 11)
        ]
        for case in invalid_cases:
            settings_page.clear_field(SettingsLocators.TEL_INPUT)
            settings_page.fill_field(SettingsLocators.TEL_INPUT, case)
            settings_page.save_settings()
            assert settings_page.find(SettingsLocators.TEL_ERROR)
            settings_page.cancel_settings()

        # Особый случай: если ввести слишком длинный (> 13) номер, то он сам обрежется
        too_long_case = '+999999999911111'
        settings_page.clear_field(SettingsLocators.TEL_INPUT)
        settings_page.fill_field(SettingsLocators.TEL_INPUT, too_long_case)
        settings_page.save_settings()
        assert settings_page.get_field_value(SettingsLocators.TEL_INPUT) == '+9999999999111'

    def test_email_validation(self, settings_page):
        settings_page.open_and_wait()
        # Сначала заполним валидными данными
        settings_page.type_valid_data_on_main_tab()
        # Попробуем перезаписать валидный email на невалидные варианты
        invalid_cases = [
            'testexample.com',    # Ни одного символа @
            'test@@example.com',  # Больше одного символа @
            '@example.com',       # До символа @ ни одного символа из множества [a-zA-Z0-9]
            'test!@example.com',  # До символа @ символы не из множества [a-zA-Z0-9._-]
            'test@.com',          # Между @ и последней точкой нет ни одного символа из множества [a-zA-Zа-яА-Я0-9]
            'test@exa!mple.com',  # Между @ и последней точкой есть символы не из [a-zA-Zа-яА-Я0-9._-]
            'test@example.c',     # После последней точки нет как минимум двух символов из множества [a-zA-Zа-яА-Я]
        ]
        for case in invalid_cases:
            settings_page.clear_field(SettingsLocators.EMAIL_INPUT_0)
            settings_page.fill_field(SettingsLocators.EMAIL_INPUT_0, case)
            settings_page.save_settings()
            assert settings_page.find(SettingsLocators.EMAIL_ERROR)
            settings_page.cancel_settings()

    def test_email_limit(self, settings_page):
        # Можно добавить не более пяти email адресов
        settings_page.open_and_wait()
        assert not settings_page.find(SettingsLocators.ADD_EMAIL_BUTTON).get_attribute('disabled')
        # Сначала заполним валидными данными
        settings_page.type_valid_data_on_main_tab()
        # Одна почта уже есть, значит можно добавить ещё 4 (заполнять поля необязательно)
        for i in range(4):
            settings_page.click(SettingsLocators.ADD_EMAIL_BUTTON)
        assert settings_page.find(SettingsLocators.ADD_EMAIL_BUTTON).get_attribute('disabled')

    def test_delete_email(self, settings_page):
        settings_page.open_and_wait()
        # Сначала заполним валидными данными
        settings_page.type_valid_data_on_main_tab()
        assert settings_page.find(SettingsLocators.EMAIL_INPUT_0)
        # Теперь удалим добавленный email
        settings_page.click(SettingsLocators.DELETE_EMAIL_BUTTON)
        assert not settings_page.find(SettingsLocators.EMAIL_INPUT_0)

    @pytest.mark.skip
    def test_full_name(self, settings_page):
        pass

    @pytest.mark.skip
    def test_inn(self, settings_page):
        pass

    @pytest.mark.skip
    def test_interface_params(self, settings_page):
        pass


class TestNotificationTab(BaseCase):
    pass


class TestAccessListTab(BaseCase):
    pass


class TestChangesHistoryTab(BaseCase):
    pass

