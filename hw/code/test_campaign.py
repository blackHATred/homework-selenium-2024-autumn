from hw.code.base import BaseCase
from selenium.webdriver.support import expected_conditions as EC

from hw.code.fixtures import *
from hw.code.ui.locators.campaign import CampaignLocators


class TestCampaignMenu(BaseCase):

    def test_first_campaign(self, campaign_page):
        campaign_page.open_and_wait()
        #if campaign_page.find(CampaignLocators.MODAL_CLOSE_BUTTON):
        #    campaign_page.click(CampaignLocators.MODAL_CLOSE_BUTTON)
        assert campaign_page.find_create_campaign_button()
    
    
    def test_create_campaign_button(self, campaign_page):
        campaign_page.open_and_wait()
        #if campaign_page.find(CampaignLocators.MODAL_CLOSE_BUTTON):
        #    campaign_page.click(CampaignLocators.MODAL_CLOSE_BUTTON)
        campaign_page.create_campaign()
        assert campaign_page.is_opened(url=Config.VK_ADS_CAMPAIGN_CREATE_URL)


    def test_campaign_search(self, campaign_page_with_deleted_campaign):
        campaign_page_with_deleted_campaign.open_and_wait()
        campaign_page_with_deleted_campaign.create_draft_campaign()
        campaign_page_with_deleted_campaign.go_to_draft()
        campaign_page_with_deleted_campaign.fill_field_campaign_name('Кампания')
        assert campaign_page_with_deleted_campaign.find_draft_rows()

    
    def test_campaign_select(self, campaign_page_with_deleted_campaign):
        campaign_page_with_deleted_campaign.open_and_wait()
        campaign_page_with_deleted_campaign.create_draft_campaign()
        campaign_page_with_deleted_campaign.go_to_draft()
        # при выделении кампании появляется кнопка удаления
        campaign_page_with_deleted_campaign.click_main_checkbox()
        assert campaign_page_with_deleted_campaign.find_delete_button_on_main_page()
 
    
    def test_campaign_click_on_del_btn(self, campaign_page_with_deleted_campaign):
        campaign_page_with_deleted_campaign.open_and_wait()
        campaign_page_with_deleted_campaign.create_draft_campaign()
        campaign_page_with_deleted_campaign.go_to_draft()
        # при выделении кампании появляется кнопка удаления
        campaign_page_with_deleted_campaign.click_main_checkbox()
        assert campaign_page_with_deleted_campaign.find_delete_button_on_main_page()

        campaign_page_with_deleted_campaign.click_delete_button_on_main_page()
        assert campaign_page_with_deleted_campaign.find_confirm_button_on_main_page()


    def test_campaign_cancel_btn(self, campaign_page_with_deleted_campaign):
        campaign_page_with_deleted_campaign.open_and_wait()
        campaign_page_with_deleted_campaign.create_draft_campaign()
        campaign_page_with_deleted_campaign.go_to_draft()
        # при выделении кампании появляется кнопка удаления
        campaign_page_with_deleted_campaign.click_main_checkbox()
        assert campaign_page_with_deleted_campaign.find_delete_button_on_main_page()

        campaign_page_with_deleted_campaign.click_delete_button_on_main_page()
        campaign_page_with_deleted_campaign.click_cancel_button()
        assert not campaign_page_with_deleted_campaign.find_confirm_button_on_main_page()


    def test_campaign_delete_campaign(self, campaign_page):
        campaign_page.open_and_wait()
        campaign_page.create_draft_campaign()
        # при выделении кампании появляется кнопка удаления
        campaign_page.delete_campaign()
        assert not campaign_page.find_draft_rows()


    def test_campaign_open_calendar(self, campaign_page_with_deleted_campaign):
        campaign_page_with_deleted_campaign.open_and_wait()
        campaign_page_with_deleted_campaign.create_draft_campaign()
        campaign_page_with_deleted_campaign.go_to_draft()
        assert campaign_page_with_deleted_campaign.find_draft_rows()

        campaign_page_with_deleted_campaign.click_date_picker_button()
        assert campaign_page_with_deleted_campaign.find_date_range_button()


    def test_campaign_select_calendar_interval(self, campaign_page_with_deleted_campaign):
        campaign_page_with_deleted_campaign.open_and_wait()
        campaign_page_with_deleted_campaign.create_draft_campaign()
        campaign_page_with_deleted_campaign.go_to_draft()
        assert campaign_page_with_deleted_campaign.find_draft_rows()

        campaign_page_with_deleted_campaign.click_date_picker_button()

        assert campaign_page_with_deleted_campaign.find_today_button()

        campaign_page_with_deleted_campaign.click_today_button()
        assert campaign_page_with_deleted_campaign.compare_dates()


    def test_campaign_cancel_calendar(self, campaign_page_with_deleted_campaign):
        campaign_page_with_deleted_campaign.open_and_wait()
        campaign_page_with_deleted_campaign.create_draft_campaign()
        campaign_page_with_deleted_campaign.go_to_draft()
        assert campaign_page_with_deleted_campaign.find_draft_rows()

        campaign_page_with_deleted_campaign.click_date_picker_button()
        
        assert campaign_page_with_deleted_campaign.find_today_button()

        campaign_page_with_deleted_campaign.click_today_button()
        campaign_page_with_deleted_campaign.click_calendar_cancel_button()
        assert not campaign_page_with_deleted_campaign.find_date_range_button()


    def test_campaign_calendar_save(self, campaign_page_with_deleted_campaign):
        campaign_page_with_deleted_campaign.open_and_wait()
        campaign_page_with_deleted_campaign.create_draft_campaign()
        campaign_page_with_deleted_campaign.go_to_draft()
        assert campaign_page_with_deleted_campaign.find_draft_rows()

        campaign_page_with_deleted_campaign.click_date_picker_button()
        
        assert campaign_page_with_deleted_campaign.find_today_button()

        campaign_page_with_deleted_campaign.click_today_button()
        campaign_page_with_deleted_campaign.click_apply_calendar_button()
        assert campaign_page_with_deleted_campaign.compare_saved_date()

