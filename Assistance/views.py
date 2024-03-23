from django.shortcuts import render, redirect
from django.http import JsonResponse
import openai
import pyttsx3
import speech_recognition as sr
from .models import ChatMessage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages

def Speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voices', voices[1].id)
    engine.setProperty('rate', 170)
    print(" ")
    print(f"You: {text}.")
    print(" ")
    engine.say(text)
    engine.runAndWait()

openai_api_key = 'YourAPI'
openai.api_key = openai_api_key

def Listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening.......")
        r.pause_threshold = 1
        audio = r.listen(source, 0, 8)  # Listening Mode

    try:
        print("Recognizer.....")
        query = r.recognize_google(audio, language='en')
    except Exception as e:
        print("Error: ", e)
        return ""  # Return an empty string if speech recognition fails

    query = query.lower()
    return query

def get_completion(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",  #Choice best model...
        messages=[
            {"role": "user", "content": prompt},
            {"role": "assistant", "content": prompt},
        ],
        max_tokens=150
    )

    answer = response.get('choices')[0]['message']['content'].strip()
    return answer


def Speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voices', voices[1].id)
    engine.setProperty('rate', 170)
    print(" ")
    print(f"You: {text}.")
    print(" ")
    engine.say(text)
    engine.runAndWait()

# openai_api_key = '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'
# openai_api_key = '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'
openai.api_key = openai_api_key

def Listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening.......")
        r.pause_threshold = 1
        audio = r.listen(source, 0, 8)  # Listening Mode

    try:
        print("Recognizer.....")
        query = r.recognize_google(audio, language='en')
    except Exception as e:
        print("Error: ", e)
        return ""  # Return an empty string if speech recognition fails

    query = query.lower()
    return query
def get_completion(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt},
            {"role": "assistant", "content": prompt},
        ],
        max_tokens=150
    )

    answer = response.get('choices')[0]['message']['content'].strip()
    return answer

def chatbot(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            prompt = request.POST.get('prompt')
            response = get_completion(prompt)
            
            # Save chat message to database
            if request.user.is_authenticated:
                ChatMessage.objects.create(user=request.user, message=prompt)
                ChatMessage.objects.create(user=request.user, output=response)
            
            return JsonResponse({'response': response})

        return render(request, 'Pages/output.html')
    else:
        return render(request,'Register/login.html')


def record(request):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        Speak("Run...")
        print("Listening.......")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=8)  # Listening Mode
    try:
        print("Recognizer.....")
        transcription = r.recognize_google(audio, language='en')
        return JsonResponse({'transcription': transcription})
    except Exception as e:
        print("Error: ", e)
        return JsonResponse({'transcription': ''})




def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        m_number = request.POST['m_number']
        password = request.POST['password']
        c_password = request.POST['c_password']
        if password == c_password:
            user = User.objects.create_user(username=username, email=email, password=password)
            # Assuming 'm_number' is a custom field of your user model
            user.m_number = m_number
            user.save()
            messages.success(request, 'Account successfully created.')
            return redirect('/home')
        else:
            messages.error(request, 'Passwords do not match!')
    return render(request, 'Register/register.html')

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/home')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('/')  # Redirect to the login page to display the error message
    return render(request, 'Register/login.html')


# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'Pages/about.html')

