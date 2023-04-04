from configparser import ConfigParser
from threading import Thread
from pytesseract import pytesseract, image_to_string
from pyautogui import FAILSAFE, PAUSE, screenshot, position, click, moveTo, write
from pygetwindow import getAllTitles, getWindowsWithTitle
from time import sleep

settings = ConfigParser()
settings.read('settings.ini')

FAILSAFE = False
PAUSE = float(settings.get('config', 'delay'))

#CORES
reset_color, bold, red, green, yellow = '\33[m', '\33[1m', '\33[1;31m', '\33[1;32m', '\33[1;33m'
blue, magenta, cyan, white = '\33[1;34m', '\33[1;35m', '\33[1;36m', '\33[1;37m'

class Start():

    def verify(self):
        while True:
            listWindow = getAllTitles()  #lista nome de todos os apps ativos no windows
            #procura League of Legendds em listWindow
            if 'League of Legends' in listWindow:
                print(f'{white}League of Legends {green}encontrado.{reset_color}')
                break
            else:
                input(f'{white}O League of Legends {red}precisa estar aberto {white}para que o programa funcione. \n \n{white}Pressione ENTER para continuar...{reset_color}')

        print(f"{white}Digite o número que corresponde ao seu desejo: ")
        print(f"{cyan}[1] {white}APENAS AUTO ACCEPT")
        print(f"{cyan}[2] {white}APENAS AUTO PICK")
        print(f"{magenta}[3] {white}AUTO PICK E AUTO ACCEPT \n \n") 
        print(f"{red}OBS: {white}Caso esteja usando mais de um monitor, por favor, deixe o Client no monitor principal para que o bot possa funcionar corretamente...")
        
        while True:
            try:
                escolha = int(input())
                break
            except ValueError:
                print(f"{red}[ERRO] {white}Escolha um número inteiro, caso queira encerrar o app, escolha um número não mencionado!")

        if escolha == 1:
            self.autoaccept()
        
        elif escolha == 2 or escolha == 3:
            champ_select = str(input("Digite o nome do campeão a ser escolhido: "))
            # champ_ban = str(input('Digite o nome do campeão a ser banido: '))
            if escolha == 3:
                autoacc = Thread(target=self.autoaccept)
                autoacc.start()
            self.autopick(pick=champ_select)
        
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
                input(f"{red}[ERRO] {white}Erro ao encontrar o League of Legends, por favor, esteja segura de que ele está aberto!")
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
            if self.get_text(search=(475, 436, 551, 453), value=settings.get('config', 'accepttext')):
                if self.click_point(region=(475, 436), rverify=(475, 436, 551, 453)) == False:
                    pass
                else:
                    sleep(12)

    def autopick(self, pick):
        while True:
            if self.get_text(search=(475, 478, 551, 493), value=settings.get('config', 'confirmbutton_text')):
                self.click_point(region=(631, 84), rverify=(588, 73, 615, 92)) #clicar no buscar
                write(pick)

                self.click_point(region=(309, 128), rverify=(283, 106, 335, 158)) #clicar no champ

                self.click_point(region=(506, 488), rverify=(465, 369, 569, 410)) #clicar em confirmar

                sleep(100)

Start().verify()