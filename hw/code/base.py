from contextlib import contextmanager

import pytest
from selenium.webdriver.remote.webdriver import WebDriver


class BaseCase:
    driver: WebDriver
    config: dict

    @contextmanager
    def switch_to_window(self, current, close=False):
        for w in self.driver.window_handles:
            if w != current:
                self.driver.switch_to.window(w)
                break
        yield
        if close:
            self.driver.close()
        self.driver.switch_to.window(current)

    @pytest.fixture(scope='function', autouse=True)
    def setup_(self, driver, config):
        self.driver = driver
        self.config = config
