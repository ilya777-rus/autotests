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

    def hide_preload_overlay2(self):
        try:
            overlay = WebDriverWait(self.browser, 6).until(
                EC.visibility_of_element_located(TenzorPageLocators.OVERLAY)
            )
            self.browser.execute_script("arguments[0].style.display = 'none';", overlay)
        except Exception as e:
            # print(f"Error hiding overlay")
            return

    def should_be_name_region(self):
        # try:
        #     self.hide_preload_overlay2()
        #     assert self.is_element_present(ContactPageLocators.REGION_SELECT), "nor region select"
        #     el = self.browser.find_element(*ContactPageLocators.REGION_SELECT)
        #     print("TEXT REGION", el.text, el.text== "Республика Башкортостан")
        #     assert el.text == "Республика Башкортостан", "not is region"
        #     assert self.is_element_present(ContactPageLocators.CITY), "not name city region"
        #     assert self.browser.find_element(*ContactPageLocators.CITY).text.strip() == "Уфа", "not is UFA !"
        #     self.should_be_patrners(locations1)
        # except StaleElementReferenceException as e:
        #     assert self.is_element_present(ContactPageLocators.REGION_SELECT), "nor region select"
        #     assert self.browser.find_element(
        #         *ContactPageLocators.REGION_SELECT).text == "Республика Башкортостан", "not is region"
        #     assert self.is_element_present(ContactPageLocators.CITY), "not name city region"
        #     assert self.browser.find_element(*ContactPageLocators.CITY).text.strip() == "Уфа", "not is UFA !"
        #     self.should_be_patrners(locations1)

        self.hide_preload_overlay2()
        element_select = self.is_element_present(ContactPageLocators.REGION_SELECT)
        assert element_select, "Нет элемента выбора регионов !"
        assert element_select.text == "Республика Башкортостан", "Название региона неверное! Ожидается Республика Башкортостан"
        element_city = self.is_element_present(ContactPageLocators.CITY)
        assert element_city, "Элемент города региона не присутствует!"
        assert element_city.text.strip() == "Уфа", "города региона неверное, ожидается 'Уфа'"
        self.should_be_patrners(locations1)
        log_message("Регион определен корректно и список партнеров успешно загружен. ОК.", "info")

    def should_be_click_region_Kamchatcka(self):
        # assert self.is_element_present(ContactPageLocators.REGION_SELECT), "not region select"
        # el = self.el_click(ContactPageLocators.REGION_SELECT, 14)
        # el.click()
        # assert self.is_element_present(ContactPageLocators.Kamchatka), "NOT kamchatka"
        # el2 = self.el_click(ContactPageLocators.Kamchatka)
        # el2.click()
        assert self.is_element_present(ContactPageLocators.REGION_SELECT), "Нет элемента выбора регионов !"
        element_select_regions = self.find_element_and_click_with_retry(ContactPageLocators.REGION_SELECT, 14)
        assert element_select_regions, "элемента выбора регионов не кликабельный!"
        log_message("Ссылка для выбора регионов успешно кликнута. ОК.", "info")
        assert self.is_element_present(ContactPageLocators.Kamchatka), "Ссылка на регион Камачатка не присутствует!"
        element_kamchatka = self.find_element_and_click_with_retry(ContactPageLocators.Kamchatka)
        assert element_kamchatka, "Ссылка на регион Камачатка не кликабельна!"
        log_message("Ссылка на регион Камачатка успешно кликнута. ОК.", "info")

    def should_be_click_region_Bashkort(self):
        assert self.is_element_present(ContactPageLocators.REGION_SELECT), "Нет элемента выбора регионов !"
        element_select_regions = self.find_element_and_click_with_retry(ContactPageLocators.REGION_SELECT, 14)
        assert element_select_regions, "элемента выбора регионов не кликабельный!"
        assert self.is_element_present(ContactPageLocators.Bashkortosrtan), "Ссылка на регион Башкортостан не присутствует!"
        element_bashkortostan = self.find_element_and_click_with_retry(ContactPageLocators.Bashkortosrtan)
        assert element_bashkortostan, "Ссылка на регион Башкортостан не кликабельна!"

    def should_be_name_region_for_kamchatka(self):
        # assert self.is_element_present(ContactPageLocators.REGION_SELECT), "nor region select"
        # assert self.el_text_change(ContactPageLocators.REGION_SELECT,
        #                            "Камчатский край"), "text not change on Kamchatcka!"
        # element = self.browser.find_element(*ContactPageLocators.REGION_SELECT)
        # assert element.text == "Камчатский край", "not is region"
        #
        # assert self.is_element_present(ContactPageLocators.CITY), "not name city region"
        # assert self.browser.find_element(
        #     *ContactPageLocators.CITY).text.strip() == "Петропавловск-Камчатский", "not is Петропавловск-Камчатский !!!"
        # self.should_be_patrners(locations2)
        #
        # assert self.browser.title == "СБИС Контакты — Камчатский край", "title not correct !!!!!"
        # assert "41-kamchatskij-kraj" in self.browser.current_url, "kamchatsk kray not in URL !!!"

        #
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

        # assert self.browser.title == "СБИС Контакты — Камчатский край", "Заголовок страницы неверный!"
        assert self.title_is("СБИС Контакты — Камчатский край"), "TITLEEEE Заголовок страницы неверный!"
        # assert "41-kamchatskij-kraj" in self.browser.current_url, "В URL не найдено '41-kamchatskij-kraj'!"
        assert self.url_contains("41-kamchatskij-kraj"), "В URL не найдено '41-kamchatskij-kraj'!"
        log_message('Проверка региона Камчатский край завершена успешно. ОК.')

    def should_be_patrners(self, locations):
        # patrners = self.browser.find_elements(*ContactPageLocators.PARTNERS)
        # print("PARTNERSS",  patrners)
        patrners = self.is_elements_present(ContactPageLocators.PARTNERS)
        # print("PARTNERSS",ptrns)
        # print(len(ptrns)==len(patrners))
        for i, p in enumerate(patrners[:len(locations)]):
            arr = p.text.split('\n')
            # assert arr[0] == locations[i]['name'], f"current name city {arr[0]} not correct is {locations[i]['name']}"
            assert arr[0] == locations[i][
                'name'], f"Текущее имя города {arr[0]} неверное, должно быть {locations[i]['name']}"
            # assert arr[1] == locations[i][
            #     'address'], f"current address city {arr[1]} not correct is {locations[i]['address']}"
            assert arr[1] == locations[i][
                'address'], f"Текущий адрес города {arr[1]} неверный, должен быть {locations[i]['address']}"



