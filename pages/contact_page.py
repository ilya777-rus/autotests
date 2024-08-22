import os

from .base_page import BasePage
from .locators import ContactPageLocators, TenzorPageLocators
import time
from .utils import locations1, locations2, FileDownloadComplete, log_message
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ContactPage(BasePage):
    def __init__(self, browser, url):
        super().__init__(browser, url)

    def should_be_click_banner_tenzor(self):
        assert self.is_element_present(ContactPageLocators.BANNER_TENZOR), "Баннер Тензор не присутствует"
        banner_element = self.find_element_and_click_with_retry(ContactPageLocators.BANNER_TENZOR)
        assert banner_element, "Баннер Тензора не кликабельный !"
        log_message("Клик на баннер 'Тензор' выполнен успешно. ОК.", "info")
        self.switch_to_current_window()

    def hide_preload_overlay2(self, locator):
        try:
            overlay = WebDriverWait(self.browser, 6).until(
                EC.visibility_of_element_located(locator)
            )
            self.browser.execute_script("arguments[0].style.display = 'none';", overlay)
            # print("overlay удаленн")
        except Exception as e:
            # print(f"Error hiding overlay")
            return

    def should_be_name_region(self):
        self.hide_preload_overlay2(TenzorPageLocators.OVERLAY)
        element_select = self.is_element_present(ContactPageLocators.REGION_SELECT)
        assert element_select, "Нет элемента выбора регионов !"
        assert element_select.text == "Республика Башкортостан", "Название региона неверное! Ожидается Республика Башкортостан"
        element_city = self.is_element_present(ContactPageLocators.CITY)
        assert element_city, "Элемент города региона не присутствует!"
        assert element_city.text.strip() == "Уфа", "города региона неверное, ожидается 'Уфа'"
        self.should_be_patrners(locations1)
        log_message("Регион определен корректно и список партнеров успешно загружен. ОК.", "info")

    def should_be_click_region_Kamchatcka(self):
        self.hide_preload_overlay2(TenzorPageLocators.OVERLAY2)
        assert self.is_element_present(ContactPageLocators.REGION_SELECT), "Нет элемента выбора регионов !"
        element_select_regions = self.find_element_and_click_with_retry(ContactPageLocators.REGION_SELECT, 14)
        assert element_select_regions, "элемента выбора регионов не кликабельный!"
        log_message("Ссылка для выбора регионов успешно кликнута. ОК.", "info")
        assert self.is_element_present(ContactPageLocators.Kamchatka), "Ссылка на регион Камачатка не присутствует!"
        element_kamchatka = self.find_element_and_click_with_retry(ContactPageLocators.Kamchatka)
        assert element_kamchatka, "Ссылка на регион Камачатка не кликабельна!"
        log_message("Ссылка на регион Камачатка успешно кликнута. ОК.", "info")

    # def should_be_click_region_Bashkort(self):
    #     assert self.is_element_present(ContactPageLocators.REGION_SELECT), "Нет элемента выбора регионов !"
    #     element_select_regions = self.find_element_and_click_with_retry(ContactPageLocators.REGION_SELECT, 14)
    #     assert element_select_regions, "элемента выбора регионов не кликабельный!"
    #     assert self.is_element_present(ContactPageLocators.Bashkortosrtan), "Ссылка на регион Башкортостан не присутствует!"
    #     element_bashkortostan = self.find_element_and_click_with_retry(ContactPageLocators.Bashkortosrtan)
    #     assert element_bashkortostan, "Ссылка на регион Башкортостан не кликабельна!"

    def should_be_name_region_for_kamchatka(self):
        element_region_select = self.is_element_present(ContactPageLocators.REGION_SELECT)
        assert element_region_select, "Элемент выбора региона не присутствует"
        assert self.el_text_change(ContactPageLocators.REGION_SELECT, "Камчатский край"), "Текст не изменился на Камчатский край!"
        assert element_region_select.text == "Камчатский край", "Регион не 'Камчатский край'"
        log_message('Текст изменился на Камчатский край. ОК.')

        element_city = self.is_element_present(ContactPageLocators.CITY)
        assert element_city, "Элемент города региона не присутствует"
        assert element_city.text.strip() == "Петропавловск-Камчатский", "Название города не Петропавловск-Камчатский!"
        log_message('Назвавние города изменилось на Петропавловск-Камчатский. ОК.')
        self.should_be_patrners(locations2)
        log_message("Проверка списка партнеров завершена успешно. ОК.")

        assert self.title_is("СБИС Контакты — Камчатский край"), "TITLEEEE Заголовок страницы неверный!"

        assert self.url_contains("41-kamchatskij-kraj"), "В URL не найдено '41-kamchatskij-kraj'!"
        log_message('Проверка региона Камчатский край завершена успешно. ОК.')

    def should_be_patrners(self, locations):
        patrners = self.is_elements_present(ContactPageLocators.PARTNERS)

        for i, p in enumerate(patrners[:len(locations)]):
            arr = p.text.split('\n')

            assert arr[0] == locations[i][
                'name'], f"Текущее имя города {arr[0]} неверное, должно быть {locations[i]['name']}"

            assert arr[1] == locations[i][
                'address'], f"Текущий адрес города {arr[1]} неверный, должен быть {locations[i]['address']}"



