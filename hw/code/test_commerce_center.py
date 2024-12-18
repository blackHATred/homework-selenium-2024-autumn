from hw.code.base import BaseCase
from selenium.webdriver.support import expected_conditions as EC

from hw.code.fixtures import *
from hw.code.ui.locators.campaign import CampaignLocators

class TestCommerceCenter(BaseCase):

    def test_open_catalog_create_form(self, commerce_center):
        commerce_center.open_and_wait()
        assert commerce_center.find_create_catalog_button()
        commerce_center.click_create_catalog_button()
        assert commerce_center.find_new_catalog_header()

    def test_search_catalog(self, commerce_center):
        file_path = os.path.join(os.path.dirname(__file__), 'assets', 'catalog_products.csv')
        commerce_center.create_catalog(file_path)
        commerce_center.search_catalog("Каталог")
        assert commerce_center.find_table_headers()

    def test_search_nonexistent_catalog(self, commerce_center):
        file_path = os.path.join(os.path.dirname(__file__), 'assets', 'catalog_products.csv')
        commerce_center.create_catalog(file_path)
        commerce_center.search_catalog("!!!")
        assert commerce_center.find_nothing_found_header()

    def test_create_name_catalog(self, commerce_center):
        commerce_center.open_and_wait()
        assert commerce_center.find_create_catalog_button()

        commerce_center.click_create_catalog_button()
        assert commerce_center.find_new_catalog_header()

        commerce_center.fill_field_catalog_name("Каталог")
        assert not commerce_center.find_required_field_name_alert()

    def test_create_catalog_manually_option(self, commerce_center):
        commerce_center.open_and_wait()
        commerce_center.click_create_catalog_button()
        assert commerce_center.find_new_catalog_header()
        commerce_center.click_manual_option()
        assert commerce_center.find_feed_input()

    def test_create_continue_button_with_empty_field(self, commerce_center):
        commerce_center.open_and_wait()
        commerce_center.click_create_catalog_button()
        assert commerce_center.find_new_catalog_header()
        commerce_center.click_manual_option()
        commerce_center.click_submit_create_button()
        assert commerce_center.find_required_field_feed_alert()

    def test_create_continue_button(self, commerce_center):
        commerce_center.open_and_wait()
        commerce_center.click_create_catalog_button()
        assert commerce_center.find_new_catalog_header()
        commerce_center.click_manual_option()
        file_path = os.path.join(os.path.dirname(__file__), 'assets', 'catalog_products.csv')
        commerce_center.upload_feed_file(file_path)
        commerce_center.click_submit_create_button()
        commerce_center.open_and_wait()
        assert commerce_center.find_table_headers()

    def test_create_cancel_button(self, commerce_center):
        commerce_center.open_and_wait()
        commerce_center.click_create_catalog_button()
        assert commerce_center.find_new_catalog_header()
        commerce_center.click_cancel_create_button()
        assert not commerce_center.find_new_catalog_header()

class TestCatalogGoods(BaseCase):

    def test_goods_search(self, commerce_center_page):
        file_path = os.path.join(os.path.dirname(__file__), 'assets', 'catalog_products.csv')
        commerce_center_page.create_catalog(file_path)
        commerce_center_page.click_catalog_item()
        assert commerce_center_page.find_items_table()
        commerce_center_page.search_goods("Худи")
        assert commerce_center_page.find_items_table()

    def test_goods_add_button(self, commerce_center_page):
        file_path = os.path.join(os.path.dirname(__file__), 'assets', 'catalog_products.csv')
        commerce_center_page.create_catalog(file_path)
        commerce_center_page.click_catalog_item()
        commerce_center_page.click_add_goods_button()
        assert commerce_center_page.find_settings_panel_header()

    def test_goods_add_cancel_button(self, commerce_center_page):
        file_path = os.path.join(os.path.dirname(__file__), 'assets', 'catalog_products.csv')
        #commerce_center_page.create_catalog(file_path)
        commerce_center_page.click_catalog_item()
        commerce_center_page.click_add_goods_button()
        assert commerce_center_page.find_settings_panel_header()
        commerce_center_page.click_cancel_add_goods_button()
        assert not commerce_center_page.find_settings_panel_header()

    def test_goods_choose_goods(self, commerce_center_page):
        file_path = os.path.join(os.path.dirname(__file__), 'assets', 'catalog_products.csv')
        commerce_center_page.create_catalog(file_path)
        commerce_center_page.click_catalog_item()
        commerce_center_page.click_current_catalog_button()
        commerce_center_page.click_catalog_item_by_name("Каталог")
        current_catalog_name = commerce_center_page.get_catalog_name()
        assert current_catalog_name == "Каталог"

