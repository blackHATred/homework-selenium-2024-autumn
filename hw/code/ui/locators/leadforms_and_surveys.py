from selenium.webdriver.common.by import By


# Так как лидформы и опросы во многом имеют одинаковую структуру, то их локаторы будут описаны в одном файле с
# общим базовым классом

class BaseLocators:
    ARCHIVE_ELEMENT_BUTTON = (By.XPATH, '//button/span[contains(text(), "Архивировать")]')
    ARCHIVE_ELEMENT_AGREE_BUTTON = (By.XPATH, '//button/span/span[contains(text(), "Архивировать")]')
    EDIT_ELEMENT_BUTTON = (By.XPATH, '//button/span[contains(text(), "Редактировать")]')
    # Сложный локатор, но увы, иначе никак
    RESTORE_ELEMENT_BUTTON = lambda n: (By.XPATH, f'//div[contains(@class, "NameCell_wrapper") and h5[text()="{n}"]]/div/div/button/span[contains(text(), "Восстановить")]')
    RESTORE_ELEMENT_AGREE_BUTTON = (By.XPATH, '//button/span/span[contains(text(), "Восстановить")]')
    SEARCH_INPUT = (By.XPATH, '//input[@placeholder="Поиск"]')
    LIST_ELEMENT = lambda n: (By.XPATH, f'//div[h5[@data-testid="lead_form_name__{n}"]]')
    SELECT_CATEGORY_DROPDOWN = (By.XPATH, '//div[contains(@class, "vkuiCustomSelectInput")]')
    ARCHIVE_CATEGORY_OPTION = (By.XPATH, '//div[contains(@title, "В архиве")]')

    # Этому локатору соответствует несколько элементов, при обработке нужно учитывать порядковый номер поля
    MUST_FILL_FIELD_ALERT = (By.XPATH, '//span[@role="alert"]/div[contains(text(), "Обязательное поле")]')
    # Этому локатору соответствует несколько элементов, при обработке нужно учитывать порядковый номер поля
    TOO_LARGE_FIELD_ALERT = (By.XPATH, '//span[@role="alert"]/div[contains(text(), "Превышена максимальная длина поля")]')

    SET_LOGO = (By.XPATH, '//*[@data-testid="set-global-image"]')
    IMAGE_UPLOAD_INPUT = (By.XPATH, '//input[@type="file"]')
    IMAGE_UPLOADING_SPINNER = (By.XPATH, '//div[contains(@class, "ImageItem_blur")]')
    # Этому локатору соответствует несколько элементов, при обработке нужно учитывать порядковый номер изображения
    UPLOADED_IMAGE_LIST_ELEMENT = (By.XPATH, '//*[contains(@class, "ItemList_item")]')
    IMAGE_CROPPER_CANCEL = (By.XPATH, '//div[contains(@class, ImageCropper)]/button/span/span[contains(text(), "Отменить")]')
    CANCEL_CREATION_BUTTON = (By.XPATH, '//*[@data-testid="cancel"]')
    NEXT_STEP_BUTTON = (By.XPATH, '//*[@data-testid="submit"]')


