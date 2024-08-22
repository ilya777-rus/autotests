import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import os


@pytest.fixture()
def browser():
    service = Service(executable_path=ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service)
    yield browser
    browser.quit()

@pytest.fixture(scope='function')
def browser_d():
    service = Service(executable_path=ChromeDriverManager().install())
    current_directory = os.getcwd()
    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": current_directory,
        "download.prompt_for_download": False,
        "directory_upgrade": True,
        "safebrowsing.enabled": True
    }
    options.add_experimental_option("prefs", prefs)
    options.add_argument("--allow-running-insecure-content")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--safebrowsing-disable-download-protection")
    browser = webdriver.Chrome(options=options, service=service)
    yield browser
    browser.quit()