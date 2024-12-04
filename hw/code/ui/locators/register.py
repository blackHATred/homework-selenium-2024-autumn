from selenium.webdriver.common.by import By


class RegisterLocators:
    RU_LANG_BUTTON = (By.XPATH, '//*[contains(text(), "Русский")]')
    EN_LANG_BUTTON = (By.XPATH, '//*[contains(text(), "English")]')
    TITLE = (By.TAG_NAME, 'h1')
    NEW_CABINET_BUTTON = (By.XPATH, '//*[@data-testid="create-new"]')
    ADVERTISER_OPTION = (By.XPATH, '//*[contains(text(), "Рекламодатель")]')
    AGENCY_OPTION = (By.XPATH, '//*[contains(text(), "Агентство")]')
    INDIVIDUAL_CHECKBOX = (By.XPATH, '//*[contains(text(), "Физическое лицо")]')
    LEGAL_ENTITY_CHECKBOX = (By.XPATH, '//*[contains(text(), "Юридическое лицо")]')
    TIN_INPUT = (By.XPATH, '//*[@name="inn"]')
    FULL_NAME_INPUT = (By.XPATH, '//*[@name="name"]')
    EMAIL_INPUT = (By.XPATH, '//*[@name="email"]')
    AGREEMENT_INPUT = (By.XPATH, '//*[@name="offer"]')
    AGREEMENT_CHECKBOX = (By.XPATH, '//*[contains(text(), "Создавая кабинет, вы принимаете условия")]')
    REQUIRED_FIELD_ALERT = (By.XPATH, '//*[contains(text(), "Обязательное поле")]')
    CREATE_CABINET_BUTTON = (By.XPATH, '//*[@data-testid="create-button"]')
