from gtts import gTTS
import os
from time import  gmtime, strftime
import datetime
import speech_recognition as sr
import wikipedia
from calculator import calcy
import Tkinter as tk
import tkMessageBox
from nltk.tag import pos_tag
import selenium
from selenium import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By




##def login_facebook():
##    try:
##        driver=webdriver.Chrome()
##        driver.get("https://facebook.com")
##
##        username=WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH, "//*[@id='email']")))
##        password = driver.find_element_by_xpath("//*[@id='pass']")
##
##        username.send_keys("shobhit.srivastava39@gmail.com")
##        password.send_keys("####")
##        driver.find_element_by_xpath("//*[@id='u_0_2']").click()
##    except:
##        return("Something Goes Wrong")


def music(data):
    import time
    driver=webdriver.Chrome()
    driver.get("https://youtube.com")
    name=WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH, "//*[@id='search']")))
    name.send_keys(data[5:])
    driver.find_element_by_xpath("//*[@id='search-icon-legacy']").click()
    time.sleep(5)
    div=driver.find_elements_by_xpath("//*[@id='video-title']")
    ans=[]
    for i in div:
        ans.append(str((i.get_attribute("href"))))
    try:
        ind=ans.index('None')
        driver.get(str(ans[ind+1]))
    except:
        driver.get(str(ans[0]))
        
            

def aud_input():
    r = sr.Recognizer()
    with sr.Microphone(6) as source:
        r.adjust_for_ambient_noise(source,1)
        print("Say something!")
        audio = r.listen(source,1,2)
    try:
        data=r.recognize_google(audio)
        work_tobe_done(data)
    except Exception as e:
        print e


def string_work(res):
    start=res.find("(")
    end=res.find(")")
    ans=res[:start-2]+res[end+1:]
    return ans
    
    

def wikipedia_search(data):
    print "You said "+data
    sentence=data
    tagged_sent = pos_tag(sentence.split())
    propernouns = [word for word,pos in tagged_sent if pos == 'NNP']
    a=propernouns[0]+" "+propernouns[1]
    res=wikipedia.summary(str(a),sentences=1)
    ans=string_work(res)
    root = tk.Tk()
    tkMessageBox.showinfo(message=ans)
    root.destroy()


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
            function="Great to hear.Ok So how may I help You?"
            tts=gTTS(text=function,lang='en')
            tts.save("help.mp3")
        os.system("mpg321 func_do.mp3")
        aud_input()
        
    elif "play" in str(data).lower():
        music(data)
        
    elif "calculate" in data:
        res=calcy(data)
        res="The answer is %s"%(res)
        tts = gTTS(text=res, lang='en')
        tts.save("res.mp3")
        os.system("mpg321 res.mp3")
        os.remove("res.mp3")

    elif "time" in data:
        a = str(datetime.datetime.now())
        ctime=a.split(" ")
        ctime=ctime[1]
        tts=gTTS(text=ctime,lang='en')
        tts.save("time.mp3")
        os.system("mpg321 time.mp3")
    else:
        wikipedia_search(data)

def time():
    a = str(datetime.datetime.now())
    ctime=a.split(" ")
    ctime=int(ctime[1][:2])
    

    if ctime>16 and ctime<21:
        if not os.path.isfile("goodeve.mp3"):
            message="Good Evening There"
            tts = gTTS(text=message, lang='en')
            tts.save("goodeve.mp3")
        os.system("mpg321 goodeve.mp3")
        
    elif ctime>=12 and ctime<16:
        if not os.path.isfile("goodaft.mp3"):
            message="Good Afternoon There"
            tts = gTTS(text=message, lang='en')
            tts.save("goodaft.mp3")
        os.system("mpg321 goodaft.mp3")
    else:
        if not os.path.isfile("goodmor.mp3"):
            message="Good Morning There"
            tts = gTTS(text=message, lang='en')
            tts.save("goodmor.mp3")
        os.system("mpg321 goodmor.mp3")
        

#time()

aud_input()
    
