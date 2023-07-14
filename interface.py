#Release  2.0
from tkinter import *
from data import *
from functions import *
from time import sleep
from threading import Thread
import urllib.request
import os


class App:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("359x265")
        self.window.title("Woontt-")
        self.window.config(bg='#202020')
        self.window.resizable(width=False, height=False)

        self.search_assistant = ''
        self.champ = 'Aatrox'
        self.index = ''
        self.champ_image = None
        self.pick_status = BooleanVar()
        self.acc_status = BooleanVar()

        self.autopick_button = Checkbutton(self.window, width=9, height=1, text="Autopick", bg='#C33128', fg='black', indicatoron=0, activebackground='#C33128', activeforeground='black', font=('Imperial 12 bold'), command=self.autopick_, variable=self.pick_status, onvalue=True, offvalue=False)
        self.autopick_button.place(x=219, y=75)

        self.autoacc_button = Checkbutton(self.window, width=9, height=1, text="Autoacc", bg='#C33128', fg='black', indicatoron=0, activebackground='#C33128', activeforeground='black', font=('Imperial 12 bold'), command=self.autoacc_, variable=self.acc_status, onvalue=True, offvalue=False)
        self.autoacc_button.place(x=219, y=132)

        self.champImage = Label(self.window)
        self.champImage.place(x=42,y=51)

        self.champList = Listbox(self.window, width=12, height=1, bg='#C33128', fg="black", font=("Imperial 12 bold"),)
        self.champList.place(x=45, y=180)

        #insert all champions name
        champs, version = get_champs()
        del(version)
        for n, champ in enumerate(champs):
            self.champList.insert(n, champ)

        self.champList.bind('<KeyRelease>', self.on_keyrelease)

        confirm = Button(self.window,  width=10, height=1, font=("Imperial 12 bold"), text="Confirm", command=self.confirm__)
        confirm.place(x=138, y=220)

        self.show_image()

        # Download image
    
    def show_image(self):
        try:
            self.index = self.champList.curselection()[0]
        except IndexError:
            self.index = 0
        path = f'champs'
        files = os.listdir(path)

        if not f'{self.champList.get(self.index)}.png' in files:
            url = get_image()[self.index]
            filename = rf'{path}\{self.champ}.png'
            urllib.request.urlretrieve(url, filename)

        self.champ_image = PhotoImage(file=rf'{path}\{self.champ}.png')
        self.champImage['image'] = self.champ_image
    
    def on_keyrelease(self, event):
        letter = event.char
        letter = letter.lower()
        key = event.keysym
        if letter:
            self.search_assistant += letter
            self.search_assistant = self.search_assistant.capitalize()
        elif key == 'BackSpace':
            self.search_assistant = ''
            self.search_assistant = self.search_assistant.capitalize()

        list, v = get_champs()
        del(v)
        for self.champ in list:
            if self.search_assistant in self.champ:
                i = list.index(self.champ)
                j = self.champList.get(0, END).index(self.champ)
                self.champList.select_clear(0, END)
                self.champList.selection_set(j)
                self.champList.activate(j)
                self.champList.see(j)
                self.champ = list[j]
                break

    def autopick_(self):
        if self.pick_status.get():
            Start.onoff_threads(Start, 'pick__on', self.champ)

        else:
            Start.onoff_threads(Start, 'pick__off')
            cdThread = Thread(target=self.cd, args=(self.autopick_button, 12, 'Autopick', self.autopick_))
            cdThread.start()

    def autoacc_(self):
        if self.acc_status.get():
            Start.onoff_threads(Start, 'acc__on')
        else:
            Start.onoff_threads(Start, 'acc__off')
            cdThread = Thread(target=self.cd, args=(self.autoacc_button, 12, 'Autoacc', self.autoacc_))
            cdThread.start()
  
    def confirm__(self):
        Start.onoff_threads(Start, None, self.champ)
        self.show_image()
        self.search_assistant = ''

    def cd(self, button, time, default_message, default_command):
        for c in range(time, 0, -1):
            button['text'] = f'in {c} sec'
            button['command'] = ''
            sleep(1)
        button['text'] = default_message
        button['command'] = default_command

 
app = App()
app.window.mainloop()
Start.onoff_threads(Start, 'pick__off')
Start.onoff_threads(Start, 'acc__off')