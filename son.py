from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By


import pandas as pd 
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()


options = Options()
options.add_argument("--window-size=1920,1200")
options.add_argument("--headless")
options.add_argument("--search-engine-choice-country")

driver = webdriver.Chrome(options=options)

driver.get("https://www.korodrogerie.de/en/nuts")

sleep(2)
driver.find_element(By.CSS_SELECTOR, ".modal-dialog .btn-close").click()
sleep(1)
driver.find_element(
    By.CSS_SELECTOR, ".cookie-permission-container .js-cookie-accept-all-button > button").click()

rows = []
with open("./competitor_comparison_template.csv", "r") as file:
    contents = file.read()
    rows = contents.split("\n")

print(rows)



result_product = []
for row in rows[1:]:
    print(row)
    columns = row.replace('"', "").split(",")
    print(columns[3])

    competitor_count = int((len(columns) - 3) / 3)

    result_competitor = []
    for i in range(competitor_count):
        driver.get(columns[3 + 1 + (i * 3)])
        sleep(1)
        product_price_element = driver.find_element(By.CLASS_NAME, "product-detail-price")
        product_price = product_price_element.text.split("€")[0].strip().replace(",", ".")
        print(product_price)

        result_competitor.append(product_price)
    result_product.append(result_competitor)

with open("./output.csv", "w+") as file:
    lines = []
    lines.append(rows[0])

    for i, row in enumerate(rows[1:]):
        columns = row.replace('"', "").split(",")
        competitor_count = int((len(columns) - 3) / 3)
        for j in range(competitor_count):
            columns[3 + 2 + (j * 3)] = result_product[i][j]
        lines.append(",".join(columns))

    file.write("\n".join(lines))


sleep(2)
driver.quit()