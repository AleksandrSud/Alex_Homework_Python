from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

        self.delay_field = (By.CSS_SELECTOR, "#delay")
        self.result_screen = (By.CSS_SELECTOR, ".screen")

        self.button_7 = (By.XPATH, "//span[text()='7']")
        self.button_plus = (By.XPATH, "//span[text()='+']")
        self.button_8 = (By.XPATH, "//span[text()='8']")
        self.button_equals = (By.XPATH, "//span[text()='=']")

    def open(self):
        self.driver.get(
            "https://bonigarcia.dev/"
            "selenium-webdriver-java/slow-calculator.html"
        )
        return self

    def set_delay(self, delay_value):
        delay_element = self.wait.until(
            EC.presence_of_element_located(self.delay_field)
        )
        delay_element.clear()
        delay_element.send_keys(str(delay_value))
        return self

    def click_7(self):
        self.wait.until(
            EC.element_to_be_clickable(self.button_7)
        ).click()
        return self

    def click_plus(self):
        self.wait.until(
            EC.element_to_be_clickable(self.button_plus)
        ).click()
        return self

    def click_8(self):
        self.wait.until(
            EC.element_to_be_clickable(self.button_8)
        ).click()
        return self

    def click_equals(self):
        self.wait.until(
            EC.element_to_be_clickable(self.button_equals)
        ).click()
        return self

    def get_result_text(self, timeout=46):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(
            EC.text_to_be_present_in_element(self.result_screen, "")
        )

        return self.driver.find_element(*self.result_screen).text

    def wait_for_specific_result(self, expected_result, timeout=46):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(
            EC.text_to_be_present_in_element(
                self.result_screen, expected_result)
        )
        return self
