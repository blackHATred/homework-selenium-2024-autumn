from hw.code.base import BaseCase
from selenium.webdriver.support import expected_conditions as EC

from hw.code.fixtures import *
from hw.code.ui.locators.campaign import CampaignLocators


class TestCampaignMenu(BaseCase):

    def test_first_campaign(self, campaign_page):
        campaign_page.open_and_wait()
        campaign_page.click(CampaignLocators.MODAL_CLOSE_BUTTON)
        assert campaign_page.find(CampaignLocators.FIRST_CAMPAIGN_HEADER, timeout=10)
    
    def test_create_campaign_button(self, campaign_page):
        campaign_page.open_and_wait()
        campaign_page.click(CampaignLocators.MODAL_CLOSE_BUTTON)
        campaign_page.click(CampaignLocators.CREATE_CAMPAIGN_BUTTON)
        assert campaign_page.is_opened(url=Config.VK_ADS_CAMPAIGN_CREATE_URL)

    @pytest.mark.skip
    def test_campaign_search(self, campaign_page_with_deleted_campaign):
        campaign_page_with_deleted_campaign.open_and_wait()
        campaign_page_with_deleted_campaign.create_draft_campaign()
        campaign_page_with_deleted_campaign.go_to_draft()
        campaign_page_with_deleted_campaign.fill_field(CampaignLocators.SEARCH_CAMPAIGN_INPUT, 'Кампания')
        assert campaign_page_with_deleted_campaign.find(CampaignLocators.DRAFT_ROWS)

    @pytest.mark.skip
    def test_campaign_select(self, campaign_page_with_deleted_campaign):
        campaign_page_with_deleted_campaign.open_and_wait()
        campaign_page_with_deleted_campaign.create_draft_campaign()
        campaign_page_with_deleted_campaign.go_to_draft()
        # при выделении кампании появляется кнопка удаления
        campaign_page_with_deleted_campaign.click(CampaignLocators.MAIN_CHECKBOX)
        assert campaign_page_with_deleted_campaign.find(CampaignLocators.DELETE_BUTTON)
 
    @pytest.mark.skip
    def test_campaign_click_on_del_btn(self, campaign_page_with_deleted_campaign):
        campaign_page_with_deleted_campaign.open_and_wait()
        campaign_page_with_deleted_campaign.create_draft_campaign()
        campaign_page_with_deleted_campaign.go_to_draft()
        # при выделении кампании появляется кнопка удаления
        campaign_page_with_deleted_campaign.click(CampaignLocators.MAIN_CHECKBOX)
        campaign_page_with_deleted_campaign.click(CampaignLocators.DELETE_BUTTON)
        assert campaign_page_with_deleted_campaign.find(CampaignLocators.CONFIRM_DELETE_BUTTON)

    @pytest.mark.skip
    def test_campaign_cancel_btn(self, campaign_page_with_deleted_campaign):
        campaign_page_with_deleted_campaign.open_and_wait()
        campaign_page_with_deleted_campaign.create_draft_campaign()
        campaign_page_with_deleted_campaign.go_to_draft()
        # при выделении кампании появляется кнопка удаления
        campaign_page_with_deleted_campaign.click(CampaignLocators.MAIN_CHECKBOX)
        campaign_page_with_deleted_campaign.click(CampaignLocators.CANCEL_BUTTON)
        assert not campaign_page_with_deleted_campaign.find(CampaignLocators.CONFIRM_DELETE_BUTTON)

    @pytest.mark.skip
    def test_campaign_delete_campaign(self, campaign_page):
        campaign_page.open_and_wait()
        campaign_page.create_draft_campaign()
        campaign_page.go_to_draft()
        # при выделении кампании появляется кнопка удаления
        campaign_page.delete_campaign()
        assert not campaign_page.find(CampaignLocators.DRAFT_ROWS)

    @pytest.mark.skip
    def test_campaign_open_calendar(self, campaign_page_with_deleted_campaign):
        campaign_page_with_deleted_campaign.open_and_wait()
        campaign_page_with_deleted_campaign.create_draft_campaign()
        campaign_page_with_deleted_campaign.go_to_draft()
        campaign_page_with_deleted_campaign.click(CampaignLocators.DATE_PICKER_BUTTON)
        assert campaign_page_with_deleted_campaign.find(CampaignLocators.DATE_RANGE_BUTTON)

    @pytest.mark.skip
    def test_campaign_select_calendar_interval(self, campaign_page_with_deleted_campaign):
        campaign_page_with_deleted_campaign.open_and_wait()
        campaign_page_with_deleted_campaign.create_draft_campaign()
        campaign_page_with_deleted_campaign.go_to_draft()
        campaign_page_with_deleted_campaign.click(CampaignLocators.TODAY_BUTTON)
        assert campaign_page_with_deleted_campaign.compare_dates()

    @pytest.mark.skip
    def test_campaign_cancel_calendar(self, campaign_page_with_deleted_campaign):
        campaign_page_with_deleted_campaign.open_and_wait()
        campaign_page_with_deleted_campaign.create_draft_campaign()
        campaign_page_with_deleted_campaign.go_to_draft()
        campaign_page_with_deleted_campaign.click(CampaignLocators.TODAY_BUTTON)
        campaign_page_with_deleted_campaign.click(CampaignLocators.CANCEL_CALENDAR_BUTTON)
        assert not campaign_page_with_deleted_campaign.find(CampaignLocators.DATE_RANGE_BUTTON)

    @pytest.mark.skip
    def test_campaign_calendar_save(self, campaign_page_with_deleted_campaign):
        campaign_page_with_deleted_campaign.open_and_wait()
        campaign_page_with_deleted_campaign.create_draft_campaign()
        campaign_page_with_deleted_campaign.go_to_draft()
        campaign_page_with_deleted_campaign.click(CampaignLocators.TODAY_BUTTON)
        assert campaign_page_with_deleted_campaign.compare_dates()

