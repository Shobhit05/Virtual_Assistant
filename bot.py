from gtts import gTTS
import os
from time import  gmtime, strftime
import time
import speech_recognition as sr
import selenium
from selenium import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

    
def login_facebook():
    try:
        driver=webdriver.Chrome()
        driver.get("https://facebook.com")

        username=WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH, "//*[@id='email']")))
        password = driver.find_element_by_xpath("//*[@id='pass']")

        username.send_keys("shobhit.srivastava39@gmail.com")
        password.send_keys("shobhit#9607")
        driver.find_element_by_xpath("//*[@id='u_0_2']").click()
    except:
        return("Something Goes Wrong")



def aud_input():
    r = sr.Recognizer()
    with sr.Microphone(6) as source:
        r.adjust_for_ambient_noise(source,1)
        print("Say something!")
        audio = r.listen(source,2,2)
        data=r.recognize_google(audio)
    work_tobe_done(data)


def work_tobe_done(data):
    if "how are you" in str(data).lower():
        if not os.path.isfile("greet.mp3"):
            greet="I am fine? What about You"
            tts=gTTS(text=greet,lang='en')
            tts.save("greet.mp3")
        os.system("mpg321 greet.mp3")
        aud_input()
    elif "i am fine" in str(data).lower():
        if not os.path.isfile("func_do.mp3"):
            function="Great to hear Ok So how may I help You?"
            tts=gTTS(text=function,lang='en')
            tts.save("func_do.mp3")
        os.system("mpg321 func_do.mp3")
                
    #login_facebook()
    

def time():
    a=strftime("%Y-%m-%d %H:%M:%S", gmtime())
    ctime=a.split(" ")
    ctime=int(ctime[1][:2])
    
    if ctime>16 and ctime<21:
        
        message="Good Evening Master"
        tts = gTTS(text=message, lang='en')
        tts.save("good.mp3")
        os.system("mpg321 good.mp3")
        
    elif ctime>12 and ctime<16:
        
        message="Good Evening Shobhit Master"
        tts = gTTS(text=message, lang='en')
        tts.save("good.mp3")
        os.system("mpg321 good.mp3")
    else:
        
        message="Good Evening Master"
        tts = gTTS(text=message, lang='en')
        tts.save("good.mp3")
        os.system("mpg321 good.mp3")
    aud_input()

    
##    functions="The functions I can do right now are: I can open the music player.Second I can open the web browser.Now what can I do for you?"
##    tts = gTTS(text=functions, lang='en')
##    tts.save("function.mp3")
##    os.system("mpg321 function.mp3")
    
        
time()
