#Release  2.0
from tkinter import *
from data import *
from functions import *
from time import sleep
from threading import Thread
import urllib.request
import os
import yaml
import locale

with open('config.yaml') as f:
    config = yaml.safe_load(f)

if config['language'] == '':
    win_language = locale.getdefaultlocale()
    config['language'] = win_language[0] + win_language
        
with open('config.yaml', 'w') as f:
    yaml.dump(config, f)

language_Inicials = config['language'][0], config['language'][1]

with open(f'languages\{language_Inicials[0]}{language_Inicials[1]}.yaml', 'r') as l:
    language = yaml.safe_load(l)

class App:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("359x265")
        self.window.title("Woontt-")
        self.window.config(bg='#202020')
        self.window.resizable(width=False, height=False)

        self.search_assistant = ''
        self.champ = config['last_champion']
        self.index = config['index_champion']
        self.pick_status = BooleanVar()
        self.acc_status = BooleanVar()

        self.autopick_button = Checkbutton(self.window, width=9, height=1, text="Autopick", bg='#C33128', fg='black', indicatoron=0, activebackground='#C33128', activeforeground='black', font=('Imperial 12 bold'), command=self.autopick_, variable=self.pick_status, onvalue=True, offvalue=False)
        self.autopick_button.place(x=219, y=50)

        self.autoacc_button = Checkbutton(self.window, width=9, height=1, text="Autoacc", bg='#C33128', fg='black', indicatoron=0, activebackground='#C33128', activeforeground='black', font=('Imperial 12 bold'), command=self.autoacc_, variable=self.acc_status, onvalue=True, offvalue=False)
        self.autoacc_button.place(x=219, y=100)

        # self.language_list = Listbox(self.window, width=10, height=1, bg='#202020', fg="white", font=("Imperial 12 bold"),)
        # self.language_list.place(x=221, y=130)

        self.champImage = Label(self.window)
        self.champImage.place(x=35,y=40)

        #put last champ image
        self.champ_image = PhotoImage(file=rf'champs\{self.champ}.png')
        self.champImage['image'] = self.champ_image

        self.champList = Listbox(self.window, width=12, height=1, bg='#C33128', fg="black", font=("Imperial 12 bold"),)
        self.champList.place(x=41, y=168)

        #insert all champions name
        champs, version = get_champs()
        del(version)
        for n, champ in enumerate(champs):
            self.champList.insert(n, champ)

        #insert all default languages
        # langs = os.listdir('languages')
        # for n, lang in enumerate(langs):
        #     if lang == 'en.yaml':
        #          lang = 'English'

        #     if lang == 'es.yaml':
        #          lang = 'Español'

        #     if lang == 'pt.yaml':
        #          lang = 'Português'
        #     self.language_list.insert(n, lang)
        
        self.champList.see(config['index_champion']) # See last champ name
        self.champList.bind('<KeyRelease>', self.on_keyrelease)

        confirm = Button(self.window,  width=10, height=1, font=("Imperial 12 bold"), text=language['confirmbutton_text'], command=self.confirm__)
        confirm.place(x=138, y=220)
    
    def show_image(self):
        try:
            self.index = self.champList.curselection()[0]
        except IndexError:
            self.index = 0

        self.champ = self.champList.get(self.index)
        files = os.listdir('champs')
        
        # print(self.champList.get(self.index)) Nome do campeão selecionado
        if not f'{self.champ}.png' in files:
            url = get_image()[self.index]
            filename = rf'champs\{self.champ}.png'
            urllib.request.urlretrieve(url, filename)

        self.champ_image = PhotoImage(file=rf'champs\{self.champ}.png')
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
                j = self.champList.get(0, END).index(self.champ)
                print(j)
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

        config['last_champion'] = self.champ
        config['index_champion'] = self.index
        with open('config.yaml', 'w') as f:
            yaml.dump(config, f)

    def cd(self, button, time, default_message, default_command):
        for c in range(time, 0, -1):
            button['text'] = f'in {c} sec'
            button['command'] = ''
            sleep(1)
        button['text'] = default_message
        button['command'] = default_command

if __name__ == '__main__':
    app = App()
    app.window.mainloop()
    Start.onoff_threads(Start, 'pick__off')
    Start.onoff_threads(Start, 'acc__off')