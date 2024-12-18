import locale
import time
from hw.code.conftest import Config
from hw.code.ui.locators.campaign import CampaignLocators
from hw.code.ui.locators.commerce_center import CommerceCenterLocators
from hw.code.ui.pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from datetime import datetime


class CommerceCenterPage(BasePage):
    url = Config.VK_ADS_COMMERCE_CENTER_URL

    def find_create_catalog_button(self):
        return self.find(CommerceCenterLocators.CREATE_CATALOG_BUTTON, timeout=10)

    def click_create_catalog_button(self):
        self.find(CommerceCenterLocators.CREATE_CATALOG_BUTTON, timeout=10)
        self.click(CommerceCenterLocators.CREATE_CATALOG_BUTTON)

    def find_new_catalog_header(self):
        return self.exists(CommerceCenterLocators.NEW_CATALOG_HEADER, timeout=10)
    
    def fill_field_catalog_name(self, name):
        self.find(CommerceCenterLocators.CATALOG_NAME_INPUT).send_keys(name)
        self.clear_field(CommerceCenterLocators.CATALOG_NAME_INPUT)
        self.fill_field(CommerceCenterLocators.CATALOG_NAME_INPUT, name)

    def find_required_field_name_alert(self):
        return self.exists(CommerceCenterLocators.REQUIRED_FIELD_NAME_ALERT)
    
    def click_manual_option(self):
        self.find(CommerceCenterLocators.MANUAL_OPTION, timeout=10)
        self.click(CommerceCenterLocators.MANUAL_OPTION)

    def find_feed_input(self):
        return self.exists(CommerceCenterLocators.FEED_INPUT, timeout=10)
    
    def upload_feed_file(self, file_path):
        self.find(CommerceCenterLocators.FEED_INPUT).send_keys(file_path)
    
    def click_submit_create_button(self):
        self.find(CommerceCenterLocators.SUBMIT_BUTTON, timeout=10)
        self.click(CommerceCenterLocators.SUBMIT_BUTTON)

    def find_required_field_feed_alert(self):
        return self.exists(CommerceCenterLocators.FIELD_ERROR_ALERT, timeout=10)
    
    def click_cancel_create_button(self):
        self.find(CommerceCenterLocators.CANCEL_BUTTON, timeout=10)
        self.click(CommerceCenterLocators.CANCEL_BUTTON)
        self.wait(5).until(EC.invisibility_of_element_located(CommerceCenterLocators.NEW_CATALOG_HEADER))

    # товары добавляются очень долго, поэтому поставлен большой таймаут
    def find_table_headers(self):
        return self.exists(CommerceCenterLocators.TABLE_HEADERS, timeout=1000)
    
    def delete_catalog_if_exists(self):
        self.open_and_wait()
        if self.exists(CommerceCenterLocators.TABLE_HEADERS):
            self.delete_catalog()
        else:
            self.open_and_wait()

    def delete_catalog(self):
        self.open_and_wait()
        while True:
            catalog_items = self.find_elements(CommerceCenterLocators.CATALOG_ITEMS)
            if not catalog_items:
                break
            for item in catalog_items:
                item.click()
                self.click_settings_button()
                self.click_delete_catalog_button()
                WebDriverWait(self.driver, 5).until(
                    EC.invisibility_of_element_located(CommerceCenterLocators.SETTINGS_HEADER)
                )
                break

    def click_settings_button(self):
        self.find(CommerceCenterLocators.SETTINGS_BUTTON, timeout=10)
        self.click(CommerceCenterLocators.SETTINGS_BUTTON) 

    def click_delete_catalog_button(self):
        self.find(CommerceCenterLocators.DELETE_CATALOG_BUTTON, timeout=10)
        self.click(CommerceCenterLocators.DELETE_CATALOG_BUTTON)
        self.find(CommerceCenterLocators.REMOVE_BUTTON, timeout=10)
        self.click(CommerceCenterLocators.REMOVE_BUTTON)

    # иногда бывает задержка в создании каталога
    def search_catalog(self, name):
        self.find(CommerceCenterLocators.SEARCH_INPUT, timeout=20)
        self.fill_field(CommerceCenterLocators.SEARCH_INPUT, name)

    def create_catalog(self,file_path, name="Каталог"):
        self.open_and_wait()
        self.click_create_catalog_button()
        self.find_new_catalog_header()
        self.click_manual_option()
        self.upload_feed_file(file_path)
        self.fill_field_catalog_name(name)
        self.click_submit_create_button()
        # подождать, пока уберется окно создания
        self.wait(5).until(EC.invisibility_of_element_located(CommerceCenterLocators.NEW_CATALOG_HEADER))
        self.open_and_wait()
        self.find_table_headers()
        # закрытие нокна создания

    def wait_active_catalog(self):
        return self.exists(CommerceCenterLocators.STATUS_ACTIVE, timeout=1000)

    def find_nothing_found_header(self):
        return self.exists(CommerceCenterLocators.NOTHING_FOUND_HEADER, timeout=10)
    
    def click_catalog_item(self):
        self.wait(10).until(EC.presence_of_element_located(CommerceCenterLocators.CATALOG_ITEMS))
        catalog_items = self.find_elements(CommerceCenterLocators.CATALOG_ITEMS)
        for item in catalog_items:
                item.click()
                break
    
    # большой таймаут, так как товары добавляются очень долго
    def find_items_table(self):
        self.find(CommerceCenterLocators.ITEMS_TABLE, timeout=1000)
        return self.exists(CommerceCenterLocators.ITEMS_TABLE, timeout=10)
    
    def search_goods(self, name):
        self.find(CommerceCenterLocators.SEARCH_INPUT, timeout=10)
        self.fill_field(CommerceCenterLocators.SEARCH_INPUT, name)

    def click_add_goods_button(self):
        self.find(CommerceCenterLocators.ADD_GOODS_BUTTON, timeout=10)
        self.click(CommerceCenterLocators.ADD_GOODS_BUTTON)

    def find_settings_panel_header(self):
        return self.exists(CommerceCenterLocators.SETTINGS_PANEL_HEADER, timeout=10)
    
    def click_cancel_add_goods_button(self):
        self.find(CommerceCenterLocators.CANCEL_ADD_GOODS_BUTTON, timeout=10)
        self.click(CommerceCenterLocators.CANCEL_ADD_GOODS_BUTTON)
        self.wait(5).until(EC.invisibility_of_element_located(CommerceCenterLocators.SETTINGS_PANEL_HEADER))

    def click_continue_add_goods_button(self):
        self.find(CommerceCenterLocators.CONTINUE_ADD_GOODS_BUTTON, timeout=10)
        self.click(CommerceCenterLocators.CONTINUE_ADD_GOODS_BUTTON)
        self.wait(5).until(EC.invisibility_of_element_located(CommerceCenterLocators.SETTINGS_PANEL_HEADER))

    def click_current_catalog_button(self):
        self.find(CommerceCenterLocators.CURRENT_CATALOG_BUTTON, timeout=10)
        self.click(CommerceCenterLocators.CURRENT_CATALOG_BUTTON)

    def click_catalog_item_by_name(self, name):
        catalog_item_locator = (By.XPATH, CommerceCenterLocators.CATALOG_ITEM_BY_NAME[1].format(name=name))
        self.find(catalog_item_locator, timeout=10)
        self.click(catalog_item_locator)

    def get_catalog_name(self):
        catalog_name_element = self.find(CommerceCenterLocators.CATALOG_NAME, timeout=10)
        return catalog_name_element.text
    
    def click_groups_tab(self):
        self.find(CommerceCenterLocators.GROUPS_TAB, timeout=10)
        self.click(CommerceCenterLocators.GROUPS_TAB)

    def find_create_group_button(self):
        return self.exists(CommerceCenterLocators.CREATE_GROUP_BUTTON, timeout=10)

    def click_create_group_button(self):
        self.find(CommerceCenterLocators.CREATE_GROUP_BUTTON, timeout=10)
        self.click(CommerceCenterLocators.CREATE_GROUP_BUTTON)

    def find_use_filters_button(self):
        return self.exists(CommerceCenterLocators.USE_FILTERS_BUTTON, timeout=10)
    
    def find_choose_goods_manually_button(self):
        return self.exists(CommerceCenterLocators.CHOOSE_GOODS_MANUALLY_BUTTON, timeout=10)
    
    def click_use_filters_button(self):
        self.find(CommerceCenterLocators.USE_FILTERS_BUTTON, timeout=10)
        self.click(CommerceCenterLocators.USE_FILTERS_BUTTON)
        self.find(CommerceCenterLocators.NEW_GROUP_HEADER, timeout=10)

    def click_choose_goods_manually_button(self):
        self.find(CommerceCenterLocators.CHOOSE_GOODS_MANUALLY_BUTTON, timeout=10)
        self.click(CommerceCenterLocators.CHOOSE_GOODS_MANUALLY_BUTTON)

    def find_new_group_header(self):
        return self.exists(CommerceCenterLocators.NEW_GROUP_HEADER, timeout=10)
    
    def click_add_filter_button(self):
        self.find(CommerceCenterLocators.ADD_FILTER_BUTTON, timeout=10)
        self.click(CommerceCenterLocators.ADD_FILTER_BUTTON)

    def count_filter_condition(self):
        return self.exists(CommerceCenterLocators.FILTER_CONDITION, timeout=10)
    
    def find_field_group_name(self):
        return self.exists(CommerceCenterLocators.GROUP_NAME_INPUT, timeout=10)
    
    def get_group_name(self):
        group_name_element = self.find(CommerceCenterLocators.GROUP_NAME_INPUT, timeout=10)
        return group_name_element.get_attribute("value")

    def click_save_button(self):
        self.find(CommerceCenterLocators.SAVE_BUTTON, timeout=10)
        self.click(CommerceCenterLocators.SAVE_BUTTON)

    def click_cancel_button(self):
        self.find(CommerceCenterLocators.CANCEL_BUTTON, timeout=10)
        self.click(CommerceCenterLocators.CANCEL_BUTTON)
        self.wait(5).until(EC.invisibility_of_element_located(CommerceCenterLocators.NEW_GROUP_HEADER))

    def find_group_item_by_name(self, name):
        group_item_locator = (By.XPATH, CommerceCenterLocators.GROUP_ITEM_BY_NAME[1].format(name=name))
        return self.exists(group_item_locator, timeout=10)
    
    def click_more_button(self):
        self.find(CommerceCenterLocators.MORE_BUTTON, timeout=10)
        self.click(CommerceCenterLocators.MORE_BUTTON)
    
    def click_group_item_by_name(self, name):
        group_item_locator = (By.XPATH, CommerceCenterLocators.GROUP_ITEM_BY_NAME_CONTAINS[1].format(name=name))
        self.find(group_item_locator, timeout=10)
        self.click(group_item_locator)


    def delete_group(self, name):

        if not self.exists((By.XPATH, CommerceCenterLocators.GROUP_ITEM_BY_NAME_CONTAINS[1].format(name=name)), timeout=10):
            return
        self.click_group_item_by_name(name)
        self.click_more_button()
        delete_button_locator = (By.XPATH, CommerceCenterLocators.DELETE_GROUP_BUTTON[1].format(name=name))
        self.find(delete_button_locator, timeout=10)
        self.click(delete_button_locator)
        self.find(CommerceCenterLocators.CONFIRM_DELETE_BUTTON, timeout=10)
        self.click(CommerceCenterLocators.CONFIRM_DELETE_BUTTON)

    def find_search_goods_input(self):
        return self.exists(CommerceCenterLocators.SEARCH_GOODS_INPUT, timeout=10)

    def search_goods_manually(self, name):
        search_input = self.wait(10).until(EC.element_to_be_clickable(CommerceCenterLocators.SEARCH_GOODS_INPUT))
        search_input.clear()
        search_input.send_keys(name)

    
    def find_nothing_found_message_goods(self):
        return self.exists(CommerceCenterLocators.NOTHING_FOUND_MESSAGE, timeout=10)
    
    def add_goods(self):
        self.click_add_manually_goods_button()
        self.fill_add_field()
        self.click_submit_manually_add_goods_button()

    def click_add_manually_goods_button(self):
        self.find(CommerceCenterLocators.ADD_LIST_BUTTON, timeout=10)
        self.click(CommerceCenterLocators.ADD_LIST_BUTTON)

    def fill_add_field(self):
        self.find(CommerceCenterLocators.TEXTAREA_FIELD, timeout=10)
        self.fill_field(CommerceCenterLocators.TEXTAREA_FIELD, "0")

    def click_submit_manually_add_goods_button(self):
        self.find(CommerceCenterLocators.ADD_TO_GROUP_BUTTON, timeout=10)
        self.click(CommerceCenterLocators.ADD_TO_GROUP_BUTTON)

    def click_selected_goods_tab(self):
        self.find(CommerceCenterLocators.SELECTED_GOODS_TAB, timeout=10)
        self.click(CommerceCenterLocators.SELECTED_GOODS_TAB)

    def fill_field_group_name(self, name):
        self.find(CommerceCenterLocators.GROUP_NAME_INPUT, timeout=10)
        self.fill_field(CommerceCenterLocators.GROUP_NAME_INPUT, name)

    def search_group(self, name):
        self.find(CommerceCenterLocators.SEARCH_INPUT_IN_GROUPS, timeout=10)
        self.fill_field(CommerceCenterLocators.SEARCH_INPUT_IN_GROUPS, name)
        return self.exists(CommerceCenterLocators.GROUP_IN_LIST_GROUP, timeout=10)
    
    def wait_for_group_in_list_group(self):
        self.wait(20).until(EC.invisibility_of_element_located(CommerceCenterLocators.NEW_GROUP_HEADER))
        self.find(CommerceCenterLocators.GROUP_IN_LIST_GROUP, timeout=10)


    def click_download_history_tab(self):
        self.find(CommerceCenterLocators.DOWNLOAD_HISTORY_TAB, timeout=10)
        self.click(CommerceCenterLocators.DOWNLOAD_HISTORY_TAB)

    def open_modal(self):
        self.click_refresh_btn()
        return self.find_modal_header()

    def click_refresh_btn(self):
        self.find(CommerceCenterLocators.REFRESH_FILE_BUTTON, timeout=10)
        self.click(CommerceCenterLocators.REFRESH_FILE_BUTTON)

    def find_modal_header(self):
        return self.exists(CommerceCenterLocators.CATALOG_DOWNLOAD_HEADER, timeout=10)    


    