class TestCampaignSettings(BaseCase):

    def test_campaign_in_sidebar(self, campaign_page):
        campaign_page.open_and_wait()
        campaign_page.create_campaign()
        assert campaign_page.find_campaign_sidebar_item()

    def test_tab_conversion(self, campaign_page):
        campaign_page.open_and_wait()
        campaign_page.create_campaign()
        campaign_page.click_tab_conversion()
        assert campaign_page.is_tab_selected_tab_conversion()
    
    
    def test_tab_branding(self, campaign_page):
        campaign_page.open_and_wait()
        campaign_page.create_campaign()
        campaign_page.click_tab_branding()
        assert campaign_page.is_tab_selected_tab_branding()


    def test_footer_error(self, campaign_page):
        campaign_page.open_and_wait()
        campaign_page.create_campaign()
        campaign_page.click_tab_conversion()
        campaign_page.click_site_conversions_option()
        campaign_page.fill_field_site_url('dd')
        campaign_page.click_continue_button()
        assert campaign_page.find_errors()


    def test_footer_continue_button(self, campaign_page):
        campaign_page.open_and_wait()
        campaign_page.create_campaign()
        campaign_page.click_tab_conversion()
        campaign_page.fill_field_site_url('dd.dd')
        campaign_page.fill_field_budget('100')
        campaign_page.click_continue_button()
        assert campaign_page.find_group_sidebar_item()

    # нужно создать кампанию

    def test_footer_save_as_draft(self, campaign_page_with_deleted_campaign):
        campaign_page_with_deleted_campaign.open_and_wait()
        campaign_page_with_deleted_campaign.create_draft_campaign()
        print('campaign created')
        campaign_page_with_deleted_campaign.go_to_draft()
        print('go to draft')
        assert campaign_page_with_deleted_campaign.find_draft_rows()

    
    def test_site_conversions_site_field(self, campaign_page):
        campaign_page.open_and_wait()
        campaign_page.create_campaign()
        campaign_page.click_tab_conversion()
        campaign_page.fill_field_site_url('dd.dd')
        assert not campaign_page.exist_site_url_error()

    def test_site_conversions_budged_field(self, campaign_page):
        campaign_page.open_and_wait()
        campaign_page.create_campaign()
        campaign_page.click_tab_conversion()
        campaign_page.fill_field_site_url('dd.dd')
        campaign_page.fill_field_budget('10')
        assert not campaign_page.exist_budget_error()

    def test_site_conversions_textarea(self, campaign_page):
        campaign_page.open_and_wait()
        campaign_page.create_campaign()
        campaign_page.click_tab_conversion()
        campaign_page.fill_field_site_url('dd.dd')
        long_text = "a" * 350  # Текст длиной 350 символов
        entered_text = campaign_page.enter_selling_proposition(long_text)
        assert len(entered_text) == 300

    def test_start_date_input(self, campaign_page):
        campaign_page.open_and_wait()
        campaign_page.create_campaign()
        campaign_page.click_tab_conversion()
        campaign_page.fill_field_site_url('dd.dd')
        campaign_page.click_calendar_button()
        assert campaign_page.find_calendar()
    
    
    def test_calendar_month(self, campaign_page):
        campaign_page.open_and_wait()
        campaign_page.create_campaign()
        campaign_page.click_tab_conversion()
        campaign_page.fill_field_site_url('dd.dd')
        campaign_page.click_calendar_button()
        campaign_page.find_calendar()
        # Проверим, что месяц не совпадает с текущим
        current_month = campaign_page.get_current_month()
        campaign_page.click_next_month_button()
        next_month = campaign_page.get_current_month()
        assert current_month != next_month



    def test_banner_radio_option_site(self, campaign_page):
        campaign_page.open_and_wait()
        campaign_page.create_campaign()
        campaign_page.click_tab_branding()
        campaign_page.choose_banner_ad_option()
        assert campaign_page.find_advertised_site_label()

