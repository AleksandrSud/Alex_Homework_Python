from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    """
    Класс для работы со страницей калькулятора.
    Содержит методы для нажатия кнопок и получения результата.
    """

    def __init__(self, driver):
        """
        Сохраняем драйвер и создаем ожидание.

        Аргументы:
            driver: сюда передаем драйвер браузера (Chrome, Firefox и т.д.)
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

        # Локаторы элементов на странице (где искать)
        self.delay_field = (By.CSS_SELECTOR, "#delay")  # поле ввода задержки
        self.result_screen = (By.CSS_SELECTOR, ".screen"
                              )  # экран с результатом

        # Кнопки калькулятора
        self.button_7 = (By.XPATH, "//span[text()='7']")
        self.button_plus = (By.XPATH, "//span[text()='+']")
        self.button_8 = (By.XPATH, "//span[text()='8']")
        self.button_equals = (By.XPATH, "//span[text()='=']")

    def open(self):
        """
        Открывает страницу калькулятора в браузере.

            self - возвращает себя, чтобы можно было писать методы подряд
        """
        self.driver.get(
            "https://bonigarcia.dev/"
            "selenium-webdriver-java/slow-calculator.html"
        )
        return self

    def set_delay(self, delay_value):
        """
        Вводит значение задержки в поле #delay.

            delay_value: число (например, 45) - сколько секунд ждать результат
        """
        # Ждем пока поле появится
        delay_element = self.wait.until(
            EC.presence_of_element_located(self.delay_field)
        )
        # Очищаем поле и вводим новое значение
        delay_element.clear()
        delay_element.send_keys(str(delay_value))
        return self

    def click_7(self):
        """
        Нажимает на кнопку с цифрой 7.
        """
        self.wait.until(
            EC.element_to_be_clickable(self.button_7)
        ).click()
        return self

    def click_plus(self):
        """
        Нажимает на кнопку с плюсом (+).
        """
        self.wait.until(
            EC.element_to_be_clickable(self.button_plus)
        ).click()
        return self

    def click_8(self):
        """
        Нажимает на кнопку с цифрой 8.
        """
        self.wait.until(
            EC.element_to_be_clickable(self.button_8)
        ).click()
        return self

    def click_equals(self):
        """
        Нажимает на кнопку равно (=).
        """
        self.wait.until(
            EC.element_to_be_clickable(self.button_equals)
        ).click()
        return self

    def get_result_text(self, timeout=46):
        """
        Ждет пока на экране появится результат и возвращает его.

            timeout: сколько секунд ждать результат (по умолчанию 46)

        Возвращает:
            строку с результатом (например, "15")
        """
        wait = WebDriverWait(self.driver, timeout)
        wait.until(
            EC.text_to_be_present_in_element(self.result_screen, "")
        )

        return self.driver.find_element(*self.result_screen).text

    def wait_for_specific_result(self, expected_result, timeout=46):
        """
        Ждет пока на экране появится конкретное число.

            expected_result: какое число ждем (например, "15")
            timeout: сколько секунд ждать (по умолчанию 46)
        """
        wait = WebDriverWait(self.driver, timeout)
        wait.until(
            EC.text_to_be_present_in_element(
                self.result_screen, expected_result)
        )
        return self
