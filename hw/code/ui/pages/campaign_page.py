from hw.code.conftest import Config
from hw.code.ui.locators.campaign import CampaignLocators
from hw.code.ui.pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from datetime import datetime


class CampaignPage(BasePage):
    url = Config.VK_ADS_CAMPAIGN_URL

    def click_create_campaign_button(self):
        self.click(CampaignLocators.CREATE_CAMPAIGN_BUTTON)

    def create_campaign(self):
        self.click(CampaignLocators.MODAL_CLOSE_BUTTON)
        self.click(CampaignLocators.CREATE_CAMPAIGN_BUTTON)

    def delete_campaign(self):
        self.open_and_wait()
        self.go_to_draft()
        # выделение кампаний
        self.click(CampaignLocators.MAIN_CHECKBOX)
        self.click(CampaignLocators.DELETE_BUTTON)
        self.click(CampaignLocators.CONFIRM_DELETE_BUTTON, timeout=10)


    def create_draft_campaign(self):
        self.create_group()
        self.click(CampaignLocators.SAVE_AS_DRAFT_BUTTON)

    def go_to_draft(self):
        self.find(CampaignLocators.MAIN_MENU_BUTTON)
        self.open_and_wait()
        self.click(CampaignLocators.CAMPAIGN_DROPDOWN_BUTTON)
        self.click(CampaignLocators.DRAFTS_OPTION)

    def compare_dates(self):
        start_date = self.find(CampaignLocators.START_DATE_INPUT).get_attribute("value")
        end_date = self.find(CampaignLocators.END_DATE_INPUT).get_attribute("value")
        return start_date == end_date

    def get_draft_campaign_count(self):
        drafts = self.find_elements(CampaignLocators.DRAFT_ROWS)
        return len(drafts)
    
    def compare_dates(self):
        start_date = self.find(CampaignLocators.START_DATE_INPUT).get_attribute("value")
        date_range_text = self.find(CampaignLocators.DATE_RANGE_TEXT).text

        # Преобразуем дату из поля ввода в формат datetime
        start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")

        # Извлекаем начальную дату из текста диапазона дат
        range_start_date_str = date_range_text.split(' — ')[0]
        range_start_date_obj = datetime.strptime(range_start_date_str, "%d %b %Y")

        return start_date_obj == range_start_date_obj

    def set_campaign_name(self, new_name):
        self.click(CampaignLocators.CAMPAIGN_NAME_INPUT)
        self.fill_field(CampaignLocators.CAMPAIGN_NAME_INPUT, new_name)
        self.find(CampaignLocators.CAMPAIGN_NAME_INPUT).send_keys(Keys.ENTER)

    def verify_campaign_name_in_sidebar(self, campaign_name):
        locator = (By.XPATH, f'//div[@class="MenuItem_cellWrapper__dSQle" and contains(@title, "{campaign_name}")]')
        return self.find(locator)
    
    def click_tab_conversion(self, option):
        self.click(CampaignLocators.TAB_CONVERSION)
        self.click(option)

    def click_tab_branding(self):
        self.click(CampaignLocators.TAB_BRANDING)

    def is_tab_selected(self, tab_locator):
        return self.find(tab_locator).get_attribute("aria-selected") == "true"
    
    def fill_field_and_save(self, locator, value):
        self.fill_field(locator, value)
        self.find(locator).send_keys(Keys.ENTER)

    # Вводим текст в поле и возвращаем обрезанный текст
    def enter_selling_proposition(self, text):
        self.clear_and_send_keys(CampaignLocators.SELLING_PROPOSITION_TEXTAREA, text)
        entered_text = self.find(CampaignLocators.SELLING_PROPOSITION_TEXTAREA).get_attribute("value")
        return entered_text
    
    def click_budget_optimization_checkbox(self):
        self.click(CampaignLocators.BUDGET_OPTIMIZATION_CHECKBOX)

    def select_budget_option(self, option_text):
        self.click(CampaignLocators.BUDGET_SELECT)
        option_locator = (By.XPATH, f'//span[contains(@class, "vkuiCustomSelectInput__title") and text()="{option_text}"]')
        self.click(option_locator)

    def click_next_month_button(self):
        self.click(CampaignLocators.NEXT_MONTH_BUTTON)

    def get_current_month(self):
        return self.find(CampaignLocators.CURRENT_MONTH).text
    
    # Для группы:

    def create_group(self):
        self.create_campaign()
        self.click_tab_conversion(CampaignLocators.SITE_CONVERSIONS_OPTION)
        self.fill_field_and_save(CampaignLocators.SITE_URL_INPUT, 'dd.dd')
        self.fill_field_and_save(CampaignLocators.BUDGET_INPUT, '100')
        self.click(CampaignLocators.CONTINUE_BUTTON)

    def get_group_count(self):
        groups = self.find_elements(CampaignLocators.GROUP_SIDEBAR_ITEM)
        return len(groups)
        
    def select_age_option(self, value):
        option_locator = (By.XPATH, CampaignLocators.AGE_OPTION.format(value))
        self.click(option_locator)
    
    # Для объявления:

    def create_ad(self):
        self.create_group()
        self.fill_field(CampaignLocators.REGION_INPUT, 'Ярославль')
        self.click(CampaignLocators.YAROSLAVL_OPTION)
        self.click(CampaignLocators.CONTINUE_BUTTON)

    def get_ad_count(self):
        ads = self.find_elements((By.XPATH, '//div[@class="MenuItem_cellWrapper__dSQle" and contains(@title, "Объявление")]'))
        # массив в боковой панели
        return len(ads)



    