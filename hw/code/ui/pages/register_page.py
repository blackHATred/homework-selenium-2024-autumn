from hw.code.conftest import Config
from hw.code.ui.locators.register import RegisterLocators
from hw.code.ui.pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class RegisterPage(BasePage):
    url = Config.VK_ADS_REGISTER_URL
    labels = {
        'ru_welcome': 'Добро пожаловать в VK Рекламу',
        'en_welcome': 'Welcome to VK Ads',
    }

    def select_ru_lang(self):
        self.click(RegisterLocators.RU_LANG_BUTTON)

    def select_en_lang(self):
        self.click(RegisterLocators.EN_LANG_BUTTON)

    def click_new_cabinet_button(self):
        self.click(RegisterLocators.NEW_CABINET_BUTTON)

    def click_advertiser_option(self):
        self.click(RegisterLocators.ADVERTISER_OPTION)

    def click_agency_option(self):
        self.click(RegisterLocators.AGENCY_OPTION)

    def click_individual_checkbox(self):
        self.click(RegisterLocators.INDIVIDUAL_CHECKBOX)

    def click_agreement_checkbox(self):
        self.find(RegisterLocators.AGREEMENT_CHECKBOX).click()

    def click_create_cabinet_button(self):
        self.click(RegisterLocators.CREATE_CABINET_BUTTON)

    def enter_with_invalid_email(self):
        if not self.find(RegisterLocators.AGREEMENT_INPUT).get_attribute('checked'):
            self.click_agreement_checkbox()
        self.clear_field(RegisterLocators.EMAIL_INPUT)
        self.click_create_cabinet_button()

    def enter_with_invalid_checkbox(self, credentials):
        if self.find(RegisterLocators.AGREEMENT_INPUT).get_attribute('checked'):
            self.click_agreement_checkbox()
        self.fill_field(RegisterLocators.EMAIL_INPUT, credentials['login'])
        self.click_create_cabinet_button()

    def enter_with_valid_data(self, credentials):
        if not self.find(RegisterLocators.AGREEMENT_INPUT).get_attribute('checked'):
            self.click_agreement_checkbox()
        self.fill_field(RegisterLocators.EMAIL_INPUT, credentials['login'])

    def register(self, credentials):
        self.click_new_cabinet_button()
        self.enter_with_valid_data(credentials)
        self.click_create_cabinet_button()
        self.wait(15).until(EC.url_contains(Config.VK_ADS_OVERVIEW_URL))  # на регистрацию может потребоваться время

