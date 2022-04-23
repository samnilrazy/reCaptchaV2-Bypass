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
#op.add_argument("--headless")
op.add_argument("--no-sandbox")
op.add_argument("--disable-dev-sh-usage")



s = Service('/app/.chromedriver/bin/chromedriver')

driver = webdriver.Chrome(service=s, options=op)
driver.maximize_window()
url = "https://iir.ai/0I3CG"
driver.set_page_load_timeout(30)
page = driver.get(url)
driver.switch_to.default_content()

time.sleep(2)



try:
    driver.find_element(By.XPATH, '/html/body/div/div/div/span').click()
    time.sleep(3)
except:
    print("Primeiro botão não encontrado")
    
    
try:
    driver.find_element(By.XPATH, '//*[@id="link-view"]/button').click()
    time.sleep(2)
except:
    print("Segundo botão não encontrado")


try:
    f = driver.find_element(By.XPATH, '//*[@id="td-outer-wrap"]/div/div[2]/div/div').text
    f = str(f)
    print("======================================\n{}\n======================================\n".format(f))


    if "Please check the captcha box to proceed to the destination page." in f:
        time.sleep(1)
    else:
        try:
            page = driver.get(url)
            time.sleep(3)
            driver.find_element(By.XPATH, '/html/body/div/div/div/span').click()
            time.sleep(3)
            driver.find_element(By.XPATH, '//*[@id="link-view"]/button').click()
            time.sleep(5)
        except:
            try:
                driver.set_page_load_timeout(30)
                page = driver.get(url)

                time.sleep(2)

                driver.find_element(By.XPATH, '/html/body/div/div/div/span').click()
                time.sleep(3)
                driver.find_element(By.XPATH, '//*[@id="link-view"]/button').click()
                time.sleep(5)
            except:
                time.sleep(2)
                driver.save_screenshot('erro.png')
                time.sleep(2)
                driver.get("https://pasteboard.co/")
                time.sleep(2)
                dir = os.getcwd()
                dir = str(dir)
                dir = "{}/erro.png".format(dir)
                driver.find_element(By.XPATH, '/html/body/section[1]/div[1]/div[2]/div/label/input').send_keys(dir)
                time.sleep(5)
                driver.find_element(By.XPATH, '/html/body/div[5]/div[6]/button[2]').click()
                time.sleep(5)
                t = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[4]/span/a').get_attribute("href")
                t = str(t)
                print("Impossivel iniciar URL: Script closed! {}".format(t))
                time.sleep(3)
                os.remove('erro.png')
                exit()
except:
    time.sleep(2)
    driver.save_screenshot('erro.png')
    time.sleep(2)
    driver.get("https://pasteboard.co/")
    time.sleep(2)
    dir = os.getcwd()
    dir = str(dir)
    dir = "{}/erro.png".format(dir)
    driver.find_element(By.XPATH, '/html/body/section[1]/div[1]/div[2]/div/label/input').send_keys(dir)
    time.sleep(5)
    driver.find_element(By.XPATH, '/html/body/div[5]/div[6]/button[2]').click()
    time.sleep(5)
    t = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[4]/span/a').get_attribute("href")
    t = str(t)
    print("Impossivel obter conteudo da pagina: Script closed!! {}".format(t))
    time.sleep(5)
    os.remove('erro.png')
    exit()



frames = driver.find_elements(By.TAG_NAME, 'iframe')
print("-----FRAMES ------\n{}\n---------------------------".format(frames))
print(len(frames))


################ TIRANDO ANUNCIOS DA TELA

#logs -->  não funcionou: 
try:
    a = driver.find_element(By.XPATH, '/html/body/div/div/div/div[3]/span')
    time.sleep(2)
    a.click()
    time.sleep(2)
except:
    print("1º Anuncio não encontrado")
    time.sleep(2)
    
try:
    a = driver.find_element(By.XPATH, '/html/body/div/div/div/div[3]/span')
    time.sleep(2)
    a.click()
    time.sleep(2)
except:
    print("2º Anuncio não encontrado")
    time.sleep(2)

try:
    a = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/span')
    time.sleep(2)
    a.click()
    time.sleep(2)
except:
     print("Close não encontrado")
     time.sleep(2)
driver.switch_to.default_content()
#WebDriverWait(driver, 50).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div[2]/div[2]/form/div[2]/div/div/div/iframe')))
#tpp = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div[2]/div[2]/form/div[2]/div/div/div/iframe'))).get_attribute("name")
tpp = WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,'//*[@id="captchaShortlink"]/div/div/iframe')))
#print("achou o frame {}".format(tpp))
#driver.switch_to.frame(frames[3])
#webDriverWait.until(ExpectedConditions.visibilityOfElementLocated(By.id("iframeLogin")));
print("achou o frame {}".format(tpp))
#driver.switch_to.frame(tpp)
time.sleep(10)
state = "N"
try:
    er = driver.find_elements(By.TAG_NAME, "div")
    e_cont = len(er)
    print("\n\n{}\n\n --> {}".format(er, e_cont))
