from  selenium.webdriver.common.by import By

class HomePageLocators:
    CONTACT_LINK = (By.CSS_SELECTOR, ".sbisru-Header__menu-item-1 > .sbisru-Header__menu-link")
    BANNER_TENZOR = (By.CSS_SELECTOR, ".sbisru-Contacts__border-left > .sbisru-Contacts__logo-tensor.mb-12 [alt='Разработчик системы СБИС — компания «Тензор»']")
    DOWNLOAD_FILE = (By.XPATH, "//*[text()='Скачать локальные версии']")

class ContactPageLocators:
    BANNER_TENZOR = (By.CSS_SELECTOR, ".sbisru-Contacts__border-left > .sbisru-Contacts__logo-tensor.mb-12 [alt='Разработчик системы СБИС — компания «Тензор»']")
    REGION_SELECT = (By.CSS_SELECTOR, ".sbisru-Contacts__underline  .sbis_ru-Region-Chooser__text.sbis_ru-link")
    CITY = (By.CSS_SELECTOR, "#city-id-2")
    PARTNERS = (By.CSS_SELECTOR, ".sbisru-Contacts-List__item")
    Kamchatka = (By.CSS_SELECTOR, "[title='Камчатский край']")
    Bashkortosrtan = (By.CSS_SELECTOR, "[title='Республика Башкортостан']")
    FORM_CITIES = (By.CSS_SELECTOR, "[name='dialog']")

class DownloadPageLocators:
    FILE = (By.CSS_SELECTOR, ".sbis_ru-DownloadNew-block .sbis_ru-DownloadNew-loadLink .sbis_ru-DownloadNew-loadLink__link.js-link")

class TenzorPageLocators:
    BLOCK_POWER_IN_PEOPLE = (By.CSS_SELECTOR, ".tensor_ru-Index__block4-content ")
    LINK_DETAILED = (By.CSS_SELECTOR, ".tensor_ru-Index__block4-content  .tensor_ru-link.tensor_ru-Index__link")
    POPUP = (By.CLASS_NAME, "tensor_ru-CookieAgreement")
    POPUP_ALL = (By.CLASS_NAME,"tensor_ru-CookieAgreement__message")
    OVERLAY = (By.CSS_SELECTOR, "div.preload-overlay[name='loadingOverlay']")
    OVERLAY2 = (By.CSS_SELECTOR, ".sbis_ru-CookieAgreement__message")

class TenzorAboutPageLocators:
    BLOCK_WORK = (By.CSS_SELECTOR, ".tensor_ru-About__block3 .tensor_ru-About__block-title")
    PHOTOS = (By.CSS_SELECTOR, ".tensor_ru-About__block3-image")

