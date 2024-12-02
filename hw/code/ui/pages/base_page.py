import time

import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from hw.code.conftest import Config


class PageNotOpenedException(Exception):
    pass


class BasePage(object):
    url = Config.VK_ADS_URL

    def is_opened(self, timeout=30):
        started = time.time()
        while time.time() - started < timeout:
            if self.driver.current_url.rstrip("/") == self.url.rstrip("/"):
                return True
        raise PageNotOpenedException(f'{self.url} did not open in {timeout} sec, current url {self.driver.current_url}')

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(self.url)
        self.is_opened()

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 15
        return WebDriverWait(self.driver, timeout=timeout)

    def open(self):
        self.driver.get(self.url)
        self.is_opened()

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    @allure.step('Click')
    def click(self, locator, timeout=None):
        self.find(locator, timeout=timeout)
        elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
        elem.click()
