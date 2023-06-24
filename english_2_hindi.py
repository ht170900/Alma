import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os
import webbrowser
from englisttohindi.englisttohindi import EngtoHindi

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

    
language = input(talk("Enter Language Hindi or English: "))
print("Language selected is " + language)

if( language == "Hindi" or language == "hindi"):
    change_voice(engine, "Microsoft Hemant - Hindi (India)")
else:
    change_voice(engine, "Microsoft Zira Desktop - English (United States)")
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

def e2h(command):
    trans = EngtoHindi(command)
    talk(trans.convert) 

def run_alma():
    command = take_command()
    print(command)
    if "how are you" in command:
        com = "I am well how are you"
        e2h(com)

    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    
    elif 'open website' in command:
        website = command.replace('open website', '')
        talk('Opening Website ' + website)
        webbrowser.open(website)

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

    elif "bye" in command:
        talk("Bye Have a nice day")
        exit()

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


    else:
        talk('Please say the command again.')


while True:
    run_alma()

