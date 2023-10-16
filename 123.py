import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia 
import webbrowser
import os, sys

def speak(audio):
    engine = pyttsx3.init()
    engine.setProperty("rate",150)
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=0.2)
        print("Listening...")
        speak('Listening..')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:   
        print("Say that again please...")
        return "None"
    return query

def takeCommandcontent():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("What Should i say, sir")
        r.pause_threshold = 1
        audio = r.listen(source)

def greet(query):
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<17:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak(query)
    speak("How are you")

def wiki(query):
    try:
        speak('Searching Wikipedia')
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)
    except Exception as e:
        speak("Coludn't search it")

def wishMe(): 
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")  
    speak("I am Zoie your personal assistant. Please tell me how may I help you")

if name == "main":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wiki' in query: 
            query = query.replace("wiki", "")  
            wiki(query)
        elif 'greet' in query:
            query=query.replace("greet","")
            greet(query)
        elif 'hello' in query:
            print("Hello!")
            speak('Hello, Tell me how can I help you')
        elif 'how are you' in query:
            speak('I am good How can I help you')
        elif '.com' in query:
            query = query.replace("open", "")
            browse(query)
        elif 'the time' in query:   
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak("Sir, the time is {strTime}")            
        elif 'open file' in query:
            path ='file location'
            os.startfile(path)            
        elif 'quit' in query:
            print("quiting..! Thank you for your time")
            speak("quiting..! Thank you for your time")
            break
        elif 'shutdown' in query:
            speak('Do you really want to shutdown')
            reply=takeCommand()
            if 'yes' in reply:
                os.system('shutdown /s /t 1')
            else:
                continue
        elif 'restart' in query:
            speak('Do you really want to restart')
            reply=takeCommand()
            if 'yes' in reply:
                os.system('shutdown /r /t 1')
        else:
                print('repeat')
import time
import smtplib

