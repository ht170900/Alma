import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os
import webbrowser
import requests
import pywhatkit as kit
from decouple import config
import time
from englisttohindi.englisttohindi import EngtoHindi
from googletrans import Translator
import json
from deep_translator import GoogleTranslator
#from AppOpener import run

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()
    
def change_voice(engine, language):
    for voice in engine.getProperty('voices'):
        if language in voice.name:
            engine.setProperty('voice', voice.id)
            talk("how are you")
            return True

    raise RuntimeError("Language not found")

def select_lan():  
    global language
    language = input(talk("Enter Language Hindi or English: "))
    print("Language selected is " + language)

    if( language == "Hindi" or language == "hindi"):
        change_voice(engine, "Microsoft Hemant - Hindi (India)")
        language = "Hindi"
        
    elif( language == "English" or language == "english"):
        change_voice(engine, "Microsoft Zira Desktop - English (United States)")
        language = "English"
    else:
        talk("please enter proper language")
        select_lan()     
select_lan()
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

def h2e(command):
        txthindi = EngtoHindi(command)
        hindi = txthindi.convert
        translator = GoogleTranslator(source='hi', target='en')
        return (translator.translate(hindi)) 
        
def e2h(command):
    trans = EngtoHindi(command)
    talk(trans.convert) 
    
def after_talk(command):
    if(language == "Hindi"):
            e2h(command)
    else:
            talk(command) 

def countdown():
    t = 30;
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    talk('Exiting')
    exit()
    

#def runInParallel(*fns):
#    proc = []
#    for fn in fns:
#        p = Process(target=fn)
#       p.start()
#        proc.append(p)
#    for p in proc:
#        p.join()
#runInParallel(take_command, countdown)

def send_whatsapp_message(number, message):
    kit.sendwhatmsg_instantly(f"+91{number}", message)
    
def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']

def wishMe():
    hour=datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        return ("Hello,Good Morning")
    elif hour >= 12 and hour < 18:
        return ("Hello,Good Afternoon")
    else:
        return ("Hello,Good Evening")

def run_alma():
    command = take_command()
    print(command)
    
    if(language == "Hindi"):
        command = h2e(command)
    
    if "how are you" in command:
        com = "I am well how are you"
        after_talk(com)
        
    
    elif "hello" in command:
        com = wishMe() 
        after_talk(com)
        
    elif "goodbye" in command or "okbye" in command or "stop" in command:
        com = 'Your personal assistant leo is shutting down, Good bye'
        exit()

    elif 'play' in command:
        song = command.replace('play', '')
        com = 'playing ' + song
        after_talk(com)
        pywhatkit.playonyt(song)
        
    elif 'google' in command:
        webbrowser.open_new_tab("https://www.google.com")
        com = "Google chrome is open now"
        after_talk(com)
        
    elif "send whatsapp message" in command:
        com1 = 'On what number should I send the message ? Please enter on the screen: '
        after_talk(com1)
        number = input("Enter the number: ")
        
        com2 = "What is the message please enter it?"
        after_talk(com2)
        message = input()
        
        send_whatsapp_message(number, message)
        com3 = "I've sent the message."
        after_talk(com3)
        
    elif 'open website' in command:
        website = command.replace('open website', '')
        com = 'Opening Website ' + website
        after_talk(com)
        webbrowser.open(website)
        
    elif "who made you" in command or "who created you" in command or "who discovered you" in command:
        com = "I was built by Harshita and Janvi"
        after_talk(com)
            
    elif 'cricket' in command:
        news = webbrowser.open_new_tab("cricbuzz.com")
        com = 'This is live news from cricbuzz'
        after_talk(com)  
    
    elif "today" in command:
        day = datetime.datetime.today().weekday() + 1
        Day_dict = {1: 'Monday', 2: 'Tuesday',
                    3: 'Wednesday', 4: 'Thursday',
                    5: 'Friday', 6: 'Saturday',
                    7: 'Sunday'}
        if day in Day_dict.keys():
            day_of_the_week = Day_dict[day]
            print(day_of_the_week)
            com = "The day is " + day_of_the_week
            print(com)
            after_talk(com)

    elif "time" in command:
        time = str(datetime.datetime.now())
        print(time)
        hour = time[11:13]
        min = time[14:16]
        com = "The time is" + hour + "Hours and" + min + "Minutes"
        print(com)
        after_talk(com)


    elif 'who is ' in command:
        person = command.replace('what is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        after_talk(info)

    elif 'search' in command:
        query = command.replace("search", '') 
        com = "Seraching online"
        after_talk(com)      
        webbrowser.open(query)
    
    elif 'what is' in command:
        query = command.replace("what is", '') 
        com = "Seraching online"
        after_talk(com)     
        webbrowser.open(query)

    elif "where is" in command:
        query = command.replace("where is", "")
        location = query
        com = "User asked to Locate" + location
        after_talk(com)
        webbrowser.open("https://www.google.nl/maps/place/"+location+"")

    elif 'date' in command:
        com = 'sorry, I have a headache'
        after_talk(com)
        
    elif 'are you single' in command:
        com = 'I am in a relationship with wifi'
        after_talk(com)

    elif 'joke' in command:
        print(pyjokes.get_joke())
        after_talk(pyjokes.get_joke())

    elif 'advice' in command:
        advice = get_random_advice()
        print(advice)
        after_talk(advice)

    else:
        com = 'Please say the command again.'
        after_talk(com)


while True:
    run_alma()

