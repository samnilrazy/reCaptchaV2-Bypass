#from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import speech_recognition as sr 
import os
from pydub import AudioSegment
import urllib.request
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

##############################

src = driver.find_element(By.ID, "audio-source").get_attribute("src")
print("O link é: {}".format(src))





urllib.request.urlretrieve(src, "ex.mp3")
time.sleep(1)
filename = "audio.wav"
r = sr.Recognizer()



# files                                                                       
src = "ex.mp3"
dst = "audio.wav"

# convert wav to mp3                                                            
audSeg = AudioSegment.from_mp3(src)
audSeg.export(dst, format="wav")
time.sleep(1)


with sr.AudioFile(filename) as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    text = r.recognize_google(audio_data)
    print("O Conteudo é: {}".format(text))
###################


print("OK")
