import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os #for music or sound
import smtplib


engine=pyttsx3.init('sapi5')   #take voice from windows
voices=engine.getProperty('voices')
# print(voices[0].id) #we have two voices that is male or female
engine.setProperty('voices',voices[0].id)   #voices[0].id is for female


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12: #morning time
        speak('good morning Rafat')
    elif  hour>=12 and hour<18:
        speak("good after noon Rafat")
    else:
        speak('good evening Rafat')
    speak('hello dear....... I am your personal Assistant Mr. Champ. Please Tell me how may I help you ')

def takeCommand():
    # it takes microphone input from user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening....')
        r.pause_threshold = 1     #secconds of non-speaking audio before a phrase is considered completed
        audio=r.listen(source)
    try:
        print("Recognising..........")
        query = r.recognize_google(audio,language='en-in')      #use google's engine
        print(f"Rafat said: {query}\n")
    except Exception as e:
        # print(e)
        print("please!! say it again")
        return 'None' # it will return the none string
    return query
    
def sendEmail(to,content):#smptlib is pre installed through which we can send email via google
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('yourmail@gmail.com',password)
    server.sendmail('yourmail@gmail.com',to,content)
    server.close()


if __name__ == '__main__':
    # speak("Rafat is very pretty")
    wishMe()
    while True:

        query=takeCommand().lower()
    # logic for executing tasks
        if 'wikipedia' in query:
            speak("searching wikipedia........please wait Rafat")
            query=query.replace('wikipedia','')
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open facebook' in query:
            webbrowser.open('facebook.com')

        elif 'open instagram' in query:
            webbrowser.open('instagram.com')

        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')

        elif 'open music' in query:
            Album='e:\\Album'
            songs=os.listdir(Album)
            print(songs)
            os.startfile(os.path.join(Album,songs[4]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f"hey!!!!!!!!friend!!!!..........the time is {strTime}")
        
        elif "open code" in query:
            path="C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)
        
        elif "email to Aman" in query:
            try:
                speak("what should I say ")
                content = takeCommand()
                to=youremail.com
                sendEmail(to,content)
                Speak('Email has been sent successfully!!!')
            except Exception as e:
                speak('sorry Rafat i am not able to send mail to this address')
        elif "exit" in query:
            speak('MR Champ  accepting command.....!!!')
            exit()