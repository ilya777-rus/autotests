import os

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from .utils import FileDownloadComplete, log_message
import time

class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        log_message(f"Открытие {self.url}")
        self.browser.get(self.url)

    def is_element_present(self, locator, time=10, retry=5):
        for attemt in range(retry):
            try:
                el = WebDriverWait(self.browser, time).until(EC.presence_of_element_located(locator))
                # print("is_element_present",bool(el), el==True)
                return el
            except StaleElementReferenceException as e:
                log_message(
                    f"Попытка {attemt + 1} из {retry} не удалась из-за StaleElementReferenceException. Пробуем еще раз...",
                    'warning')
        raise  TimeoutException("Не удалось найти элемент за определенное время!")
            # except TimeoutException as e:
            #     print(e.msg)
            #     return False
            # return True

    def is_elements_present(self, locator, time=16, retry=5):
        for attemt in range(retry):
            try:
                elements = WebDriverWait(self.browser, time).until(EC.presence_of_all_elements_located(locator))
                return elements
            except StaleElementReferenceException as e:
                log_message(
                    f"Попытка {attemt + 1} из {retry} не удалась из-за StaleElementReferenceException. Пробуем еще раз...",
                    'warning')
        raise TimeoutException("Не удалось найти элементы за определенное время!")

    def el_click(self, locator, time=10):
        try:
            el = WebDriverWait(self.browser, time).until(EC.element_to_be_clickable(locator))
            return el

        except TimeoutException as e:
            print(e.msg)
            return False

    def el_text_change(self, locator, text, time=10, retry=5):
        for attemt in range(retry):
            try:
                el = WebDriverWait(self.browser, time).until(EC.text_to_be_present_in_element(locator, text))
                return el
            except StaleElementReferenceException as e:
                log_message(
                    f"Попытка {attemt + 1} из {retry} не удалась из-за StaleElementReferenceException. Пробуем еще раз...",
                    'warning')
        raise TimeoutException("Не удалось найти изменение текста!!")


    def alert(self):
        try:
            alert = WebDriverWait(self.browser, 3).until(EC.alert_is_present())
            alert.accept()
        except TimeoutException as e:
            print("Errror alert ")

    def complete_download_file(self, download_directory, known_files, times=8):
        try:
            start_t=time.time()
            file_download_wait = WebDriverWait(self.browser, times).until(
                FileDownloadComplete(download_directory, known_files)
            )
            end_t = time.time()
            elapsed_time = end_t - start_t

            print(f"Время выполнения: {elapsed_time:.2f} секунд")
            if file_download_wait:
                new_file_path = os.path.join(download_directory, file_download_wait)
            else:
                return False
        except TimeoutException as e:
            print('error', e.msg)
            return False
        return new_file_path

    def get_file_size_in_mb(self, file_path):
        size_bytes = os.path.getsize(file_path)
        size_mb = size_bytes / (1024 * 1024)
        return round(size_mb, 2)

    def switch_to_current_window(self):
        handles = self.browser.window_handles
        self.browser.switch_to.window(handles[-1])

    def scroll_to_element(self, element):
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)

    def pop_up_delete(self, locator, retry=5):
        for attemt in range(retry):
            try:
                el = WebDriverWait(self.browser, 12).until(
                    EC.presence_of_element_located(locator)
                )
                # self.browser.execute_script("""
                #     var element = document.getElementsByClassName('tensor_ru-CookieAgreement')[0];
                #     if (element) {
                #         element.parentNode.removeChild(element);
                #     }
                # """)
                self.browser.execute_script("arguments[0].style.display = 'none';", el)
                # el2 = WebDriverWait(self.browser, 5).until(
                #     EC.invisibility_of_element_located(locator)
                # )
                # el2 = WebDriverWait(self.browser, 5).until_not(EC.presence_of_element_located(locator))
                print("Элемент был удален.")
                return
            # except TimeoutException as e:
            #     print("Не удалось удалить элемент за время:", str(e))
            except StaleElementReferenceException as e:
                log_message(
                    f"Попытка {attemt + 1} из {retry} не удалась из-за StaleElementReferenceException. Пробуем еще раз...",
                    'warning')
        raise TimeoutException("Не удалось удалить элемент за время:!!")

    def element_until_find(self, locator):
        try:
            el = WebDriverWait(self.browser, 5).until_not(EC.presence_of_element_located(locator))
            return el
        except TimeoutException:

            log_message(
                f"Не удалось за время подтвердить , что елемент отсутствует",
                'warning')


    def find_element_and_click_with_retry(self, locator, time=12, retry=5, delay=1):
        for attemt in range(retry):
            try:
                WebDriverWait(self.browser, time).until(EC.element_to_be_clickable(locator)).click()
                return True
            except StaleElementReferenceException as e:
                 # print(f"Попытка {attemt+1} не удалась из {retry}. Пробуем еще...")
                 log_message(f"Попытка {attemt + 1} из {retry} не удалась из-за StaleElementReferenceException. Пробуем еще раз...", 'warning')
                # time.sleep(delay)
        raise TimeoutException("Не удалось найти элемент после нескольких попыток!")

    def find_element_with_retry_for_present(self, locator, time=12, retry=5, delay=1):
        for attemt in range(retry):
            try:
                element = WebDriverWait(self.browser, time).until(EC.element_to_be_clickable(locator))
                return element
            except StaleElementReferenceException as e:
                # print(f"Попытка {attemt+1} не удалась из {retry}. Пробуем еще...")
                log_message(
                    f"Попытка {attemt + 1} из {retry} не удалась из-за StaleElementReferenceException. Пробуем еще раз...",
                    'warning')
                # time.sleep(delay)
        raise TimeoutException("Не удалось найти элемент после нескольких попыток!")

    def url_to_be(self, exepted_url, time=5):
        try:
            res = WebDriverWait(self.browser, time).until(EC.url_to_be(exepted_url))
            return res
        except TimeoutException as e:
            log_message("Не удалось найти ожидаемый url!", 'error')

    def url_contains(self, contain_url, time=5):
        try:
            res = WebDriverWait(self.browser, time).until(EC.url_contains(contain_url))
            return res
        except TimeoutException as e:
            log_message(f"Не удалось найти фрагмент:{contain_url} ожидаемого url!", 'error')

    def title_is(self, expected_title, time = 5):
        try:
            res = WebDriverWait(self.browser, time).until(EC.title_is(expected_title))
            return res
        except TimeoutException as e:
            log_message("Не удалось найти ожидаемый title!", 'error')