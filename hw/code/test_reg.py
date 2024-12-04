from hw.code.base import BaseCase
from hw.code.ui.locators.register import RegisterLocators
from selenium.webdriver.support import expected_conditions as EC

from hw.code.fixtures import *


class TestRegistration(BaseCase):
    def test_redirect(self, register_page_with_deleted_user):
        register_page_with_deleted_user.open()
        # У незарегистрированного, но вошедшего через mail ru oauth произойдет редирект на регистрацию
        assert register_page_with_deleted_user.is_opened()

    def test_switch_language(self, register_page_with_deleted_user):
        register_page_with_deleted_user.open_and_wait()
        register_page_with_deleted_user.select_ru_lang()
        assert 'Добро пожаловать в VK Рекламу' == ' '.join(register_page_with_deleted_user.find(RegisterLocators.TITLE).text.split())
        register_page_with_deleted_user.select_en_lang()
        assert 'Welcome to VK Ads' == ' '.join(register_page_with_deleted_user.find(RegisterLocators.TITLE).text.split())
        register_page_with_deleted_user.select_ru_lang()

    def test_new_cabinet_option(self, register_page_with_deleted_user):
        register_page_with_deleted_user.open_and_wait()
        register_page_with_deleted_user.click_new_cabinet_button()
        assert register_page_with_deleted_user.is_opened(url=Config.VK_ADS_REGISTER_NEW_URL)

    def test_checkboxes(self, register_page_with_deleted_user):
        register_page_with_deleted_user.open_and_wait()
        register_page_with_deleted_user.click_new_cabinet_button()
        WebDriverWait(register_page_with_deleted_user.driver, 2).until(EC.url_contains(Config.VK_ADS_REGISTER_NEW_URL))

        # Если выбран чекбокс "агентство", то появляется только один чекбокс "юр. лицо".
        register_page_with_deleted_user.click_agency_option()
        assert register_page_with_deleted_user.find(RegisterLocators.LEGAL_ENTITY_CHECKBOX)

        # Если выбран чекбокс "рекламодатель", то появляются чекбоксы "физ. лицо" и "юр. лицо".
        register_page_with_deleted_user.click_advertiser_option()
        assert register_page_with_deleted_user.find(RegisterLocators.INDIVIDUAL_CHECKBOX)
        assert register_page_with_deleted_user.find(RegisterLocators.LEGAL_ENTITY_CHECKBOX)

        # Если выбрано физическое лицо, то появляются поля "ИНН" и "ФИО".
        register_page_with_deleted_user.click_individual_checkbox()
        assert register_page_with_deleted_user.find(RegisterLocators.TIN_INPUT)
        assert register_page_with_deleted_user.find(RegisterLocators.FULL_NAME_INPUT)

    def test_registration(self, register_page_with_deleted_user, credentials):
        register_page_with_deleted_user.open_and_wait()
        register_page_with_deleted_user.click_new_cabinet_button()
        WebDriverWait(register_page_with_deleted_user.driver, 2).until(EC.url_contains(Config.VK_ADS_REGISTER_NEW_URL))

        # Если не выставлен обязательный чекбокс, то регистрация не пройдет
        register_page_with_deleted_user.enter_with_invalid_checkbox(credentials)
        assert register_page_with_deleted_user.find(RegisterLocators.REQUIRED_FIELD_ALERT)

        # Если не заполнено обязательное поле, то регистрация не пройдет
        register_page_with_deleted_user.enter_with_invalid_email()
        assert register_page_with_deleted_user.find(RegisterLocators.REQUIRED_FIELD_ALERT)

        # Если введены валидные данные и все обязательные поля заполнены, то регистрация должна пройти успешно:
        # произойдет редирект на главную страницу личного кабинета
        register_page_with_deleted_user.enter_with_valid_data(credentials)
        register_page_with_deleted_user.click_create_cabinet_button()
        assert register_page_with_deleted_user.is_opened(url=Config.VK_ADS_OVERVIEW_URL)

