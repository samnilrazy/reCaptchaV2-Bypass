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

url = "https://iir.ai/OZkS"
page = driver.get(url)

time.sleep(3)



try:
    driver.find_element(By.XPATH, '/html/body/div/div/div/span').click()
    time.sleep(3)
except:
    print("Primeiro botão não encontrado")
    
    
try:
    driver.find_element(By.XPATH, '//*[@id="link-view"]/button').click()
    time.sleep(1)
except:
    print("Segundo botão não encontrado")




time.sleep(3)
frames = driver.find_elements(By.TAG_NAME, 'iframe')
print("-----FRAMES ------\n{}\n---------------------------".format(frames)
driver.switch_to.frame(frames[3])


sitekey = driver.find_element(By.XPATH, '//*[@id="recaptcha-anchor"]').click()

driver.switch_to.default_content()
time.sleep(3)

frames = driver.find_elements(By.TAG_NAME, 'iframe')
driver.switch_to.frame(frames[15])

sitekey = driver.find_element(By.XPATH, '//*[@id="recaptcha-audio-button"]').click()
time.sleep(3)

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
#audio-response
time.sleep(2)
driver.find_element(By.ID, 'audio-response').send_keys(text)
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="recaptcha-verify-button"]').click()
time.sleep(3)

driver.switch_to.default_content()
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="invisibleCaptchaShortlink"]').click()



print("OK")
