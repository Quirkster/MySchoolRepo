import win32com.client as win
import pyautogui as pg
import speech_recognition as sr
import time
import webbrowser as wb
speak = win.Dispatch("SAPI.SpVoice")
r = sr.Recognizer()
with sr.Microphone() as source:
    #speak.Speak("This is Bob the robot and I am listening for your input")
    speak.Speak("hi")
    print("Come on don't be shy")
    audio = r.listen(source)
    print("Thinking...")
try:
    words = r.recognize_google(audio)
    print(words)
    if 'YouTube' in words:
        words = words.split()
        index = len(words)
        #print(index)
        print(words)
        words = words[:index-2]
        print(words)
        index=len(words)
        link="https://www.youtube.com/results?search_query="
        z=0
        for i in words:
            link += words[z]
            print(link)
            z += 1
    elif 'Google' in words:
        words = words.split()
        index = len(words)
        #print(index)
        print(words)
        words = words[:index-2]
        print(words)
        index=len(words)
        link="https://www.google.com/search?q="
        z=0
        for i in words:
            link += words[z]
            print(link)
            z += 1     
        
    #speak.Speak("Ok Anna, let's look for" + link)
    wb.open(link)
except sr.UnknownValueError:
    print("couldn't understand audio")
except sr.RequestError as e:
    print("could not get results")
