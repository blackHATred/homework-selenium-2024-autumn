from selenium.webdriver.common.by import By


class MainPage:
    TEL_INPUT = (By.XPATH, '//*[@data-testid="general-phone"]')

    CANCEL_BUTTON = (By.XPATH, '//*[@data-testid="settings-cancel"]')
