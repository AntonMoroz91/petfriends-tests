# locators.py
from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL_FIELD = (By.ID, "email")
    PASSWORD_FIELD = (By.ID, "pass")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")


class MainPageLocators:
    HEADER = (By.TAG_NAME, "h1")
    MY_PETS_LINK = (By.LINK_TEXT, "Мои питомцы")

    # Статистика — ищем по нормализованному тексту
    PETS_COUNT_STAT = (By.XPATH, "//div[contains(normalize-space(), 'Питомцев')]")

    # Таблица
    TABLE_ROWS = (By.CSS_SELECTOR, "table.table tbody tr")
    PET_IMAGES = (By.CSS_SELECTOR, "table.table tbody tr th img")
    PET_NAMES = (By.CSS_SELECTOR, "table.table tbody tr td:nth-child(2)")
    PET_BREEDS = (By.CSS_SELECTOR, "table.table tbody tr td:nth-child(3)")
    PET_AGES = (By.CSS_SELECTOR, "table.table tbody tr td:nth-child(4)")