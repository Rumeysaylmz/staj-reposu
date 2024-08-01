from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.window import WindowTypes

from time import sleep

options = Options()
options.add_argument("--window-size=1920,1200")
options.add_argument("--headless")
options.add_argument("--search-engine-choice-country")

service = Service(executable_path='./chromedriver')

driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.korodrogerie.de/en/nuts")

sleep(2)
driver.find_element(By.CSS_SELECTOR, ".modal-dialog .btn-close").click()
sleep(1)
driver.find_element(
    By.CSS_SELECTOR, ".cookie-permission-container .js-cookie-accept-all-button > button").click()


boxes = driver.find_elements(By.CLASS_NAME, "product-box")


for box in boxes:
    driver.execute_script("arguments[0].scrollIntoView();", box)

    product_name_element = box.find_element(By.CLASS_NAME, "product-name")
    product_name = product_name_element.get_attribute("title")
    product_link = product_name_element.get_attribute("href")

    driver.switch_to.new_window("tab")
    driver.get(product_link)
    sleep(2)

    product_number = driver.find_element(
        By.CSS_SELECTOR, ".product-detail-properties-table > tbody > tr .properties-value").text

    driver.close()
    driver.switch_to.window(driver.window_handles[0])

    product_price_element = box.find_element(By.CLASS_NAME, "real-price")
    product_price = product_price_element.text

    print(
        f'### {product_name} ###\nPrice: {product_price}\nNumber: {product_number}\n')


sleep(100)

# driver.quit()