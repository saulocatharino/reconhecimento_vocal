import speech_recognition as sr
import time
import os

def tudo():
    try:
        r = sr.Recognizer()
        lang = "pt-BR"

        with sr.Microphone() as source:

            print("\n Diga Algo!")
            audio = r.listen(source)

            txt = r.recognize_google(audio,language=lang)

        try:
            print("-----------------------------------------")
            print()
            print("Você disse:\n" + r.recognize_google(audio, language=lang))
            print()
        except:
            time.sleep(1)
    except:
        time.sleep(1)
        tudo()

while True:
    tudo()