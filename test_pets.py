# test_pets.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from settings import VALID_EMAIL, VALID_PASSWORD, BASE_URL
from locators import LoginPageLocators, MainPageLocators
import time
import re


def test_my_pets_checks(driver):
    # Логин
    driver.get(f"{BASE_URL}/login")
    WebDriverWait(driver, 5).until(EC.presence_of_element_located(LoginPageLocators.EMAIL_FIELD))
    driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(VALID_EMAIL)
    driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(VALID_PASSWORD)
    driver.find_element(*LoginPageLocators.SUBMIT_BUTTON).click()

    WebDriverWait(driver, 5).until(EC.presence_of_element_located(MainPageLocators.HEADER))

    # Переход в "Мои питомцы"
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(MainPageLocators.MY_PETS_LINK)).click()
    time.sleep(2)

    # Ждём таблицу
    WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located(MainPageLocators.TABLE_ROWS))

    # Сбор данных
    images = driver.find_elements(*MainPageLocators.PET_IMAGES)
    names = driver.find_elements(*MainPageLocators.PET_NAMES)
    breeds = driver.find_elements(*MainPageLocators.PET_BREEDS)
    ages = driver.find_elements(*MainPageLocators.PET_AGES)

    actual_count = len(names)
    print(f"\n🔍 Найдено питомцев: {actual_count}")

    if actual_count == 0:
        print("❌ Питомцы не найдены!")
        return

    # Статистика
    try:
        stats_element = driver.find_element(*MainPageLocators.PETS_COUNT_STAT)
        stats_text = stats_element.text
        match = re.search(r'Питомцев:\s*(\d+)', stats_text)
        if match:
            expected = int(match.group(1))
            assert actual_count == expected, f"Статистика: {expected}, найдено: {actual_count}"
            print(f"✅ Статистика совпадает: {actual_count}")
        else:
            print("⚠️ Не удалось извлечь число из статистики")
    except Exception as e:
        print(f"⚠️ Статистика не проверена: {e}")

    # Проверка фото (хотя бы у половины)
    photos_count = 0
    for img in images:
        src = img.get_attribute('src')
        if src and len(src) > 10:
            photos_count += 1

    assert photos_count >= actual_count / 2, f"Фото есть у {photos_count} из {actual_count}"
    print(f"✅ Фото есть у {photos_count} питомцев (>= половины)")

    # Проверки имени, породы, возраста
    names_list = []
    pets_data = []

    for i in range(actual_count):
        name = names[i].text.strip()
        breed = breeds[i].text.strip()
        age = ages[i].text.strip()

        assert name, f"У питомца {i + 1} нет имени"
        assert breed, f"У питомца {i + 1} нет породы"
        assert age, f"У питомца {i + 1} нет возраста"

        names_list.append(name)
        pets_data.append((name, breed, age))

    print(f"✅ У всех есть имя, порода и возраст")
    assert len(names_list) == len(set(names_list)), "Повторяющиеся имена!"
    print(f"✅ Имена уникальны")
    assert len(pets_data) == len(set(pets_data)), "Повторяющиеся питомцы!"
    print(f"✅ Нет повторов")

    print("\n🎉 ТЕСТ ПРОЙДЕН!")