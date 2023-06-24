import pyttsx3

engine = pyttsx3.init()

for voice in engine.getProperty('voices'):
    print(voice)
engine.setProperty('voice', voice.id)
def change_voice(engine, language):
    for voice in engine.getProperty('voices'):
        if language in voice.name:
            engine.setProperty('voice', voice.id)
            return True

    raise RuntimeError("error")
import pyttsx3

engine = pyttsx3.init()
change_voice(engine, "Microsoft Hemant - Hindi (India)")
engine.say("कैसे हो")
engine.runAndWait()