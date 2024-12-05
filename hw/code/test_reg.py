from hw.code.base import BaseCase
from hw.code.ui.locators.register import RegisterLocators
from selenium.webdriver.support import expected_conditions as EC

from hw.code.fixtures import *


class TestRegistration(BaseCase):
    @pytest.fixture(autouse=True)
    def setup(self, register_page):
        register_page.open_and_wait()

    def test_redirect(self, register_page):
        # У незарегистрированного, но вошедшего через mail ru oauth произойдет редирект на регистрацию
        # Фикстура register_page гарантирует, что пользователь авторизован, но не зарегистрирован
        assert register_page.is_opened()

    def test_switch_language(self, register_page):
        register_page.select_ru_lang()
        # Надпись может содержать пробелы и переносы строк, поэтому приводим к нужному виду через join
        assert register_page.labels['ru_welcome'] == ' '.join(register_page.find(RegisterLocators.TITLE).text.split())
        register_page.select_en_lang()
        assert register_page.labels['en_welcome'] == ' '.join(register_page.find(RegisterLocators.TITLE).text.split())
        register_page.select_ru_lang()  # Возвращаем язык на русский

    def test_new_cabinet_option(self, register_page):
        register_page.click_new_cabinet_button()
        assert register_page.is_opened(url=Config.VK_ADS_REGISTER_NEW_URL)

    def test_checkboxes(self, register_page, driver):
        register_page.click_new_cabinet_button()
        register_page.wait(2).until(EC.url_contains(Config.VK_ADS_REGISTER_NEW_URL))

        # Если выбран чекбокс "агентство", то появляется только один чекбокс "юр. лицо".
        register_page.click_agency_option()
        assert register_page.find(RegisterLocators.LEGAL_ENTITY_CHECKBOX)

        # Если выбран чекбокс "рекламодатель", то появляются чекбоксы "физ. лицо" и "юр. лицо".
        register_page.click_advertiser_option()
        assert register_page.find(RegisterLocators.INDIVIDUAL_CHECKBOX)
        assert register_page.find(RegisterLocators.LEGAL_ENTITY_CHECKBOX)

        # Если выбрано физическое лицо, то появляются поля "ИНН" и "ФИО".
        register_page.click_individual_checkbox()
        assert register_page.find(RegisterLocators.TIN_INPUT)
        assert register_page.find(RegisterLocators.FULL_NAME_INPUT)

    def test_registration(self, register_page, credentials, driver):
        register_page.click_new_cabinet_button()
        register_page.wait(2).until(EC.url_contains(Config.VK_ADS_REGISTER_NEW_URL))

        # Если не выставлен обязательный чекбокс, то регистрация не пройдет
        register_page.enter_with_invalid_checkbox(credentials)
        assert register_page.find(RegisterLocators.REQUIRED_FIELD_ALERT)

        # Если не заполнено обязательное поле, то регистрация не пройдет
        register_page.enter_with_invalid_email()
        assert register_page.find(RegisterLocators.REQUIRED_FIELD_ALERT)

        # Если введены валидные данные и все обязательные поля заполнены, то регистрация должна пройти успешно:
        # произойдет редирект на главную страницу личного кабинета
        register_page.enter_with_valid_data(credentials)
        register_page.click_create_cabinet_button()
        assert register_page.is_opened(url=Config.VK_ADS_OVERVIEW_URL)

