import datetime #import package for date and time
import webbrowser#import package for webbrowser
import  speech_recognition as sr #import pacakge for webbrowser
import pyttsx3
import wikipedia #import pacakage of wikipedia

engine = pyttsx3.init("sapi5") #this is an api key for text to speech by microsoft
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning!")
    elif hour>=12 and hour<18:
        speak("Good afternoon")
    else:
        speak("Good evening")

    speak("Jarvis  Here  How can I help you today?")


def takeCommand(): #it takes microphone as input and return as string
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listning....")
        r.pause_threshold= 1
        audio = r.listen(source)

    try:
        print("Recoginizing.....")
        query = r.recognize_google(audio,language= 'en-in')
        print("user said",query)

    except Exception as e:
        print("Say again")
        speak("please speak again i can't recognized")
        return "None"

    return query


if __name__ == '__main__':
    wishMe()
    speak("now i am Ready to take your commands")
    if 1:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia',"")
            results = wikipedia.summary(query,sentences = 2)
            speak("According to wikipedia..")
            speak(results)
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'stop jarvis' in query:
            speak("Ok See you soon Bye Have a Nice day")
            quit()

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak("Sir the time is")
            speak(strTime)

        elif 'play music' in query:
            webbrowser.open("https://amitness.com/shuffle")
            speak("Ok the music is going to play")

        elif 'hello javis' in query:
            speak("hello how are you  sir")

        elif 'what is your age' in query:
            speak("I am not allowed to tell my age by my programmer")

        elif 'no one gonna know' in query:
            speak("they gonna know")

        elif 'whats going jarvis' in query:
            speak("Nothing special another day at your service ")

