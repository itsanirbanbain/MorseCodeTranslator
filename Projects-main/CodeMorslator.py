from tkinter import *
from tkinter import messagebox
from playsound import playsound
import pyttsx3 as pyttsx
import time

# Dictionary representing the morse code chart
MORSE_CODE_DICT = {  # Capital letters
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--',
                                        'X': '-..-', 'Y': '-.--', 'Z': '--..',
                    # small letters
                    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',
                                        'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.',
                                        'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
                                        'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..',
                                        # Numbers
                    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
                                        '7': '--...', '8': '---..', '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-',
                                        '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', ',': ','}
rt = Tk()


def engToMorseFunc():
    message = e1.get()
    cipher = ''
    if message != "":
        for letter in message:
            if letter != ' ':
                cipher += MORSE_CODE_DICT[letter] + ' '
            else:
                cipher += ' '
        my_lab10 = Label(
            rt, text="Eng->Morse: " + cipher, bg="white", font=("Arial", 19))
        my_lab10.pack()
    else:
        pass


def morseToEngFunc():
    message = e0.get()
    if message != "":
        message += ' '
        decipher = ''
        citext = ''
        for letter in message:
            if (letter != ' '):
                i = 0
                citext += letter

            else:
                i += 1
                if i == 2:
                    decipher += ' '
                else:
                    k = MORSE_CODE_DICT.keys()
                    v = MORSE_CODE_DICT.values()
                    decipher += list(k)[list(v).index(citext)]
                    citext = ''
        my_lab00 = Label(
            rt, text="Morse->Eng: " + decipher, font=("Arial", 19))
        my_lab00.pack()


def morseToEngSoundFunc():
    message = e2.get()
    if message != "":
        message += ''
        decipher = ''
        citext = ''
        k = MORSE_CODE_DICT.keys()
        v = MORSE_CODE_DICT.values()
        for letter in message:
            if (letter != ' '):
                i = 0
                citext += letter

            else:
                i += 1
                if i == 2:
                    decipher += ' '
                else:
                    decipher += list(k)[list(v).index(citext)]
                    citext = ''
    engine = pyttsx.init()
    engine.say(decipher)
    engine.runAndWait()
    my_lable = Label(rt, text="Morse->Eng(sound): " +
                     decipher, font=("Arial", 19))
    my_lable.pack()


def englishToMorseSound():
    message = e3.get()
    cipher = ''
    if message != " ":
        for letter in message:
            if letter != ' ':
                cipher = cipher + MORSE_CODE_DICT[letter]+' '
            else:
                cipher += ' '
    dot = 'dit.mp3'
    dash = 'dah.mp3'
    for m in cipher:
        if m == '.':
            playsound(dot)
        elif m == '-':
            playsound(dash)
        else:
            time.sleep(0.4)
    my_lab10 = Label(
        rt, text="Eng->Morse(sound): " + cipher, font=("Arial", 19))
    my_lab10.pack()


def clearAll():

    e0.delete(0, END)
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)


# Box Specs
rt.configure(background='light blue')
rt.title('MORSELATOR')
rt.geometry("1250x850")

# features
# entry fields
e0 = Entry(rt, width=50, borderwidth=7, fg="black", font=("Arial", 14))
e1 = Entry(rt, width=50, borderwidth=7, fg="black", font=("Arial", 14))
e2 = Entry(rt, width=50, borderwidth=7, fg="black", font=("Arial", 14))
e3 = Entry(rt, width=50, borderwidth=7, fg="black", font=("Arial", 14))
# heading
headTitle = Label(rt, text="Morse Code Translator", bg="light blue",
                  font=("Times New Roman", 35), fg="red")

# content list
my_lab0 = Label(rt, bg="light green",
                text="Morse Code to English", font=("Times New Roman", 22))
my_lab1 = Label(rt, bg="light green",
                text="English to Morse Code", font=("Times New Roman", 22))
my_lab2 = Label(rt, bg="light green", text="Morse Code to English in Sound",
                font=("Times New Roman", 22))
my_lab3 = Label(rt, text="English to Morse Code in Sound",
                bg="light green", font=("Times New Roman", 22))

# button list
b0 = Button(rt, text="Submit", bg="cyan", borderwidth=5,
            width=10, command=morseToEngFunc)
b1 = Button(rt, text="Submit", bg="cyan", borderwidth=5,
            width=10, command=engToMorseFunc)
b2 = Button(rt, text="Submit", bg="cyan", borderwidth=5,
            width=10, command=morseToEngSoundFunc)
b3 = Button(rt, text="Submit", bg="cyan", borderwidth=5,
            width=10, command=englishToMorseSound)
# packing
headTitle.pack()

my_lab1.pack()
e1.pack()
b1.pack()

my_lab0.pack()
e0.pack()
b0.pack()

my_lab2.pack()
e2.pack()
b2.pack()

my_lab3.pack()
e3.pack()
b3.pack()

button_clear = Button(rt, text="Clear", borderwidth=10,
                      width=8, bg="white", fg="black", command=clearAll)
button_quit = Button(rt, text="Exit !", borderwidth=10,
                     width=12, bg="red", command=rt.quit)
button_clear.pack()

button_quit.pack()

rt.mainloop()
