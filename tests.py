
import time
import pytest
from pages.home_page import HomePage
from pages.tenzor_page import TeznzorPage
from pages.tenzor_about_page import TenzorAboutPage
from pages.contact_page import ContactPage
from pages.download_page import DownloadPage
from pages.utils import log_message

LINK = "https://sbis.ru/"

@pytest.mark.scen1
def test_clcik_contact_and_banner(browser):
    log_message("Start test_clcik_contact_and_banner", "info")
    home_page = HomePage(browser, LINK)
    home_page.open()
    home_page.should_be_click_contact_link()
    contact_page = ContactPage(browser, browser.current_url)
    contact_page.should_be_click_banner_tenzor()
    tenzor_page = TeznzorPage(browser, browser.current_url)
    tenzor_page.should_be_correct_url()
    tenzor_page.should_be_block_power_in_people()
    tenzor_page.should_be_link_detailed_click()
    tenzor_about_page = TenzorAboutPage(browser, browser.current_url)
    tenzor_about_page.should_be_work_block()
    tenzor_about_page.should_be_height_and_weight_photos_in_work_block()
    log_message("End test_clcik_contact_and_banner\n", 'info')

@pytest.mark.scen2
def test_scen2(browser):
    log_message('Start test_scen2')
    home_page = HomePage(browser, LINK)
    home_page.open()
    home_page.should_be_click_contact_link()
    contact_page=ContactPage(browser, browser.current_url)

    contact_page.should_be_name_region()
    contact_page.should_be_click_region_Kamchatcka()
    contact_page.should_be_name_region_for_kamchatka()
    log_message('End test_scen2\n')

@pytest.mark.scen3
def test_scen3(browser_d):
    log_message("Старт test_scen3")
    home_page = HomePage(browser_d, LINK)
    home_page.open()
    home_page.click_local_versions()
    download_page = DownloadPage(browser_d, browser_d.current_url)
    download_page.should_be_download_sbis_plugin()
    log_message("Конец test_scen3\n")



