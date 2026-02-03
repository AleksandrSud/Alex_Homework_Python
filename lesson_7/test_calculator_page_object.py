import pytest
from selenium import webdriver
from CalculatorPage import CalculatorPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_calculator(driver):
    calculator_page = CalculatorPage(driver)
    calculator_page.open()
    calculator_page.set_delay(45)
    calculator_page.click_7()
    calculator_page.click_plus()
    calculator_page.click_8()
    calculator_page.click_equals()

    calculator_page.wait_for_specific_result("15", timeout=46)

    result = calculator_page.get_result_text()

    assert result == "15"

    driver.quit()
