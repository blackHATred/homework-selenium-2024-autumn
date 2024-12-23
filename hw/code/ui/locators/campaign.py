from selenium.webdriver.common.by import By

class CampaignMenuLocators:
    CREATE_CAMPAIGN_BUTTON = (By.XPATH, '//*[contains(text(), "Создать кампанию")]')
    MODAL_CLOSE_BUTTON = (By.XPATH, '//div[@role="button" and @aria-label="Закрыть"]')
    SEARCH_CAMPAIGN_INPUT = (By.XPATH, '//input[@data-testid="filter-search-input" and @placeholder="Поиск кампаний"]')
    FIRST_CAMPAIGN_HEADER = (By.XPATH, '//*contains(text(), "Создайте первую рекламную кампанию")]')

    CAMPAIGN_DROPDOWN_BUTTON = (By.XPATH, '//button[@data-testid="tags-selector" and .//span[text()="Все кампании"]]')
    DRAFTS_BUTTON = (By.XPATH, "//div[@role='button' and .//span[@data-testid='drafts']]")
    DRAFT_ROWS = (By.XPATH, '//div[contains(@class, "BaseTable__row") and .//div[contains(@class, "statusCell_text") and text()="Черновик"]]')
    CAMPAIGN_SEARCH_INPUT = (By.XPATH, '//input[@placeholder="Поиск кампаний" and @data-testid="filter-search-input"]')
    CHECKBOX_ON = (By.XPATH, '//div[contains(@class, "vkuiCheckbox__icon--on") and .//svg[@class="vkuiIcon vkuiIcon--20 vkuiIcon--w-20 vkuiIcon--h-20 vkuiIcon--check_box_on_20"]]')
    # к сожалению, более емкие локаторы не подходят
    MAIN_CHECKBOX = (By.XPATH, '//label[@class="vkuiCheckbox vkuiCheckbox--sizeY-compact vkuiCheckbox--simple vkuiTappable vkuiInternalTappable vkuiTappable--hasHover vkuiTappable--hasActive vkui-focus-visible" and .//input[@id="checkbox-all"]]')
    MAIN_CHECKBOX_LABEL = (By.XPATH, '//label[@for="checkbox-all"]')
    DELETE_BUTTON = (By.XPATH, '//span[contains(@class, "vkuiButton__content") and text()="Удалить"]')
    CONFIRM_DELETE_BUTTON = (By.XPATH, '//div[contains(@class, "confirmRemoveModal_footer")]//button[contains(@class, "vkuiButton--appearance-negative") and .//span[text()="Удалить"]]')
    CANCEL_BUTTON = (By.XPATH, '//button[contains(@class, "vkuiButton--appearance-accent") and .//span[text()="Отмена"]]')

    DATE_PICKER_BUTTON = (By.XPATH, '//button[@data-testid="filter-data-picker"]')
    DATE_TEXT = (By.XPATH, './/div[contains(@class, "RangeDatePickerManager_rangeText")]')
    DATE_RANGE_BUTTON = (By.XPATH, '//button[contains(@class, "rdrStaticRange") and .//span[text()="Этот год"]]')
    TODAY_BUTTON = (By.XPATH, '//button[contains(@class, "rdrStaticRange") and .//span[text()="Сегодня"]]')
    START_DATE_INPUT = (By.XPATH, "//input[@name='startDate']")
    END_DATE_INPUT = (By.XPATH, "//input[@name='endDate']")
    SHOW_CALENDAR_BUTTON = (By.XPATH, '//button[@type="button" and @aria-label="Показать календарь" and contains(@class, "vkuiIconButton")]')
    CANCEL_CALENDAR_BUTTON = (By.XPATH, '//button[contains(@class, "vkuiButton--appearance-accent") and .//span[text()="Отменить"]]')
    APPLY_CALENDAR_BUTTON = (By.XPATH, '//button[contains(@class, "vkuiButton--appearance-accent") and .//span[text()="Применить"]]')
    DATE_RANGE_TEXT = (By.XPATH, '//div[contains(@class, "RangeDatePickerManager_rangeText")]')
    
