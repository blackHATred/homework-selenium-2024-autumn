import time

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from hw.code.ui.locators.index import IndexLocators


class PageNotOpenedException(Exception):
    pass


class BasePage(object):
    url: str = ''
    locators = IndexLocators
    driver: WebDriver

    def is_opened(self, timeout: int = 30, url: str = None):
        if url is None:
            url = self.url
        started = time.time()
        while time.time() - started < timeout:
            if url in self.driver.current_url:
                return True
        raise PageNotOpenedException(f'{url} did not open in {timeout} sec, current url {self.driver.current_url}')

    def __init__(self, driver):
        self.driver = driver
        # self.driver.get(self.url)
        # self.is_opened()

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 30
        return WebDriverWait(self.driver, timeout=timeout)

    def open(self):
        self.driver.get(self.url)

    def open_and_wait(self):
        self.open()
        self.wait().until(EC.url_matches(self.url))

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def click(self, locator, timeout=None):
        self.find(locator, timeout=timeout)
        elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
        elem.click()

    def fill_field(self, field_locator: tuple[str, str], value: str):
        self.find(field_locator).send_keys(value)
        # Может быть такое, что вебдрайвер не успевает отработать, поэтому нужно очевидным образом подождать ввода
        self.wait().until(EC.text_to_be_present_in_element_value(field_locator, value))

    def clear_field(self, field_locator: tuple[str, str]):
        self.find(field_locator).clear()

    def get_field_value(self, field_locator: str):
        return self.find(field_locator).get_attribute('value')
