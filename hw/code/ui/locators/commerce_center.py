from selenium.webdriver.common.by import By

class CommerceCenterPageLocators:
    CREATE_CATALOG_BUTTON = (By.XPATH, '//button[@data-testid="create-catalog" and .//span[text()="Создать каталог"]]')
    NEW_CATALOG_HEADER = (By.XPATH, '//h2[contains(@class, "ModalSidebarPage_title__Uu-FC") and text()="Новый каталог"]')
    CATALOG_NAME_INPUT = (By.XPATH, '//input[@data-testid="catalogName-input"]')
    REQUIRED_FIELD_NAME_ALERT = (By.XPATH, '//span[contains(@class, "vkuiFormItem__bottom") and @role="alert" and .//div[text()="Обязательное поле"]]')
    MANUAL_OPTION = (By.XPATH, '//div[@data-testid="catalog-source_type-select" and .//h4[text()="Вручную"]]')
    FEED_INPUT = (By.XPATH, '//input[@type="file" and @accept="text/csv,text/tab-separated-values,application/xml,.yml"]')
    SUBMIT_BUTTON = (By.XPATH, '//button[@data-testid="submit" and @title="Создать каталог" and .//span[text()="Создать каталог"]]')
    FIELD_ERROR_ALERT = (By.XPATH, '//div[contains(@class, "formBanner_container__Y0PJ7 error medium") and .//span[text()="Обязательное поле"]]')
    CANCEL_BUTTON = (By.XPATH, '//button[@data-testid="cancel" and .//span[text()="Отмена"]]')
    TABLE_HEADERS = (By.XPATH, '//div[@role="gridcell" and contains(@class, "BaseTable__header-cell")]')
    CATALOG_ITEMS = (By.XPATH, '//a[@data-testid="catalog-item"]')
    SEARCH_INPUT = (By.XPATH, '//input[@data-testid="search"]')
    NOTHING_FOUND_HEADER = (By.XPATH, '//h2[contains(@class, "vkuiPlaceholder__header") and text()="Ничего не нашлось"]')
    STATUS_ACTIVE = (By.XPATH, '//div[@class="StatusCell_cell__JNHWT" and contains(text(), "Активный")]')
    
