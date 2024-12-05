from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from hw.code.conftest import Config
from hw.code.ui.locators.settings import MainTabLocators, NotificationTabLocators, AccessListTabLocators, \
    LogsTabLocators
from hw.code.ui.pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

from hw.code.ui.pages.index_page import IndexPage


class BaseSettingsPage(BasePage):

    def save_settings(self):
        self.wait(3).until(EC.visibility_of_element_located(MainTabLocators.SAVE_BUTTON))
        self.wait(3).until(EC.element_to_be_clickable(MainTabLocators.SAVE_BUTTON))
        self.click(MainTabLocators.SAVE_BUTTON)

    def cancel_settings(self):
        self.wait(3).until(EC.visibility_of_element_located(MainTabLocators.CANCEL_BUTTON))
        self.wait(3).until(EC.element_to_be_clickable(MainTabLocators.CANCEL_BUTTON))
        self.click(MainTabLocators.CANCEL_BUTTON)


class SettingsPage(BaseSettingsPage):
    url = Config.VK_ADS_SETTINGS_URL
    valid_test_data = {
        'tel': '+9999999999111',
        'email': 'alexander-batovkin@mail.ru',
        'full_name': 'Батовкин Александр Егорович',
        'english_name': 'Alexander Batovkin',
        'tin': '744918114973'
    }
    translation = {
        'Общие': 'General',
        'Обзор': 'Overview',
        'Добавить email': 'Add email',
    }

    def delete_account(self):
        self.open_and_wait()
        self.wait(5).until(EC.presence_of_element_located(MainTabLocators.DELETE_ACCOUNT_BUTTON))
        self.click(MainTabLocators.DELETE_ACCOUNT_BUTTON)
        self.wait(5).until(EC.presence_of_element_located(MainTabLocators.DELETE_ACCOUNT_CONFIRM_BUTTON))
        self.wait(5).until(EC.visibility_of_element_located(MainTabLocators.DELETE_ACCOUNT_CONFIRM_BUTTON))
        self.click(MainTabLocators.DELETE_ACCOUNT_CONFIRM_BUTTON)
        IndexPage.vkid_logged_in = False  # После удаления аккаунта пользователь разлогинивается из VK ID

    def type_valid_data_on_main_tab(self):
        self.clear_field(MainTabLocators.TEL_INPUT)
        self.fill_field(MainTabLocators.TEL_INPUT, SettingsPage.valid_test_data['tel'])
        while self.exists(MainTabLocators.EMAIL_INPUT_0, timeout=.2):
            self.click(MainTabLocators.DELETE_EMAIL_BUTTON)
        self.click(MainTabLocators.ADD_EMAIL_BUTTON)
        self.clear_field(MainTabLocators.EMAIL_INPUT_0)
        self.fill_field(MainTabLocators.EMAIL_INPUT_0, SettingsPage.valid_test_data['email'])
        self.clear_field(MainTabLocators.FULL_NAME_INPUT)
        self.fill_field(MainTabLocators.FULL_NAME_INPUT, SettingsPage.valid_test_data['full_name'])
        self.clear_field(MainTabLocators.TIN_INPUT)
        self.fill_field(MainTabLocators.TIN_INPUT, SettingsPage.valid_test_data['tin'])

    def type_full_name(self, full_name):
        self.clear_field(MainTabLocators.FULL_NAME_INPUT)
        self.fill_field(MainTabLocators.FULL_NAME_INPUT, full_name)

    def set_en_lang(self):
        self.click(MainTabLocators.INTERFACE_LANGUAGE_BUTTON)
        self.wait(5).until(EC.visibility_of_element_located(MainTabLocators.INTERFACE_LANGUAGE_EN_OPTION))
        self.click(MainTabLocators.INTERFACE_LANGUAGE_EN_OPTION)
        self.save_settings()
        self.driver.refresh()
        self.wait(5).until(EC.url_matches(Config.VK_ADS_SETTINGS_URL))

    def set_ru_lang(self):
        self.click(MainTabLocators.INTERFACE_LANGUAGE_BUTTON)
        self.wait(5).until(EC.visibility_of_element_located(MainTabLocators.INTERFACE_LANGUAGE_RU_OPTION))
        self.click(MainTabLocators.INTERFACE_LANGUAGE_RU_OPTION)
        self.save_settings()
        self.driver.refresh()
        self.wait(5).until(EC.url_matches(Config.VK_ADS_SETTINGS_URL))


class NotificationSettingsPage(BaseSettingsPage):
    url = Config.VK_ADS_SETTINGS_NOTIFICATIONS_URL
    test_data = {
        'email': 'alexander.batovkin@mail.ru',
    }

    def set_email_notifications(self):
        self.click(NotificationTabLocators.EMAIL_NOTIFICATIONS_BUTTON(self.test_data['email']))


