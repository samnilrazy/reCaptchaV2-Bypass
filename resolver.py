from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import urllib.request
import speech_recognition as sr 
import time
import os
from pydub import AudioSegment
from selenium.webdriver.chrome.service import Service
print("Iniciando...")



s = Service('/app/.chromedriver/bin/chromedriver')

path = os.path.abspath(os.getcdw())

driver = webdriver.Chrome(service=s)

driver.get("https://www.google.com/recaptcha/api2/demo")


frames = driver.find_elements(By.TAG_NAME, "iframe")
driver.switch_to.frame(frames[0])
time.sleep(4)

driver.find_element(By.CLASS_NAME, "recaptcha-checkbox-border").click()


driver.switch_to.default_content()

frames = driver.find_element(By.XPATH, "/html/body/div[2]/div[4]").find_elements(By.TAG_NAME, "iframe")
time.sleep(4)

driver.switch_to.default_content()

frames = driver.find_elements(By.TAG_NAME, "iframe")

driver.switch_to.frame(frames[-1])

frames = driver.find_elements(By.ID, "recaptcha-audio-button").click()

driver.switch_to.default_content()

frames = driver.find_elements(By.TAG_NAME, "iframe")

driver.switch_to.frame(frames[-1])

time.sleep(4) #/html/body/div/div/div[3]/div/button

driver.find_elements(By.XPATH, "/html/body/div/div/div[3]/div/button")
print("concluido")




