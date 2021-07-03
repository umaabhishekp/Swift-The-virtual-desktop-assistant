import pyttsx3
import speech_recognition as sr
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import subprocess
import cv2
import os
from GoogleNews import GoogleNews

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say('Welcome! I am swift')
print('Welcome! I am swift')
engine.say('What can I do for you!!')
print('What can I do for you!!')
engine.runAndWait()
def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:

            print('I am listening!')
            r.adjust_for_ambient_noise(source)
            r.pause_threshold = 1
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'swift' in command:
                command = command.replace('swift', '')
                print(command)
    except:
        talk("Pardon me! You are not audible!")
        print("Pardon me! You are not audible!")
        return "None"
        pass
    return command


def run_Nimbus():
    command = take_command()
    print(command)
    if 'play' in command or 'play music' in command:
        talk('Playing a song from your computer!')
        print('Playing a song from your computer!')
        music_dir = 'D:\\music'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir, songs[0]))
    elif 'hello' in command:
        talk('Yes!. Your audible!. What can I do for you?')
        print('Yes!. Your audible!. What can I do for you?')
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('The time is' +time)
        print(time)
    elif 'wikipedia' in command:
        search = command.replace('wikipedia', '')
        info = wikipedia.summary(search, 1)
        print("Accroding to wikipedia")
        talk("Accroding to wikipedia")
        print(info)
        talk(info)
    elif 'who is' in command:
        search = command.replace('who is', '')
        info = wikipedia.summary(search, 1)
        print(info)
        talk(info)
    elif 'how are you' in command:
        talk('Thanks for your concern. I am doing good!!')
        print('Thanks for your concern. I am doing good!!')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif "who made you" in command or "created you" in command:
        who = "I am created by Uma Abhishek Polakonda."
        talk(who)
        print(who)
    elif 'stop' in command:
        stop_listening()
    elif 'What can you do for me' in command or 'help me' in command:
        print("There are Three things that i can do for you. I can search for anything on google, or youtube, or wikipedia")
        talk("There are three things that i can do for you. i can search for anything on google, or youtube, or wikipedia")
        print(f"Please tell me in Which platform should I search")
        talk(f"please tell me in Which platform should i search")
        while 1:
            query1 = take_command().lower()
            if query1 != "none":
                if "google" in query1:
                    talk(f"opening  google !")
                    print(f"opening  google !")
                    talk('Here are some results which may be useful for you!')
                    print('Here are some results which may be useful for you!')
                    webbrowser.open("www.google.com/search?q=" + query1 + "")
                    break

                elif "youtube" in query1:
                    talk(f"opening youtube!")
                    print(f"opening youtube!")
                    talk('Here are some results which may be useful for you!')
                    print('Here are some results which may be useful for you!')
                    webbrowser.open("www.youtube.com/results?search_query=" + query1 + "")
                    break

                elif "wikipedia" in query1:
                    print("seraching .......")
                    talk("seraching .......")
                    result = (wikipedia.summary(query1, sentences=3))
                    talk('Here are some results which may be useful for you!')
                    print('Here are some results which may be useful for you!')
                    print("Accroding to wikipedia")
                    talk("Accroding to wikipedia")
                    print(result)
                    talk(result)

                    break
    elif 'google' in command:
        talk(f"opening  google !")
        print(f"opening  google !")
        webbrowser.open("www.google.com/search?q=")
    elif 'youtube' in command:
        talk(f"opening  YouTube !")
        print(f"opening  YouTube !")
        webbrowser.open("www.youtube.com")
    elif 'calculator' in command:
        cal()
    elif 'camera' in command:
        open_camera()
    elif 'visual studio code' in command:
        print('Opening visual studio code')
        talk('Opening visual studio code')
        codepath = "C:\\Users\\Uma Abhishek P\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codepath)

    elif 'pycharm' in command:
        print('Opening Pycharm IDE...Please wait!')
        talk('Opening Pycharm IDE...Please wait!')
        codepath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.1.3\\bin\\pycharm64.exe"

    elif 'zoom' in command:
        print('Opening Zoom application...Please wait!')
        talk('Opening Zoom application...Please wait!')
        codepath = "C:\\Users\\Uma Abhishek P\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"




def stop_listening():
    print('Thanks for your time! Good Bye!')
    talk('Thanks for your time! Good Bye!')
    exit()

def cal():
    print("opening calculator")
    talk("opening calculator")
    subprocess.Popen("C:\\Windows\\System32\\calc.exe")

def open_camera():
    print("opening Camera")
    talk("opening camera")
    video = cv2.VideoCapture(0)
    if (video.isOpened() == False):
        print("Error Reading Video File")

    frame_width = int(video.get(3))
    frame_height = int(video.get(4))

    size = (frame_width, frame_height)

    result = cv2.VideoWriter(
        'Myvideo.avi', cv2.VideoWriter_fourcc(*'MJPG'), 10, size)
    while(True):
        ret, frame = video.read()
        if ret == True:
            result.write(frame)
            cv2.imshow('Frame:', frame)
            if cv2.waitKey(1) & 0xFF == ord('s'):
                break
        else:
            break


while True:
    run_Nimbus()


