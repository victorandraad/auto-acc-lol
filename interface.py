from tkinter import *
from data import *
from functions import *
from time import sleep
import urllib.request
import os

window = Tk()
window.geometry("359x265")
window.title("Woontt-")
window.config(bg='#202020')
window.resizable(width=False, height=False)

search_assistant = ''
champs = ''
index = ''
champ_image = None
pick_status = BooleanVar()

# Download image
def show_image():
    global champ_image
    global champs
    global index
    try:
        index = champList.curselection()[0]
    except IndexError:
        index = 0
    path = f'champs'
    files = os.listdir(path)
    champs = get_champs()[0]

    if not f'{champList.get(index)}.png' in files:
        url = get_image()[index]
        filename = rf'{path}\{champs[index]}.png'
        urllib.request.urlretrieve(url, filename)

    champ_image = PhotoImage(file=rf'{path}\{champs[index]}.png')
    champImage['image'] = champ_image


def on_keyrelease(event):
    global search_assistant
    global champ
    letter = event.char
    letter = letter.lower()
    key = event.keysym
    if letter:
        search_assistant += letter
        search_assistant = search_assistant.capitalize()
    elif key == 'BackSpace':
        search_assistant = ''
        search_assistant = search_assistant.capitalize()

    list, v = get_champs()
    del(v)
    for champ in list:
        if search_assistant in champ:
            sleep(0.05)
            i = list.index(champ)
            j = champList.get(0, END).index(champ)
            champList.select_clear(0, END)
            champList.selection_set(j)
            champList.activate(j)
            champList.see(j)
            break

def get_champ():
    if pick_status.get():
        print("a")
    else:
        print('b')
    show_image()
    # functions.autopick(champs[index])

autopick_button = Checkbutton(window, width=9, height=1, text="Autopick", bg='#C33128', fg='black', indicatoron=0, activebackground='#C33128', activeforeground='black', font=('Imperial 12 bold'), command=get_champ, variable=pick_status, onvalue=True, offvalue=False)
autopick_button.place(x=219, y=75)

autoacc_button = Checkbutton(window, width=9, height=1, text="Autoacc", bg='#C33128', fg='black', indicatoron=0, activebackground='#C33128', activeforeground='black', font=('Imperial 12 bold'), command=Start.autoacc)
autoacc_button.place(x=219, y=132)

champImage = Label(window)
champImage.place(x=42,y=51)

champList = Listbox(window, width=12, height=1, bg='#C33128', fg="black", font=("Imperial 12 bold"),)
champList.place(x=45, y=180)

#insert all champions name
champs, version = get_champs()
del(version)
for n, champ in enumerate(champs):
    champList.insert(n, champ)

champList.bind('<KeyRelease>', on_keyrelease)

confirm = Button(window,  width=10, height=1, font=("Imperial 12 bold"), text="Confirm", command=get_champ)
confirm.place(x=138, y=220)

show_image()
window.mainloop()