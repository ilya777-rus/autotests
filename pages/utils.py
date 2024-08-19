import logging

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

locations1 = [
    {"name": "СБИС - Уфа", "address": "ул. Октябрьской Революции, д. 78"},
    {"name": "СБИС | ЦЕНТР ВНЕДРЕНИЯ", "address": "ул. Менделеева, д. 219, 1ЭТАЖ"},
    {"name": "СБИС | ЦЕНТР ВНЕДРЕНИЯ", "address": "ул. Революционная, д. 173, 1ЭТАЖ"},
    {"name": "Ай-Ти Консультант", "address": "ул. Новоженова"},
    {"name": "Криптолинк", "address": "ул. Батырская 4/2 офис 404"},
    {"name": "АБТ Сервисы для бизнеса", "address": "ул. Кирова, д. 52, оф. 702 (7 этаж)"},
    {"name": "ИП Русаков В.В.", "address": "ул. Султанова, 2"},
    {"name": "РПЦИ Акцент плюс", "address": "бул. Молодежный, 10"},
    {"name": "Группа компаний Софт-Сервис", "address": "ул. Менделеева, 134/7"},
    {"name": "Корпорация РД", "address": "ул. Маршала Жукова, 29 3 этаж, блок Б"},
    {"name": "Акцент плюс", "address": "бул. Молодежный, 10"},
    {"name": "ИП Мухамедьянова Гузель Зигануровна - УФА", "address": "пр-кт Октября, д. 1, к. 2 каб. 402"}
]

locations2 = [
    {"name": "СБИС - Камчатка", "address": "ул.Ленинская, 59, оф.202, 205"},
]

# logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
# logger = logging.getLogger(__name__)
# Настройка логирования
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)  # Установите уровень логирования

# Формат сообщений
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Обработчик для вывода в консоль
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
console_handler.setLevel(logging.INFO)  # Установите уровень для консольного вывода

# Обработчик для записи в файл
file_handler = logging.FileHandler('app.log', encoding='utf-8')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)  # Установите уровень для записи в файл

# Добавляем обработчики к логгеру
logger.addHandler(console_handler)
logger.addHandler(file_handler)

def log_message(message, level = 'info'):
    levels = {
        'debug': logger.debug,
        'info': logger.info,
        'warning': logger.warning,
        'error': logger.error,
        'critical': logger.critical
    }
    log_func = levels.get(level, logger.info)
    log_func(message)


class FileDownloadComplete:
    def __init__(self, download_dir, known_files):
        self.download_dir = download_dir
        self.known_files = known_files
        self.new_file = None

    def __call__(self, driver):
        current_files = set(os.listdir(self.download_dir))
        new_files = current_files - self.known_files
        if new_files:
            self.new_file = new_files.pop()
            return self.new_file
        return False
