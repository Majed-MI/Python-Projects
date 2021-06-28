# Jarvis Audio speaking and implementing function for the work advised by the user
# importing modules
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

# voice engine opening for the jarvis
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# setting the voice id for the jarvis
engine.setProperty('voice',voices[0].id)

# speaking function and audio as the value
def speak(audio):
    # voice engine taking the audio value and running and waiting function
    engine.say(audio)
    engine.runAndWait()

# wishing me when i run the program
def wishMe():
    # hour declaring from the datetime module
    hour = int(datetime.datetime.now().hour)
    # morning afternoon evening and night clarification
    if hour >= 0 and  hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    elif hour >= 18 and hour < 20:
        speak("Good Evening")
    else:
        speak("Good Night")
    speak("I am Jarvis . Sir, Please tell me how may i help you?")

# taking Command function
def takeCommand():
    # speak recognition open for which user can speak and jarvis can listen
    r = sr.Recognizer()
    # microphone open to take the voice from user and the audio value is going to be listened by the jarvis
    with sr.Microphone() as source:
        print("listening....")
        # waiting jarvis to hear the voice for 1 seconds
        r.pause_threshold = 1
        # audio value takes the voice from the user and putting it in the source value
        audio = r.listen(source)

    # try to catch the voice without error
    try:
        print("Recognizing..")
        # taking the query value for the input voice and audio is the value which is to be
        # recognized and language is english but bengalitype
        query = r.recognize_google(audio, language="en-BAN")
        # what user said will be printed
        print(f"User Said: {query}")

    # error handling and printing the error and show some text too
    except Exception as e:
        print(e)
        print("Say that again please!...")
        return "None"
    return query

# only applicable when under these function
if __name__ == '__main__':
    # calling wishme function to get greeting from jarviss
    wishMe()
    # while loop to continue again and again
    while True:
        # taking command in lower case so everything seems ok
        query = takeCommand().lower()

        # wikipedia if said by user
        if 'wikipedia' in query:
            # try to do these without erro
            try:
                speak("Searching Wikipedia..")
                # if wikipedia and something is said with it then it will take wikipedia one way and the other
                # in other way means it will separate
                query = query.replace("wikipedia","")
                # results declaring which will wikipedia summarize the query and 2 sentences will be given
                # by the jarvis
                results = wikipedia.summary(f'{query}', sentences=2 )
                speak("According to Wikipedia")
                # printing the results and also speaking by jarvis
                print(results)
                speak(results)
            # error handling
            except Exception as e:
                print(e)

        # if user says open youtube
        elif 'open youtube' in query:
            # webbrowser module implementing and opening youtube
            webbrowser.open("youtube.com")
            print("Opening Youtube")

        # if user says open google
        elif 'open google' in query:
            webbrowser.open("google.com")
            print("Opening Google")

        # if user says open stack overflow
        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
            print("Opening Stack OverFlow")

        # if user says open whatsapp
        elif 'open whatsapp' in query:
            webbrowser.open("whatsapp.com")
            print("Opening Whatsapp")

        # if user says play music
        elif 'play music' in query:
            # targeting the music directory file
            music_dir = "C:\\Users\\iftekhar\\Music\\Playlists"
            # songs value declaring which will direct the music directory path in a list
            songs = os.listdir(music_dir)
            # printing all the song name
            print(songs)
            # starting the file with os.path.join function and the song[0] will start
            os.startfile((os.path.join(music_dir,songs[0])))
            print("Playing Musics")

        # if user says time
        elif 'time' in query:
            # strTime as value to get the datetime in the format given
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            # speaking the time from jarvis and printing
            speak(f"The time is {strTime}")
            print(f"The time is {strTime}")

        # if user says studio code
        elif 'studio code' in query:
            # targeting the vs code file
            vs_code = "C:\\Users\\iftekhar\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            # starting vscode
            os.startfile(vs_code)
            print("Opening VS Code")

        # if user says program
        elif 'program' in query:
            pycharm = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.3\\bin\\pycharm64.exe"
            os.startfile(pycharm)
            print("Opening Pycharm")


