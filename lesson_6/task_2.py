from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/textinput")


driver.find_element(By.CSS_SELECTOR, "#newButtonName").send_keys("SkyPro")


button = driver.find_element(By.CSS_SELECTOR, "#updatingButton.btn-primary")
button.click()


WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, "#updatingButton"), "SkyPro"))

print(button.text)

driver.quit()