except:
    print("Impossivel localizar divs dentro do iframe")
    
    
    
try: # tentar achar no captcha box
    #botao = driver.find_element(By.XPATH, '//*[@id="recaptcha-anchor"]')
    #botao = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="recaptcha-anchor"]')))
    #botao = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="recaptcha-anchor"]/div[1]')))
    #botao = driver.find_element(By.XPATH, '//*[@id="recaptcha-anchor"]/div[1]')
    #botao = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#captchaShortlink > div > div > iframe')))
    #botao = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'recaptcha-anchor')))
    driver.switch_to.default_content()
    print("Default")
    botao = driver.find_element(By.XPATH, value='//*[@id="captchaShortlink"]/div/div/iframe').click()
    state = "Okk"
    driver.switch_to.default_content()
except:
    #################################################################################
    #driver.switch_to.default_content()
    time.sleep(2)
    driver.save_screenshot('erro.png')
    time.sleep(2)
    driver.get("https://pasteboard.co/")
    time.sleep(2)
    dir = os.getcwd()
    dir = str(dir)
    dir = "{}/erro.png".format(dir)
    driver.find_element(By.XPATH, '/html/body/section[1]/div[1]/div[2]/div/label/input').send_keys(dir)
    time.sleep(5)
    driver.find_element(By.XPATH, '/html/body/div[5]/div[6]/button[2]').click()
    time.sleep(5)
    t = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[4]/span/a').get_attribute("href")
    t = str(t)
    #################################################################################
    print("Imposivel localizar captcha box. Script finalizado: {}".format(t))
    time.sleep(3)
    os.remove('erro.png')
    exit()
        
        
        
time.sleep(5)
#botao = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="recaptcha-anchor"]/div[1]')))
#ActionChains(driver).move_to_element(botao).click(botao).perform()
#botao.click()

#frames = driver.find_elements(By.TAG_NAME, 'iframe')
#driver.switch_to.frame(frames[9])
#tpp = WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,'/html/body/div[7]/div[4]/iframe')))


#WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[src='https://www.recaptcha.net/recaptcha/api2/bframe?hl=en&v=QENb_qRrX0-mQMyENQjD6Fuj&k=6LcNwNYdAAAAAKXZrWouTBrt8oi1j1wT04ULQSli']")))
#WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button#recaptcha-audio-button"))).click()

iframe = driver.find_element(By.XPATH, "/html/body/div/div[4]/iframe")
driver.switch_to.frame(iframe)

#/html/body/div[7]/div[4]/iframe --> bframe
#/html/body/div/div/div[3]/div[2]/div[1]/div[1]/div[2]/button --> audio button
sitekey = driver.find_element(By.ID, 'recaptcha-audio-button').click()
#sitekey = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'recaptcha-audio-button')))
time.sleep(3)

##############################
#src = driver.find_element(By.ID, "audio-source").get_attribute("src")

try:
    src = driver.find_element(By.ID, "audio-source").get_attribute("src")
    print("O link é: {}".format(src))
except:
    #################################################################################
    #driver.switch_to.default_content()
    time.sleep(2)
    driver.save_screenshot('erro.png')
    time.sleep(2)
    driver.get("https://pasteboard.co/")
    time.sleep(2)
    dir = os.getcwd()
    dir = str(dir)
    dir = "{}/erro.png".format(dir)
    driver.find_element(By.XPATH, '/html/body/section[1]/div[1]/div[2]/div/label/input').send_keys(dir)
    time.sleep(5)
    driver.find_element(By.XPATH, '/html/body/div[5]/div[6]/button[2]').click()
    time.sleep(5)
    t = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[4]/span/a').get_attribute("href")
    t = str(t)
    #################################################################################
    print("Imposivel obter src, confira o print: {}".format(t))
    time.sleep(3)
    os.remove('erro.png')
    exit()





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
driver.switch_to.default_content()

############# PASSOU DO CAPTCHA





###### ESPERANDO 10s

def tent():
    status = "Erro"
    while status == "Erro":
        try:
            ff = driver.find_element(By.XPATH, '//*[@id="td-outer-wrap"]/div/div[2]/div/div/div/center/center/div/a').get_attribute("href")
            ff = str(ff)
            if "javascript:" in ff:
                status = "Erro"
            else:
                print(f"Conteúdo: {ff}")
                status = "Passou"
        except:
            status = "Erro"
            time.sleep(2)
tent()

print("OK")
