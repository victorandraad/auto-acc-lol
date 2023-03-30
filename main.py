import pygetwindow, pyautogui
import pytesseract
from time import sleep

class Start(): 
    def verify(self):
        while True:
            listWindow = pygetwindow.getAllTitles()  #lista nome de todos os apps ativos no windows
            #procura League of Legendds em listWindow
            if 'League of Legends' in listWindow:
                print(f'League of Legends encontrado.')
                break

        print("Digite o número que corresponde ao seu desejo: ")
        print("[1] APENAS AUTO ACCEPT")
        print("[2] APENAS AUTO PICK")
        print("[3] AUTO PICK E AUTO ACCEPT (Ainda não disponível) \n \n") 
        print("OBS: Caso esteja usando mais de um monitor, por favor, deixe o Client no monitor principal para que o bot possa funcionar corretamente...")
        
        while True:
            try:
                escolha = int(input())
                break
            except ValueError:
                print("[ERRO] Escolha um número inteiro, caso queira encerrar o app, escolha um número não mencionado!")

        if escolha == 1:
            self.autoaccept()
        
        if escolha == 2:
            champ_select = str(input("Digite o nome do campeão a ser escolhido: "))
            # champ_ban = str(input('Digite o nome do campeão a ser banido: '))
            self.autopick(pick=champ_select)

    def get_elements(self, l, t, w, h, value):
        listWindow = pygetwindow.getAllTitles()  #lista nome de todos os apps ativos no windows

        if 'League of Legends (TM) Client' in listWindow:
            sleep(60)
            return
        
        else:
            try:
                hwnd_lol = pygetwindow.getWindowsWithTitle('League of Legends')[0] # pega o codigo da janela do lol
                self.left, self.top, self.width, self.height = hwnd_lol.left, hwnd_lol.top, hwnd_lol.width, hwnd_lol.height

                x1, y1, x2, y2 = (l / 1024) * self.width, (t / 576) * self.height, (w / 1024) * self.width, (h / 576) * self.height
                self.region = (self.left + x1, self.top +y1, x2 - x1, y2 - y1)

                screenshot = pyautogui.screenshot(region=(self.region))
                pytesseract.pytesseract.tesseract_cmd = r'Tesseract-OCR\tesseract.exe'
            except IndexError:
                input("[ERRO] Erro ao encontrar o League of Legends, por favor, esteja segura de que ele está aberto!")

            texto = pytesseract.image_to_string(screenshot)
            if value in texto:
                return True
            sleep(4)

    def autoaccept(self):
        while True:
            if self.get_elements(475, 436, 551, 453, 'ACEITAR'):
                pyautogui.moveTo(self.region)
                pyautogui.click(self.region)
                sleep(12)


    def autopick(self, pick):
        while True:
            if self.get_elements(344, 11, 478, 37, 'SELECIONE'):
                pyautogui.click(self.left + (631 / 1024) * self.width, self.top + (84 / 576) * self.height)
                pyautogui.write(pick)
                sleep(1)

                pyautogui.click(self.left + (309 / 1024) * self.width, self.top + (128 / 576) * self.height)
                sleep(1)

                pyautogui.click(self.left  + (506 / 1024) * self.width, self.top + (488 / 576) * self.height)
                sleep(100)
            if self.get_elements(385, 12, 464, 36, 'BANA'):
                pass
                                
    
Start().verify()