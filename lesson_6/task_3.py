from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
    )

driver.find_element(By.CSS_SELECTOR, "#image-container")

image = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located(
        (By.CSS_SELECTOR, "#image-container img:nth-child(3)")
        )
    )


print(image.get_attribute("src"))

driver.quit()
