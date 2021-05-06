import sys
import sysconfig
import datetime
from datetime import datetime
import os
from os import system
import json

cls = lambda: system('cls')
cls()

#Verbindung zu Data.json
with open("C:/Users/Gaming PC/Documents/GitHub/Intelligent-AI-Chatbot/Chatbot/Data.json") as f:
    data = json.load(f)

#Sprache überprüfen
global ERROR_NO_RESULT
ERROR_NO_RESULT = "-"
if data['Sprache'] == "DE":
    ERROR_NO_RESULT = data['ERROR_NO_RESULT_DE']
elif data['Sprache'] == "EN":
    ERROR_NO_RESULT = data['ERROR_NO_RESULT_EN']

#Text überprüfen
def text():
    Frage = input("<Du> ")
    if Frage == "cls":
        cls()
        text()
    elif Frage in data['Fragen']:
        index = data['Fragen'].index(Frage)
        Antwort = data['Antworten'][index]
        print(f"<AI> {Antwort}")
        text()
    else:
        print(f"<AI> {ERROR_NO_RESULT}")
        text()

text()