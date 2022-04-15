#from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import speech_recognition as sr 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import os
import traceback
from pydub import AudioSegment
import urllib.request
import time
print("Iniciando...")


op = webdriver.ChromeOptions()
op.add_argument("--headless")
op.add_argument("--no-sandbox")
op.add_argument("--disable-dev-sh-usage")



s = Service('/app/.chromedriver/bin/chromedriver')

driver = webdriver.Chrome(service=s, options=op)
driver.maximize_window()
url = "https://iir.ai/OZkS"
driver.set_page_load_timeout(30)
page = driver.get(url)

time.sleep(15)



try:
    driver.find_element(By.XPATH, '/html/body/div/div/div/span').click()
    time.sleep(3)
except:
    print("Primeiro botão não encontrado")
    
    
try:
    driver.find_element(By.XPATH, '//*[@id="link-view"]/button').click()
    time.sleep(10)
except:
    print("Segundo botão não encontrado")


    
f = driver.find_element(By.XPATH, '//*[@id="td-outer-wrap"]/div/div[2]/div/div').text
f = str(f)
print("======================================\n{}\n======================================\n".format(f))

if "Please check the captcha box to proceed to the destination page." in f:
    time.sleep(1)
else:
    driver.find_element(By.XPATH, '/html/body/div/div/div/span').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="link-view"]/button').click()
    time.sleep(5)



frames = driver.find_elements(By.TAG_NAME, 'iframe')
print("-----FRAMES ------\n{}\n---------------------------".format(frames))
print(len(frames))

#WebDriverWait(driver, 50).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div[2]/div[2]/form/div[2]/div/div/div/iframe')))
#tpp = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div[2]/div[2]/form/div[2]/div/div/div/iframe')))
tpp = WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[starts-with(@src, 'https://www.google.com/recaptcha/api2/anchor')]")))
print("achou o frame {}".format(tpp))
#driver.switch_to.frame(frames[3])
#driver.switch_to.frame(tpp)
time.sleep(10)
state = "N"
count = 0
try:
    er = driver.find_elements(By.TAG_NAME, "div")
    e_cont = len(er)
    print("\n\n{}\n\n --> {}".format(er, e_cont))
except:
    print("Impossivel localizar divs dentro do iframe")
try:
    #botao = driver.find_element(By.XPATH, '//*[@id="recaptcha-anchor"]')
    #botao = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="recaptcha-anchor"]')))
    botao = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[starts-with(@id, 'recaptcha-anchor')]")))
    state = "Ok"
    #driver.switch_to.default_content()
except Exception as e:
    while state == "N":
        count = count+1
        print("Imposivel localizar captcha box, tentando novamente...({})".format(count))
        traceback.print_exc()
        time.sleep(10)
        try:
            #botao = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="recaptcha-anchor"]')))
            botao = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[starts-with(@id, 'recaptcha-anchor')]")))
            state = "Ok"
        except:
            time.sleep(1)
        
        
        
time.sleep(30)
botao.click()
#botao = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="recaptcha-anchor"]/div[1]')))
#ActionChains(driver).move_to_element(botao).click(botao).perform()
#botao.click()

driver.switch_to.default_content()
time.sleep(3)

frames = driver.find_elements(By.TAG_NAME, 'iframe')
driver.switch_to.frame(frames[9])

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
