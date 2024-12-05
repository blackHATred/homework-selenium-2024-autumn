from selenium.webdriver.common.by import By

class CampaignMenuLocators:
    CREATE_CAMPAIGN_BUTTON = (By.XPATH, '//*[contains(text(), "Создать кампанию")]')
    MODAL_CLOSE_BUTTON = (By.XPATH, '//div[@role="button" and @aria-label="Закрыть"]')
    SEARCH_CAMPAIGN_INPUT = (By.XPATH, '//input[@data-testid="filter-search-input" and @placeholder="Поиск кампаний"]')
    FIRST_CAMPAIGN_HEADER = (By.XPATH, '//*contains(text(), "Создайте первую рекламную кампанию")]')

    CAMPAIGN_DROPDOWN_BUTTON = (By.XPATH, '//button[@data-testid="tags-selector" and .//span[text()="Все кампании"]]')
    DRAFTS_BUTTON = (By.XPATH, '//div[contains(@class, "TagSelector_menuItem__yLaIs")]//div[@role="button" and .//span[@data-testid="drafts" and contains(text(), "Черновики")]]')
    DRAFT_ROWS = (By.XPATH, '//div[contains(@class, "BaseTable__row") and .//div[contains(@class, "statusCell_text__St5Pm") and text()="Черновик"]]')
    CAMPAIGN_SEARCH_INPUT = (By.XPATH, '//input[@placeholder="Поиск кампаний" and @data-testid="filter-search-input"]')
    CHECKBOX_ON = (By.XPATH, '//div[contains(@class, "vkuiCheckbox__icon--on") and .//svg[@class="vkuiIcon vkuiIcon--20 vkuiIcon--w-20 vkuiIcon--h-20 vkuiIcon--check_box_on_20"]]')
    MAIN_CHECKBOX = (By.XPATH, '//input[@id="checkbox-all"]/following-sibling::div[contains(@class, "vkuiCheckbox__icon--on")]')
    DELETE_BUTTON = (By.XPATH, '//span[contains(@class, "vkuiButton__content") and text()="Удалить"]')
    CONFIRM_DELETE_BUTTON = (By.XPATH, '//button[contains(@class, "vkuiButton--appearance-negative") and .//span[text()="Удалить"]]')
    CANCEL_BUTTON = (By.XPATH, '//button[contains(@class, "vkuiButton--appearance-accent") and .//span[text()="Отмена"]]')

    DATE_PICKER_BUTTON = (By.XPATH, '//button[@data-testid="filter-data-picker"]')
    DATE_RANGE_BUTTON = (By.XPATH, '//button[contains(@class, "rdrStaticRange") and .//span[text()="Этот год"]]')
    TODAY_BUTTON = (By.XPATH, '//button[contains(@class, "rdrStaticRange") and .//span[text()="Сегодня"]]')
    START_DATE_INPUT = (By.XPATH, '//span[@data-testid="start-date" and contains(@class, "vkuiDateInput__input")]')
    END_DATE_INPUT = (By.XPATH, '//span[@data-testid="end-date" and contains(@class, "vkuiDateInput__input")]')
    SHOW_CALENDAR_BUTTON = (By.XPATH, '//button[@type="button" and @aria-label="Показать календарь" and contains(@class, "vkuiIconButton")]')
    CANCEL_CALENDAR_BUTTON = (By.XPATH, '//button[contains(@class, "vkuiButton--appearance-accent") and .//span[text()="Отменить"]]')
    APPLY_CALENDAR_BUTTON = (By.XPATH, '//button[contains(@class, "vkuiButton--appearance-accent") and .//span[text()="Применить"]]')
    DATE_RANGE_TEXT = (By.XPATH, '//div[contains(@class, "RangeDatePickerManager_rangeText__VQM6k")]')
    
