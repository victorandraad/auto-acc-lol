from threading import Thread
from pytesseract import pytesseract, image_to_string
from pyautogui import FAILSAFE, PAUSE, screenshot, position, click, moveTo, write
from pygetwindow import getAllTitles, getWindowsWithTitle
from time import sleep
from tkinter import *

class Start():      
    def get_text(self, value, search=(int, int, int, int)):
        listWindow = getAllTitles()  #lista nome de todos os apps ativos no windows
        if 'League of Legends (TM) Client' in listWindow:
            sleep(60)
            return
        
        else:
            try:
                hwnd_lol = getWindowsWithTitle('League of Legends')[0] # pega o codigo da janela do lol
                self.left, self.top, self.width, self.height = hwnd_lol.left, hwnd_lol.top, hwnd_lol.width, hwnd_lol.height

                x1, y1, x2, y2 = (search[0] / 1024) * self.width, (search[1] / 576) * self.height, (search[2] / 1024) * self.width, (search[3] / 576) * self.height
                self.region = (self.left + x1, self.top +y1, x2 - x1, y2 - y1)

                appscreenshot = screenshot(region=(self.region))
                pytesseract.tesseract_cmd = r'Tesseract-OCR\tesseract.exe'
            except IndexError:
                input(f"[ERRO] Erro ao encontrar o League of Legends, por favor, esteja segura de que ele está aberto!")
            try:
                texto = image_to_string(appscreenshot)
                if value in texto:
                    return True
                sleep(4)
            except (AttributeError, SystemError):
                pass

    def click_point(self, region=(int, int), rverify=(int, int, int, int)):
        rx, ry = position()
        s1 = screenshot(region=(rverify[0], rverify[1], rverify[2], rverify[3]))
        sleep(PAUSE)
        click(self.left + (region[0] / 1024) * self.width, self.top + (region[1] / 576) * self.height, duration=0)
        moveTo(rx, ry, duration=0)

        if s1 == screenshot(region=(rverify[0], rverify[1], rverify[2], rverify[3])):
            return False

    def autoaccept(self):
        while True:
            if self.get_text(search=(475, 436, 551, 453), value='ACEITAR'):
                if self.click_point(region=(475, 436), rverify=(475, 436, 551, 453)) == False:
                    pass
                else:
                    sleep(12)

    def autopick(self, pick):
        while True:
            if self.get_text(search=(475, 478, 551, 493), value='CONFIRMAR'):
                self.click_point(region=(631, 84), rverify=(588, 73, 615, 92)) #clicar no buscar
                write(pick)

                self.click_point(region=(309, 128), rverify=(283, 106, 335, 158)) #clicar no champ

                self.click_point(region=(506, 488), rverify=(465, 369, 569, 410)) #clicar em confirmar

                sleep(100)

class Interface():
    def __init__(self):
        Thread(target=self.gui).start()

    def gui(self):
        window = Tk()
        window.title("QueueLol")
        window.geometry("350x300")
        window.iconphoto(False, PhotoImage(file='logo.png'))
        self.acc = IntVar()
        self.pick = IntVar()  

        top_label = Label(window, width=400, height=1, text=("==Qu=uu=e==e=lo==l=l==="), font=("Arial 15 bold"), fg="white", bg="#429ef5")
        top_label.pack()

        autoacc_label = Label(window, width=8, height=2, text="Autoacc", font=("Arial 15"))
        autoacc_label.pack(side=LEFT, anchor=NW)

        autoacc_button = Checkbutton(window, height=3, variable=self.acc, command=self.manager_acc)
        autoacc_button.pack(side=LEFT, anchor=NW)

        self.autopick_label = Label(window, width=8, height=2, text="Autopick", font=("Arial 15"))
        self.autopick_label.pack(side=LEFT, anchor=NW)

        autopick_button = Checkbutton(window, height=3, variable=self.pick, command=self.manager_pick)
        autopick_button.pack(side=LEFT, anchor=NW)

        window.mainloop()

    def manager_acc(self):
        if self.acc.get():
            print("iniciado")
            sacc = Thread(target=Start().autoaccept)
            sacc.start()
    
    def manager_pick(self):
        self.autopick_label['text'] = 'Insp.'
            
Interface()