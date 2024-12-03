from selenium.webdriver.common.by import By


class AuthLocators:
    MAIL_RU_OAUTH_OPTION_BUTTON = (By.XPATH, '//*[@data-test-id="oAuthService_mail_ru"]')
    EMAIL_INPUT = (By.XPATH, '//*[@name="username"]')
    NEXT_BUTTON = (By.XPATH, '//*[@data-test-id="next-button"]')
    AUTH_PROBLEMS_BUTTON = (By.XPATH, '//*[@data-test-id="auth-problems"]')
    USE_PASSWORD_BUTTON = (By.XPATH, '//*[@data-test-id="auth-by-password"]/*/a')
    PASSWORD_INPUT = (By.XPATH, '//*[@name="password"]')
    SUBMIT_BUTTON = (By.XPATH, '//*[@data-test-id="submit-button"]')

