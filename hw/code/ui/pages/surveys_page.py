from hw.code.conftest import Config
from hw.code.ui.locators.leadforms_and_surveys import SurveyLocators
from hw.code.ui.pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class SurveysPage(BasePage):
    url = Config.VK_ADS_SURVEYS_URL

    def is_element_in_list(self, element_name: str):
        return self.exists(SurveyLocators.LIST_ELEMENT(element_name))

    def archive_all_surveys(self):
        while self.exists(SurveyLocators.ARCHIVE_ELEMENT_BUTTON):
            self.focus(SurveyLocators.ARCHIVE_ELEMENT_BUTTON)
            self.click(SurveyLocators.ARCHIVE_ELEMENT_BUTTON)
            self.click(SurveyLocators.ARCHIVE_ELEMENT_AGREE_BUTTON)
            self.open_and_wait()

    """
    Создание Опроса
    """

    """
    1 шаг
    """

    def click_create_survey_button(self):
        self.click(SurveyLocators.CREATE_SURVEY_BUTTON)
        self.wait().until(EC.visibility_of_element_located(SurveyLocators.NEXT_STEP_BUTTON))

    def click_next_step_button(self, repeats: int = 1):
        for _ in range(repeats):
            self.focus(SurveyLocators.NEXT_STEP_BUTTON)
            self.click(SurveyLocators.NEXT_STEP_BUTTON)

    @property
    def is_survey_creation_modal_opened(self):
        return self.exists(SurveyLocators.NEXT_STEP_BUTTON)

    @property
    def must_fill_field_alerts(self):
        self.wait().until(EC.presence_of_element_located(SurveyLocators.MUST_FILL_FIELD_ALERT))
        return len(self.find_all(SurveyLocators.MUST_FILL_FIELD_ALERT))

    @property
    def too_large_field_alerts(self):
        return len(self.find_all(SurveyLocators.TOO_LARGE_FIELD_ALERT))

    def clear_survey_name(self):
        self.find(SurveyLocators.SURVEY_NAME_INPUT).send_keys('\b' * 100)

    def set_survey_name(self, name: str):
        self.clear_survey_name()
        self.fill_field(SurveyLocators.SURVEY_NAME_INPUT, name)

    def is_survey_name_set(self, name: str):
        return self.get_field_value(SurveyLocators.SURVEY_NAME_INPUT) == name

    def set_company_name(self, name: str):
        self.clear_field(SurveyLocators.COMPANY_NAME_INPUT)
        self.fill_field(SurveyLocators.COMPANY_NAME_INPUT, name)

    def set_header_text(self, text: str):
        self.clear_field(SurveyLocators.HEADER_TEXT_INPUT)
        self.fill_field(SurveyLocators.HEADER_TEXT_INPUT, text)

    def set_description_text(self, text: str):
        self.clear_field(SurveyLocators.DESCRIPTION_TEXT_INPUT)
        self.fill_field(SurveyLocators.DESCRIPTION_TEXT_INPUT, text)

    def set_logo(self, path: str):
        self.click(SurveyLocators.SET_LOGO)
        self.find(SurveyLocators.IMAGE_UPLOAD_INPUT).send_keys(path)
        # Последняя загрузившаяся картинка по умолчанию становится первой в очереди
        self.focus(SurveyLocators.UPLOADED_IMAGE_LIST_ELEMENT)
        self.click(SurveyLocators.UPLOADED_IMAGE_LIST_ELEMENT)
        # может потребоваться время на обработку картинки
        self.wait().until(EC.presence_of_element_located(SurveyLocators.PREVIEW_LOGO))

    @property
    def is_logo_set(self):
        return self.exists(SurveyLocators.PREVIEW_LOGO)

    def is_company_name_set(self, name: str):
        return self.find(SurveyLocators.PREVIEW_COMPANY_NAME).text == name

    def is_header_text_set(self, text: str):
        return self.find(SurveyLocators.PREVIEW_HEADER_TEXT).text == text

    def is_description_text_set(self, text: str):
        return self.find(SurveyLocators.PREVIEW_DESCRIPTION_TEXT).text == text

    @property
    def is_second_step_opened(self):
        # может потребоваться время на обработку картинки при открытии второго шага
        return self.exists(SurveyLocators.QUESTION_ADD_BUTTON, timeout=10)

    """
    2 шаг
    """

    @property
    def is_question_error_shown(self):
        return self.exists(SurveyLocators.QUESTION_ELEMENT_ERROR)

    def set_question_text(self, text: str):
        self.clear_field(SurveyLocators.QUESTION_INPUT)
        self.fill_field(SurveyLocators.QUESTION_INPUT, text)

    def is_question_element_visible(self, text: str):
        return self.exists(SurveyLocators.PREVIEW_QUESTION_HEADER(text))

    def click_add_question_button(self):
        self.click(SurveyLocators.QUESTION_ADD_BUTTON)

    @property
    def question_count(self):
        return len(self.find_all(SurveyLocators.QUESTION_ELEMENT))

    def click_add_variant_button(self):
        self.click(SurveyLocators.QUESTION_ADD_VARIANT_BUTTON)

    @property
    def is_add_variant_button_visible(self):
        return self.exists(SurveyLocators.QUESTION_ADD_VARIANT_BUTTON)

    def delete_variant(self):
        self.focus(SurveyLocators.QUESTION_DELETE_VARIANT_BUTTON)
        self.click(SurveyLocators.QUESTION_DELETE_VARIANT_BUTTON)

    @property
    def is_radio_answer_type_shown(self):
        return self.exists(SurveyLocators.PREVIEW_QUESTION_RADIO_OPTION)

    def click_question_type_dropdown(self):
        self.focus(SurveyLocators.QUESTION_TYPE_DROPDOWN)
        self.click(SurveyLocators.QUESTION_TYPE_DROPDOWN)

    def select_many_answers_option(self):
        self.focus(SurveyLocators.QUESTION_TYPE_MANY_ANSWERS_OPTION)
        self.click(SurveyLocators.QUESTION_TYPE_MANY_ANSWERS_OPTION)

    @property
    def is_checkbox_answer_type_shown(self):
        return self.exists(SurveyLocators.PREVIEW_QUESTION_CHECKBOX_OPTION)

    def select_text_answer_option(self):
        self.focus(SurveyLocators.QUESTION_TYPE_TEXT_ANSWER_OPTION)
        self.click(SurveyLocators.QUESTION_TYPE_TEXT_ANSWER_OPTION)

    @property
    def is_text_answer_type_shown(self):
        return self.exists(SurveyLocators.PREVIEW_QUESTION_TEXTAREA)

    def select_scale_answer_option(self):
        self.focus(SurveyLocators.QUESTION_TYPE_SCALE_ANSWER)
        self.click(SurveyLocators.QUESTION_TYPE_SCALE_ANSWER)

    @property
    def is_scale_answer_type_shown(self):
        return self.exists(SurveyLocators.PREVIEW_QUESTION_SCALE_OPTION)

    def delete_question(self):
        self.focus(SurveyLocators.QUESTION_DELETE_BUTTON)
        self.click(SurveyLocators.QUESTION_DELETE_BUTTON)

    @property
    def is_third_step_opened(self):
        return self.exists(SurveyLocators.RESULTS_HEADER_INPUT)

    """
    3 шаг
    """

    def clear_results_header(self):
        self.find(SurveyLocators.RESULTS_HEADER_INPUT).send_keys('\b' * 1000)

    def clear_results_description(self):
        self.find(SurveyLocators.RESULTS_DESCRIPTION_INPUT).send_keys('\b' * 1000)

    def set_results_header(self, text: str):
        self.clear_results_header()
        self.fill_field(SurveyLocators.RESULTS_HEADER_INPUT, text)

    def set_results_description(self, text: str):
        self.clear_results_description()
        self.fill_field(SurveyLocators.RESULTS_DESCRIPTION_INPUT, text)

    def is_results_header_set(self, text: str):
        return self.exists(SurveyLocators.PREVIEW_RESULTS_HEADER(text))

    def is_results_description_set(self, text: str):
        return self.exists(SurveyLocators.PREVIEW_RESULTS_DESCRIPTION(text))

    """
    ------------------------------------------
    """

    def create_example_survey(self, name: str):
        self.open_and_wait()
        self.click_create_survey_button()
        self.set_survey_name(name)
        self.set_company_name('Company')
        self.set_header_text('Header')
        self.set_description_text('Description')
        self.set_logo(f'{Config.ASSETS_DIR}/img.png')
        self.click_next_step_button()
        self.click_question_type_dropdown()
        self.select_scale_answer_option()
        self.find(SurveyLocators.QUESTION_INPUT).send_keys('Question')
        self.click_next_step_button()
        self.set_results_header('Results header')
        self.set_results_description('Results description')
        self.click_next_step_button()
        self.wait().until(EC.presence_of_element_located(SurveyLocators.LIST_ELEMENT(name)))

    def click_edit_survey(self):
        self.focus(SurveyLocators.EDIT_ELEMENT_BUTTON)
        self.click(SurveyLocators.EDIT_ELEMENT_BUTTON)
        self.wait().until(EC.visibility_of_element_located(SurveyLocators.NEXT_STEP_BUTTON))

    def select_archive_category(self):
        self.click(SurveyLocators.SELECT_CATEGORY_DROPDOWN)
        self.click(SurveyLocators.ARCHIVE_CATEGORY_OPTION)

    def archive_survey(self):
        self.focus(SurveyLocators.ARCHIVE_ELEMENT_BUTTON)
        self.click(SurveyLocators.ARCHIVE_ELEMENT_BUTTON)
        self.click(SurveyLocators.ARCHIVE_ELEMENT_AGREE_BUTTON)
        self.open_and_wait()

    def restore_survey(self, name: str):
        self.focus(SurveyLocators.RESTORE_ELEMENT_BUTTON(name))
        self.click(SurveyLocators.RESTORE_ELEMENT_BUTTON(name))
        self.click(SurveyLocators.RESTORE_ELEMENT_AGREE_BUTTON)
        self.open_and_wait()

    def search_survey(self, name: str):
        self.fill_field(SurveyLocators.SEARCH_INPUT, name)

    def clear_search(self):
        self.find(SurveyLocators.SEARCH_INPUT).send_keys('\b' * 1000)