class CampaignSettingsLocators:
    CAMPAIGN_SIDEBAR_ITEM = (By.XPATH, '//div[@class="MenuItem_cellWrapper__dSQle" and contains(@title, "Кампания")]')
    TAB_CONVERSION = (By.XPATH, '//div[@role="tab" and @data-testid="tab-conversion" and contains(@class, "vkuiTabsItem")]')
    TAB_BRANDING = (By.XPATH, '//div[@role="tab" and @data-testid="tab-branding" and contains(@class, "vkuiTabsItem")]')

    # Целевые действия
    SITE_CONVERSIONS_OPTION = (By.XPATH, '//div[@data-id="site_conversions" and contains(.//span, "Сайт")]')
    SITE_URL_INPUT = (By.XPATH, '//input[@placeholder="Введите ссылку на сайт" and contains(@class, "vkuiInput__el")]')
    SITE_URL_ERROR = (By.XPATH, '//span[@role="alert" and contains(@class, "vkuiFormItem__bottom") and contains(text(), "Не удалось подгрузить данные ссылки")]')
    BUDGET_INPUT = (By.XPATH, '//input[@placeholder="Не задан" and @data-testid="targeting-not-set" and contains(@class, "vkuiInput__el")]')
    BUDGET_INPUT_ERROR = (By.XPATH, '//span[@role="alert" and contains(@class, "vkuiFormItem__bottom") and contains(text(), "Укажите бюджет не меньше 100₽")]')
    SELLING_PROPOSITION_TEXTAREA = (By.XPATH, '//textarea[@placeholder="Опишите ваше предложение" and contains(@class, "vkuiTextarea__el")]')
    BUDGET_SELECT = (By.XPATH, '//div[contains(@class, "Budget_select")]//input[@data-testid="budget"]')
    START_DATE_INPUT = (By.XPATH, '//span[@data-testid="start-date" and contains(@class, "vkuiDateInput__input")]')
    CALENDAR = (By.XPATH, '//div[contains(@class, "vkuiCalendar")]')
    NEXT_MONTH_BUTTON = (By.XPATH, '//div[@role="button" and @aria-label[contains(., "Следующий месяц")]]')
    CURRENT_MONTH = (By.XPATH, '//span[contains(@class, "vkuiCalendarHeader__month")]')

    # Узнаваемость и охват
    RADIO_OPTION_SITE = (By.XPATH, '//label[contains(@class, "vkuiRadio") and .//span[text()="Сайт"]]')
    BANNER_AD_OPTION = (By.XPATH, '//div[@data-id="branding_multi" and contains(@class, "Option_item")]')
    ADVERTISED_SITE_LABEL = (By.XPATH, '//h2[contains(@class, "FormItem_top") and contains(.//span, "Рекламируемый сайт")]')
    SHOWS_PER_USER_LABEL = (By.XPATH, '//h2[contains(@class, "FormItem_top") and contains(.//span, "Показов на пользователя")]')

    # Футер
    ERROR_BUTTON = (By.XPATH, '//button[contains(@class, "ErrorsTooltip_button") and contains(@class, "vkuiButton")]')
    CONTINUE_BUTTON = (By.XPATH, '//div[contains(@class, "CreateFooter_actionsWrap")]//button[contains(@class, "vkuiButton") and .//span[text()="Продолжить"]]')
    SAVE_AS_DRAFT_BUTTON = (By.XPATH, '//button[contains(@class, "vkuiButton") and .//span[text()="Сохранить как черновик"]]')
    MAIN_MENU_BUTTON = (By.XPATH, '//button[contains(@class, "header_logoNewSidebar") and @data-route="root"]')
    

class GroupLocators:
    GROUP_SIDEBAR_ITEM = (By.XPATH, '//div[@role="button" and @data-testid="menu-item" and contains(.//span, "Группа")]')
    SET_DATES_BUTTON = (By.XPATH, '//span[contains(@class, "vkuiSimpleCell__children") and contains(text(), "Настроить даты проведения")]')
    SET_DATES_BUTTON = (By.XPATH, '//div[@role="button" and contains(@class, "GroupDates_expand__67Aq+") and .//span[text()="Настроить даты проведения"]]')
    SET_TIME_BUTTON = (By.XPATH, '//span[contains(@class, "vkuiSimpleCell__children") and contains(text(), "Настроить время показа")]')
    MY_TIME_BUTTON = (By.XPATH, '//button[contains(@class, "Preset_button__+hw+w") and .//span[text()="Моё время"]]')
    # длинные локаторы, так как нудно учитывать конкретный слот в большом массиве
    TIME_SLOT_ACTIVE = (By.XPATH, '//div[@data-id="0" and @data-day-id="0" and @data-hour-id="0" and contains(@class, "Cell_cell") and (contains(@class, "Cell_cell_checked"))]')
    TIME_SLOT_NOT_ACTIVE = (By.XPATH, '//div[@data-id="0" and @data-day-id="0" and @data-hour-id="0" and contains(@class, "Cell_cell") and not(contains(@class, "Cell_cell_checked"))]')
    ADD_GROUP_BUTTON = (By.XPATH, '//button[contains(@class, "AddGroupButton_addButton") and .//span[text()="Добавить ещё группу"]]')
    REGION_INPUT = (By.XPATH, '//input[@placeholder="Страна, регион или город" and contains(@class, "vkuiSearch__nativeInput")]')
    SEARCH_TOOLTIP_NO_RESULTS = (By.XPATH, '//div[contains(@class, "Tooltip_tooltip") and @role="tooltip"]//span[contains(text(), "Ничего не нашлось")]')
    SEARCH_TOOLTIP_SHORT_REQUEST = (By.XPATH, '//div[contains(@class, "Tooltip_tooltip") and @role="tooltip"]//span[text()="Введите поисковый запрос"]')
    YAROSLAVL_OPTION = (By.XPATH, '//div[contains(@class, "Branch_title") and .//span/b[text()="Ярославль"]]')
    YAROSLAVL_LABEL = (By.XPATH, '//h4[contains(@class, "RegionsList_label") and text()="Ярославль"]')
    YAROSLAVL_REMOVE_BUTTON = (By.XPATH, '//h4[contains(@class, "RegionsList_label") and text()="Ярославль"]/following-sibling::button[contains(@class, "RegionsList_close")]')
    DEMOGRAPHY_SECTION = (By.XPATH, '//div[@role="button" and .//h3[text()="Демография"]]')
    CONTINUE_BUTTON = (By.XPATH, '//button[contains(@class, "vkuiButton") and .//span[text()="Продолжить"]]')


class AdLocators:
    ADD_AD_BUTTON = (By.XPATH, '//button[contains(@class, "AdForm_addButton") and .//span[text()="Добавить ещё объявление"]]')
    ADD_ITEMS = (By.XPATH, '//div[contains(@class, "MenuItem_cellWrapper") and contains(@title, "Объявление")]')

class CampaignLocators(CampaignMenuLocators, CampaignSettingsLocators, GroupLocators, AdLocators):
    pass