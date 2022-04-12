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

s = Service('/app/.chromedriver/bin/chromedriver')
driver = webdriver.Chrome(service=s)



#driver = webdriver.Chrome(ChromeDriverManager().install()) 

options = webdriver.ChromeOptions() 
options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
options.add_argument("--headless")
options.headless = True
options.add_argument("window-size=1400,800")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-sh-usage")
options.add_argument("--disable-blink-features")
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
#options.add_argument("user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1")
options.add_argument('--disable-notifications')
options.add_argument("--mute-audio")



PROXY = '159.203.84.241:3128'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f'--proxy-server{PROXY}')

#driver = webdriver.Chrome(options=options) #VScode
driver = webdriver.Chrome(executable_path= os.environ.get("CHROMEDRIVER_PATH"), chrome_options=options, service=s) # Heroku

#driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")


driver.get("https://iir.ai/OZkS")

recaptcha_control_frame = None

# //*[@id="link-view"]/button
driver.find_element_by_xpath('//*[@id="link-view"]/button').click()
time.sleep(1)

WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[starts-with(@src, 'https://www.recaptcha.net/recaptcha/api2/anchor')]")))
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@id='recaptcha-anchor']"))).click()
time.sleep(3) 
#frames = driver.find_elements_by_tag_name("iframe")
#recaptcha_control_frame = None
#recaptcha_challenge_frame = None

driver.switch_to.frame(recaptcha_control_frame)
driver.switch_to.default_content()



#frames = driver.find_elements_by_tag_name("iframe")
#driver.switch_to.frame(recaptcha_challenge_frame)
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"/html/body/div[4]/div[4]/iframe")))
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="recaptcha-audio-button"]'))).click()
time.sleep(1)

driver.switch_to.frame(recaptcha_control_frame)
driver.switch_to.default_content()

# //*[@id="audio-source"]
# //*[@id=":2"] = play
# /html/body/div/div/div[7]/a = download
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"/html/body/div[4]/div[4]/iframe")))
src = driver.find_element_by_id("audio-source").get_attribute("src")
src = str(src)
print("O link é: {}".format(src))
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[7]/a'))).click()



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
