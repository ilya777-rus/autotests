
import pytest
from pages.home_page import HomePage
from pages.contact_page import ContactPage
from pages.download_page import DownloadPage
from pages.utils import log_message
LINK = "https://sbis.ru/"


def test_scen3(browser_d):
    log_message("Старт test_scen3")
    home_page = HomePage(browser_d, LINK)
    home_page.open()
    # home_page.should_be_click_contact_link()
    home_page.click_local_versions()
    # contact_page = ContactPage(browser_d, browser_d.current_url)
    # contact_page.click_local_versions()
    download_page = DownloadPage(browser_d, browser_d.current_url)
    download_page.should_be_download_sbis_plugin()
    log_message("Конец test_scen3\n")

@pytest.mark.skip
def test_22(browser):
    log_message("start test22")
    home_page = HomePage(browser, LINK)
    home_page.open()
    home_page.should_be_click_contact_link()
    log_message("end test22\n")