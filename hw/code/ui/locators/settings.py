from selenium.webdriver.common.by import By


class MainTabLocators:
    TEL_INPUT = (By.XPATH, '//*[@data-testid="general-phone"]')

    CANCEL_BUTTON = (By.XPATH, '//*[@data-testid="settings-cancel"]')
    DELETE_ACCOUNT_BUTTON = (By.XPATH, '//*[contains(@class, "DeleteAccount_button")]')
    DELETE_ACCOUNT_CONFIRM_BUTTON = (By.XPATH, '//*[contains(text(), "Да, удалить")]')


class NotificationTabLocators:
    pass


class AccessListTabLocators:
    pass


class ChangesHistoryTabLocators:
    pass


class SettingsLocators(MainTabLocators, NotificationTabLocators, AccessListTabLocators, ChangesHistoryTabLocators):
    pass
