import os
import automation_practice_form_po


class AutomationPracticeFormTestSuite:
    def __init__(self):
        self.automation_practice_form = automation_practice_form_po.AutomationPracticeFormPO(
            "https://qa-guru.github.io/one-page-form/automation-practice-form.html")

    def setup(self):
        self.automation_practice_form.setup()
        self.tmp_file_name = self._create_tmp_file()

    def _create_tmp_file(self):
        file_path = os.path.abspath('test_file.jpg')
        with open(file_path, 'w') as file:
            file.write("Test")
        return file_path

    def test_form_positive01(self):
        self.automation_practice_form.fill_in_form(self.tmp_file_name, "Dmitry", "Bugaev", "bugaev@example.com", "Male",
                                                   "1234567890", ("1988", "4", "22"), ("Maths", "English"),
                                                   ("Sports", "Music"),
                                                   "г. Санкт-Петербург, ул. Невский проспект, д 101", "NCR", "Noida")
        self.automation_practice_form.assert_form(self.tmp_file_name, "Dmitry", "Bugaev", "bugaev@example.com", "Male",
                                                  "1234567890", ("1988", "4", "22"), ("Maths", "English"),
                                                  ("Sports", "Music"),
                                                  "г. Санкт-Петербург, ул. Невский проспект, д 101", "NCR", "Noida")

    def test_form_positive02(self):
        # TODO: придумай другой набор тестовых данных Сделал ниже =)
        self.automation_practice_form.fill_in_form(self.tmp_file_name, "Dmitry", "Bugaev", "bugaev@example.com", "Male",
                                                   "1234567890", ("1988", "4", "22"), ("Maths", "English"),
                                                   ("Sports", "Music"),
                                                   "г. Санкт-Петербург, ул. Невский проспект, д 101", "NCR", "Noida")
        self.automation_practice_form.assert_form(self.tmp_file_name, "Dmitry", "Bugaev", "bugaev@example.com", "Male",
                                                  "1234567890", ("1988", "4", "22"), ("Maths", "English"),
                                                  ("Sports", "Music"),
                                                  "г. Санкт-Петербург, ул. Невский проспект, д 101", "NCR", "Noida")

    def test_form_positive03(self):
        self.automation_practice_form.fill_in_form(self.tmp_file_name, "Artyr", "Klimov", "abc@mail.ru", "Male",
                                                   "2345678901", ("1992", "1", "23"), ("Physics", "Biology"),
                                                   ("Reading", ""), "г. Спб, Хасанская 12", "Rajasthan", "Jaipur")
        self.automation_practice_form.assert_form(self.tmp_file_name, "Artyr", "Klimov", "abc@mail.ru", "Male",
                                                  "2345678901", ("1992", "1", "23"), ("Physics", "Biology"),
                                                  ("Reading", ""), "г. Спб, Хасанская 12", "Rajasthan", "Jaipur")

    def test_form_not_positive(self):
        self.automation_practice_form.fill_in_form(self.tmp_file_name, first_name="", last_name="Klimov",
                                                   email="abc@mail.ru", gender="Male",
                                                   user_number="2345678901", birth_day=("1992", "1", "23"),
                                                   subjects=("Physics", "Biology"),
                                                   hobbies=("Reading", ""), current_address="г. Спб, Хасанская 12",
                                                   state="Rajasthan", city="Jaipur")
        self.automation_practice_form.get_form_error_text()

    def test_form_positive05_only_required(self):
        self.automation_practice_form.fill_in_form(first_name="Artyr",
                                                   last_name="Klimov",
                                                   gender="Male",
                                                   user_number="1234567890")
        self.automation_practice_form.assert_form_only_required_fields(first_name="Artyr",
                                                                       last_name="Klimov",
                                                                       gender="Male",
                                                                       user_number="1234567890")

    def tear_down(self):
        if os.path.exists(self.tmp_file_name):
            os.remove(self.tmp_file_name)
        self.automation_practice_form.tear_down()


test_suite = AutomationPracticeFormTestSuite()

try:
    test_suite.setup()
    test_suite.test_form_positive01()
    # TODO: в общем виде работать не будет, и в нашем виде работать не будет, так как setup и tear_down должны
    #  вызываться перед каждым тестом ... так же в идеале перед каждым тестом создается PO - подумайте как
    #  решить малой кровью (в будущем через Test Runner)
    #  Сделано ниже =)
    print("Тест 1 прошел успешно")
except Exception as e:
    print(f"Тест 1 УПАЛ С ОШИБКОЙ: {e}")
finally:
    test_suite.tear_down()

# Вызываются отдельно, по простому (тупому)
try:
    test_suite.setup()
    test_suite.test_form_positive02()
    print("Тест 2 прошел успешно")
except Exception as e:
    print(f"Тест 2 УПАЛ С ОШИБКОЙ: {e}")
finally:
    test_suite.tear_down()

try:
    test_suite.setup()
    test_suite.test_form_positive03()
    print("Тест 3 прошел успешно")
except Exception as e:
    print(f"Тест 3 УПАЛ С ОШИБКОЙ: {e}")
finally:
    test_suite.tear_down()

# Следующий негативный проверяем сообщение по валидации обязательного поля
try:
    test_suite.setup()
    test_suite.test_form_not_positive()
    print("Тест 4 прошел успешно, отобразилось сообщение валидации, а не форма оь успехе")
except Exception as e:
    print(f"Тест 4 УПАЛ С ОШИБКОЙ: {e}")
finally:
    test_suite.tear_down()

# Тест с дополнительной функцией из последней тудушки файла automation_practice_form_po.py
try:
    test_suite.setup()
    test_suite.test_form_positive05_only_required()
    print("Тест 5 прошел успешно")
except Exception as e:
    print(f"Тест 5 УПАЛ С ОШИБКОЙ: {e}")
finally:
    test_suite.tear_down()