class CatalogLocators:
    
    SETTINGS_BUTTON = (By.XPATH, '//button[contains(@class, "vkuiButton--appearance-neutral") and .//span[text()="Настройки"]]')
    DELETE_CATALOG_BUTTON = (By.XPATH, '//button[@data-testid="delete" and @title="Удалить каталог" and .//span[text()="Удалить каталог"]]')
    REMOVE_BUTTON = (By.XPATH, '//button[@data-testid="button-remove" and .//span[text()="Удалить"]]')
    SETTINGS_HEADER = (By.XPATH, '//h2[contains(@class, "ModalSidebarPage_title__Uu-FC") and text()="Настройки каталога"]')

    #Goods
    ITEMS_TABLE = (By.XPATH, '//div[contains(@class, "BaseTable") and @role="table"]')
    ADD_GOODS_BUTTON = (By.XPATH, '//button[contains(@class, "vkuiButton--appearance-accent") and .//span[text()="Добавить товары"]]')
    SETTINGS_PANEL_HEADER = (By.XPATH, '//h2[contains(@class, "vkuiPanelHeader__content-in") and text()="Настройки каталога"]')
    CANCEL_ADD_GOODS_BUTTON = (By.XPATH, '//button[@data-testid="cancel" and @title="Отменить" and .//span[text()="Отменить"]]')
    CONTINUE_ADD_GOODS_BUTTON = (By.XPATH, '//button[@data-testid="submit" and @title="Продолжить" and .//span[text()="Продолжить"]]')
    CURRENT_CATALOG_BUTTON = (By.XPATH, '//div[@data-testid="current-catalog"]')
    #CATALOG_ITEM_BY_NAME = (By.XPATH, "//a[@data-testid='catalog-item']//h4[text()='Каталог']")
    CATALOG_ITEM_BY_NAME = (By.XPATH, '//a[@data-testid="catalog-item" and .//h4[contains(text(), "{name}")]]')
    CATALOG_NAME = (By.XPATH, '//div[@data-testid="current-catalog"]//h4')
    #Group
    GROUPS_TAB = (By.XPATH, '//div[@data-testid="catalog-tabs-groups" and .//span[text()="Группы"]]')
    CREATE_GROUP_BUTTON = (By.XPATH, '//button[contains(@class, "vkuiButton--appearance-accent") and .//span[text()="Создать группу"]]')
    USE_FILTERS_BUTTON = (By.XPATH, '//div[@role="button" and .//span[text()="Использовать фильтры"]]')
    CHOOSE_GOODS_MANUALLY_BUTTON = (By.XPATH, '//div[@role="button" and .//span[text()="Выбрать товары вручную"]]')
    NEW_GROUP_HEADER = (By.XPATH, '//h2[contains(@class, "ModalSidebarPage_title__Uu-FC") and text()="Новая группа товаров"]')
    ADD_FILTER_BUTTON = (By.XPATH, '//button[contains(@class, "Filters_filterConditionAdd__nwksc") and .//span[text()="Добавить фильтр"]]')
    FILTER_CONDITION = (By.XPATH, '//div[contains(@class, "Condition_wrap__5hsh- Condition_withIndicator__KUEys")]')
    # есть наалогичные элементы, поэтому иначе никак
    GROUP_NAME_INPUT = (By.XPATH, '//div[@class="vkuiFormItem vkuiFormItem--withPadding vkuiInternalFormItem vkuiFormItem--sizeY-none vkuiInternalFormItem--sizeY-none"]//input[@class="vkuiTypography vkuiInput__el vkuiText vkuiText--sizeY-none" and @name="groupName"]')
    SAVE_BUTTON = (By.XPATH, '//button[@type="submit" and @data-testid="submit" and .//span[text()="Сохранить"]]')
    CANCEL_BUTTON = (By.XPATH, '//button[@type="button" and @data-testid="cancel" and .//span[text()="Отмена"]]')
    GROUP_ITEM_BY_NAME = (By.XPATH, '//a[@data-testid="catalog-groups-nav-item" and .//h2[contains(@class, "vkuiHeader__content") and text()="{name}"]]')
    GROUP_ITEM_BY_NAME_CONTAINS = (By.XPATH, '//a[@data-testid="catalog-groups-nav-item" and .//h2[contains(@class, "vkuiHeader__content") and contains(text(), "{name}")]]')
    MORE_BUTTON = (By.XPATH, '//button[contains(@class, "Toolbar_actionsButton__32Sv4") and .//svg[@class="vkuiIcon--more_horizontal_24"]]')
    DELETE_GROUP_BUTTON = (By.XPATH, '//label[@data-testid="dropdown-item" and .//span[text()="Удалить группу"]]')
    CONFIRM_DELETE_BUTTON = (By.XPATH, '//button[@data-testid="button-remove" and .//span[text()="Удалить"]]')
    # есть несколько полей поиска
    SEARCH_GOODS_INPUT = (By.XPATH, "//input[@class='vkuiTypography vkuiTypography--normalize vkuiTypography--weight-3 vkuiSearch__nativeInput vkuiHeadline--sizeY-none vkuiHeadline--level-1']")
    ITEMS_TABLE = (By.XPATH, '//div[contains(@class, "BaseTable") and @role="table"]')
    NOTHING_FOUND_MESSAGE = (By.XPATH, '//h2[contains(@class, "vkuiPlaceholder__header") and text()="Ничего не нашлось"]')
    ADD_LIST_BUTTON = (By.XPATH, '//button[@data-testid="group-add-list" and .//span[text()="Добавить списком"]]')
    TEXTAREA_FIELD = (By.XPATH, '//textarea[@class="vkuiTypography vkuiTextarea__el vkuiText vkuiText--sizeY-none"]')
    ADD_TO_GROUP_BUTTON = (By.XPATH, '//button[@type="submit" and .//span[text()="Добавить в группу"]]')
    SELECTED_GOODS_TAB = (By.XPATH, '//div[@role="tab" and .//span[text()="Выбранные"]]')
    GROUP_IN_LIST_GROUP = (By.XPATH, '//a[@data-testid="catalog-groups-nav-item" and .//h2[contains(@class, "vkuiHeader__content")]]')
    # есть несколько полей поиска
    SEARCH_INPUT_IN_GROUPS = (By.XPATH,"//div[@class='CatalogGroups_controls__MC4-s']//input[@data-testid='search']")

    # Download
    DOWNLOAD_HISTORY_TAB = (By.XPATH, '//div[@role="tab" and @data-testid="catalog-tabs-history" and .//span[text()="История загрузок"]]')
    REFRESH_FILE_BUTTON = (By.XPATH, '//button[contains(@class, "UpdateBannerInfo_refreshButton__uZEpU") and .//span[text()="Обновить файл"]]')
    CATALOG_DOWNLOAD_HEADER = (By.XPATH, '//div[@class="vkuiPanelHeader__content"]//h2[@class="vkuiPanelHeader__content-in" and text()="Настройки каталога"]')


class CommerceCenterLocators(CatalogLocators, CommerceCenterPageLocators):
    pass