class CampaignSettingsLocators:
    CAMPAIGN_SIDEBAR_ITEM = (By.XPATH, '//div[@class="MenuItem_cellWrapper__dSQle" and contains(@title, "Кампания")]')
    CAMPAIGN_NAME_INPUT = (By.XPATH, "//div[contains(@class, 'EditableTitle_container_editable__wQN4Z')]//h2[contains(@class, 'EditableTitle_title__5fIJC')]")
    TAB_CONVERSION = (By.XPATH, '//div[@role="tab" and @data-testid="tab-conversion" and contains(@class, "vkuiTabsItem")]')
    TAB_BRANDING = (By.XPATH, '//div[@role="tab" and @data-testid="tab-branding" and contains(@class, "vkuiTabsItem")]')

    # Целевые действия
    SITE_CONVERSIONS_OPTION = (By.XPATH, '//div[@data-id="site_conversions" and contains(.//span, "Сайт")]')
    SITE_URL_INPUT = (By.XPATH, '//input[@placeholder="Введите ссылку на сайт" and contains(@class, "vkuiInput__el")]')
    SITE_URL_ERROR = (By.XPATH, '//span[@role="alert" and contains(@class, "vkuiFormItem__bottom") and contains(text(), "Не удалось подгрузить данные ссылки")]')
    BUDGET_INPUT = (By.XPATH, '//input[@placeholder="Не задан" and @data-testid="targeting-not-set" and contains(@class, "vkuiInput__el")]')
    BUDGET_INPUT_ERROR = (By.XPATH, '//span[@role="alert" and contains(@class, "vkuiFormItem__bottom") and contains(text(), "Укажите бюджет не меньше 100₽")]')
    SELLING_PROPOSITION_TEXTAREA = (By.XPATH, '//textarea[@placeholder="Опишите ваше предложение" and contains(@class, "vkuiTextarea__el")]')
    BUDGET_OPTIMIZATION_CHECKBOX = (By.XPATH, '//input[@data-testid="budget-optimization" and @type="checkbox"]')
    REQUIRED_DATA_FIELD_SYMBOL = (By.XPATH, '//span[contains(@class, "FormItem_requiredSymbol__8X6va") and text()="*"]')
    BUDGET_SELECT = (By.XPATH, '//div[contains(@class, "Budget_select__GQI9c")]//input[@data-testid="budget"]')
    START_DATE_INPUT = (By.XPATH, '//span[@data-testid="start-date" and contains(@class, "vkuiDateInput__input")]')
    CALENDAR = (By.XPATH, '//div[contains(@class, "vkuiCalendar")]')
    NEXT_MONTH_BUTTON = (By.XPATH, '//div[@role="button" and @aria-label[contains(., "Следующий месяц")]]')
    CURRENT_MONTH = (By.XPATH, '//span[contains(@class, "vkuiCalendarHeader__month")]')

    # Узнаваемость и охват
    RADIO_OPTION_SITE = (By.XPATH, '//label[contains(@class, "vkuiRadio") and .//span[text()="Сайт"]]')
    BANNER_AD_OPTION = (By.XPATH, '//div[@data-id="branding_multi" and contains(@class, "Option_item__gJMDY")]')
    ADVERTISED_SITE_LABEL = (By.XPATH, '//h2[contains(@class, "FormItem_top__A6tjT") and contains(.//span, "Рекламируемый сайт")]')
    FREQUENCY_SETTINGS_CHECKBOX = (By.XPATH, '//label[contains(@class, "ShowsSwitch_switch__ccQ+5")]//input[@type="checkbox"]')
    SHOWS_PER_USER_LABEL = (By.XPATH, '//h2[contains(@class, "FormItem_top__A6tjT") and contains(.//span, "Показов на пользователя")]')

    # Футер
    ERROR_BUTTON = (By.XPATH, '//button[contains(@class, "ErrorsTooltip_button__YyIDS") and contains(@class, "vkuiButton")]')
    CONTINUE_BUTTON = (By.XPATH, '//div[contains(@class, "CreateFooter_actionsWrap__9H7gw")]//button[contains(@class, "vkuiButton") and .//span[text()="Продолжить"]]')
    SAVE_AS_DRAFT_BUTTON = (By.XPATH, '//button[contains(@class, "vkuiButton") and .//span[text()="Сохранить как черновик"]]')
    MAIN_MENU_BUTTON = (By.XPATH, '//button[contains(@class, "header_logoNewSidebar__xxqHV") and @data-route="root"]')
    

