from tkinter import *
import speedtest
import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import  os

def sptext():  # speech to text
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing")
            data = recognizer.recognize_google(audio)
            print(data)
            lab_down.config(text=data)
            return data
        except sr.UnknownValueError:
            print("not understanding")


# sptext()-speech to text

# text to speech

def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty('voice', voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 140)
    engine.say(x)
    engine.runAndWait()

def about():
   msg=("This is python Mini project" )
        # created by Aachal.it is voice assistance which works like alexa\nsome of the questions which you can ask is -\n1.what is your name")
   lab_down.config(text=msg)
def func():
    speechtx("hello welcome to python mini project what can i do for you")
    # if sptext().lower() == "hey peter":
    while True:
        data1 = sptext().lower()
        if " name" in data1:
            name = "my name is peter"
            speechtx(name)
        elif "my birthday" in data1:
            day = "your birthday is on 25 nov "
            speechtx(day)
        elif "age" in data1:
            age = "you are 20 yaers old"
            speechtx(age)

        elif ' time' in data1:
            time = datetime.datetime.now().strftime("%I%M%p")
            speechtx(time)
        elif ' date' in data1:
            date = datetime.datetime.now().date()
            speechtx(date)
        elif 'day' in data1:
            day = datetime.datetime.now().day
            speechtx(day)
        elif 'youtube' in data1:
            webbrowser.open("https://www.youtube.com/")
        elif 'instagram' in data1:
            webbrowser.open("https://www.instagram.com/")
        elif 'joke' in data1:
            joke_1 = pyjokes.get_joke(language="en", category="neutral")
            print(joke_1)
            speechtx(joke_1)
            # speechtx("A bear walks into a bar and says, “Give me a whiskey and … cola.Why the big pause asks the bartender. The bear shrugged. Im not sure; I was born with them.")
        elif 'song' in data1:
            add = "D:\songs"
            listsong = os.listdir(add)
            print(listsong)
            os.startfile(os.path.join(add, listsong[0]))
        elif 'photos' in data1:
            add = "F:\Aachal"
            listsong = os.listdir(add)
            print(listsong)
            os.startfile(os.path.join(add, listsong[0]))
        elif "stop" in data1:
            speechtx("thank you for using our voice assistance")
            break
        else:
            speechtx("not recognizable")
        # else:
        # print("thanks")

sp=Tk()
sp.title("Python Voice Assistance")

menu = Menu(sp)
sp.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open...')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=sp.quit)

helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)

helpmenu.add_command(label='About',command=about)
sp.geometry("500x650")
sp.config(bg="Blue")




lab=Label(sp,text="Python Voice Assistance",font=("Time New Roman",20,"bold"),bg="Blue",fg="white")
lab.place(x=60,y=40,height=50,width=380)



lab_down=Label(sp,text="",font=("Time New Roman",20,"bold"),bg="Blue")
lab_down.place(x=60,y=200,height=200,width=380)



button=Button(sp,text="Start voice assistance",font=("Time New Roman",20,"bold"),relief=RAISED,bg="red",command=func)
button.place(x=60,y=460,height=50,width=380)

sp.mainloop()