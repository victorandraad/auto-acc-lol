#Release 2.0
from configparser import ConfigParser
from pytesseract import pytesseract, image_to_string
from pyautogui import FAILSAFE, PAUSE, screenshot, position, click, moveTo, write
from pygetwindow import getAllTitles, getWindowsWithTitle
from time import sleep
from threading import Thread
from tkinter import *

config = ConfigParser()
config.read('settings.ini')
PAUSE = config.get('config', 'delay')
PAUSE = float(PAUSE)
FAILSAFE = False

class Start:
  
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
                pass

            try:
                texto = image_to_string(appscreenshot)
                if value in texto:
                    return True
                sleep(4)
            except (AttributeError, SystemError, UnboundLocalError):
                pass

    def click_point(self, region=(int, int), rverify=(int, int, int, int)):
        rx, ry = position()
        s1 = screenshot(region=(rverify[0], rverify[1], rverify[2], rverify[3]))
        sleep(PAUSE)
        click(self.left + (region[0] / 1024) * self.width, self.top + (region[1] / 576) * self.height, duration=0)
        moveTo(rx, ry, duration=0)

        if s1 == screenshot(region=(rverify[0], rverify[1], rverify[2], rverify[3])):
            return False

    def autoacc(self, Nada=None):
        while self.acc_on:
            if self.get_text(self=Start, search=(475, 436, 551, 453), value=config.get('language', 'accepttext')):
                if self.click_point(self=Start, region=(475, 436), rverify=(475, 436, 551, 453)) == False:
                    pass
                else:
                    self.sleepAcc = sleep(12)

    def autopick(self, Nada=None):
        while self.autopick_on:
            if self.get_text(self=Start, search=(475, 478, 551, 493), value=config.get('language', 'confirmbutton_text')):
                self.click_point(self=Start, region=(631, 84), rverify=(588, 73, 615, 92)) #clicar no buscar
                write(self.pick)

                self.click_point(self=Start, region=(309, 128), rverify=(283, 106, 335, 158)) #clicar no champ

                self.click_point(self=Start, region=(506, 488), rverify=(465, 369, 569, 410)) #clicar em confirmar

                self.sleepPick = sleep(12)

    def onoff_threads(self, method=None, champ=None):
        self.pickThread = Thread(target=self.autopick, args=(Start, None))
        self.accThread = Thread(target=self.autoacc, args=(Start, None))
        self.pick = champ

        if method == 'pick__off':
            self.autopick_on = False

        elif method == 'pick__on':
            self.autopick_on = True
            self.pickThread.start()

        if method == 'acc__off':
            self.acc_on = False

        elif method == 'acc__on':
            self.acc_on = True
            self.accThread.start()