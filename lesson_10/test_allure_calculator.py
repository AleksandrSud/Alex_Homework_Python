import allure
import pytest
from selenium import webdriver
from CalculatorPage import CalculatorPage


@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
class TestCalculator:
    """
    Тесты для проверки функциональности калькулятора с задержкой
    """

    @pytest.fixture
    def driver(self):
        """Фикстура для создания драйвера"""

        with allure.step("Настройка браузера Chrome"):
            driver = webdriver.Firefox()
            driver.maximize_window()
            yield driver
            with allure.step("Закрытие браузера"):
                driver.quit()

    @allure.title("Тест сложения 7 + 8 = 15 с задержкой 45 секунд")
    @allure.description(
        "Проверяем, что калькулятор правильно складывает "
        "числа с учетом задержки")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.tag("smoke", "positive")
    def test_calculator_7_plus_8_equals_15(self, driver):
        """Тест сложения 7 + 8 с задержкой 45 секунд"""

        with allure.step("Инициализация страницы калькулятора"):
            calculator_page = CalculatorPage(driver)

        with allure.step("Открытие страницы калькулятора"):
            calculator_page.open()

        with allure.step("Установка задержки: 45 секунд"):
            calculator_page.set_delay(45)

        with allure.step("Ввод выражения: 7 + 8"):
            with allure.step("Нажатие кнопки 7"):
                calculator_page.click_7()

            with allure.step("Нажатие кнопки +"):
                calculator_page.click_plus()

            with allure.step("Нажатие кнопки 8"):
                calculator_page.click_8()

            with allure.step("Нажатие кнопки ="):
                calculator_page.click_equals()

        with allure.step("Ожидание результата 15 (максимум 46 секунд)"):
            calculator_page.wait_for_specific_result("15", timeout=46)

        with allure.step("Получение результата с экрана"):
            result = calculator_page.get_result_text()

        with allure.step("Проверка результата"):
            with allure.step("Ожидаемое значение: 15"):
                with allure.step(f"Фактическое значение: {result}"):
                    assert result == "15"

        allure.attach(
            name="Результат теста",
            body=f"Сложение 7 + 8 выполнено успешно. Результат: {result}",
            attachment_type=allure.attachment_type.TEXT
        )
