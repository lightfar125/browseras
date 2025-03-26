from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument('--headless')

driver = webdriver.Remote(
    command_executor='http://localhost:6903/wd/hub',
    options=options
)

driver.get("https://www.google.com")
print(driver.title)

driver.quit()

