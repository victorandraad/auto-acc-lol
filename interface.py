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
        self.champs = ''
        self.champ = 'Aatrox'
        self.index = ''
        self.champ_image = None
        self.pick_status = BooleanVar()
        self.acc_status = BooleanVar()

        autopick_button = Checkbutton(self.window, width=9, height=1, text="Autopick", bg='#C33128', fg='black', indicatoron=0, activebackground='#C33128', activeforeground='black', font=('Imperial 12 bold'), command=self.get_champ, variable=self.pick_status, onvalue=True, offvalue=False)
        autopick_button.place(x=219, y=75)

        autoacc_button = Checkbutton(self.window, width=9, height=1, text="Autoacc", bg='#C33128', fg='black', indicatoron=0, activebackground='#C33128', activeforeground='black', font=('Imperial 12 bold'), command=self.autoacc_, variable=self.acc_status, onvalue=True, offvalue=False)
        autoacc_button.place(x=219, y=132)

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

        confirm = Button(self.window,  width=10, height=1, font=("Imperial 12 bold"), text="Confirm", command=self.get_champ)
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
        self.champs = get_champs()[0]

        if not f'{self.champList.get(self.index)}.png' in files:
            url = get_image()[self.index]
            filename = rf'{path}\{self.champs[self.index]}.png'
            urllib.request.urlretrieve(url, filename)

        self.champ_image = PhotoImage(file=rf'{path}\{self.champs[self.index]}.png')
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
                break

    def get_champ(self):
        self.show_image()
        if self.pick_status.get():
            pick_onoff = True
            Thread(target=Start.autopick, args=(Start, self.champ, pick_onoff)).start()
        else:
            Start.autopick.pick_onoff = False

    def autoacc_(self):
        if self.acc_status.get():
            print('a')
        else:
            print('b')

app = App()
app.window.mainloop()