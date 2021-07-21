import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import psutil
import pyjokes

engine = pyttsx3.init()
engine.say('This is Friday')
engine.runAndWait()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
newVoiceRate = 150
engine.setProperty('rate', newVoiceRate)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak('This is Friday')

def time():
    Time= datetime.datetime.now().strftime('%I:%M:%S')
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month= int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak('the current date is')
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak('Welcome back sir')
   
    hour = datetime.datetime.now().hour

    if hour > 6 and hour <= 12:
        speak('Good morning')
    elif hour >=12 and hour <18:
        speak('Good afternoon')
    elif hour >=18 and hour <= 24:
        speak('Good evening') 
    else:
        speak('Good night')       

    speak('Friday at your service. How can i help you?')

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('Recognizing...') 
        query = r.recognize_google(audio, 'en=US')
        print(query)   
    except Exception as e:
        print(e)
        speak('Say that again please...')
        return 'None'
    return query
def sendmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(from_addrs = '', password= '')
    server.sendmail( '', to, content)  
    server.close()

def cpu():
    usage = str(psutil.cpu.percent())
    speak('CPU is at' + usage)

    battery = psutil.sensors_battery
    speak('battery is at')
    speak(battery.percent)

def jokes():
    speak(pyjokes.get_joke())    


if __name__ == '__main__':

    wishme()
    while True:
        query = takeCommand().lower()
        print(query)

        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'offline' in query:
            quit()
        elif 'wikipedia' in query:
            speak('Searching...') 
            query = query.replace('wikipedia', '')
            result = wikipedia.summary(query, sentence = 2)  
            speak(result) 
        elif 'send mail' in query:
            try:
                speak('What should i  say?')
                content = takeCommand()
                to = ''
                sendmail(to, content)
                speak('Email sent successfully')
            except Exception as e:
                speak(e)
                speak('Unable to send the message')  
        elif 'search in chrome' in query:
            speak('What should i search')
            chromepath = "C:\Program Files\Google\Chrome\Application\chrome.exe %s"
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + '.com')
        elif 'logout' in query:
            os.system('shutdown - 1')    
        elif 'shutdown' in query:
            os.system('shutdown /s /t 1') 
        elif 'restart' in query:
            os.system('shutdown /r /t 1') 
        elif 'play songs' in query:
            songs_dir = "F:\musics\music"
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0])) 
        elif 'remenber' in query:
             speak('What should i remember?')
             data = takeCommand()
             speak('you said i should remember', data)
             remember = open('data.txt', 'w')  
             remember.write(data)
             remember.close() 
        elif 'do you know anything' in query:
            remember = open('data.txt', 'r')   
            speak('you said i should remember that' + remember.read())  

        elif 'cpu' in query:
            cpu()    
        elif 'jokes' in query:
            jokes()    













