from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_validation():
    driver = webdriver.Edge()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    fields = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
    }

    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input"))
    )

    for name, value in fields.items():
        selector = f"input[name='{name}']"
        field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, selector))
        )
        field.send_keys(value)

    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((
            By.CSS_SELECTOR, "button.btn.btn-outline-primary"))
    )
    button.click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#zip-code.alert-danger"))
    )

    zip_div = driver.find_element(By.CSS_SELECTOR, "#zip-code")
    assert "alert-danger" in zip_div.get_attribute("class")

    driver.quit()