class TestGroup(BaseCase):
    

    def test_group_data(self, campaign_page):
        campaign_page.open_and_wait()
        campaign_page.create_group()
        # теперь у нас есть группа
        campaign_page.click_group_sidebar_item()
        assert campaign_page.find_set_dates_button()

    
    def test_group_time(self, campaign_page):
        campaign_page.open_and_wait()
        campaign_page.create_group()
        campaign_page.click_set_dates_button()
        assert campaign_page.find_set_time_button()

    
    def test_group_time_calendar_on(self, campaign_page):
        campaign_page.open_and_wait()
        campaign_page.create_group()
        campaign_page.click_set_time_button()
        campaign_page.click_time_active_slot()
        assert campaign_page.find_time_slot_not_active()

    
    def test_group_time_calendar_off(self, campaign_page):
        campaign_page.open_and_wait()
        campaign_page.create_group()
        campaign_page.click_set_time_button()
        campaign_page.click_time_active_slot()
        assert campaign_page.find_time_slot_not_active()
        campaign_page.click_time_not_active_slot()
        assert campaign_page.find_time_slot_active()

    
    def test_group_count(self, campaign_page):
        campaign_page.open_and_wait()
        campaign_page.create_group()
        new_count = campaign_page.get_group_count()
        assert new_count == 1
    
        campaign_page.click_add_group_button()
        final_count = campaign_page.get_group_count()
        
        assert final_count == new_count + 1

    
    def test_region_input_short_request(self, campaign_page):
        campaign_page.open_and_wait()
        campaign_page.create_group()
        assert campaign_page.find_region_input()
        campaign_page.fill_region_input('a')
        assert campaign_page.find_search_tooltip_short_request()

    
    def test_region_input_no_results(self, campaign_page):
        campaign_page.open_and_wait()
        campaign_page.create_group()
        assert campaign_page.find_region_input()
        campaign_page.fill_region_input('Aaaaaaaa')
        assert campaign_page.find_search_tooltip_no_results()

    
    def test_region_input_choose_option(self, campaign_page):
        campaign_page.open_and_wait()
        campaign_page.create_group()
        assert campaign_page.find_region_input()
        campaign_page.fill_region_input('Ярославль')

        campaign_page.click_yaroslavl_option()
        assert campaign_page.find_yaroslavl_label()


    def test_region_input_remove_option(self, campaign_page):
        campaign_page.open_and_wait()
        campaign_page.create_group()
        campaign_page.fill_region_input('Ярославль')
        campaign_page.click_yaroslavl_option()
        campaign_page.click_yaroslavl_remove_button()
        assert not campaign_page.exists_yaroslavl_label()

class TestAd(BaseCase):

    def test_add_ad(self, campaign_page):
        campaign_page.open_and_wait()
        campaign_page.create_ad()
        # объявление создано
        default_count = campaign_page.get_ad_count()
        assert default_count == 1

        campaign_page.click_add_ad_button()
        new_count = campaign_page.get_ad_count()

        assert new_count == default_count + 1

