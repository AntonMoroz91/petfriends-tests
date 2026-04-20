# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(autouse=True)
def driver():
    # Опционально: запуск в фоне (раскомментируй, если нужно)
    # chrome_options = Options()
    # chrome_options.add_argument("--headless")

    driver = webdriver.Chrome()
    driver.implicitly_wait(10)  # Неявное ожидание для всех элементов (задание 30.5.1)
    driver.maximize_window()

    yield driver

    driver.quit()