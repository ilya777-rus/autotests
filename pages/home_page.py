from .base_page import BasePage
from .locators import HomePageLocators
import time
from selenium.common.exceptions import StaleElementReferenceException
from .utils import  log_message

class HomePage(BasePage):

    def __init__(self, browser, url):
        super().__init__(browser, url)

    def should_be_click_contact_link(self):
        # try:
        #     assert self.is_element_present(HomePageLocators.CONTACT_LINK), "contac link is not  !"
        #     el = self.el_click(HomePageLocators.CONTACT_LINK)
        #     el.click()
        # except  StaleElementReferenceException as e:
        #     print("Erroor ", str(e))
        #     self.el_click(HomePageLocators.CONTACT_LINK).click()

        assert self.is_element_present(HomePageLocators.CONTACT_LINK), "Ссылка 'Контакты' не присутствует!"
        log_message("Ссылка 'Контакты' присутствует. ОК.", "info")
        contact_element = self.find_element_and_click_with_retry(HomePageLocators.CONTACT_LINK)
        assert contact_element, "Ссылка 'Контакты' не кликабельная!"
        log_message("Клик на ссылку 'Контакты' выполнен успешно. ОК.", "info")
        # try:
        #     contact_element.click()
        #     log_message("Клик на ссылку 'Контакты' выполнен успешно. ОК.", "info")
        # except Exception as e:
        #     log_message(f"Клик на ссылку 'Контакты' не удалось выполнить. ERROR: {str(e)} ", "error")
            # contact_element.click()

    def click_local_versions(self):
        # assert self.is_element_present(HomePageLocators.DOWNLOAD_FILE), "not link for download file"
        # element = self.el_click(HomePageLocators.DOWNLOAD_FILE)
        # self.scroll_to_element(element)
        # element.click()
        element_local_versions = self.is_element_present(HomePageLocators.DOWNLOAD_FILE)
        assert element_local_versions, "ссылка на локальные версии не присутствует!"
        log_message("Ссылка на локальные версии успешно найдена. ОК.")
        self.scroll_to_element(element_local_versions)
        element_local_versions_click = self.find_element_and_click_with_retry(HomePageLocators.DOWNLOAD_FILE)
        assert element_local_versions_click, "ссылка на локальные версии не кликабельна!"

        # self.scroll_to_element(element_local_versions)
        # element_local_versions.click()
        log_message("Ссылка на локальные версии успешно кликнута. ОК.")


