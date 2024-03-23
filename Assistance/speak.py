import pyttsx3

def Speak(Text):
    engine = pyttsx3.init('sapi5')  # sapi is a windows API for voice....
    voices = engine.getProperty('voices')
    engine.setProperty('voices', voices[1].id)
    engine.setProperty('rate',170)
    # engine.say("Hello Sir I am Robot")
    print(" ")
    print(f"You : {Text}.")
    print(" ")
    engine.say(Text)
    # engine.save_to_file(text=str)
    engine.runAndWait()

# Speak("Hello Baby")
import speech_recognition as sr
def prompinput():
    s = sr.Recognizer()
    Speak("Say your Prompt....")
    with s.Microphone() as m:
        audio=sr.listen(m)
        query=sr.recognize_google(audio,language='eng-in')
        return query
        
print(prompinput())

