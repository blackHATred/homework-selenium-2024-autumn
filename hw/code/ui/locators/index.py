from selenium.webdriver.common.by import By


class IndexLocators:
    # Название класса начинается с ButtonCabinet и имеет продолжение в виде рандомных символов
    GO_TO_CABINET_BUTTON = (By.XPATH, '//*[contains(@class, "ButtonCabinet")]')
