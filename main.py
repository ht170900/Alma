import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
from multiprocessing import Process
import sys
import os
import webbrowser
import requests
import pywhatkit as kit
from decouple import config
import time
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
    language = input(talk("Enter Language Hindi or English: "))
    print("Language selected is " + language)

    if( language == "Hindi" or language == "hindi"):
        change_voice(engine, "Microsoft Hemant - Hindi (India)")
    elif( language == "English" or language == "english"):
        change_voice(engine, "Microsoft Zira Desktop - English (United States)")
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
    
if __name__=='__main__':
    p1 = Process(target = countdown)
    p1.start()
    p2 = Process(target = take_command)
    p2.start()

def send_whatsapp_message(number, message):
    kit.sendwhatmsg_instantly(f"+91{number}", message)
    
def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']

def wishMe():
    hour=datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        talk("Hello,Good Morning")
    elif hour >= 12 and hour < 18:
        talk("Hello,Good Afternoon")
    else:
        talk("Hello,Good Evening")

def run_alma():
    command = take_command()
    print(command)
    if "how are you" in command:
        talk("I am well how are you")
    
    elif "hello" in command:
        wishMe() 
        
    elif "goodbye" in command or "okbye" in command or "stop" in command:
        talk('Your personal assistant leo is shutting down, Good bye')
        exit()
                
    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
        
    elif 'open google' in command:
        webbrowser.open_new_tab("https://www.google.com")
        talk("Google chrome is open now")

    elif "send whatsapp message" in command:
        talk('On what number should I send the message ? Please enter in the console: ')
        number = input("Enter the number: ")
        talk("What is the message please enter it?")
        message = input()
        send_whatsapp_message(number, message)
        talk("I've sent the message sir.")
        
    elif 'open website' in command:
        website = command.replace('open website', '')
        talk('Opening Website ' + website)
        webbrowser.open(website)
        
    elif "who made you" in command or "who created you" in command or "who discovered you" in command:
        talk("I was built by Harshita and Janvi")
                
    elif 'cricket' in command:
        news = webbrowser.open_new_tab("cricbuzz.com")
        talk('This is live news from cricbuzz')
    
    elif 'open application' in command:
        inp = command.replace('open application', '')
        if inp:
            talk('Opening' + inp)
            #os.system(inp)
            #run(inp)
        else:
            talk('No Such app or maybe you said wrong name')

    elif "which day it is" in command:
        day = datetime.datetime.today().weekday() + 1
        Day_dict = {1: 'Monday', 2: 'Tuesday',
                    3: 'Wednesday', 4: 'Thursday',
                    5: 'Friday', 6: 'Saturday',
                    7: 'Sunday'}
        if day in Day_dict.keys():
            day_of_the_week = Day_dict[day]
            print(day_of_the_week)
            talk("The day is " + day_of_the_week)
        

    elif "tell me the time" in command:
        time = str(datetime.datetime.now())
        print(time)
        hour = time[11:13]
        min = time[14:16]
        talk( "The time is" + hour + "Hours and" + min + "Minutes") 


    elif 'who is ' in command:
        person = command.replace('what is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'search' in command:
        query = command.replace("search", '') 
        talk("Seraching online")      
        webbrowser.open(query)
    
    elif 'what is' in command:
        query = command.replace("what is", '') 
        talk("Seraching online")      
        webbrowser.open(query)

    elif "where is" in command:
        query = command.replace("where is", "")
        location = query
        talk("User asked to Locate")
        talk(location)
        webbrowser.open("https://www.google.nl/maps/place/"+location+"")

    elif 'date' in command:
        talk('sorry, I have a headache')

    elif 'are you single' in command:
        talk('I am in a relationship with wifi')

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'advice' in command:
        advice = get_random_advice()
        talk(advice)

    else:
        talk('Please say the command again.')


while True:
    run_alma()

