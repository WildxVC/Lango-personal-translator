# Authors: Vinayak Chhatrashali
#          Harshvardhan Singh Sisodia
import speech_recognition as sr
import pyttsx3
from translate import Translator
from playsound import playsound
from gtts import gTTS
import os
from tabulate import tabulate


# Initialize the recognizer
r = sr.Recognizer()

# Function to convert text to
# speech


def SpeakText(command):

    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


SpeakText("Hey! I am Lango Your personal translator!  Help me with a few details")
SpeakText("you can refer to the list on your screen for the language code.")


l1 = [["af", "afrikaans",
       "sq", "albanian",
       "am", "amharic",
       "ar", "arabic"],
      ["hy", "armenian",
       "az", "azerbaijani",
       "eu", "basque",
       "be", "belarusian"],
      ["bn", "bengali",
       "bs", "bosnian",
       "bg", "bulgarian",
       "ca", "catalan"],
      ["ceb", "cebuano",
       "ny", "chichewa",
       "zh-cn", "chinese (simplified)",
       "zh-tw", "chinese (traditional)"],
      ["co", "corsican",
       "hr", "croatian",
       "cs", "czech",
       "da", "danish"],
      ["nl", "dutch",
       "en", "english",
       "eo", "esperanto",
       "et", "estonian"],
      ["tl", "filipino",
       "fi", "finnish",
       "fr", "french",
       "fy", "frisian"],
      ["gl", "galician",
       "ka", "georgian",
       "de", "german",
       "el", "greek"],
      ["gu", "gujarati",
       "ht", "haitian creole",
       "ha", "hausa",
       "ha", " 'hawaiian"],
      ["iw", "hebrew",
       "he", "hebrew",
       "hi", "hindi",
       "hm", " 'hmong"],
      ["hu", "hungarian",
       "is", "icelandic",
       "ig", "igbo",
       "id", "indonesian"],
      ["ga", "irish",
       "it", "italian",
       "ja", "japanese",
       "jw", "javanese"],
      ["kn", "kannada",
       "kk", "kazakh",
       "km", "khmer",
       "ko", "korean"],
      ["ku", "kurdish (kurmanji)",
       "ky", "kyrgyz",
       "lo", "lao",
       "la", "latin"],
      ["lv", "latvian",
       "lt", "lithuanian",
       "lb", "luxembourgish",
       "mk", "macedonian"],
      ["mg", "malagasy",
       "ms", "malay",
       "ml", "malayalam",
       "mt", "maltese"],
      ["mi", "maori",
       "mr", "marathi",
       "mn", "mongolian",
       "my", "myanmar (burmese)"],
      ["ne", "nepali",
       "no", "norwegian",
       "or", "odia",
       "ps", "pashto"],
      ["fa", "persian",
       "pl", "polish",
       "pt", "portuguese",
       "pa", "punjabi"],
      ["ro", "romanian",
       "ru", "russian",
       "sm", "samoan",
       "gd", "scots gaelic"],
      ["sr", "serbian",
       "st", "sesotho",
       "sn", "shona",
       "sd", "sindhi"],
      ["si", "sinhala",
       "sk", "slovak",
       "sl", "slovenian",
       "so", "somali"],
      ["es", "spanish",
       "su", "sundanese",
       "sw", "swahili",
       "sv", "swedish"],
      ["tg", "tajik",
       "--", "--",
       "--", "--",
       "th", "thai"],
      ["tr", "turkish",
       "uk", "ukrainian",
       "--", "--",
       "ug", "uyghur"],
      ["uz", "uzbek",
       "vi", "vietnamese",
       "cy", "welsh",
       "xh", "xhosa"],
      ["yi", "yiddish",
       "yo", "yoruba",
       "zu", "zulu", "--", "--"]]
table1 = tabulate(l1, headers=['Code', 'Language',  'Code', 'Language',
                               'Code', 'Language', 'Code', 'Language'], tablefmt='orgtbl')
print(table1)

flanguage = input("From language: ")
tlanguage = input("To language: ")

# Loop infinitely for user to
# speak
with sr.Microphone() as source:
    print("Speak 'Hello lango' to initiate the Translator !")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    r.adjust_for_ambient_noise(source, duration=0.2)
    audio = r.listen(source)
    MyText = r.recognize_google(audio)
    MyText = MyText.lower()

while not 'hello lango' in MyText:
    SpeakText("Sorry sir couldn't hear you,speak again please!")
    with sr.Microphone() as source:
        print("Speak 'Hello lango' to initiate the Translator !")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        r.adjust_for_ambient_noise(source, duration=0.2)
        audio = r.listen(source)
        MyText = r.recognize_google(audio)
        MyText = MyText.lower()

if 'hello lango' in MyText:

    SpeakText("Hello Sir!")
    SpeakText("Please speak something you want to translate")

    # Exception handling to handle
    # exceptions at the runtime
    try:

        # use the microphone as source for input.
        with sr.Microphone() as source2:

            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            r.adjust_for_ambient_noise(source2, duration=0.2)

            # listens for the user's input
            audio2 = r.listen(source2)

            # Using google to recognize audio
            MyText = r.recognize_google(audio2, language=flanguage)
            MyText = MyText.lower()
            # lang = detect(MyText)
            # print("Language = " + lang)
            print("Did you say : "+MyText)
            p = Translator(to_lang=tlanguage, from_lang=flanguage)
            translated = p.translate(MyText)
            print(translated)
            # speech = gTTS(text=translated, lang=tlanguage)
            # speech.save('C:\\Users\\vinay\\Music\\Python Langonew\\temp3030.mp3')
            # playsound('C:\\Users\\vinay\\Music\\Python Langonew\\temp3030.mp3')
            # os.remove("C:\\Users\\vinay\\Music\\Python Langonew\\temp3030.mp3")
            SpeakText(translated)
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        # if "C:\\Users\\vinay\\Music\\Python Langonew\\temp3030.mp3":
        #     os.remove(
        #         "C:\\Users\\vinay\\Music\\Python Langonew\\temp3030.mp3")

    except sr.UnknownValueError:
        SpeakText("Ooops didn't hear, Say Again")
        # if "C:\\Users\\vinay\\Music\\Python Langonew\\temp3030.mp3":
        #     os.remove("C:\\Users\\vinay\\Music\\Python Langonew\\temp3030.mp3")