class LeadFormsLocators(BaseLocators):
    START_TUTORIAL_BUTTON = (By.XPATH, '//button/span/span[contains(text(), "Пройти обучение")]')

    # Модальное окно обучения
    WATCH_COURSE_OPTION = (By.XPATH, '//div[@class="vkuiSimpleCell__content"]/span[contains(text(), "Смотреть курс на обучающей платформе")]')
    WATCH_EXPERT_VIDEO_OPTION = (By.XPATH, '//div[@class="vkuiSimpleCell__content"]/span[contains(text(), "Смотреть видеоурок от экспертов VK")]')
    CREATE_WITH_HINTS_OPTION = (By.XPATH, '//div[@class="vkuiSimpleCell__content"]/span[contains(text(), "Создать лид-форму с подсказками")]')
    VIDEO_MODAL = (By.XPATH, '//*[@id="_modal_28"]')

    # Подсказки
    HINT_1_LABEL = (By.XPATH, '//h5[contains(text(), "Шаг 1. Оформление")]')
    HINT_2_LABEL = (By.XPATH, '//h5[contains(text(), "Предпросмотр")]')
    HINT_BACK_BUTTON = (By.XPATH, '//button/span/span[contains(text(), "Назад")]')
    HINT_CONTINUE_BUTTON = (By.XPATH, '//button/span/span[contains(text(), "Далее")]')
    HINT_CLOSE = (By.XPATH, '//div[contains(@class, "RichTooltop_closeBtn")]')
    CLOSE_HINTS_MODAL_AGREE_BUTTON = (By.XPATH, '//button/span/span[contains(text(), "Прервать")]')
    CLOSE_HINTS_MODAL_CANCEL_BUTTON = (By.XPATH, '//button/span/span[contains(text(), "Отмена")]')

    #
    # Создание лид-формы
    #
    CREATE_LEADFORM_BUTTON = (By.XPATH, '//button/span/span[contains(text(), "Создать лид-форму")]')

    # ------------- 1 шаг -------------
    LEADFORM_NAME_INPUT = (By.XPATH, '//input[@placeholder="Название лид-формы"]')
    COMPANY_NAME_INPUT = (By.XPATH, '//input[@placeholder="Название компании"]')
    HEADER_TEXT_INPUT = (By.XPATH, '//input[@placeholder="Текст заголовка"]')
    DESCRIPTION_TEXT_INPUT = (By.XPATH, '//input[@placeholder="Введите описание"]')
    PREVIEW_LOGO = (By.XPATH, '//div[contains(@class, "TitleBlock-module_appLogo")]/img')
    PREVIEW_COMPANY_NAME = (By.XPATH, '//div[contains(@class, "TitleBlock-module_topLineLeft")]/span')
    PREVIEW_HEADER_TEXT = (By.XPATH, '//div[contains(@class, "TitleBlock-module_topLineLeft")]/h2')
    PREVIEW_DESCRIPTION_TEXT = (By.XPATH, '//div[contains(@class, "TitleBlock-module_topLineLeft")]/h4')

    # ------------- 2 шаг -------------
    QUESTIONS_LABEL = (By.XPATH, '//h4[contains(text(), "Вопросы")]')
    DELETE_PHONE_CONTACT_OPTION = (By.XPATH, '//button[@data-id="phone"]')
    DELETE_NAME_CONTACT_OPTION = (By.XPATH, '//button[@data-id="first_name"]')
    CONTACT_OPTION_REQUIRED_LABEL = (By.XPATH, '//p[contains(text(), "Минимальное количество полей: 1")]')
    ADD_CONTACT_OPTION_BUTTON = (By.XPATH, '//button/span/span[contains(text(), "Добавить контактные данные")]')
    # Этому локатору соответствует несколько элементов, при обработке нужно учитывать порядковый номер поля
    CONTACT_OPTION = (By.XPATH, '//label[contains(@class, "vkuiCheckbox")]')
    ADD_CONTACT_OPTIONS_AGREE_BUTTON = (By.XPATH, '//div[contains(@class, "ModalManagerPage_footer")]/button/span/span[contains(text(), "Добавить")]')
    PREVIEW_CONTACT_NAME = (By.XPATH, '//*[contains(@class, "vkuiFormField")]/input[@placeholder="Введите имя"]')
    PREVIEW_CONTACT_EMAIL = (By.XPATH, '//*[contains(@class, "vkuiFormField")]/input[@placeholder="Введите email"]')
    PREVIEW_CONTACT_PHONE = (By.XPATH, '//*[contains(@class, "vkuiFormField")]/input[@type="tel"]')
    PREVIEW_CONTACT_LINK = (By.XPATH, '//*[contains(@class, "vkuiFormField")]/input[@placeholder="Введите ссылку на соц. сеть"]')
    PREVIEW_CONTACT_BIRTH_DATE = (By.XPATH, '//*[contains(@class, "vkuiFormField")]/span[contains(@class, "vkuiDateInput")]')
    PREVIEW_CONTACT_CITY = (By.XPATH, '//*[contains(@class, "vkuiFormField")]/input[@placeholder="Введите город"]')
    ADD_QUESTION_BUTTON = (By.XPATH, '//button/span/span[contains(text(), "Добавить вопрос")]')
    DELETE_QUESTION_BUTTON = (By.XPATH, '//div[contains(@class, "Question")]/button[@aria-label="Remove"]')
    QUESTION_ELEMENT = (By.XPATH, '//div[contains(@class, "Question") and contains(text(), "Вопрос")]')
    QUESTION_ELEMENT_ERROR = (By.XPATH, '//div[contains(@class, "Question_error")]')
    QUESTION_INPUT = (By.XPATH, '//textarea[@placeholder="Напишите вопрос"]')
    QUESTION_TYPE_DROPDOWN = (By.XPATH, '//div[contains(@class, "HintSelector_hintSelectorButton")]')
    QUESTION_TYPE_ONE_ANSWER_OPTION = (By.XPATH, '//span[contains(text(), "Выбор одного ответа")]')
    QUESTION_TYPE_MANY_ANSWERS_OPTION = (By.XPATH, '//span[contains(text(), "Выбор нескольких ответов")]')
    QUESTION_TYPE_TEXT_ANSWER_OPTION = (By.XPATH, '//span[contains(text(), "Ответ в произвольной форме")]')
    QUESTION_ADD_VARIANT_BUTTON = (By.XPATH, '//button/span/span[contains(text(), "Добавить ответ")]')
    QUESTION_VARIANT_INPUT = (By.XPATH, '//input[@placeholder="Введите ответ"]')
    QUESTION_DELETE_VARIANT_BUTTON = (By.XPATH, '//button[contains(@class, "Answer_removeBtn")]')
    PREVIEW_QUESTION_HEADER = lambda q: (By.XPATH, f'//div[contains(@class, "OnePageContentBlock")]/h3[contains(text(), "{q}")]')
    PREVIEW_QUESTION_TEXTAREA = (By.XPATH, '//textarea[@placeholder="Введите текст"]')
    PREVIEW_QUESTION_RADIO_OPTION = (By.XPATH, '//div[contains(@class, "vkuiRadioGroup")]/label[contains(@class, "vkuiRadio")]')
    PREVIEW_QUESTION_CHECKBOX_OPTION = (By.XPATH, '//div[contains(@class, "OnePageContentBlock")]/label[contains(@class, "vkuiCheckbox")]')

    # ------------- 3 шаг -------------
    RESULTS_LABEL = (By.XPATH, '//h4[contains(text(), "Результат")]')
    # Увы, но эти два элемента можно различать только по порядковому номеру
    RESULTS_HEADER_INPUT = (By.XPATH, '(//input[contains(@class, "vkuiInput__el")])[1]')
    RESULTS_DESCRIPTION_INPUT = (By.XPATH, '(//input[contains(@class, "vkuiInput__el")])[2]')
    PREVIEW_RESULTS_HEADER = lambda h: (By.XPATH, f'//h2[contains(@class, "vkuiTitle") and contains(text(), "{h}")]')
    PREVIEW_RESULTS_DESCRIPTION = lambda d: (By.XPATH, f'//h4[contains(@class, "vkuiHeadline") and contains(text(), "{d}")]')

    # ------------- 4 шаг -------------
    SETTINGS_LABEL = (By.XPATH, '//h2[contains(text(), "Настройки лид-формы")]')
    SETTINGS_NAME_INPUT = (By.XPATH, '//input[@placeholder="Введите фамилию, имя и отчество"]')
    SETTINGS_ADDRESS_INPUT = (By.XPATH, '//input[@placeholder="Введите адрес"]')


