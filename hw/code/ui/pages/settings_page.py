from selenium.common import TimeoutException

from hw.code.conftest import Config
from hw.code.ui.locators.settings import MainTabLocators, NotificationTabLocators, AccessListTabLocators, \
    LogsTabLocators, AsideMenuSettingsButtonLocators
from hw.code.ui.pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

from hw.code.ui.pages.index_page import IndexPage


class BaseSettingsPage(BasePage):

    def save_settings(self):
        try:
            self.wait(3).until(EC.visibility_of_element_located(MainTabLocators.SAVE_BUTTON))
        except TimeoutException:
            # Если кнопка не отобразилась, то значит, что сохранять нечего
            return
        self.wait(3).until(EC.element_to_be_clickable(MainTabLocators.SAVE_BUTTON))
        self.click(MainTabLocators.SAVE_BUTTON)

    def cancel_settings(self):
        self.wait(3).until(EC.visibility_of_element_located(MainTabLocators.CANCEL_BUTTON))
        self.wait(3).until(EC.element_to_be_clickable(MainTabLocators.CANCEL_BUTTON))
        self.click(MainTabLocators.CANCEL_BUTTON)

    def click_aside_settings_button(self):
        self.click(AsideMenuSettingsButtonLocators.SETTINGS_BUTTON)

    @property
    def cabinet_name_label(self):
        return self.find(MainTabLocators.CABINET_NAME_LABEL).text

    @property
    def general_tab_text(self):
        return self.find(MainTabLocators.GENERAL_TAB).text

    @property
    def overview_button_text(self):
        return self.find(MainTabLocators.OVERVIEW_BUTTON).text


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

    def type_phone_number(self, tel):
        self.clear_field(MainTabLocators.TEL_INPUT)
        self.fill_field(MainTabLocators.TEL_INPUT, tel)

    def type_email(self, email):
        self.clear_field(MainTabLocators.EMAIL_INPUT_0)
        self.fill_field(MainTabLocators.EMAIL_INPUT_0, email)

    def add_email(self):
        self.click(MainTabLocators.ADD_EMAIL_BUTTON)

    @property
    def add_email_button(self):
        return self.find(MainTabLocators.ADD_EMAIL_BUTTON)

    def type_tin(self, tin):
        self.clear_field(MainTabLocators.TIN_INPUT)
        self.fill_field(MainTabLocators.TIN_INPUT, tin)

    def delete_all_emails(self):
        while self.exists(MainTabLocators.EMAIL_INPUT_0):
            self.click(MainTabLocators.DELETE_EMAIL_BUTTON)

    def type_cabinet_name(self, name):
        self.clear_field(MainTabLocators.CABINET_NAME_INPUT)
        self.fill_field(MainTabLocators.CABINET_NAME_INPUT, name)

    def click_hotkeys_button(self):
        self.click(MainTabLocators.HOTKEYS_BUTTON)
        self.wait(5).until(EC.visibility_of_element_located(MainTabLocators.HOTKEYS_MODAL))

    @property
    def hotkeys_modal(self):
        return self.find(MainTabLocators.HOTKEYS_MODAL)

    @property
    def full_name(self):
        return self.get_field_value(MainTabLocators.FULL_NAME_INPUT)

    @property
    def phone_number(self):
        return self.get_field_value(MainTabLocators.TEL_INPUT)

    @property
    def cabinet_name(self):
        return self.get_field_value(MainTabLocators.CABINET_NAME_INPUT)

    @property
    def cabinet_name_input(self):
        return self.find(MainTabLocators.CABINET_NAME_INPUT)

    @property
    def full_name_error(self):
        return self.exists(MainTabLocators.FULL_NAME_ERROR)

    @property
    def phone_number_error(self):
        return self.find(MainTabLocators.TEL_ERROR)

    @property
    def email_error(self):
        return self.find(MainTabLocators.EMAIL_ERROR)

    @property
    def tin_incorrect_error(self):
        return self.exists(MainTabLocators.TIN_INCORRECT_ERROR)

    @property
    def tin_invalid_error(self):
        return self.exists(MainTabLocators.TIN_INVALID_ERROR)

    @property
    def tin_incorrect_len_error(self):
        return self.exists(MainTabLocators.TIN_INCORRECT_LEN_ERROR)

    @property
    def is_add_email_button_available(self):
        return not self.find(MainTabLocators.ADD_EMAIL_BUTTON).get_attribute('disabled')

    @property
    def is_delete_email_button_available(self):
        return self.exists(MainTabLocators.DELETE_EMAIL_BUTTON)

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

    @property
    def warning_message(self):
        return self.exists(NotificationTabLocators.WARNING_MESSAGE)

    @property
    def is_finances_option_available(self):
        return self.find(NotificationTabLocators.FINANCE_OPTION_LABEL).get_attribute('disabled') is None


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
        self.wait(5).until(EC.visibility_of_element_located(AccessListTabLocators.THESE_USERS_HAVE_ACCESS_LABEL))

    def send_invite_to_valid_user_again(self):
        self.clear_field(AccessListTabLocators.USER_ID_INPUT)
        self.fill_field(AccessListTabLocators.USER_ID_INPUT, self.valid_vk_ads_cabinet_id)
        self.click(AccessListTabLocators.SUBMIT_BUTTON)
        self.wait(2).until(EC.visibility_of_element_located(AccessListTabLocators.USER_ALREADY_ADDED_MESSAGE))

    def click_delete_invite_button(self):
        self.focus(AccessListTabLocators.DELETE_INVITE_BUTTON)  # Кнопка не отобразится, пока не наведешь курсор
        self.click(AccessListTabLocators.DELETE_INVITE_BUTTON)
        self.wait(2).until(EC.visibility_of_element_located(AccessListTabLocators.MODAL))

    def click_cancel_delete_invite_button(self):
        self.click(AccessListTabLocators.DELETE_INVITE_CANCEL_BUTTON)

    def click_confirm_delete_invite_button(self):
        self.click(AccessListTabLocators.DELETE_INVITE_CONFIRM_BUTTON)

    def delete_all_invites(self):
        while not self.exists(AccessListTabLocators.EMPTY_ACCESS_LIST_MESSAGE):
            self.click_delete_invite_button()
            self.click_confirm_delete_invite_button()

    @property
    def empty_list_message(self):
        return self.exists(AccessListTabLocators.EMPTY_ACCESS_LIST_MESSAGE)

    def click_invite_button(self):
        self.click(AccessListTabLocators.SEND_INVITE_BUTTON)

    def click_top_invite_button(self):
        self.click(AccessListTabLocators.SEND_INVITE_BUTTON_TOP)

    @property
    def is_modal_opened(self):
        return self.exists(AccessListTabLocators.MODAL)

    @property
    def is_user_id_input_visible(self):
        return self.exists(AccessListTabLocators.USER_ID_INPUT)

    @property
    def is_submit_button_visible(self):
        return self.exists(AccessListTabLocators.SUBMIT_BUTTON)

    @property
    def is_cancel_button_visible(self):
        return self.exists(AccessListTabLocators.CANCEL_BUTTON)

    @property
    def is_delete_invite_button_visible(self):
        return self.exists(AccessListTabLocators.DELETE_INVITE_BUTTON)

    def click_cancel_button(self):
        self.click(AccessListTabLocators.CANCEL_BUTTON)

    def type_user_id(self, user_id):
        self.clear_field(AccessListTabLocators.USER_ID_INPUT)
        self.fill_field(AccessListTabLocators.USER_ID_INPUT, user_id)

    @property
    def user_id_field_value(self):
        return self.get_field_value(AccessListTabLocators.USER_ID_INPUT)

    @property
    def something_went_wrong_message(self):
        return self.exists(AccessListTabLocators.SOMETHING_WENT_WRONG_MESSAGE)

    @property
    def user_already_added_message(self):
        return self.exists(AccessListTabLocators.USER_ALREADY_ADDED_MESSAGE)

    @property
    def these_users_have_access_label(self):
        return self.exists(AccessListTabLocators.THESE_USERS_HAVE_ACCESS_LABEL)

    def click_search_input(self):
        self.click(AccessListTabLocators.SEARCH_INPUT)

    def type_search_input(self, search_text):
        self.click_search_input()
        # Из-за специфики компонента нужно эмулировать нажатие клавиши Backspace вместо использования clear_field
        self.find(AccessListTabLocators.SEARCH_INPUT).send_keys('\b' * 100)
        self.fill_field(AccessListTabLocators.SEARCH_INPUT, search_text)

    @property
    def empty_search_message(self):
        return self.exists(AccessListTabLocators.EMPTY_SEARCH_MESSAGE)


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

    def click_delete_all_filters(self):
        self.click(LogsTabLocators.FILTER_DELETE_ALL_BUTTON)

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

    @property
    def is_filter_category_object_type_visible(self):
        return self.is_visible(LogsTabLocators.FILTER_CATEGORY_OBJECT_TYPE)

    @property
    def is_check_all_button_visible(self):
        return self.is_visible(LogsTabLocators.CHECK_ALL_BUTTON)

    def click_check_all_button(self):
        self.click(LogsTabLocators.CHECK_ALL_BUTTON)

    @property
    def is_uncheck_all_button_visible(self):
        return self.is_visible(LogsTabLocators.UNCHECK_ALL_BUTTON)

    def click_uncheck_all_button(self):
        self.click(LogsTabLocators.UNCHECK_ALL_BUTTON)

    def click_cancel_filter(self):
        self.click(LogsTabLocators.CANCEL_FILTER_BUTTON)

    def click_apply_filter(self):
        self.click(LogsTabLocators.APPLY_FILTER_BUTTON)

    def click_filter_category_object_type_button(self):
        self.click(LogsTabLocators.FILTER_CATEGORY_OBJECT_TYPE)

    def click_filter_category_what_changed_button(self):
        self.click(LogsTabLocators.FILTER_CATEGORY_WHAT_CHANGED)

    def click_filter_category_author_button(self):
        self.click(LogsTabLocators.FILTER_CATEGORY_AUTHOR)

    @property
    def is_applied_filter_element_visible(self):
        return self.is_visible(LogsTabLocators.APPLIED_FILTER_ELEMENT)

    @property
    def is_delete_all_button_visible(self):
        return self.is_visible(LogsTabLocators.FILTER_DELETE_ALL_BUTTON)

    def click_delete_filter(self):
        self.click(LogsTabLocators.FILTER_DELETE_BUTTON)
