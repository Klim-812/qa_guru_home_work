import pytest
import os

# Сделаны туду:
# 1) Написать тест для "API", который через indirect фикстуру меняет заголовки авторизации (User, Admin, Guest).
@pytest.mark.parametrize("auth_headers",["User","Admin","Guest"], indirect= True)
def test_api_auth(auth_headers):
    print(f"-> Заголовок: {auth_headers}")
    # Проверяем, что возвращается строка (если Guest — "None", иначе "Bearer")
    if auth_headers == "None":
        assert True  # Гость без токена — ок
    else:
        assert auth_headers.startswith("Bearer ")

# 2) Написать динамическую параметризацию, которая сканирует указанную папку и генерирует тесты под каждый найденный там .txt или .json файл.
def test_dynamic_scan_file(dynamic_file_scenario):
    print(f"\n-> Запуск динамического сценария: {dynamic_file_scenario['id']}")

    filepath = dynamic_file_scenario['filepath']

    if filepath:
        print(f"-> Обработка файла: {filepath}")
        assert os.path.exists(filepath)
    else:
        # Если папка была пуста
        print("-> Файлы не найдены, проверяем заглушку")
        assert filepath is None

# 3) Сделать комбинаторный тест формы регистрации (Имя * Фамилия * Возраст) с красивыми кастомными ids.
@pytest.mark.parametrize("first_name",["Ivan","Olga","Анна"],ids=lambda x:f"name_{x}")
@pytest.mark.parametrize("last_name",["Ivanov","Petrova","Смирнова"],ids=lambda x:f"surname_{x}")
@pytest.mark.parametrize("age",[19,25,32],ids=lambda x:f"age_{x}")
def test_kombi_registration(first_name,last_name,age):
    print(f"\n[Регистрация] Имя: {first_name}, Фамилия: {last_name}, Возраст: {age}")

    # Имитация бизнес-логики: регистрация разрешена только с 18 лет
    assert age >= 19