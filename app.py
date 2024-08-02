import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
    except sr.RequestError:
        print("Sorry, my speech service is down.")

def handle_command(command):
    if "hello" in command:
        speak("Hello! How can I assist you today?")
    elif "goodbye" in command:
        speak("Goodbye! Have a nice day.")
        exit()
    elif "how are you" in command:
        speak("I'm doing well, thank you.")
    else:
        speak("Sorry, I didn't understand that command.")

while True:
    command = listen().lower()
    handle_command(command)
