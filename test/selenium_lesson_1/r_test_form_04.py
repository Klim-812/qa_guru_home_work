import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#Первый шаг - выделение каждого теста в отдельную функцию и ее последующий вызов

def test01():
    print("Рефакторинг - итерация 1!")

    # 1. Запуск браузера Chrome
    driver = webdriver.Chrome()

    try:
        # 2. Открытие страницы
        driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
        driver.maximize_window()
        time.sleep(5)  # Пауза, чтобы визуально заметить открытие

        # 3. Поиск элементов и заполнение полей
        # Находим поле Full Name по его ID и вводим текст
        full_name_field = driver.find_element(By.ID, "userName")
        #web_elements = driver.find_elements(By.XPATH, "someXPath")

        full_name_field.send_keys("Климов Артур")

        # Находим поле Email по его ID и вводим текст
        email_field = driver.find_element(By.ID, "userEmail")
        email_field.send_keys("ivan@example.com")

        # Находим кнопку Submit по ее ID и кликаем
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        # 4. Проверка результата
        time.sleep(5)  # Пауза, чтобы увидеть результат отправки

        # Находим блок с отправленными данными
        result_box = driver.find_element(By.ID, "output")

        # Проверяем, что в блоке результата появился введенный текст
        assert "Климов Артур" in result_box.text
        print("Тест успешно пройден! Данные введены верно")

    finally:
        # 5. Закрытие браузера в любом случае
        driver.quit()

def test02():
    print("Рефакторинг - итерация 1!")

    # 1. Запуск браузера Chrome
    driver = webdriver.Chrome()

    try:
        # 2. Открытие страницы
        driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
        driver.maximize_window()
        time.sleep(5)  # Пауза, чтобы визуально заметить открытие

        # 3. Поиск элементов и заполнение полей
        # Находим поле Full Name по его ID и вводим текст
        full_name_field = driver.find_element(By.ID, "userName")
        #web_elements = driver.find_elements(By.XPATH, "someXPath")

        full_name_field.send_keys("")

        # Находим поле Email по его ID и вводим текст
        email_field = driver.find_element(By.ID, "userEmail")
        email_field.send_keys("ivanexample.com")

        # Находим кнопку Submit по ее ID и кликаем
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        # 4. Проверка результата
        time.sleep(5)  # Пауза, чтобы увидеть результат отправки

        # Находим блок с отправленными данными
        result_box = driver.find_element(By.ID, "output")

        # Проверяем, что в блоке результата появился введенный текст
        if result_box.is_displayed():
            assert "ivanexample.com" in result_box.text
            print("Тест успешно пройден!")
        else:
            print("Имейл указан неверно")

    finally:
        # 5. Закрытие браузера в любом случае
        driver.quit()

def test03():
    print("Рефакторинг - итерация 1! Поле fullname принимает цифры ")

    # 1. Запуск браузера Chrome
    driver = webdriver.Chrome()

    try:
        # 2. Открытие страницы
        driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
        driver.maximize_window()
        time.sleep(5)  # Пауза, чтобы визуально заметить открытие

        # 3. Поиск элементов и заполнение полей
        # Находим поле Full Name по его ID и вводим текст
        full_name_field = driver.find_element(By.ID, "userName")

        full_name_field.send_keys('12345 6789')

        # Находим кнопку Submit по ее ID и кликаем
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        # 4. Проверка результата
        time.sleep(5)  # Пауза, чтобы увидеть результат отправки

        # Находим блок с отправленными данными
        result_box = driver.find_element(By.ID, "output")

        # Проверяем, что в блоке результата появился введенный текст
        assert '12345 6789' in result_box.text
        print("Тест успешно пройден! Full name принимает цифры")

    finally:
        # 5. Закрытие браузера в любом случае
        driver.quit()

def test04():
    print("""
    Рефакторинг - итерация 1! Добавлены тесты на Current Address и Permanent Address, 
    а так же проверка плейсхолдера Current Address
    """)

    # 1. Запуск браузера Chrome
    driver = webdriver.Chrome()

    try:
        # 2. Открытие страницы
        driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
        driver.maximize_window()
        time.sleep(5)  # Пауза, чтобы визуально заметить открытие

        # 4. Поиск элементов и заполнение полей
        # Находим поле currentAddress по его ID, проверяем что есть плейсхолдер и вводим текст
        current_address_field = driver.find_element(By.ID, "currentAddress")
        actual_placeholder = current_address_field.get_attribute("placeholder")
        expected_placeholder = "Current Address"

        current_address_field.send_keys("Санкт-Петербург, Маршала Казакова 10 к 1")

        # Находим поле Permanent Address по его ID и вводим текст
        permanent_address = driver.find_element(By.ID, "permanentAddress")
        permanent_address.send_keys("Санкт-Петербург, Хасанская 117")

        # Находим кнопку Submit по ее ID и кликаем
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        # 5. Проверка результата
        time.sleep(5)  # Пауза, чтобы увидеть результат отправки

        # Находим блок с отправленными данными
        result_box = driver.find_element(By.ID, "output")

        # Проверяем, что в блоке результата появился введенный текст и плейсхолдер корректный
        assert "Санкт-Петербург, Маршала Казакова 10 к 1" and "Санкт-Петербург, Хасанская 117" in result_box.text
        assert actual_placeholder == expected_placeholder
        print("Тест успешно пройден! Выведены currentAddress и permanentAddress, плейсхолдер верный")

    finally:
        # 5. Закрытие браузера в любом случае
        driver.quit()

test01()
test02()
test03()
test04()
