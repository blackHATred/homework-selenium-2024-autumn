from selenium.webdriver.common.by import By


class AsideMenuSettingsButtonLocators:
    SETTINGS_BUTTON = (By.XPATH, '//a[@href="/hq/settings"]')


class MainTabLocators:
    TEL_INPUT = (By.XPATH, '//*[@data-testid="general-phone"]')
    EMAIL_INPUT_0 = (By.XPATH, '//*[@data-testid="email-0"]')
    FULL_NAME_INPUT = (By.XPATH, '//*[@data-testid="general-ord-name"]')
    TIN_INPUT = (By.XPATH, '//*[@data-testid="general-ord-inn"]')
    CABINET_NAME_INPUT = (By.XPATH, '//*[@data-testid="account-item"]')

    ADD_EMAIL_BUTTON = (By.XPATH, '//*[@data-testid="add-email"]')
    # Этому локатору соответствует несколько кнопок, при обработке нужно учитывать порядковый номер удаляемой почты
    DELETE_EMAIL_BUTTON = (By.XPATH, '//*[contains(@class, "vkuiRemovable__action")]')
    CANCEL_BUTTON = (By.XPATH, '//*[@data-testid="settings-cancel"]')
    SAVE_BUTTON = (By.XPATH, '//*[@data-testid="settings-save"]')
    DELETE_ACCOUNT_BUTTON = (By.XPATH, '//*[contains(@class, "DeleteAccount_button")]')
    DELETE_ACCOUNT_CONFIRM_BUTTON = (By.XPATH, '//*[contains(text(), "Да, удалить")]')
    INTERFACE_LANGUAGE_BUTTON = (By.XPATH, '//*[@data-testid="interface-language"]')
    INTERFACE_LANGUAGE_RU_OPTION = (By.XPATH, '//*[@class="vkuiCustomSelectOption__children" and contains(text(), "RU")]')
    INTERFACE_LANGUAGE_EN_OPTION = (By.XPATH, '//*[@class="vkuiCustomSelectOption__children" and contains(text(), "EN")]')
    GENERAL_TAB = (By.XPATH, '//*[@data-testid="tabs-item-settings"]')
    OVERVIEW_BUTTON = (By.XPATH, '//*[@data-testid="left-menu"]')
    HOTKEYS_BUTTON = (By.XPATH, '//*[contains(@class, "vkuiButton__content") and contains(text(), "Список горячих клавиш")]')
    HOTKEYS_MODAL = (By.XPATH, '//*[@id="_modal_2"]')

    TEL_ERROR = (By.XPATH, '//div[contains(text(), "Некорректный номер телефона")]')
    EMAIL_ERROR = (By.XPATH, '//div[contains(text(), "Некорректный email адрес")]')
    FULL_NAME_ERROR = (By.XPATH, '//div[contains(text(), "Некорректные символы. Разрешена только кириллица дефис и пробел")]')
    TIN_INVALID_ERROR = (By.XPATH, '//div[contains(text(), "Невалидный ИНН")]')
    TIN_INCORRECT_ERROR = (By.XPATH, '//div[contains(text(), "Некорректный ИНН")]')
    TIN_INCORRECT_LEN_ERROR = (By.XPATH, '//div[contains(text(), "Длина ИНН должна быть 12 символов")]')

    CABINET_NAME_LABEL = (By.XPATH, '//*[contains(@class, "AccountSwitch_changeAccountName")]')


class NotificationTabLocators:
    EMAIL_NOTIFICATIONS_BUTTON = lambda email: (By.XPATH, f'//span[contains(text(), "{email}")]')
    WARNING_MESSAGE = (By.XPATH, '//*[contains(@class, "Warning_message")]')
    FINANCE_OPTION_LABEL = (By.XPATH, '//input[contains(@class, "vkuiCheckbox")]')


