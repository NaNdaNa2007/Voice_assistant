import speech_recognition as sr
import pyttsx3
import wikipedia
import pywhatkit
from datetime import datetime

listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            listener.adjust_for_ambient_noise(source, duration=1)
            voice = listener.listen(source, timeout=5, phrase_time_limit=5)
            command = listener.recognize_google(voice)
            print("You said:", command)
            return command.lower()

    except Exception:
        return ""


while True:
    command = take_command()

    if "play" in command:
        song = command.replace("play", "").strip()
        talk("Playing " + song)
        pywhatkit.playonyt(song)

    elif "who is" in command:
        person = command.replace("who is", "").strip()
        try:
            info = wikipedia.summary(person, sentences=1)
            print(info)
            talk(info)
        except Exception:
            talk("Sorry, I couldn't find information.")

    elif "time" in command:
        current_time = datetime.now().strftime("%I:%M %p")
        talk("Current time is " + current_time)

    elif "stop" in command:
        talk("Goodbye")
        break

    elif command == "":
        continue

    else:
        talk("I did not understand.")
