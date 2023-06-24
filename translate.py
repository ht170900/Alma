"""
import pandas as pd
from googletrans import Translator
data = pd.read_csv("command.csv")
print(data)
translator = Translator()
translations = {}
for column in data.columns:
    unique = data[column].unique()
    for element in unique:
        translations[element] = translator.translate(element).text
for i in translations.items():
    print(i)

data.replace(translations, inplace=True)
print(data)
"""

"""
translator = Translator()
from_lang="Hindi"
to_lang="English"
translator= Translator(hindi,src= from_lang,dest= to_lang)
text = translator.text
talk(text)
print(text)

"""

"""
import os
import json
from deep_translator import GoogleTranslator
translator = GoogleTranslator(source='en', target='hi')
print(translator.translate("Welcome to our tutorial!"))
"""
"""
    elif 'open application' in command:
        inp = command.replace('open application', '')
        if inp:
            talk('Opening' + inp)
            #os.system(inp)
            #run(inp)
        else:
            talk('No Such app or maybe you said wrong name')

    """