class AccessListTabLocators:
    EMPTY_ACCESS_LIST_MESSAGE = (By.XPATH, '//h2[contains(text(), "Доступа к другим кабинетам пока нет")]')
    SEND_INVITE_BUTTON = (By.XPATH, '//*[@data-testid="add-user"]')
    SEND_INVITE_BUTTON_TOP = (By.XPATH, '//*[@data-testid="settings-add-account"]')  # Та же кнопка, но сверху
    MODAL = (By.XPATH, '//*[contains(@class, "ModalRoot")]')
    SUBMIT_BUTTON = (By.XPATH, '//*[@data-testid="submit"]')
    CANCEL_BUTTON = (By.XPATH, '//*[@data-testid="cancel"]')
    USER_ID_INPUT = (By.XPATH, '//*[@data-testid="userid-input"]')
    SOMETHING_WENT_WRONG_MESSAGE = (By.XPATH, '//span[@role="alert" and contains(text(), "Что-то пошло не так")]')
    USER_ALREADY_ADDED_MESSAGE = (By.XPATH, '//span[@role="alert" and contains(text(), "Кабинет с таким ID уже добавлен")]')
    # Этому локатору соответствует несколько кнопок, при обработке нужно учитывать порядковый номер удаляемого кабинета
    DELETE_INVITE_BUTTON = (By.XPATH, '//*[@data-test="remove-button"]')
    DELETE_INVITE_CONFIRM_BUTTON = (By.XPATH, '//button[span/span[contains(text(), "Закрыть доступ")]]')
    DELETE_INVITE_CANCEL_BUTTON = (By.XPATH, '//button[span/span[contains(text(), "Отменить")]]')
    SEARCH_INPUT = (By.XPATH, '//*[@data-testid="search"]')
    EMPTY_SEARCH_MESSAGE = (By.XPATH, '//h2[contains(text(), "Ничего не нашлось")]')
    THESE_USERS_HAVE_ACCESS_LABEL = (By.XPATH, '//span[contains(text(), "Имеют доступ к этому кабинету")]')


class LogsTabLocators:
    FILTER_BUTTON = (By.XPATH, '//*[@data-testid="filter-button"]')
    FILTER_CATEGORY_OBJECT_TYPE = (By.XPATH, '//button[span/span/span[contains(text(), "Тип объекта")]]')
    FILTER_CATEGORY_WHAT_CHANGED = (By.XPATH, '//button[span/span/span[contains(text(), "Что изменилось")]]')
    FILTER_CATEGORY_AUTHOR = (By.XPATH, '//button[span/span/span[contains(text(), "Автор изменения")]]')
    FILTER_OPTIONS_CONTAINER = (By.XPATH, '//*[contains(@class, "FilterSection_optionItems")]')

    CHECK_ALL_BUTTON = (By.XPATH, '//button[span/span[contains(text(), "Выбрать все")]]')
    UNCHECK_ALL_BUTTON = (By.XPATH, '//button[span/span[contains(text(), "Сбросить")]]')
    APPLY_FILTER_BUTTON = (By.XPATH, '//button[span/span[contains(text(), "Применить")]]')
    CANCEL_FILTER_BUTTON = (By.XPATH, '//button[span/span[contains(text(), "Отмена")]]')

    # Этим двум локаторам соответствуют несколько кнопок, при обработке нужно учитывать порядковый номер применяемого фильтра
    APPLIED_FILTER_ELEMENT = (By.XPATH, '//span[contains(@class, "vkuiFootnote")]')
    FILTER_DELETE_BUTTON = (By.XPATH, '//span[contains(@class, "vkuiFootnote")]/button')
    FILTER_DELETE_ALL_BUTTON = (By.XPATH, '//button[span/span[contains(text(), "Сбросить все")]]')

    SEARCH_INPUT = (By.XPATH, '//input[@placeholder="Поиск"]')

    # Локатор для всех доступных опций фильтрации
    OPTION = (By.XPATH, '//input[contains(@class, "vkuiCheckbox")]')