class AccessSettingsPage(BaseSettingsPage):
    url = Config.VK_ADS_SETTINGS_ACCESS_URL
    valid_vk_ads_cabinet_id = '17428371'
    invalid_vk_ads_cabinet_id = '00000000'

    def send_invite_to_invalid_user(self):
        self.clear_field(AccessListTabLocators.USER_ID_INPUT)
        self.fill_field(AccessListTabLocators.USER_ID_INPUT, self.invalid_vk_ads_cabinet_id)
        self.click(AccessListTabLocators.SUBMIT_BUTTON)
        self.wait(2).until(EC.visibility_of_element_located(AccessListTabLocators.SOMETHING_WENT_WRONG_MESSAGE))

    def send_invite_to_valid_user(self):
        self.clear_field(AccessListTabLocators.USER_ID_INPUT)
        self.fill_field(AccessListTabLocators.USER_ID_INPUT, self.valid_vk_ads_cabinet_id)
        self.click(AccessListTabLocators.SUBMIT_BUTTON)

    def send_invite_to_valid_user_again(self):
        self.clear_field(AccessListTabLocators.USER_ID_INPUT)
        self.fill_field(AccessListTabLocators.USER_ID_INPUT, self.valid_vk_ads_cabinet_id)
        self.click(AccessListTabLocators.SUBMIT_BUTTON)
        self.wait(2).until(EC.visibility_of_element_located(AccessListTabLocators.USER_ALREADY_ADDED_MESSAGE))

    def delete_all_invites(self):
        while not self.exists(AccessListTabLocators.EMPTY_ACCESS_LIST_MESSAGE):
            self.focus(AccessListTabLocators.DELETE_INVITE_BUTTON)  # Кнопка не отобразится, пока не наведешь курсор
            self.click(AccessListTabLocators.DELETE_INVITE_BUTTON)
            self.wait(2).until(EC.visibility_of_element_located(AccessListTabLocators.MODAL))
            self.click(AccessListTabLocators.DELETE_INVITE_CONFIRM_BUTTON)


class LogsSettingsPage(BaseSettingsPage):
    url = Config.VK_ADS_SETTINGS_LOGS_URL
    filter_categories = {
        'Тип объекта': ('Кампания', 'Группа объявлений', 'Объявление', 'Бюджет', 'Список офлайн-конверсий'),
        'Что изменилось': (
            'Пополнение бюджета', 'Возврат средств',  # Подкатегория "Бюджет"
            'Кампания создана', 'Кампания восстановлена', 'Название', 'Статус', 'Макс. цена конверсии', 'Бюджет', 'Даты проведения',  # Подкатегория "Кампания"
            'Группа создана', 'Группа удалена', 'Группа восстановлена', 'Название', 'Статус', 'Макс. цена конверсии', 'Бюджет', 'Даты проведения', 'Время показа', 'Регионы показа', 'Пол', 'Возраст', 'Возрастная маркировка', 'Интересы', 'Пользовательские аудитории', 'Места размещения', 'Устройства',  # Подкатегория "Группа"
            'Создан', 'Обновлен', 'Удален'  # Подкатегория "Список офлайн-конверсий"
        ),
        'Автор изменения': ('VK Реклама', )
    }

    def open_filter_modal(self):
        self.focus(LogsTabLocators.FILTER_BUTTON)
        # Делаем n повторов, пока не откроется модальное окно
        # Это нужно потому что иногда модальное окно тупит
        counter = 0
        while counter < Config.CLICK_RETRIES:
            counter += 1
            try:
                self.click(LogsTabLocators.FILTER_BUTTON)
                self.wait(1).until(EC.visibility_of_element_located(LogsTabLocators.FILTER_OPTIONS_CONTAINER))
                return
            except TimeoutException as e:
                if counter == Config.CLICK_RETRIES:
                    raise e

    def delete_all_filters(self):
        while self.exists(LogsTabLocators.APPLIED_FILTER_ELEMENT):
            self.click(LogsTabLocators.FILTER_DELETE_BUTTON)

    def apply_one_filter(self):
        self.open_filter_modal()
        self.click(LogsTabLocators.FILTER_BUTTON)
        self.click(LogsTabLocators.CHECK_ALL_BUTTON)
        self.click(LogsTabLocators.APPLY_FILTER_BUTTON)

    def apply_two_filters(self):
        self.open_filter_modal()
        self.click(LogsTabLocators.CHECK_ALL_BUTTON)
        self.click(LogsTabLocators.FILTER_CATEGORY_WHAT_CHANGED)
        self.click(LogsTabLocators.CHECK_ALL_BUTTON)
        self.click(LogsTabLocators.APPLY_FILTER_BUTTON)

    def get_current_available_filter_options(self) -> list[str]:
        options = []
        for el in self.find_all(LogsTabLocators.FILTER_OPTIONS):
            options.append(el.text.strip())
        return options

    def get_options_check_status(self) -> list[bool]:
        options = []
        for el in self.find_all(LogsTabLocators.OPTION):
            options.append(el.is_selected())
        return options
