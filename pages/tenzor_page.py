import time

from .base_page import BasePage
from  .locators import TenzorPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException

from .utils import log_message


class TeznzorPage(BasePage):
    def __init__(self, browser, url):
        super().__init__(browser, url)

    def should_be_correct_url(self):
        assert self.url_to_be("https://tensor.ru/"), "Url не соответствует https://tensor.ru/!"

    def should_be_block_power_in_people(self):
        element_block_power_in_people = self.is_element_present(TenzorPageLocators.BLOCK_POWER_IN_PEOPLE)
        assert element_block_power_in_people, "Блок 'Сила в людях' не найден!"
        self.scroll_to_element(element_block_power_in_people)
        log_message("Блок 'Сила в людях' успешно найден. ОК.", "info")


    def should_be_link_detailed_click(self):
        assert self.is_element_present(TenzorPageLocators.LINK_DETAILED), "Ссылка 'Подробнее' отсутствует !"
        self.pop_up_delete(TenzorPageLocators.POPUP)


        element_link_detyled = self.find_element_and_click_with_retry(TenzorPageLocators.LINK_DETAILED)
        assert element_link_detyled , "Элемент ссылка 'Подробнее' не кликабельна!"
        log_message("Клик на ссылку 'Подробнее' выполнен успешно. ОК.", "info")
        # self.switch_to_current_window()
        # assert self.browser.current_url == "https://tensor.ru/about", "ссылка не соответствует:https://tensor.ru/about url about"
        assert self.url_to_be("https://tensor.ru/about"), "URL ссылка не соответствует:https://tensor.ru/about "

    def hide_preload_overlay(self):
        try:
            overlay = WebDriverWait(self.browser, 6).until(
                EC.visibility_of_element_located(TenzorPageLocators.OVERLAY)
            )
            self.browser.execute_script("arguments[0].style.display = 'none';", overlay)
        except Exception as e:
            print(f"Error hiding overlay")