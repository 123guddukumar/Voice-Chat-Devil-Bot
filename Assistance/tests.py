# from django.test import TestCase

import openai

# import pyttsx3

# def Speak(Text):
#     engine = pyttsx3.init('sapi5')  # sapi is a windows API for voice....
#     voices = engine.getProperty('voices')
#     engine.setProperty('voices', voices[1].id)
#     engine.setProperty('rate',170)
#     # engine.say("Hello Sir I am Robot")
#     print(" ")
#     print(f"You : {Text}.")
#     print(" ")
#     engine.say(Text)
#     # engine.save_to_file(text=str)
#     engine.runAndWait()
    
# # openai_api_key = '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'
# openai_api_key = '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'
# openai.api_key = openai_api_key

# def get_completion(prompt):
#     query = openai.ChatCompletion.create(
#         model='gpt-4',
#         messages=[{"role": "user", "content": prompt }],
#         max_tokens=150
#     )
#     response = query.get('choices')[0]['message']['content']
#     return response
# import speech_recognition as sr
# def Listen():
#     r = sr.Recognizer()

#     with sr.Microphone() as source:
#         print("Listening.......")
#         r.pause_threshold = 1
#         audio = r.listen(source, 0, 8)  # Listening Mode

#     try:
#         print("Recognizer.....")
#         query = r.recognize_google(audio, language='en')
#         return query
#     except Exception as e:
#         print("Error: ", e)
#         return ""  # Return an empty string if speech recognition fails

# Speak("Say Prompt.....")
# prom = Listen()
# message = prom
# response = get_completion(message)

# print("Response:", response)
# # Speak(response)
# # import openai

# # Set your OpenAI API key
openai_api_key = 'YourApi'
openai.api_key = openai_api_key

def list_available_models():
    try:
        models = openai.Engine.list()
        return [model["id"] for model in models.data]
    except Exception as e:
        print("An error occurred while retrieving available models:", e)
        return None

# Call the function to list available models
available_models = list_available_models()

if available_models:
    print("Available models for your API key:")
    for model in available_models:
        print(model)
else:
    print("Failed to retrieve available models.")
