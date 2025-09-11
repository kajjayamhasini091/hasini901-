"""
AI Desktop Virtual Assistant (voice + fallback text input)

Features:
- Speech recognition (SpeechRecognition + PyAudio)
- Text-to-speech (pyttsx3, offline)
- Wikipedia search
- Open websites (Google, YouTube, Gmail)
- Play a song on YouTube using pywhatkit
- Open common local applications (example for Windows)
- Exit/stop commands
"""

import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia
import pywhatkit
import os
import sys
import subprocess
import time
import platform
import random

# ---------------------- Configuration ----------------------
VOICE_RATE = 150
VOICE_VOLUME = 1.0
WIKI_SENTENCES = 2
# You can add paths for apps you want to open on your machine
LOCAL_APPS = {
    "notepad": "notepad" if platform.system() == "Windows" else "gedit",  # example
    "calculator": "calc" if platform.system() == "Windows" else "gnome-calculator",
}
# -----------------------------------------------------------

# Initialize TTS engine
engine = pyttsx3.init()
engine.setProperty("rate", VOICE_RATE)
engine.setProperty("volume", VOICE_VOLUME)
voices = engine.getProperty("voices")
# choose voice index (0 or 1 usually). Change if you want different voice.
if len(voices) > 0:
    engine.setProperty("voice", voices[0].id)


def speak(text: str):
    """Speak the given text (and print it)."""
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


def wish_user():
    """Greet user based on time of day."""
    hour = datetime.datetime.now().hour
    if 5 <= hour < 12:
        greet = "Good morning"
    elif 12 <= hour < 17:
        greet = "Good afternoon"
    elif 17 <= hour < 21:
        greet = "Good evening"
    else:
        greet = "Hello"

    extras = ["How can I help you today?", "What can I do for you?", "I'm here — tell me a command."]
    speak(f"{greet}. {random.choice(extras)}")


def take_command_listen(timeout=6, phrase_time_limit=8):
    """
    Listen from microphone and return recognized text.
    If microphone or PyAudio is not available, raises an exception.
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=0.6)
        audio = r.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"You: {query}")
        return query
    except sr.WaitTimeoutError:
        print("Listening timed out — no speech detected.")
        return ""
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return ""
    except sr.RequestError as e:
        print(f"Recognition request error: {e}")
        return ""


def take_command():
    """
    Try to capture voice command. If microphone/PyAudio isn't available,
    fall back to text input from keyboard.
    """
    try:
        # test microphone access
        mic_list = sr.Microphone.list_microphone_names()
        if not mic_list:
            raise RuntimeError("No microphones found")
        text = take_command_listen()
        if text is None:
            return ""
        return text
    except Exception as e:
        # Fallback
        print("Microphone not available or error:", e)
        speak("I can't access the microphone. Please type your command.")
        return input("Type command: ")


def tell_time():
    now = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The time is {now}")


def tell_date():
    today = datetime.datetime.now().strftime("%A, %B %d, %Y")
    speak(f"Today is {today}")


def search_wikipedia(query: str):
    try:
        speak("Searching Wikipedia...")
        # remove keyword if present
        keywords = ["wikipedia", "search wikipedia for", "search wikipedia", "tell me about", "who is", "what is"]
        q = query.lower()
        for k in keywords:
            if k in q:
                q = q.replace(k, "")
        q = q.strip()
        if not q:
            speak("Please say what you want me to search on Wikipedia.")
            return
        summary = wikipedia.summary(q, sentences=WIKI_SENTENCES)
        speak(summary)
    except Exception as e:
        print("Wikipedia error:", e)
        speak("Sorry, I couldn't find information on Wikipedia for that query.")


def open_website(url: str):
    speak(f"Opening {url}")
    webbrowser.open(url)


def play_youtube(song: str):
    speak(f"Playing {song} on YouTube")
    try:
        pywhatkit.playonyt(song)
    except Exception as e:
        print("pywhatkit error:", e)
        speak("Sorry, I couldn't play that right now.")


def open_local_app(app_name: str):
    key = app_name.lower().strip()
    if key in LOCAL_APPS:
        cmd = LOCAL_APPS[key]
        speak(f"Opening {app_name}")
        try:
            # Windows: simple command; Linux: command name; macOS: could use 'open -a'
            if platform.system() == "Windows":
                subprocess.Popen(cmd)
            elif platform.system() == "Darwin":  # macOS
                subprocess.Popen(["open", "-a", cmd])
            else:  # Linux
                subprocess.Popen([cmd])
        except Exception as e:
            print("Error opening local app:", e)
            speak("Sorry, I couldn't open that application.")
    else:
        speak(f"I don't have a shortcut to open {app_name}. You can add its path to the LOCAL_APPS dict.")


def main_loop():
    wish_user()

    while True:
        speak("Listening for your command.")
        command = take_command().lower()

        if not command:
            # If the user didn't say anything, continue listening
            time.sleep(0.5)
            continue

        # Exit commands
        if any(phrase in command for phrase in ["exit", "quit", "stop", "goodbye", "shutdown", "sleep"]):
            speak("Goodbye. Have a great day!")
            break

        # Time / Date
        elif "time" in command and "what" in command or command.strip() == "time" or "the time" in command:
            tell_time()

        elif "date" in command or "day" in command and "what" in command:
            tell_date()

        # Wikipedia queries
        elif "wikipedia" in command or command.startswith("who is") or command.startswith("what is") or "tell me about" in command:
            search_wikipedia(command)

        # Play song on YouTube: "play despacito" or "play song <name>"
        elif command.startswith("play ") or "play " in command and "youtube" in command:
            # attempt to extract song
            song = command.replace("play", "").replace("on youtube", "").strip()
            if song:
                play_youtube(song)
            else:
                speak("Which song would you like me to play?")

        # Open websites
        elif "open youtube" in command:
            open_website("https://www.youtube.com")
        elif "open google" in command:
            open_website("https://www.google.com")
        elif "open gmail" in command or "open email" in command:
            open_website("https://mail.google.com")

        # Search web query using Google
        elif command.startswith("search for ") or command.startswith("search "):
            query = command.replace("search for", "").replace("search", "").strip()
            if query:
                speak(f"Searching the web for {query}")
                open_website(f"https://www.google.com/search?q={query.replace(' ', '+')}")
            else:
                speak("What would you like me to search for?")

        # Local apps
        elif "open notepad" in command or "open notepad" in command:
            open_local_app("notepad")
        elif "open calculator" in command or "open calc" in command:
            open_local_app("calculator")
        elif command.startswith("open "):
            app_candidate = command.replace("open ", "").strip()
            open_local_app(app_candidate)

        # Fallback: repeat or unknown
        else:
            speak("I didn't get that. You can say commands like: 'what is the time', 'search wikipedia for <topic>', 'play <song>', 'open youtube', or 'open notepad'.")


if __name__ == "__main__":
    try:
        main_loop()
    except KeyboardInterrupt:
        speak("Assistant stopped by user. Goodbye.")
        sys.exit(0)
