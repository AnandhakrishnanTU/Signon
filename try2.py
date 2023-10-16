import pyttsx3

text_speech=pyttsx3.init()

anser=input("say something :")

text_speech.say(anser)

text_speech.runAndWait()