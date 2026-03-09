from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    """
    Класс для работы со страницей оформления заказа интернет-магазина SauceDemo

    На этой странице пользователь заполняет свои данные (имя, фамилию, индекс)
    и видит итоговую стоимость заказа перед подтверждением
    """

    def __init__(self, driver):
        """
        Создает объект страницы оформления заказа
        """
        self.driver = driver
        # Ждем появления элементов до 10 секунд
        self.wait = WebDriverWait(driver, 10)

    def fill_shipping_info(
            self, first_name: str, last_name: str, postal_code: str):
        """
        Заполняет форму с данными покупателя

        1. Ждет появления поля для имени и вводит имя
        2. Находит поле для фамилии и вводит фамилию
        3. Находит поле для почтового индекса и вводит индекс

        first_name - имя покупателя (строка) Например: "Иван"
        last_name - фамилия покупателя (строка) Например: "Петров"
        postal_code - почтовый индекс (строка) Например: "123456"
        """
        # Вводим имя (ждем пока поле появится)
        first_name_field = self.wait.until(
            EC.presence_of_element_located((By.ID, "first-name"))
        )
        first_name_field.send_keys(first_name)
        print(f"✅ Введено имя: {first_name}")

        # Вводим фамилию
        last_name_field = self.driver.find_element(By.ID, "last-name")
        last_name_field.send_keys(last_name)
        print(f"Введена фамилия: {last_name}")

        # Вводим почтовый индекс
        postal_code_field = self.driver.find_element(By.ID, "postal-code")
        postal_code_field.send_keys(postal_code)
        print(f"Введен индекс: {postal_code}")

        return self

    def continue_to_overview(self):
        """
        Переходит к просмотру заказа

        1. Находит кнопку Continue и нажимает ее
        2. Ждет пока загрузится страница с итоговой суммой
        """
        # Нажимаем кнопку Continue
        continue_button = self.driver.find_element(By.ID, "continue")
        continue_button.click()
        print("Нажимаем кнопку Continue")

        # Ждем пока появится итоговая сумма
        self.wait.until(
            EC.presence_of_element_located((
                By.CLASS_NAME, "summary_total_label"))
        )
        print("Страница с итоговой суммой загружена")

        return self

    def get_total_price(self) -> str:
        """
        Получает итоговую стоимость заказа со страницы

        1. Ждет пока появится элемент с итоговой суммой
        2. Берет текст из элемента (например "Total: $58.29")
        3. Вырезает из текста только число (убирает "Total: $")

        Возвращает:
        Строку с итоговой стоимостью (только число)
        Например: "58.29"
        """
        # Ждем пока появится элемент с итоговой суммой
        total_element = self.wait.until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "summary_total_label"))
        )

        # Получаем текст (например "Total: $58.29")
        total_text = total_element.text
        print(f"Текст с суммой: {total_text}")

        # Вырезаем только число
        # split("$")[-1] берет все что после знака $
        total_value = total_text.split("$")[-1]

        return total_value
