import speech_recognition as sr
import pyttsx3
from colorama import Fore, Back, init
from pylogger.operators import cls

init()


def speak(text):
    # Init engine
    engine = pyttsx3.init("sapi5", False)
    engine.say(text)
    engine.runAndWait()


def listen(time) -> str:
    # Initialize recognizer class (for recognizing the speech)
    print(
        f">>>{Fore.LIGHTBLACK_EX} Speak your message to the model(say help for help message, say type to use type mode){Fore.RESET}",
        end="\r",
        flush=True,
    )
    r = sr.Recognizer()
    # Reading Microphone as source
    # listening the speech and store in audio_text variable
    with sr.Microphone() as source:
        audio_text = r.listen(source)
        # recognize_() method will throw a request
        # error if the API is unreachable,
        # hence using exception handling

        try:
            # using google speech recognition
            return r.recognize_google(audio_text)
        except:
            return "Did not get input"
