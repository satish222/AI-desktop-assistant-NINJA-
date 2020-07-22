import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

print('Initializing NINJA')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
#-----------------speak function will produce the string we passed to it----------
def speak(text):
    engine.say(text)
    engine.runAndWait()
#-----------------this function wishes us asper the current time------------
def wishMe():
    
    hour = datetime.datetime.now().hour

    if hour>=0 and hour<12:
        speak('Good Morning'+MASTER)
    elif hour>=12 and hour<18:
        speak('Good Afternoon'+MASTER)
    else:
        speak('Good Evening'+MASTER)
    
    speak('I am NINJA. How may i help you?')
#------------this function will take command from the microphone----------
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        audio = r.listen(source)
    
    try:
        print("recognizing...")
        query=r.recognize_google(audio, language='en-in')
        print(f'user said: {query}\n')

    except Exception:
        print('Say that again please')
        query=None
    return query
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('kollasatishkumar222@gmail.com','Satya@143')
    server.sendmail('kollasatish100@gmail.com',to,content)
    server.close()
#-----------------------------Main program------------------
def main():
    global MASTER
    MASTER = 'Satish'
    speak('Initializing NINJA...')
    wishMe()
    query=takeCommand()

    #-------logic for executing tasks as per the query-----------
    if 'wikipedia' in query.lower():
        speak('Searching wikipedia...')
        query=query.replace('wikipedia','')
        results=wikipedia.summary(query, sentences=2)
        print(results)
        speak(results)
    elif 'open youtube' in query.lower():
        url="youtube.com"
        chrome_path='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open google' in query.lower():
        url="google.com"
        chrome_path='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)


    elif 'open reddit' in query.lower():
        url="reddit.com"
        chrome_path='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open facebook' in query.lower():
        url="facebook.com"
        chrome_path='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'play music' in query.lower():
        songs= os.listdir("D:/songs")
        print(songs)
        os.startfile(os.path.join("D:/songs",songs[0]))

    elif 'the time' in query.lower():
        strTime=datetime.datetime.now().strftime("%H:%M:%S")
        speak(f'{MASTER} the tiem is {strTime}')
        print(strTime)

    elif 'email to satish' in query.lower():
        try:
            speak('What should i send?')
            content = takeCommand()
            to = 'kollasatish100@gmail.com'
            sendEmail(to,content)
            speak('Email has been sent succesfully')
        except Exception as e:
            print(e)
main()



