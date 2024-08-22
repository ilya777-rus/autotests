from .base_page import BasePage
from  .locators import TenzorAboutPageLocators
from  .utils import log_message
class TenzorAboutPage(BasePage):
    def __init__(self, browser, url):
        super().__init__(browser, url)

    def should_be_work_block(self):
        assert self.is_element_present(TenzorAboutPageLocators.BLOCK_WORK), "Блок 'Работаем' не найден"
        block_work = self.browser.find_element(*TenzorAboutPageLocators.BLOCK_WORK)
        self.scroll_to_element(block_work)
        log_message("Блок 'Работаем' успешно найден. ОК.", "info")

    def should_be_height_and_weight_photos_in_work_block(self):
        assert self.is_elements_present(TenzorAboutPageLocators.PHOTOS), 'Фотографии не обнаружены!'
        photos = self.is_elements_present(TenzorAboutPageLocators.PHOTOS)
        assert len(photos)==4, "Фотографий ожидается в количестве 4 шт"
        first_height = photos[0].get_attribute("height")
        first_width = photos[0].get_attribute("width")
        log_message(f"Размеры первой фотографии: высота={first_height}, ширина={first_width}",'info')

        for index,photo in enumerate(photos[1:], start=2):
            height = photo.get_attribute("height")
            width = photo.get_attribute("width")

            log_message(f"Фотография {index}: height={height}, width={width}", 'debug')

            assert first_height==height, f"Разные высоты: у первой фото - {first_height} , а у текущей - {height}"
            assert first_width == width, f"Разные широты: у первой фото - {first_width} , а у текущей - {width}"

        log_message("Все фотографии имеют одинаковую высоту и ширину. ОК.", 'info')