class TestCatalogGroup(BaseCase):

    def test_group_create_button(self, commerce_center_page):
        file_path = os.path.join(os.path.dirname(__file__), 'assets', 'catalog_products.csv')
        commerce_center_page.create_catalog(file_path)
        commerce_center_page.click_catalog_item()
        commerce_center_page.click_groups_tab()
        assert commerce_center_page.find_create_group_button()

        commerce_center_page.click_create_group_button()
        assert commerce_center_page.find_use_filters_button()
        assert commerce_center_page.find_choose_goods_manually_button()

    def test_group_use_filters(self, commerce_center_page):
        file_path = os.path.join(os.path.dirname(__file__), 'assets', 'catalog_products.csv')
        commerce_center_page.create_catalog(file_path)
        commerce_center_page.click_catalog_item()
        commerce_center_page.click_groups_tab()
        assert commerce_center_page.find_create_group_button()

        commerce_center_page.click_create_group_button()
        assert commerce_center_page.find_use_filters_button()
        commerce_center_page.click_use_filters_button()
        assert commerce_center_page.find_new_group_header()

    def test_group_add_filter(self, commerce_center_page):
        file_path = os.path.join(os.path.dirname(__file__), 'assets', 'catalog_products.csv')
        commerce_center_page.create_catalog(file_path)
        commerce_center_page.click_catalog_item()
        commerce_center_page.click_groups_tab()
        assert commerce_center_page.find_create_group_button()

        commerce_center_page.click_create_group_button()
        assert commerce_center_page.find_use_filters_button()

        commerce_center_page.click_use_filters_button()
        commerce_center_page.click_add_filter_button()
        assert commerce_center_page.count_filter_condition()

    def test_group_save_filter_button(self, commerce_center_page):
        file_path = os.path.join(os.path.dirname(__file__), 'assets', 'catalog_products.csv')
        commerce_center_page.create_catalog(file_path)
        commerce_center_page.click_catalog_item()
        commerce_center_page.click_groups_tab()
        assert commerce_center_page.find_create_group_button()

        commerce_center_page.click_create_group_button()
        assert commerce_center_page.find_use_filters_button()

        commerce_center_page.click_use_filters_button()
        assert commerce_center_page.find_new_group_header()
        assert commerce_center_page.find_field_group_name()

        name = commerce_center_page.get_group_name()
        commerce_center_page.click_save_button()
        assert commerce_center_page.find_group_item_by_name(name)

    
    def test_group_cancel_filter_button(self, commerce_center_page):
        file_path = os.path.join(os.path.dirname(__file__), 'assets', 'catalog_products.csv')
        commerce_center_page.create_catalog(file_path)
        commerce_center_page.click_catalog_item()
        commerce_center_page.click_groups_tab()
        # удалим предыдущие группы
        commerce_center_page.delete_group("Группа")

        assert commerce_center_page.find_create_group_button()

        commerce_center_page.click_create_group_button()
        assert commerce_center_page.find_use_filters_button()

        commerce_center_page.click_use_filters_button()
        commerce_center_page.click_cancel_button()
        assert not commerce_center_page.find_new_group_header()
    

    def test_group_manually_add_button(self, commerce_center_page):
        file_path = os.path.join(os.path.dirname(__file__), 'assets', 'catalog_products.csv')
        commerce_center_page.create_catalog(file_path)
        commerce_center_page.click_catalog_item()
        commerce_center_page.click_groups_tab()
        # удалим предыдущие группы
        commerce_center_page.delete_group("Группа")
        assert commerce_center_page.find_create_group_button()
        commerce_center_page.click_create_group_button()

        assert commerce_center_page.find_choose_goods_manually_button()

        commerce_center_page.click_choose_goods_manually_button()
        assert commerce_center_page.find_new_group_header()


    def test_group_manually_add_search(self, commerce_center_page):
        file_path = os.path.join(os.path.dirname(__file__), 'assets', 'catalog_products.csv')
        commerce_center_page.create_catalog(file_path)
        commerce_center_page.click_catalog_item()
        commerce_center_page.click_groups_tab()
        commerce_center_page.delete_group("Группа")
        assert commerce_center_page.find_create_group_button()
        commerce_center_page.click_create_group_button()
        assert commerce_center_page.find_choose_goods_manually_button()

        commerce_center_page.click_choose_goods_manually_button()
        assert commerce_center_page.find_new_group_header()
        assert commerce_center_page.find_search_goods_input()
        commerce_center_page.search_goods_manually("Худи")
        assert commerce_center_page.find_items_table()


    def test_group_manually_add_search_nonexistent_goods(self, commerce_center_page):
        file_path = os.path.join(os.path.dirname(__file__), 'assets', 'catalog_products.csv')
        commerce_center_page.create_catalog(file_path)
        commerce_center_page.click_catalog_item()
        commerce_center_page.click_groups_tab()
        commerce_center_page.delete_group("Группа")
        assert commerce_center_page.find_create_group_button()
        commerce_center_page.click_create_group_button()
        assert commerce_center_page.find_choose_goods_manually_button()

        commerce_center_page.click_choose_goods_manually_button()
        commerce_center_page.search_goods_manually("!!!")
        assert commerce_center_page.find_nothing_found_message_goods()

    def test_group_manually_add_add_button(self, commerce_center_page):
        file_path = os.path.join(os.path.dirname(__file__), 'assets', 'catalog_products.csv')
        commerce_center_page.create_catalog(file_path)
        commerce_center_page.click_catalog_item()
        commerce_center_page.click_groups_tab()
        commerce_center_page.delete_group("Группа")
        assert commerce_center_page.find_create_group_button()
        commerce_center_page.click_create_group_button()
        assert commerce_center_page.find_choose_goods_manually_button()

        commerce_center_page.click_choose_goods_manually_button()
        commerce_center_page.add_goods()
        commerce_center_page.click_selected_goods_tab()
        assert commerce_center_page.find_items_table()

    def test_group_manually_add_save_button(self, commerce_center_page):
        file_path = os.path.join(os.path.dirname(__file__), 'assets', 'catalog_products.csv')
        commerce_center_page.create_catalog(file_path)
        commerce_center_page.click_catalog_item()
        commerce_center_page.click_groups_tab()
        commerce_center_page.delete_group("Группа")
        assert commerce_center_page.find_create_group_button()
        commerce_center_page.click_create_group_button()
        assert commerce_center_page.find_choose_goods_manually_button()

        commerce_center_page.click_choose_goods_manually_button()
        commerce_center_page.add_goods()
        commerce_center_page.click_save_button()
        commerce_center_page.wait_for_group_in_list_group()
        assert commerce_center_page.find_items_table()

    def test_group_manually_add_cancel_button(self, commerce_center_page):
        file_path = os.path.join(os.path.dirname(__file__), 'assets', 'catalog_products.csv')
        commerce_center_page.create_catalog(file_path)
        commerce_center_page.click_catalog_item()
        commerce_center_page.click_groups_tab()
        commerce_center_page.delete_group("Группа")
        assert commerce_center_page.find_create_group_button()
        commerce_center_page.click_create_group_button()
        assert commerce_center_page.find_choose_goods_manually_button()

        commerce_center_page.click_choose_goods_manually_button()
        commerce_center_page.click_cancel_button()
        assert not commerce_center_page.find_new_group_header()

    def test_group_list_search(self, commerce_center_page):
        file_path = os.path.join(os.path.dirname(__file__), 'assets', 'catalog_products.csv')
        commerce_center_page.create_catalog(file_path)
        commerce_center_page.click_catalog_item()
        commerce_center_page.click_groups_tab()

        assert commerce_center_page.search_group("Все")

class TestCatalogDownload(BaseCase):

    def test_download_history(self, commerce_center_page):
        file_path = os.path.join(os.path.dirname(__file__), 'assets', 'catalog_products.csv')
        commerce_center_page.create_catalog(file_path)
        commerce_center_page.click_catalog_item()
        commerce_center_page.click_download_history_tab()
        assert commerce_center_page.open_modal()


    


