import pandas as pd
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os
import webbrowser
import csv 
import pandas as pd
from englisttohindi.englisttohindi import EngtoHindi
from googletrans import Translator
import json
from deep_translator import GoogleTranslator

def talk(text):
    engine.say(text)
    engine.runAndWait()
    
listener = sr.Recognizer()
engine = pyttsx3.init()

def change_voice(engine, language):
    for voice in engine.getProperty('voices'):
        if language in voice.name:
            engine.setProperty('voice', voice.id)
            return True

    raise RuntimeError("Language not found")

language = input(talk("Enter Language Hindi or English: "))
print("Language selected is " + language)

if( language == "Hindi" or language == "hindi"):
    change_voice(engine, "Microsoft Hemant - Hindi (India)")
else:
    change_voice(engine, "Microsoft Zira Desktop - English (United States)")
engine.runAndWait()

engine = pyttsx3.init()
change_voice(engine, "Microsoft Hemant - Hindi (India)")
engine.say("कैसे हो")
engine.runAndWait()



def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alma' in command:
                command = command.replace('hey alma', '')
                print(command)
    except:
        pass
    return command

command = take_command()
print(command)

txthindi = EngtoHindi(command)
hindi = txthindi.convert

translator = GoogleTranslator(source='hi', target='en')
print(translator.translate(hindi))

