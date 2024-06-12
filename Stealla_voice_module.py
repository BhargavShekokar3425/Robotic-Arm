#task 1: Speech recognition module installation
#task 2: Wish command
#task 3: Ask if Stella could help you by any way 
#task 4:Take command
#task 5: Wikipedia brainstorm -upto 2 lines
#task 6: opening websites like google, youtube, geek for geeks, weather
#task 7: play music
#task 8: date and time 

import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyaudio

engine_vc= pyttsx3.init('sapi5')
voices=engine_vc.getProperty('voices')
#print(voices[0].id)

def speak(audio):
    engine_vc.say(audio)
    engine_vc.runAndWait()

def WishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak("Good Morning!")
        
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    
    else:
        speak("Good Evening!")
    
    speak("I am Terris, How may I help you?")

def takeCmd():
    #it takes microphone input from the user and returns string object
    
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Sun rha hu bol tu....")
        r.pause_threshold=1
        audio=r.listen(source)
    
    try:
        print("Samajhne ki koshish kar rha hu ...")
        query=r.recognize_google(audio, language='en-in')
        print(f"Aapne bola : {query}\n")
    
    except Exception as e:
        print("Aap jo bol rhe samjh nahi aa rha , mu se supari nikal ke baat kar")
        return "None"
    return query
        
    
c1=1
if __name__== "__main__":
    speak(" Bhargav is in First year")
    WishMe()
    while c1==1:
        query=takeCmd().lower()
    # logic for executinmg task
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query= query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        
        elif 'open google' in query:
            webbrowser.open('google.com')
        
        elif 'open geeksforgeeks' in query:
            webbrowser.open('geeksforgeeks.com')
        
        elif 'time' in query:
            sTime=datetime.datetime.now().strftime('%H:%M:%S')
            speak(f"The time is {sTime}")
        
        elif 'exit' in query:
            c1=0
    
    