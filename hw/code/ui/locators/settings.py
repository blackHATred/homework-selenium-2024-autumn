from selenium.webdriver.common.by import By


class AsideMenuSettingsButtonLocators:
    SETTINGS_BUTTON = (By.XPATH, '//*[@data-testid="left-menu"]')


class MainTabLocators:
    TEL_INPUT = (By.XPATH, '//*[@data-testid="general-phone"]')
    EMAIL_INPUT_0 = (By.XPATH, '//*[@data-testid="email-0"]')
    FULL_NAME_INPUT = (By.XPATH, '//*[@data-testid="general-ord-name"]')
    TIN_INPUT = (By.XPATH, '//*[@data-testid="general-ord-inn"]')

    ADD_EMAIL_BUTTON = (By.XPATH, '//*[@data-testid="add-email"]')
    # Этому локатору соответствует несколько кнопок, при обработке нужно учитывать порядковый номер удаляемой почты
    DELETE_EMAIL_BUTTON = (By.XPATH, '//button[@area-label="Удалить"]')
    CANCEL_BUTTON = (By.XPATH, '//*[@data-testid="settings-cancel"]')
    SAVE_BUTTON = (By.XPATH, '//*[@data-testid="settings-save"]')
    DELETE_ACCOUNT_BUTTON = (By.XPATH, '//*[contains(@class, "DeleteAccount_button")]')
    DELETE_ACCOUNT_CONFIRM_BUTTON = (By.XPATH, '//*[contains(text(), "Да, удалить")]')

    TEL_ERROR = (By.XPATH, '//div[contains(text(), "Некорректный номер телефона")]')
    EMAIL_ERROR = (By.XPATH, '//div[contains(text(), "Некорректный email адрес")]')


class NotificationTabLocators:
    pass


class AccessListTabLocators:
    pass


class ChangesHistoryTabLocators:
    pass


class SettingsLocators(MainTabLocators, NotificationTabLocators, AccessListTabLocators, ChangesHistoryTabLocators,
                       AsideMenuSettingsButtonLocators):
    pass