class TestCampaignSettings(BaseCase):

    def test_campaign_in_sidebar(self, campaign_page):
        campaign_page.open_and_wait()
        campaign_page.create_campaign()
        assert campaign_page.find(CampaignLocators.CAMPAIGN_SIDEBAR_ITEM, timeout=10)

    @pytest.mark.skip
    def test_valid_campaign_name(self, campaign_page):
        campaign_page.open_and_wait()
        campaign_page.create_campaign()
        new_campaign_name = "Test"
        campaign_page.set_campaign_name(new_campaign_name)
        assert campaign_page.verify_campaign_name_in_sidebar(new_campaign_name)

    @pytest.mark.skip
    def test_tab_conversion(self, campaign_page):
        campaign_page.open_and_wait()
        campaign_page.create_campaign()
        campaign_page.click_tab_conversion(CampaignLocators.SITE_CONVERSIONS_OPTION)
        assert campaign_page.is_tab_selected(CampaignLocators.TAB_CONVERSION)
    
    @pytest.mark.skip
    def test_tab_branding(self, campaign_page):
        campaign_page.open_and_wait()
        campaign_page.create_campaign()
        campaign_page.click_tab_branding()
        assert campaign_page.is_tab_selected(CampaignLocators.TAB_BRANDING)

    @pytest.mark.skip
    def test_footer_error(self, campaign_page):
        campaign_page.open_and_wait()
        campaign_page.create_campaign()
        campaign_page.click_tab_conversion(CampaignLocators.SITE_CONVERSIONS_OPTION)
        campaign_page.click(CampaignLocators.SITE_CONVERSIONS_OPTION)
        campaign_page.fill_field_and_save(CampaignLocators.SITE_URL_INPUT, 'dd')
        campaign_page.click(CampaignLocators.CONTINUE_BUTTON)
        assert campaign_page.find(CampaignLocators.ERROR_BUTTON)

    @pytest.mark.skip
    def test_footer_continue_button(self, campaign_page):
        campaign_page.open_and_wait()
        campaign_page.create_campaign()
        campaign_page.click_tab_conversion(CampaignLocators.SITE_CONVERSIONS_OPTION)
        campaign_page.fill_field_and_save(CampaignLocators.SITE_URL_INPUT, 'dd.dd')
        campaign_page.fill_field_and_save(CampaignLocators.BUDGET_INPUT, '100')
        campaign_page.click(CampaignLocators.CONTINUE_BUTTON)
        assert campaign_page.find(CampaignLocators.GROUP_SIDEBAR_ITEM)

    @pytest.mark.skip
    def test_footer_save_as_draft(self, campaign_page_with_deleted_campaign):
        campaign_page_with_deleted_campaign.open_and_wait()
        campaign_page_with_deleted_campaign.create_draft_campaign()
        campaign_page_with_deleted_campaign.go_to_draft()
        assert campaign_page_with_deleted_campaign.find(CampaignLocators.DRAFT_ROWS)

    
    @pytest.mark.skip
    def test_site_conversions_site_field(self, campaign_page):
        campaign_page.open_and_wait()
        campaign_page.create_campaign()
        campaign_page.click_tab_conversion(CampaignLocators.SITE_CONVERSIONS_OPTION)
        campaign_page.fill_field_and_save(CampaignLocators.SITE_URL_INPUT, 'dd.dd')
        assert not campaign_page.find(CampaignLocators.SITE_URL_ERROR)

    @pytest.mark.skip
    def test_site_conversions_budged_field(self, campaign_page):
        campaign_page.open_and_wait()
        campaign_page.create_campaign()
        campaign_page.click_tab_conversion(CampaignLocators.SITE_CONVERSIONS_OPTION)
        campaign_page.fill_field_and_save(CampaignLocators.BUDGET_INPUT, '10')
        assert not campaign_page.find(CampaignLocators.BUDGET_INPUT_ERROR)

    @pytest.mark.skip
    def test_site_conversions_textarea(self, campaign_page):
        campaign_page.open_and_wait()
        campaign_page.create_campaign()
        campaign_page.click_tab_conversion(CampaignLocators.SITE_CONVERSIONS_OPTION)
        long_text = "a" * 350  # Текст длиной 350 символов
        entered_text = campaign_page.enter_selling_proposition(long_text)
        assert len(entered_text) == 300

    @pytest.mark.skip
    def test_budget_optimization_checkbox(self, campaign_page):
        campaign_page.open_and_wait()
        campaign_page.create_campaign()
        campaign_page.click_tab_conversion(CampaignLocators.SITE_CONVERSIONS_OPTION)
        campaign_page.click_budget_optimization_checkbox()
        assert not campaign_page.find(CampaignLocators.BUDGET_INPUT)

    @pytest.mark.skip
    def test_select_budget_option(self, campaign_page):
        campaign_page.open_and_wait()
        campaign_page.create_campaign()
        campaign_page.click_tab_conversion(CampaignLocators.SITE_CONVERSIONS_OPTION)
        campaign_page.select_budget_option("за всё время")
        assert campaign_page.find(CampaignLocators.REQUIRED_DATA_FIELD_SYMBOL)

    @pytest.mark.skip
    def test_start_date_input(self, campaign_page):
        campaign_page.open_and_wait()
        campaign_page.create_campaign()
        campaign_page.click_tab_conversion(CampaignLocators.SITE_CONVERSIONS_OPTION)
        campaign_page.click(CampaignLocators.START_DATE_INPUT)
        assert campaign_page.find(CampaignLocators.CALENDAR)
    
    @pytest.mark.skip
    def test_calendar_month(self, campaign_page):
        campaign_page.open_and_wait()
        campaign_page.create_campaign()
        campaign_page.click_tab_conversion(CampaignLocators.SITE_CONVERSIONS_OPTION)
        campaign_page.click(CampaignLocators.START_DATE_INPUT)
        campaign_page.find(CampaignLocators.CALENDAR)
        # Проверим, что месяц не совпадает с текущим
        current_month = campaign_page.get_current_month()
        campaign_page.click_next_month_button()
        next_month = campaign_page.get_current_month()
        assert current_month != next_month


    @pytest.mark.skip
    def test_banner_radio_option_site(self, campaign_page):
        campaign_page.open_and_wait()
        campaign_page.create_campaign()
        campaign_page.click_tab_branding()
        campaign_page.click(CampaignLocators.BANNER_AD_OPTION)
        campaign_page.click(CampaignLocators.RADIO_OPTION_SITE)
        assert self.find(CampaignLocators.ADVERTISED_SITE_LABEL)


    @pytest.mark.skip
    def test_banner_frequency_settings(self, campaign_page):
        campaign_page.open_and_wait()
        campaign_page.create_campaign()
        campaign_page.click_tab_branding()
        campaign_page.click(CampaignLocators.BANNER_AD_OPTION)
        campaign_page.click(CampaignLocators.RADIO_OPTION_SITE)
        campaign_page.fill_field_and_save(CampaignLocators.SITE_URL_INPUT, 'dd.dd')
        campaign_page.click(CampaignLocators.FREQUENCY_SETTINGS_CHECKBOX)
        assert campaign_page.find(CampaignLocators.SHOWS_PER_USER_LABEL)

