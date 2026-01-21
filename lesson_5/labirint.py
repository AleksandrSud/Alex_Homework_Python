from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()

driver.get("https://www.labirint.ru")


search_locator = "#search-field"

search_input = driver.find_element(By.CSS_SELECTOR, search_locator)

search_input.send_keys("Python")
search_input.send_keys(Keys.RETURN)
# driver.find_element(By.CSS_SELECTOR, search_locator)
book_locator = "div.product-card"

books = driver.find_elements(By.CSS_SELECTOR, "div.product-card")

print(len(books))
for book in books:
    author = book.find_element("div.product-author").text
    print(book.text)


sleep(5)
