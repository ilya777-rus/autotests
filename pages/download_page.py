import os
from .home_page import HomePage
from  .locators import DownloadPageLocators
from .utils import log_message

class DownloadPage(HomePage):
    def should_be_download_sbis_plugin(self):
        assert self.is_element_present(DownloadPageLocators.FILE), "Нет ссылки для скачивания файла!"
        log_message("Элемент для скачивания файла присутствует. ОК.")
        element_download_file = self.find_element_and_click_with_retry(DownloadPageLocators.FILE,35)
        assert element_download_file , "Элемент для скачивания файла не кликабельной!"
        log_message("Элемент для скачивания файла был успешно кликнут. ОК.")
        download_directory = os.getcwd()
        known_files = set(os.listdir(download_directory))
        self.alert()
        new_file_path = self.complete_download_file(download_directory, known_files)
        assert os.path.isfile(new_file_path), f"Файл не был загружен! Новый путь файла: {new_file_path}"
        log_message("Плагин был успешно скачен. ОК.")
        assert 'sbisplugin-setup-web' in new_file_path, f"Имя файла должно содержать 'sbisplugin-setup-web', а текущее {new_file_path}"
        file_size_mb = self.get_file_size_in_mb(new_file_path)
        assert file_size_mb == 11.05, f"Размер файла - {file_size_mb} MB, ожидаемое {11.05} MB."
        log_message("Размер скаченного файла совпадает с указанным на сайте. ОК.")
