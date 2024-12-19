import time

from hw.code.conftest import Config
from hw.code.ui.locators.leadforms_and_surveys import LeadFormsLocators
from hw.code.ui.pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class LeadFormsPage(BasePage):
    url = Config.VK_ADS_LEADFORMS_URL

    def is_element_in_list(self, element_name: str):
        return self.exists(LeadFormsLocators.LIST_ELEMENT(element_name))

    def click_start_tutorial(self):
        self.click(LeadFormsLocators.START_TUTORIAL_BUTTON)
        self.wait().until(EC.visibility_of_element_located(LeadFormsLocators.WATCH_COURSE_OPTION))

    def click_watch_course_option(self):
        self.click(LeadFormsLocators.WATCH_COURSE_OPTION)
        self.driver.switch_to.window(self.driver.window_handles[1])

    def click_watch_expert_video_option(self):
        self.click(LeadFormsLocators.WATCH_EXPERT_VIDEO_OPTION)

    def click_create_with_hints_option(self):
        self.click(LeadFormsLocators.CREATE_WITH_HINTS_OPTION)

    @property
    def is_tutorial_modal_opened(self):
        return all((self.exists(LeadFormsLocators.WATCH_COURSE_OPTION),
                    self.exists(LeadFormsLocators.WATCH_EXPERT_VIDEO_OPTION),
                    self.exists(LeadFormsLocators.CREATE_WITH_HINTS_OPTION)))

    def close_vk_expert_page(self):
        if self.is_vk_expert_page_opened:
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])

    @property
    def is_vk_expert_page_opened(self):
        self.is_opened(url=Config.VK_EXPERT_URL)
        return Config.VK_EXPERT_URL in self.driver.current_url

    @property
    def is_video_player_opened(self):
        # Для прогрузки видео может потребоваться время
        return self.find(LeadFormsLocators.VIDEO_MODAL, 10)

    @property
    def is_first_hint_opened(self):
        return self.exists(LeadFormsLocators.HINT_1_LABEL)

    @property
    def is_second_hint_opened(self):
        return self.exists(LeadFormsLocators.HINT_2_LABEL)

    def click_next_hint(self):
        self.click(LeadFormsLocators.HINT_CONTINUE_BUTTON)

    def click_previous_hint(self):
        self.click(LeadFormsLocators.HINT_BACK_BUTTON)

    def click_stop_tutorial(self):
        self.click(LeadFormsLocators.HINT_CLOSE)

    @property
    def is_close_hints_modal_opened(self):
        return all((self.is_visible(LeadFormsLocators.CLOSE_HINTS_MODAL_AGREE_BUTTON),
                    self.is_visible(LeadFormsLocators.CLOSE_HINTS_MODAL_CANCEL_BUTTON)))

    def click_cancel_hint_modal(self):
        self.click(LeadFormsLocators.CLOSE_HINTS_MODAL_CANCEL_BUTTON)

    def click_agree_hint_modal(self):
        self.click(LeadFormsLocators.CLOSE_HINTS_MODAL_AGREE_BUTTON)

    def archive_all_lead_forms(self):
        while self.exists(LeadFormsLocators.ARCHIVE_ELEMENT_BUTTON):
            self.focus(LeadFormsLocators.ARCHIVE_ELEMENT_BUTTON)
            self.click(LeadFormsLocators.ARCHIVE_ELEMENT_BUTTON)
            self.click(LeadFormsLocators.ARCHIVE_ELEMENT_AGREE_BUTTON)
            self.wait().until(EC.invisibility_of_element_located(LeadFormsLocators.ARCHIVE_ELEMENT_AGREE_BUTTON))
            self.open_and_wait()

    """
    Создание лид-формы
    """

    """
    1 шаг
    """

    def click_create_leadform_button(self):
        self.click(LeadFormsLocators.CREATE_LEADFORM_BUTTON)
        self.wait().until(EC.visibility_of_element_located(LeadFormsLocators.CANCEL_CREATION_BUTTON))

    def click_next_step_button(self, repeats: int = 1):
        for _ in range(repeats):
            self.focus(LeadFormsLocators.NEXT_STEP_BUTTON)
            self.click(LeadFormsLocators.NEXT_STEP_BUTTON)

    @property
    def is_leadform_creation_modal_opened(self):
        return self.exists(LeadFormsLocators.CANCEL_CREATION_BUTTON)

    def click_cancel_creation_leadform_button(self):
        self.click(LeadFormsLocators.CANCEL_CREATION_BUTTON)
        self.wait().until_not(EC.visibility_of_element_located(LeadFormsLocators.CANCEL_CREATION_BUTTON))

    @property
    def must_fill_field_alerts(self):
        self.wait().until(EC.presence_of_element_located(LeadFormsLocators.MUST_FILL_FIELD_ALERT))
        return len(self.find_all(LeadFormsLocators.MUST_FILL_FIELD_ALERT))

    @property
    def too_large_field_alerts(self):
        return len(self.find_all(LeadFormsLocators.TOO_LARGE_FIELD_ALERT))

    def clear_leadform_name(self):
        self.find(LeadFormsLocators.LEADFORM_NAME_INPUT).send_keys('\b' * 100)

    def set_leadform_name(self, name: str):
        self.clear_field(LeadFormsLocators.LEADFORM_NAME_INPUT)
        self.fill_field(LeadFormsLocators.LEADFORM_NAME_INPUT, name)

    def is_leadform_name_set(self, name: str):
        return self.get_field_value(LeadFormsLocators.LEADFORM_NAME_INPUT) == name

    def set_company_name(self, name: str):
        self.clear_field(LeadFormsLocators.COMPANY_NAME_INPUT)
        self.fill_field(LeadFormsLocators.COMPANY_NAME_INPUT, name)

    def set_header_text(self, text: str):
        self.clear_field(LeadFormsLocators.HEADER_TEXT_INPUT)
        self.fill_field(LeadFormsLocators.HEADER_TEXT_INPUT, text)

    def set_description_text(self, text: str):
        self.clear_field(LeadFormsLocators.DESCRIPTION_TEXT_INPUT)
        self.fill_field(LeadFormsLocators.DESCRIPTION_TEXT_INPUT, text)

    def set_logo(self, path: str):
        self.click(LeadFormsLocators.SET_LOGO)
        self.find(LeadFormsLocators.IMAGE_UPLOAD_INPUT).send_keys(path)
        # Последняя загрузившаяся картинка по умолчанию становится первой в очереди
        self.focus(LeadFormsLocators.UPLOADED_IMAGE_LIST_ELEMENT)
        self.click(LeadFormsLocators.UPLOADED_IMAGE_LIST_ELEMENT)
        # может потребоваться время на обработку картинки
        self.wait(20).until(EC.presence_of_element_located(LeadFormsLocators.IMAGE_CROPPER_CANCEL))
        self.click(LeadFormsLocators.IMAGE_CROPPER_CANCEL)
        self.wait().until(EC.presence_of_element_located(LeadFormsLocators.PREVIEW_LOGO))

    @property
    def is_logo_set(self):
        return self.exists(LeadFormsLocators.PREVIEW_LOGO)

    def is_company_name_set(self, name: str):
        return self.find(LeadFormsLocators.PREVIEW_COMPANY_NAME).text == name

    def is_header_text_set(self, text: str):
        return self.find(LeadFormsLocators.PREVIEW_HEADER_TEXT).text == text

    def is_description_text_set(self, text: str):
        return self.find(LeadFormsLocators.PREVIEW_DESCRIPTION_TEXT).text == text

    @property
    def is_second_step_opened(self):
        # может потребоваться время на обработку картинки при открытии второго шага
        return self.exists(LeadFormsLocators.QUESTIONS_LABEL, timeout=10)

    """
    2 шаг
    """

    def delete_all_contact_data(self):
        self.click(LeadFormsLocators.DELETE_PHONE_CONTACT_OPTION)
        self.click(LeadFormsLocators.DELETE_NAME_CONTACT_OPTION)

    @property
    def is_contacts_error_shown(self):
        return self.exists(LeadFormsLocators.CONTACT_OPTION_REQUIRED_LABEL)

    def click_add_contact_data_button(self):
        self.click(LeadFormsLocators.ADD_CONTACT_OPTION_BUTTON)
        self.wait().until(EC.presence_of_element_located(LeadFormsLocators.CONTACT_OPTION))

    def click_all_contact_data_option(self):
        for option in self.find_all(LeadFormsLocators.CONTACT_OPTION):
            option.click()

    def click_save_contact_data(self):
        # иногда кнопка "Добавить" не кликается с первого раза
        self.focus(LeadFormsLocators.ADD_CONTACT_OPTIONS_AGREE_BUTTON)
        self.click(LeadFormsLocators.ADD_CONTACT_OPTIONS_AGREE_BUTTON)
        self.wait().until_not(EC.visibility_of_element_located(LeadFormsLocators.ADD_CONTACT_OPTIONS_AGREE_BUTTON))

    @property
    def is_preview_contact_name_input_visible(self):
        return self.exists(LeadFormsLocators.PREVIEW_CONTACT_NAME)

    @property
    def is_preview_contact_email_input_visible(self):
        return self.exists(LeadFormsLocators.PREVIEW_CONTACT_EMAIL)

    @property
    def is_preview_contact_phone_input_visible(self):
        return self.exists(LeadFormsLocators.PREVIEW_CONTACT_PHONE)

    @property
    def is_preview_contact_link_input_visible(self):
        return self.exists(LeadFormsLocators.PREVIEW_CONTACT_LINK)

    @property
    def is_preview_contact_birth_date_input_visible(self):
        return self.exists(LeadFormsLocators.PREVIEW_CONTACT_BIRTH_DATE)

    @property
    def is_preview_contact_city_input_visible(self):
        return self.exists(LeadFormsLocators.PREVIEW_CONTACT_CITY)

    def click_add_question_button(self):
        self.click(LeadFormsLocators.ADD_QUESTION_BUTTON)
        self.wait().until(EC.presence_of_element_located(LeadFormsLocators.QUESTION_INPUT))

    @property
    def is_question_error_shown(self):
        return self.exists(LeadFormsLocators.QUESTION_ELEMENT_ERROR)

    def set_question_text(self, text: str):
        self.clear_field(LeadFormsLocators.QUESTION_INPUT)
        self.fill_field(LeadFormsLocators.QUESTION_INPUT, text)

    def is_question_text_set(self, text: str):
        return self.get_field_value(LeadFormsLocators.QUESTION_INPUT) == text

    def is_question_element_visible(self, text: str):
        return self.exists(LeadFormsLocators.PREVIEW_QUESTION_HEADER(text))

    def click_add_variant_button(self):
        self.click(LeadFormsLocators.QUESTION_ADD_VARIANT_BUTTON)

    @property
    def is_add_variant_button_visible(self):
        return self.exists(LeadFormsLocators.QUESTION_ADD_VARIANT_BUTTON)

    def delete_variant(self):
        self.focus(LeadFormsLocators.QUESTION_DELETE_VARIANT_BUTTON)
        self.click(LeadFormsLocators.QUESTION_DELETE_VARIANT_BUTTON)

    @property
    def is_radio_answer_type_shown(self):
        return self.exists(LeadFormsLocators.PREVIEW_QUESTION_RADIO_OPTION)

    def click_question_type_dropdown(self):
        self.focus(LeadFormsLocators.QUESTION_TYPE_DROPDOWN)
        self.click(LeadFormsLocators.QUESTION_TYPE_DROPDOWN)

    def select_many_answers_option(self):
        self.focus(LeadFormsLocators.QUESTION_TYPE_MANY_ANSWERS_OPTION)
        self.click(LeadFormsLocators.QUESTION_TYPE_MANY_ANSWERS_OPTION)

    @property
    def is_checkbox_answer_type_shown(self):
        return self.exists(LeadFormsLocators.PREVIEW_QUESTION_CHECKBOX_OPTION)

    def select_text_answer_option(self):
        self.focus(LeadFormsLocators.QUESTION_TYPE_TEXT_ANSWER_OPTION)
        self.click(LeadFormsLocators.QUESTION_TYPE_TEXT_ANSWER_OPTION)

    @property
    def is_text_answer_type_shown(self):
        return self.exists(LeadFormsLocators.PREVIEW_QUESTION_TEXTAREA)

    def delete_question(self):
        self.focus(LeadFormsLocators.DELETE_QUESTION_BUTTON)
        self.click(LeadFormsLocators.DELETE_QUESTION_BUTTON)

    @property
    def is_third_step_opened(self):
        return self.exists(LeadFormsLocators.RESULTS_LABEL)

    """
    3 шаг
    """

    def clear_results_header(self):
        self.find(LeadFormsLocators.RESULTS_HEADER_INPUT).send_keys('\b' * 1000)

    def clear_results_description(self):
        self.find(LeadFormsLocators.RESULTS_DESCRIPTION_INPUT).send_keys('\b' * 1000)

    def set_results_header(self, text: str):
        self.clear_results_header()
        self.fill_field(LeadFormsLocators.RESULTS_HEADER_INPUT, text)

    def set_results_description(self, text: str):
        self.clear_results_description()
        self.fill_field(LeadFormsLocators.RESULTS_DESCRIPTION_INPUT, text)

    def is_results_header_set(self, text: str):
        return self.exists(LeadFormsLocators.PREVIEW_RESULTS_HEADER(text))

    def is_results_description_set(self, text: str):
        return self.exists(LeadFormsLocators.PREVIEW_RESULTS_DESCRIPTION(text))

    def is_fourth_step_opened(self):
        return self.exists(LeadFormsLocators.SETTINGS_LABEL)

    """
    4 шаг
    """

    def clear_settings_name(self):
        self.find(LeadFormsLocators.SETTINGS_NAME_INPUT).send_keys('\b' * 1000)

    def set_settings_name(self, name: str):
        self.clear_settings_name()
        self.fill_field(LeadFormsLocators.SETTINGS_NAME_INPUT, name)

    def clear_settings_address(self):
        self.find(LeadFormsLocators.SETTINGS_ADDRESS_INPUT).send_keys('\b' * 1000)

    def set_settings_address(self, address: str):
        self.clear_settings_address()
        self.fill_field(LeadFormsLocators.SETTINGS_ADDRESS_INPUT, address)

    """
    ------------------------------------------
    """

    def create_example_lead_form(self, name: str):
        self.open_and_wait()
        self.click_create_leadform_button()
        self.set_leadform_name(name)
        self.set_company_name('Company')
        self.set_header_text('Header')
        self.set_description_text('Description')
        self.set_logo(f'{Config.ASSETS_DIR}/img.png')
        self.click_next_step_button(2)
        self.set_results_header('Results header')
        self.set_results_description('Results description')
        self.click_next_step_button()
        self.set_settings_name('Full name')
        self.set_settings_address('Address')
        self.click_next_step_button()
        self.wait().until(EC.presence_of_element_located(LeadFormsLocators.LIST_ELEMENT(name)))

    def click_edit_lead_form(self):
        self.focus(LeadFormsLocators.EDIT_ELEMENT_BUTTON)
        self.click(LeadFormsLocators.EDIT_ELEMENT_BUTTON)
        self.wait().until(EC.visibility_of_element_located(LeadFormsLocators.CANCEL_CREATION_BUTTON))

    def select_archive_category(self):
        self.click(LeadFormsLocators.SELECT_CATEGORY_DROPDOWN)
        self.click(LeadFormsLocators.ARCHIVE_CATEGORY_OPTION)

    def archive_lead_form(self):
        self.focus(LeadFormsLocators.ARCHIVE_ELEMENT_BUTTON)
        self.click(LeadFormsLocators.ARCHIVE_ELEMENT_BUTTON)
        self.click(LeadFormsLocators.ARCHIVE_ELEMENT_AGREE_BUTTON)
        self.wait().until(EC.invisibility_of_element_located(LeadFormsLocators.ARCHIVE_ELEMENT_AGREE_BUTTON))
        self.open_and_wait()

    def restore_lead_form(self, name: str):
        self.focus(LeadFormsLocators.RESTORE_ELEMENT_BUTTON)
        self.click(LeadFormsLocators.RESTORE_ELEMENT_BUTTON)
        self.click(LeadFormsLocators.RESTORE_ELEMENT_AGREE_BUTTON)
        self.wait().until(EC.invisibility_of_element_located(LeadFormsLocators.RESTORE_ELEMENT_AGREE_BUTTON))
        self.open_and_wait()

    def search_lead_form(self, name: str):
        self.fill_field(LeadFormsLocators.SEARCH_INPUT, name)

    def clear_search(self):
        self.find(LeadFormsLocators.SEARCH_INPUT).send_keys('\b' * 1000)

