import pygetwindow, pyautogui
import pytesseract
import threading
from time import sleep

class Start():
    pyautogui.FAILSAFE = False
    pyautogui.PAUSE = 0.2
    def verify(self):
        while True:
            listWindow = pygetwindow.getAllTitles()  #lista nome de todos os apps ativos no windows
            #procura League of Legendds em listWindow
            if 'League of Legends' in listWindow:
                print(f'League of Legends encontrado.')
                break
            else:
                input('O League of Legends precisa estar aberto para que o programa funcione \n \nPressione ENTER para continuar...')

        print("Digite o número que corresponde ao seu desejo: ")
        print("[1] APENAS AUTO ACCEPT")
        print("[2] APENAS AUTO PICK")
        print("[3] AUTO PICK E AUTO ACCEPT \n \n") 
        print("OBS: Caso esteja usando mais de um monitor, por favor, deixe o Client no monitor principal para que o bot possa funcionar corretamente...")
        
        while True:
            try:
                escolha = int(input())
                break
            except ValueError:
                print("[ERRO] Escolha um número inteiro, caso queira encerrar o app, escolha um número não mencionado!")

        if escolha == 1:
            self.autoaccept()
        
        else:
            champ_select = str(input("Digite o nome do campeão a ser escolhido: "))
            # champ_ban = str(input('Digite o nome do campeão a ser banido: '))
            if escolha == 3:
                autoacc = threading.Thread(target=self.autoaccept)
                autoacc.start()
            self.autopick(pick=champ_select)
        
    def get_text(self, value, search=(int, int, int, int)):
        listWindow = pygetwindow.getAllTitles()  #lista nome de todos os apps ativos no windows

        if 'League of Legends (TM) Client' in listWindow:
            sleep(60)
            return
        
        else:
            try:
                hwnd_lol = pygetwindow.getWindowsWithTitle('League of Legends')[0] # pega o codigo da janela do lol
                self.left, self.top, self.width, self.height = hwnd_lol.left, hwnd_lol.top, hwnd_lol.width, hwnd_lol.height

                x1, y1, x2, y2 = (search[0] / 1024) * self.width, (search[1] / 576) * self.height, (search[2] / 1024) * self.width, (search[3] / 576) * self.height
                self.region = (self.left + x1, self.top +y1, x2 - x1, y2 - y1)

                screenshot = pyautogui.screenshot(region=(self.region))
                pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
            except IndexError:
                input("[ERRO] Erro ao encontrar o League of Legends, por favor, esteja segura de que ele está aberto!")
            try:
                texto = pytesseract.image_to_string(screenshot)
                if value in texto:
                    return True
                sleep(4)
            except:
                pass

    def click_point(self, region=(int, int), rverify=(int, int, int, int)):
        rx, ry = pyautogui.position()
        s1 = pyautogui.screenshot(region=(rverify[0], rverify[1], rverify[2], rverify[3]))
        pyautogui.click(self.left + (region[0] / 1024) * self.width, self.top + (region[1] / 576) * self.height, duration=0)
        pyautogui.moveTo(rx, ry, duration=0)
        if s1 == pyautogui.screenshot(region=(rverify[0], rverify[1], rverify[2], rverify[3])):
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
                pyautogui.write(pick)

                self.click_point(region=(309, 128), rverify=(283, 106, 335, 158)) #clicar no champ

                self.click_point(region=(506, 488), rverify=(465, 369, 569, 410)) #clicar em confirmar

                sleep(100)

            if self.get_text(search=(385, 12, 464, 36), value='BANA'):
                pass
                                
    
Start().verify()