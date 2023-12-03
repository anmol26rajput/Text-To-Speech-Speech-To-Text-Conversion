from tkinter import *
from tkinter.messagebox import showinfo
from gtts import gTTS
import speech_recognition as sr
import os

mainwindow= Tk()
mainwindow.title('Text-To-Speech & Speech-To-Text Converter')
mainwindow.geometry('500x500')
mainwindow.resizable(0, 0)
mainwindow.configure(bg='#ffafbd')

def say(text1):
     language = 'en'
     speech = gTTS(text = text1, lang = language, slow = False)
     speech.save("text.mp3")
     os.system("start text.mp3")

def recordvoice():
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio=r.listen(source)
            try:    
                text = r.recognize_google(audio,language="en-IN")
            except:
                pass
            return text

def TextToSpeech():
    texttospeechwindow = Toplevel(mainwindow)
    texttospeechwindow.title('Text-to-Speech Converter')
    texttospeechwindow.geometry("500x500")
    texttospeechwindow.configure(bg='#b06ab3')

    Label(texttospeechwindow, text='Text-to-Speech Converter', font=("Helvetica", 15), bg='#ddd6f3').place(x=130)

    text = Text(texttospeechwindow, height=6, width=35, font=12)
    text.place(x=50, y=70)
    
    speakbutton = Button(texttospeechwindow, text='play', bg='#56ab2f', command=lambda: say(str(text.get(1.0, END))))
    speakbutton.place(x=220, y=240)

def SpeechToText():
    speechtotextwindow = Toplevel(mainwindow)
    speechtotextwindow.title('Speech-to-Text Converter')
    speechtotextwindow.geometry("500x500")
    speechtotextwindow.configure(bg='#c4e0e5')

    Label(speechtotextwindow, text='Speech-to-Text Converter', font=("Comic Sans MS", 15), bg='#ffd89b').place(x=130)

    text = Text(speechtotextwindow, font=12, height=6, width=35)
    text.place(x=60, y=70)
    
    recordbutton = Button(speechtotextwindow, text='Record', bg='#19547b', command=lambda: text.insert(END, recordvoice()))
    recordbutton.place(x=230, y=250)

Label(mainwindow, text='Text-To-Speech and Speech-To-Text Converter',
     font=('Times New Roman', 16), bg='#4568dc', wrap=True, wraplength=450).place(x=50, y=0)

texttospeechbutton = Button(mainwindow, text='Text-To-Speech Conversion', font=('Times New Roman', 16), bg='#b06ab3', command=TextToSpeech)
texttospeechbutton.place(x=130, y=150)

speechtotextbutton = Button(mainwindow, text='Speech-To-Text Conversion', font=('Times New Roman', 16), bg='#b06ab3', command=SpeechToText)
speechtotextbutton.place(x=130, y=250)

mainwindow.update()
mainwindow.mainloop()