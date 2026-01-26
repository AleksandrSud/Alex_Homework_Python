from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/classattr")

xpath = (
        "//button[contains(concat(' ', normalize-space(@class), ' '), "
        "' btn-primary ')]"
    )

button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath))
    )
button.click()

WebDriverWait(driver, 10).until(EC.alert_is_present())
driver.switch_to.alert.accept()

print("Нажал")


driver.quit()