class TestGroup(BaseCase):
    
    @pytest.mark.skip
    def test_group_data(self, campaign_page):
        campaign_page.open_and_wait()
        campaign_page.create_group()
        # теперь у нас есть группа
        campaign_page.click(CampaignLocators.GROUP_SIDEBAR_ITEM)
        assert campaign_page.find(CampaignLocators.GROUP_DATES_LABEL)

    @pytest.mark.skip
    def test_group_time(self, campaign_page):
        campaign_page.open_and_wait()
        campaign_page.create_group()
        campaign_page.click(CampaignLocators.SET_TIME_BUTTON)
        assert campaign_page.find(CampaignLocators.MY_TIME_BUTTON)

    @pytest.mark.skip
    def test_group_time_calendar_on(self, campaign_page):
        campaign_page.open_and_wait()
        campaign_page.create_group()
        campaign_page.click(CampaignLocators.SET_TIME_BUTTON)
        campaign_page.click(CampaignLocators.TIME_SLOT_ACTIVE)
        assert campaign_page.find(CampaignLocators.TIME_SLOT_NOT_ACTIVE)

    @pytest.mark.skip
    def test_group_time_calendar_off(self, campaign_page):
        campaign_page.open_and_wait()
        campaign_page.create_group()
        campaign_page.click(CampaignLocators.SET_TIME_BUTTON)
        campaign_page.click(CampaignLocators.TIME_SLOT_ACTIVE)
        campaign_page.click(CampaignLocators.TIME_SLOT_NOT_ACTIVE)
        assert campaign_page.find(CampaignLocators.TIME_SLOT_ACTIVE)

    @pytest.mark.skip
    def test_group_count(self, campaign_page):
        campaign_page.open_and_wait()
        campaign_page.create_group()
        new_count = campaign_page.get_group_count()
        assert new_count == 1
    
        campaign_page.click(CampaignLocators.ADD_GROUP_BUTTON)
        final_count = campaign_page.get_group_count()
        
        assert final_count == new_count + 1

    @pytest.mark.skip
    def test_region_input_short_request(self, campaign_page):
        campaign_page.open_and_wait()
        campaign_page.create_group()
        campaign_page.fill_field(CampaignLocators.REGION_INPUT, 'a')
        assert campaign_page.find(CampaignLocators.SEARCH_TOOLTIP_SHORT_REQUEST)

    @pytest.mark.skip
    def test_region_input_no_results(self, campaign_page):
        campaign_page.open_and_wait()
        campaign_page.create_group()
        campaign_page.fill_field(CampaignLocators.REGION_INPUT, 'Aaaaaaaa')
        assert campaign_page.find(CampaignLocators.SEARCH_TOOLTIP_NO_RESULTS)

    @pytest.mark.skip
    def test_region_input_choose_option(self, campaign_page):
        campaign_page.open_and_wait()
        campaign_page.create_group()
        campaign_page.fill_field(CampaignLocators.REGION_INPUT, 'Ярославль')
        campaign_page.click(CampaignLocators.YAROSLAVL_OPTION)
        assert campaign_page.find(CampaignLocators.YAROSLAVL_LABEL)

    @pytest.mark.skip
    def test_region_input_remove_option(self, campaign_page):
        campaign_page.open_and_wait()
        campaign_page.create_group()
        campaign_page.fill_field(CampaignLocators.REGION_INPUT, 'Ярославль')
        campaign_page.click(CampaignLocators.YAROSLAVL_OPTION)
        campaign_page.click(CampaignLocators.YAROSLAVL_REMOVE_BUTTON)
        assert not campaign_page.find(CampaignLocators.YAROSLAVL_LABEL)

    @pytest.mark.skip
    def test_age(self, campaign_page):
        campaign_page.open_and_wait()
        campaign_page.create_group()
        campaign_page.click(CampaignLocators.DEMOGRAPHY_SECTION)
        campaign_page.select_age_option('18+')
        assert campaign_page.find(CampaignLocators.AGE_WARNING_BANNER)

class TestAd(BaseCase):
    @pytest.mark.skip
    def test_add_ad(self, campaign_page):
        campaign_page.open_and_wait()
        campaign_page.create_ad()
        # объявление создано
        default_count = campaign_page.get_ad_count()
        assert default_count == 1

        campaign_page.click(CampaignLocators.ADD_AD_BUTTON)
        new_count = campaign_page.get_ad_count()

        assert new_count == default_count + 1

