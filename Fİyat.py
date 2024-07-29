from selenium import webdriver
import chromedriver_autoinstaller
import time

chromedriver_autoinstaller.install()



driver = webdriver.Chrome()

driver.get("https://www.korodrogerie.de/en/nuts")

time.sleep(60)
driver.quit

