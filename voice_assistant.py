import speech_recognition as sr
from gtts import gTTS
import os
import webbrowser

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand your command. Please try again.")
        return ""
    except sr.RequestError:
        print("Sorry, there was an error with the speech recognition service.")
        return ""

def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save("output.mp3")
    os.system("start output.mp3")

def open_website(url):
    webbrowser.open(url)

def main():
    while True:
        command = listen()
        if "hello" in command.lower():
            speak("Hello! How can I assist you?")
        elif "open website" in command.lower():
            speak("Sure, which website would you like to open?")
            website = listen()
            if "google" in website.lower():
                open_website("https://www.google.com")
            elif "youtube" in website.lower():
                open_website("https://www.youtube.com")
            elif "reddit" in website.lower():
                open_website("https://www.reddit.com")
            else:
                speak("Sorry, I don't have a link for that website.")
        elif "goodbye" in command.lower():
            speak("Goodbye! Have a great day!")
            break
        else:
            speak("Sorry, I don't understand that command.")

if __name__ == "__main__":
    main()