class GroupLocators:
    GROUP_SIDEBAR_ITEM = (By.XPATH, '//div[@role="button" and @data-testid="menu-item" and contains(.//span, "Группа")]')
    SET_DATES_BUTTON = (By.XPATH, '//span[contains(@class, "vkuiSimpleCell__children") and contains(text(), "Настроить даты проведения")]')
    SET_DATES_BUTTON = (By.XPATH, '//div[@role="button" and contains(@class, "GroupDates_expand__67Aq+") and .//span[text()="Настроить даты проведения"]]')
    SET_TIME_BUTTON = (By.XPATH, '//span[contains(@class, "vkuiSimpleCell__children") and contains(text(), "Настроить время показа")]')
    MY_TIME_BUTTON = (By.XPATH, '//button[contains(@class, "Preset_button__+hw+w") and .//span[text()="Моё время"]]')
    TIME_SLOT_ACTIVE = (By.XPATH, '//div[@data-id="0" and @data-day-id="0" and @data-hour-id="0" and contains(@class, "Cell_cell__9eaRF") and contains(@class, "Cell_cell_checked__jp-QY")]')
    TIME_SLOT_NOT_ACTIVE = (By.XPATH, '//div[@data-id="0" and @data-day-id="0" and @data-hour-id="0" and contains(@class, "Cell_cell__9eaRF") and not(contains(@class, "Cell_cell_checked__jp-QY"))]')
    ADD_GROUP_BUTTON = (By.XPATH, '//button[contains(@class, "AddGroupButton_addButton__qM3RA") and .//span[text()="Добавить ещё группу"]]')
    REGION_INPUT = (By.XPATH, '//input[@placeholder="Страна, регион или город" and contains(@class, "vkuiSearch__nativeInput")]')
    SEARCH_TOOLTIP_NO_RESULTS = (By.XPATH, '//div[contains(@class, "Tooltip_tooltip__piez5") and @role="tooltip"]//span[contains(text(), "Ничего не нашлось")]')
    SEARCH_TOOLTIP_SHORT_REQUEST = (By.XPATH, '//div[contains(@class, "Tooltip_tooltip__piez5") and @role="tooltip"]//span[text()="Введите поисковый запрос"]')
    YAROSLAVL_OPTION = (By.XPATH, '//div[contains(@class, "Branch_title__FvS4M") and .//span/b[text()="Ярославль"]]')
    YAROSLAVL_LABEL = (By.XPATH, '//h4[contains(@class, "RegionsList_label__KPYrN") and text()="Ярославль"]')
    YAROSLAVL_REMOVE_BUTTON = (By.XPATH, '//h4[contains(@class, "RegionsList_label__KPYrN") and text()="Ярославль"]/following-sibling::button[contains(@class, "RegionsList_close__XtcC-")]')
    DEMOGRAPHY_SECTION = (By.XPATH, '//div[@role="button" and .//h3[text()="Демография"]]')
    AGE_SELECT = (By.XPATH, '//div[contains(@class, "vkuiCustomSelectInput__input-group")]')
    AGE_OPTION = (By.XPATH, '//select[@class="vkuiCustomSelect__control"]/option[@value="{}"]')
    AGE_WARNING_BANNER = (By.XPATH, '//div[contains(@class, "RichBanner_bannerDescription__hr8Fh")]//h4[text()="Указанный возраст меньше выставленной маркировки"]')
    CONTINUE_BUTTON = (By.XPATH, '//button[contains(@class, "vkuiButton") and .//span[text()="Продолжить"]]')


class AdLocators:
    ADD_AD_BUTTON = (By.XPATH, '//button[contains(@class, "AdForm_addButton__lw-oq") and .//span[text()="Добавить ещё объявление"]]')


class CampaignLocators(CampaignMenuLocators, CampaignSettingsLocators, GroupLocators, AdLocators):
    pass