import os
from selenium import webdriver

op = webdriver.ChromeOptions()
op.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
op.add_argument("--headless")
op.add_argument("--no-sandbox")
op.add_argument("--disable-dev-sh-usage")


driver = webdriver.Chrome(executable_path= os.eviron.get("CHROMEDRIVER_PATH"), chrome_options=op)

driver.get("https://youtube.com")

print(driver.page_source)
