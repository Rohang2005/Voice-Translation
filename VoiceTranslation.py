from deep_translator import GoogleTranslator
import pyttsx3
from gtts import gTTS
import os
import sys
import speech_recognition as sr
from langdetect import detect
def take_audio_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say Something")
        recognizer.adjust_for_ambient_noise(source)
        audio_data = recognizer.listen(source) 
    return audio_data

def transcribe_audio(audio_data):
    recognizer = sr.Recognizer() 
    try:
        print("Converting your speech to text....")
        text = recognizer.recognize_google(audio_data)
        return text
    except sr.UnknownValueError:
        print("Cound not understand spoken language or audio please try again.")
        sys.exit()
    except sr.RequestError as e:
        print("Could not translate due to unexpected error.")
        sys.exit()

def language_detect(audio):
    language=detect(audio)
    return language
        
def translate_text(text, lang1, lang2):
    try:
        translated_text = GoogleTranslator(source=lang1, target=lang2).translate(text)
        return translated_text
    except Exception as e:
        print("An error occurred during translation")
        return None

def main():
    audio_data = take_audio_input()
    text = transcribe_audio(audio_data)
    language=language_detect(text)
    print(text)
    print('Your language is: ',language)
    verify=input('Is this your language?Yes(y) or No(n): ')
    if(verify=='y'):
        lang1 =language
        lang2 = input("Enter the language to be converted to ")
        translated_text = translate_text(text, lang1, lang2)
        print(translated_text)
        
    else:
        
        lang1 = input("Enter the language from which conversion has to take place ")
        lang2 = input("Enter the language to be converted to ")
        translated_text = translate_text(text, lang1, lang2)
        print(translated_text)

    engine = pyttsx3.init()

    if translated_text:
        #print("Translated Text: ", translated_text)
        #engine.say(translated_text)
        #engine.runAndWait()
        tts = gTTS(translated_text, lang=lang2)
        tts.save("output.mp3")
        os.system("start output.mp3")

if __name__ == "__main__":
    main()
