from anticaptchaofficial.recaptchav2proxyless import *
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time
print("Iniciando...")
s = Service('/app/.chromedriver/bin/chromedriver')

driver = webdriver.Chrome(service=s)

url = "https://www.google.com/recaptcha/api2/demo"
page = driver.get(url)

time.sleep(10)

frames = driver.find_elements(By.TAG_NAME, 'iframe')
driver.switch_to.frame(frames[0])


sitekey = driver.find_element(By.XPATH, '//*[@id="recaptcha-anchor"]/div[1]').click()

driver.switch_to.default_content()
time.sleep(10)

frames = driver.find_elements(By.TAG_NAME, 'iframe')
driver.switch_to.frame(frames[2])

sitekey = driver.find_element(By.XPATH, '//*[@id="recaptcha-audio-button"]').click()
time.sleep(10)


print("OK")
