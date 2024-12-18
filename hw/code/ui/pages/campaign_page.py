import locale
import time
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
        self.find(CampaignLocators.CREATE_CAMPAIGN_BUTTON, timeout=10)
        self.click(CampaignLocators.CREATE_CAMPAIGN_BUTTON)

    def find_create_campaign_button(self):
        return self.find(CampaignLocators.CREATE_CAMPAIGN_BUTTON, timeout=10)

    def create_campaign(self):
        #self.click(CampaignLocators.MODAL_CLOSE_BUTTON)
        self.click(CampaignLocators.CREATE_CAMPAIGN_BUTTON)

    def fill_field_campaign_name(self, name):
        #self.wait(10).until(EC.presence_of_element_located(CampaignLocators.CAMPAIGN_NAME_INPUT))
        self.find(CampaignLocators.SEARCH_CAMPAIGN_INPUT, timeout=10)
        self.fill_field(CampaignLocators.SEARCH_CAMPAIGN_INPUT, name)

    def find_draft_rows(self):
        return self.exists(CampaignLocators.DRAFT_ROWS, timeout=10)

    def click_main_checkbox(self):
        self.click(CampaignLocators.MAIN_CHECKBOX)

    def find_delete_button_on_main_page(self):
        return self.find(CampaignLocators.DELETE_BUTTON, timeout=10)
    
    def click_delete_button_on_main_page(self):
        self.click(CampaignLocators.DELETE_BUTTON)

    def find_confirm_button_on_main_page(self):
        return self.exists(CampaignLocators.CONFIRM_DELETE_BUTTON, timeout=10)

    def click_cancel_button(self):
        self.click(CampaignLocators.CANCEL_BUTTON)
        self.wait(10).until(EC.invisibility_of_element_located(CampaignLocators.CONFIRM_DELETE_BUTTON))

    def find_date_picker_button(self):
        return self.find(CampaignLocators.DATE_PICKER_BUTTON, timeout=10)

    def find_date_range_button(self):
        return self.exists(CampaignLocators.APPLY_CALENDAR_BUTTON)

    def find_today_button(self):
        return self.exists(CampaignLocators.TODAY_BUTTON, timeout=10)
    
    def click_today_button(self):
        self.click(CampaignLocators.TODAY_BUTTON)
    
    def click_calendar_cancel_button(self):
        self.click(CampaignLocators.CANCEL_CALENDAR_BUTTON)

    def find_campaign_sidebar_item(self):
        return self.find(CampaignLocators.CAMPAIGN_SIDEBAR_ITEM, timeout=10)
    
    def delete_campaign_if_exists(self):
        self.open_and_wait()
        if self.exists(CampaignLocators.CAMPAIGN_DROPDOWN_BUTTON):
            self.delete_campaign()  
        else:
            pass


    def delete_campaign(self):
        self.open_and_wait()
        self.go_to_draft()
        # выделение кампаний
        if self.exists(CampaignLocators.MAIN_CHECKBOX):
            checkbox = self.find(CampaignLocators.MAIN_CHECKBOX, timeout=10)
            checkbox.click()
            self.click(CampaignLocators.DELETE_BUTTON)
            del_button = self.find(CampaignLocators.CONFIRM_DELETE_BUTTON, timeout=10)
            del_button.click()
            self.wait(10).until(EC.invisibility_of_element_located(CampaignLocators.DRAFT_ROWS))


    def create_draft_campaign(self):
        self.create_group()
        self.click(CampaignLocators.SAVE_AS_DRAFT_BUTTON)

    def go_to_draft(self):
        self.find(CampaignLocators.MAIN_MENU_BUTTON)
        self.open_and_wait()
        self.click(CampaignLocators.CAMPAIGN_DROPDOWN_BUTTON)
        # ожидаем, пока кнопка будет видна
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(CampaignLocators.DRAFTS_BUTTON))
        self.click(CampaignLocators.DRAFTS_BUTTON)

    def click_date_picker_button(self):
        date_picker_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(CampaignLocators.DATE_PICKER_BUTTON)
        )
        date_picker_button.click()

    def compare_dates(self):
        start_date_input = self.find(CampaignLocators.START_DATE_INPUT, timeout=10)
        end_date_input = self.find(CampaignLocators.END_DATE_INPUT, timeout=10)

        start_date_value = start_date_input.get_attribute('value')
        end_date_value = end_date_input.get_attribute('value')

        return start_date_value == end_date_value
    
    def click_apply_calendar_button(self):
        self.click(CampaignLocators.APPLY_CALENDAR_BUTTON)
    
    def compare_saved_date(self):
        date_picker_button = self.find(CampaignLocators.DATE_PICKER_BUTTON, timeout=10)
        date_text_element = date_picker_button.find_element(*CampaignLocators.DATE_TEXT)
        date_text = date_text_element.text

        date_parts = date_text.split()
        day = date_parts[0]

        today = datetime.today()
        today_day = today.day

        # Сравнение даты с сегодняшним числом
        return day == str(today_day)
    
    def get_draft_campaign_count(self):
        drafts = self.find_elements(CampaignLocators.DRAFT_ROWS)
        
        return len(drafts)

    def set_campaign_name(self, new_name):
        self.click(CampaignLocators.CAMPAIGN_NAME_INPUT)
        input_element = self.find(CampaignLocators.CAMPAIGN_NAME_INPUT)
        input_element.clear()
        input_element.send_keys(new_name)
        input_element.send_keys(Keys.ENTER)

    def click_tab_conversion(self):
        self.click(CampaignLocators.TAB_CONVERSION)
        self.click(CampaignLocators.SITE_CONVERSIONS_OPTION)

    def click_tab_branding(self):
        self.click(CampaignLocators.TAB_BRANDING)

    def is_tab_selected_tab_conversion(self):
        return self.find(CampaignLocators.TAB_CONVERSION).get_attribute("aria-selected") == "true"
    
    def is_tab_selected_tab_branding(self):
        return self.find(CampaignLocators.TAB_BRANDING).get_attribute("aria-selected") == "true"
    
    def click_site_conversions_option(self):
        self.click(CampaignLocators.SITE_CONVERSIONS_OPTION)

    def fill_field_budget(self, budget):
        self.wait(10).until(EC.presence_of_element_located(CampaignLocators.BUDGET_INPUT))
        self.fill_field_and_save(CampaignLocators.BUDGET_INPUT, budget)

    def fill_field_site_url(self, url):
        self.wait(10).until(EC.presence_of_element_located(CampaignLocators.SITE_URL_INPUT))
        self.fill_field_and_save(CampaignLocators.SITE_URL_INPUT, url)
    
    def fill_field_and_save(self, locator, value):
        self.wait(10).until(EC.presence_of_element_located(locator))
        self.fill_field(locator, value)
        self.find(locator).send_keys(Keys.ENTER)

    def click_continue_button(self):
        self.click(CampaignLocators.CONTINUE_BUTTON)

    def find_errors(self):
        return self.find(CampaignLocators.ERROR_BUTTON, timeout=10)
    
    def find_group_sidebar_item(self):
        return self.find(CampaignLocators.GROUP_SIDEBAR_ITEM, timeout=10)
    
    def click_group_sidebar_item(self):
        self.click(CampaignLocators.GROUP_SIDEBAR_ITEM)

    def exist_site_url_error(self):
        return self.exists(CampaignLocators.SITE_URL_ERROR)
    
    def exist_budget_error(self):
        return self.exists(CampaignLocators.BUDGET_INPUT_ERROR)
    
    def find_budget_input(self):
        return self.find(CampaignLocators.BUDGET_INPUT, timeout=10)
    
    def click_calendar_button(self):
        self.click(CampaignLocators.SHOW_CALENDAR_BUTTON)

    def find_calendar(self):
        return self.find(CampaignLocators.CALENDAR, timeout=10)
    
    def choose_banner_ad_option(self):
        self.click(CampaignLocators.BANNER_AD_OPTION)
        self.click(CampaignLocators.RADIO_OPTION_SITE)

    def find_advertised_site_label(self):
        return self.find(CampaignLocators.ADVERTISED_SITE_LABEL, timeout=10)

    def find_shows_per_user_label(self):
        return self.find(CampaignLocators.SHOWS_PER_USER_LABEL, timeout=10)

    # Вводим текст в поле и возвращаем обрезанный текст
    def enter_selling_proposition(self, text):
        self.clear_and_send_keys(CampaignLocators.SELLING_PROPOSITION_TEXTAREA, text)
        entered_text = self.find(CampaignLocators.SELLING_PROPOSITION_TEXTAREA).get_attribute("value")
        return entered_text

    def click_next_month_button(self):
        self.click(CampaignLocators.NEXT_MONTH_BUTTON)

    def get_current_month(self):
        return self.find(CampaignLocators.CURRENT_MONTH).text
    
    def clear_and_send_keys(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)
        element.send_keys(Keys.ENTER)
    
    # Для группы:

    def create_group(self):
        self.create_campaign()
        self.click_tab_conversion()
        self.fill_field_and_save(CampaignLocators.SITE_URL_INPUT, 'dd.dd')
        self.fill_field_and_save(CampaignLocators.BUDGET_INPUT, '100')
        self.click(CampaignLocators.CONTINUE_BUTTON)

    def get_group_count(self):
        groups = self.find_elements(CampaignLocators.GROUP_SIDEBAR_ITEM)
        return len(groups)

    def find_set_dates_button(self):
        return self.find(CampaignLocators.SET_DATES_BUTTON, timeout=10) 
    
    def click_set_dates_button(self):
        self.click(CampaignLocators.SET_DATES_BUTTON)

    def find_set_time_button(self):
        return self.find(CampaignLocators.SET_TIME_BUTTON, timeout=10)
    
    def click_set_time_button(self):
        self.click(CampaignLocators.SET_TIME_BUTTON)

    def click_time_active_slot(self):
        self.click(CampaignLocators.TIME_SLOT_ACTIVE)

    def click_time_not_active_slot(self):
        self.click(CampaignLocators.TIME_SLOT_NOT_ACTIVE)

    def find_time_slot_not_active(self):
        return self.find(CampaignLocators.TIME_SLOT_NOT_ACTIVE, timeout=10)
    
    def find_time_slot_active(self):
        return self.find(CampaignLocators.TIME_SLOT_ACTIVE, timeout=10)
    
    def click_add_group_button(self):
        self.click(CampaignLocators.ADD_GROUP_BUTTON)

    def find_region_input(self):
        return self.exists(CampaignLocators.REGION_INPUT, timeout=10)

    def fill_region_input(self, region):
        self.wait(10).until(EC.presence_of_element_located(CampaignLocators.REGION_INPUT))
        self.fill_field(CampaignLocators.REGION_INPUT, region)

    def find_search_tooltip_short_request(self):
        self.wait(10).until(EC.presence_of_element_located(CampaignLocators.SEARCH_TOOLTIP_SHORT_REQUEST))
        return self.find(CampaignLocators.SEARCH_TOOLTIP_SHORT_REQUEST, timeout=10)

    def find_search_tooltip_no_results(self):
        return self.find(CampaignLocators.SEARCH_TOOLTIP_NO_RESULTS, timeout=10)
    
    def click_yaroslavl_option(self):
        self.click(CampaignLocators.YAROSLAVL_OPTION)

    def find_yaroslavl_label(self):
        return self.find(CampaignLocators.YAROSLAVL_LABEL, timeout=10)
    
    def exists_yaroslavl_label(self):
        return self.exists(CampaignLocators.YAROSLAVL_LABEL)
    
    def click_yaroslavl_remove_button(self):
        self.click(CampaignLocators.YAROSLAVL_REMOVE_BUTTON)

    def click_demography_section(self):
        return self.click(CampaignLocators.DEMOGRAPHY_SECTION)
    
    def find_age_warning_banner(self):
        return self.find(CampaignLocators.AGE_WARNING_BANNER, timeout=10)
    
    # Для объявления:

    def click_add_ad_button(self):
        self.click(CampaignLocators.ADD_AD_BUTTON)

    def create_ad(self):
        self.create_group()
        self.fill_region_input('Ярославль')
        self.click_yaroslavl_option()
        self.click(CampaignLocators.CONTINUE_BUTTON)

    def get_ad_count(self):
        ads = self.find_elements((By.XPATH, '//div[@class="MenuItem_cellWrapper__dSQle" and contains(@title, "Объявление")]'))
        # массив в боковой панели
        return len(ads)



    