class SurveyLocators(BaseLocators):
    CREATE_SURVEY_BUTTON = (By.XPATH, '//button/span/span[contains(text(), "Создать опрос")]')

    # ------------- 1 шаг -------------
    SURVEY_NAME_INPUT = (By.XPATH, '//input[@placeholder="Введите название"]')
    COMPANY_NAME_INPUT = (By.XPATH, '//input[@placeholder="Введите название компании"]')
    HEADER_TEXT_INPUT = (By.XPATH, '//input[@placeholder="Введите заголовок"]')
    DESCRIPTION_TEXT_INPUT = (By.XPATH, '//textarea[@placeholder="Введите описание опроса"]')
    PREVIEW_LOGO = (By.XPATH, '//div[contains(@class, "TitleBlock-module_appLogo")]/img')
    PREVIEW_COMPANY_NAME = (By.XPATH, '//div[contains(@class, "TitleBlock-module")]/span')
    PREVIEW_HEADER_TEXT = (By.XPATH, '//div[contains(@class, "TitleBlock-module")]/h2')
    PREVIEW_DESCRIPTION_TEXT = (By.XPATH, '//div[contains(@class, "TitleBlock-module")]/h4')

    # ------------- 2 шаг -------------
    QUESTION_TYPE_DROPDOWN = (By.XPATH, '//div[contains(@class, "HintSelector_hintSelectorButton")]')
    QUESTION_TYPE_ONE_ANSWER_OPTION = (By.XPATH, '//span[contains(text(), "Один из списка")]')
    QUESTION_TYPE_MANY_ANSWERS_OPTION = (By.XPATH, '//span[contains(text(), "Несколько из списка")]')
    QUESTION_TYPE_TEXT_ANSWER_OPTION = (By.XPATH, '//span[contains(text(), "Ответ в свободной форме")]')
    QUESTION_TYPE_SCALE_ANSWER = (By.XPATH, '//span[contains(text(), "Шкала")]')

    PREVIEW_QUESTION_HEADER = lambda q: (By.XPATH, f'//div[contains(@class, "SurveyQuestion")]/h1[contains(text(), "{q}")]')
    PREVIEW_QUESTION_TEXTAREA = (By.XPATH, '//textarea[@placeholder="Введите текст"]')
    PREVIEW_QUESTION_RADIO_OPTION = (By.XPATH, '//div[contains(@class, "vkuiRadioGroup")]/label[contains(@class, "vkuiRadio")]')
    PREVIEW_QUESTION_CHECKBOX_OPTION = (By.XPATH, '//div[contains(@class, "SurveyQuestion")]/label[contains(@class, "vkuiCheckbox")]')
    PREVIEW_QUESTION_SCALE_OPTION = (By.XPATH, '//div[contains(@class, "ScaleAnswer-module_wrapper")]')

    QUESTION_INPUT = (By.XPATH, '//textarea[@placeholder="Текст вопроса"]')
    QUESTION_ELEMENT_ERROR = (By.XPATH, '//div[contains(@class, "Question_error")]')
    QUESTION_ADD_VARIANT_BUTTON = (By.XPATH, '//button/span/span[contains(text(), "Добавить вариант")]')
    QUESTION_ADD_BUTTON = (By.XPATH, '//button/span/span[contains(text(), "Добавить вопрос")]')
    QUESTION_VARIANT_INPUT = (By.XPATH, '//input[@placeholder="Введите ответ"]')
    QUESTION_DELETE_VARIANT_BUTTON = (By.XPATH, '//button[contains(@class, "Answer_removeBtn")]')
    # По мнению разработчиков Вк рекламы, у кнопки дублирование вопроса aria-label тоже "Remove" :P
    QUESTION_DELETE_BUTTON = (By.XPATH, '(//button[@aria-label="Remove"])[2]')
    QUESTION_ELEMENT = (By.XPATH, '//div[contains(@class, "Question_question__")]')

    # ------------- 3 шаг -------------
    # Увы, но эти два элемента можно различать только по порядковому номеру
    RESULTS_HEADER_INPUT = (By.XPATH, '//input[@placeholder="Введите заголовок"]')
    RESULTS_DESCRIPTION_INPUT = (By.XPATH, '//input[@placeholder="Введите описание: например, поблагодарите за прохождение опроса"]')
    PREVIEW_RESULTS_HEADER = lambda h: (By.XPATH, f'//h2[contains(@class, "vkuiTitle") and contains(text(), "{h}")]')
    PREVIEW_RESULTS_DESCRIPTION = lambda d: (By.XPATH, f'//h4[contains(@class, "vkuiHeadline") and contains(text(), "{d}")]')
