import time

import pytest
import undetected_chromedriver as uc


class Config:
    VK_ADS_URL = 'https://ads.vk.com'
    VK_ADS_CABINET_URL = f'{VK_ADS_URL}/hq/overview'
    VK_ADS_SETTINGS_URL = f'{VK_ADS_URL}/hq/settings'
    USER_DATA_DIR = '/Users/smail/Library/Application Support/Google/Chrome'
    USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'


def pytest_addoption(parser):
    parser.addoption('--browser', default='chrome')
    parser.addoption('--url', default=Config.VK_ADS_URL)
    parser.addoption('--headless', action='store_false')
    parser.addoption('--debug_log', action='store_true')
    parser.addoption('--selenoid', action='store_true')
    parser.addoption('--vnc', action='store_true')


@pytest.fixture(scope='session')
def config(request):
    browser = request.config.getoption('--browser')
    url = request.config.getoption('--url')
    debug_log = request.config.getoption('--debug_log')
    headless = request.config.getoption('--headless')
    if request.config.getoption('--selenoid'):
        if request.config.getoption('--vnc'):
            vnc = True
        else:
            vnc = False
        selenoid = 'http://127.0.0.1:4444/wd/hub'
    else:
        selenoid = None
        vnc = False

    return {
        'browser': browser,
        'url': url,
        'debug_log': debug_log,
        'selenoid': selenoid,
        'vnc': vnc,
        'headless': headless
    }


@pytest.fixture
def driver():
    options = uc.ChromeOptions()
    #options = webdriver.ChromeOptions()
    options.add_argument(f'--user-data-dir={Config.USER_DATA_DIR}')
    options.add_argument(f'--user-agent={Config.USER_AGENT}')
    options.add_argument('--profile-directory=Profile 1')
    driver = uc.Chrome(options=options)
    #driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    time.sleep(30)
    driver.close()
    # driver.quit()
