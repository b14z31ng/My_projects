import sys
import subprocess
import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes
import random
import smtplib


listener = sr.Recognizer()
jarvis = pyttsx3.init('sapi5')
voices = jarvis.getProperty('voices')
jarvis.setProperty('voice', voices[1].id)
jarvis.setProperty('rate', 190)
jarvis.setProperty('volume', 1.0)


def talk(text):
    jarvis.say(text)
    jarvis.runAndWait()


def quitings():
    sys.exit()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            talk('how can I help you, Reshad Sir?')
            print('how can I help you, Reshad Sir?')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
            if 'jarvis' in command:
                if 'jarvis' == command:
                    talk('yes say something')
                    print('yes say something')
                else:
                    command = command.replace('jarvis', '')

    except:
        pass
    return command


def run_jarvis():
    command = take_command()
    if 'quit' in command:
        cmdlist = ['at your service, sir', 'anytime sir', 'see you soon, sir', 'your wish is my command', 'have a nice day, sir']
        random.shuffle(cmdlist)
        talk(cmdlist[1])
        print(cmdlist[1])
        quitings()
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'tell me about' in command:
        try:
            look_for = command.replace('tell me about', '')
            info = wikipedia.summary(look_for, 3)
            print(info)
            talk(info)
        except:
            talk('I did not get it but I am going to search it for you')
            pywhatkit.search(command)
    elif 'jokes' in command:
        talk(pyjokes.get_joke())
    elif 'do a sum' in command:
        talk('opening calculator sir')
        print('opening calculator sir')
        subprocess.Popen('calc.exe')
    elif 'date' in command:
        talk('Sorry vaiya, I am in another relation')
    elif 'messenger' in command:
        talk('opening messenger sir')
        print('opening messenger sir')
        subprocess.Popen(['C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe', 'www.messenger.com'])
    elif 'check mail' in command:
        talk('just a minute, sir')
        print('just a minute, sir')
        subprocess.Popen(['C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe', 'www.gmail.com'])
    elif 'check maps' in command:
        talk('just a minute, sir')
        print('just a minute, sir')
        subprocess.Popen(['C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe', 'www.maps.com'])
    else:
        talk('I did not get it but I am going to search it for you')
        pywhatkit.search(command)


while True:
    x = 0
    while x == 0:
        run_jarvis()
        x += 1
    while x == 1:
        i = input("press enter to rerun and enter q and hit enter to exit: ").lower()
        if not i:
            run_jarvis()
        elif i == 'q':
            cmd1list = ['at your service, sir', 'anytime sir', 'see you soon, sir', 'your wish is my command',
                       'have a nice day, sir']
            random.shuffle(cmd1list)
            talk(cmd1list[1])
            print(cmd1list[1])
            quitings()
            x = 0
        else:
            print('please put a valid command')