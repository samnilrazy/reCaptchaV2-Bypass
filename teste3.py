# open the file
import speech_recognition as sr 
import os 
import subprocess
from selenium import webdriver
from pydub import AudioSegment
from pydub.silence import split_on_silence
import time
import pyautogui


filename = "payload.wav"
r = sr.Recognizer()


inkk = 'https://convertio.co/pt/mp3-wav/'

nav = webdriver.Chrome()
nav.get(inkk)

nav.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/div/div[2]/div[1]/div[1]/label').click()
#nav.find_element_by_id("Enviar").click()
time.sleep(3)
pyautogui.write('payload.mp3') 
pyautogui.press('enter')
time.sleep(2)
nav.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/div[2]/div/div[2]/div[2]/div/div[2]/div[2]/button').click()
time.sleep(15)
nav.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div[2]/div/div[1]/table/tbody/tr/td[6]/a').click()
print("OK")

with sr.AudioFile(filename) as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    text = r.recognize_google(audio_data)
    print("O Conteudo é: {}".format(text))
