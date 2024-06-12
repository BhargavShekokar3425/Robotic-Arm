import pyfirmata 
from pyfirmata import Arduino, SERVO
from time import sleep
import pyttsx3
import speech_recognition as sr
import word2number



port ='COM3'
base=9
shoulder=10
elbow=11
wrist=12
grip=13
board=Arduino(port)

board.digital[base]=SERVO #base
board.digital[shoulder]=SERVO #shoulder
board.digital[elbow]=SERVO #elbow
board.digital[wrist]=SERVO #wrist
board.digital[grip]=SERVO #grip

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')

def word_to_number(word):
    return word2number.word_to_number(word)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCmd():
    #it takes microphone input from the user and returns string object
    
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        audio=r.listen(source)
    
    try:
        print("Trying to understand...")
        query=r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    
    except Exception as e:
        print("Didn't get that, please say it again")
        return "None"
    return query


def rotateServo(pin, angle):
    board.digital[pin].write(angle)
    sleep(0.015)


if __name__=="__main__":
    
    speak("Tell us the pin you wanna operate with ")
    pin=takeCmd().lower()
    speak("Angle please")
    angle=float(word_to_number(takeCmd().lower()))
    while True:
        rotateServo(pin, angle)
