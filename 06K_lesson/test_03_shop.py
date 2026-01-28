from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_purchase_process():

    driver = webdriver.Firefox()

    driver.get("https://www.saucedemo.com/")

    wait = WebDriverWait(driver, 20)

    username_field = wait.until(
            EC.presence_of_element_located((By.ID, "user-name"))
        )
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    username_field.send_keys("standard_user")
    password_field.send_keys("secret_sauce")
    login_button.click()

    wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
        )

    backpack_add_button = wait.until(
            EC.element_to_be_clickable(
                (By.ID, "add-to-cart-sauce-labs-backpack"))
        )
    backpack_add_button.click()

    tshirt_add_button = wait.until(
            EC.element_to_be_clickable(
                (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"))
        )
    tshirt_add_button.click()

    onesie_add_button = wait.until(
            EC.element_to_be_clickable((
                By.ID, "add-to-cart-sauce-labs-onesie"))
        )
    onesie_add_button.click()

    cart_button = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
        )
    cart_button.click()

    wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "cart_list"))
        )

    checkout_button = wait.until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        )
    checkout_button.click()

    wait.until(
            EC.presence_of_element_located((By.ID, "first-name"))
        )

    first_name_field = driver.find_element(By.ID, "first-name")
    first_name_field.send_keys("Александр")

    last_name_field = driver.find_element(By.ID, "last-name")
    last_name_field.send_keys("Сударчиков")

    postal_code_field = driver.find_element(By.ID, "postal-code")
    postal_code_field.send_keys("453560")

    continue_button = driver.find_element(By.ID, "continue")
    continue_button.click()

    wait.until(
            EC.presence_of_element_located((
                By.CLASS_NAME, "summary_total_label"))
        )

    total_element = driver.find_element(By.CLASS_NAME, "summary_total_label")
    total_text = total_element.text

    print(f"{total_text}")

    total_amount = total_text.split("$")[1]

    assert total_amount == "58.29", (
            f"{total_amount}. "
            f"'{total_text}'"
        )

    driver.quit()
