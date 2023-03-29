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
        print("[3] AUTO PICK E AUTO ACCEPT\n \n")
        print("OBS: Caso esteja usando mais de um monitor, por favor, deixe o Client no monitor principal para que o bot possa funcionar corretamente...")
        
        while True:
            try:
                self.escolha = int(input())
                break
            except ValueError:
                print("[ERRO] Escolha um número inteiro, caso queira encerrar o app, escolha um número não mencionado!")

        if self.escolha == 1:
            self.autoaccept()
        
        if self.escolha == 2:
            self.autopick()

    def get_elements(self, l, t, w, h, value):
        listWindow = pygetwindow.getAllTitles()  #lista nome de todos os apps ativos no windows

        if 'League of Legends (TM) Client' in listWindow:
            sleep(60)
            return
        
        else:
            try:
                hwnd_lol = pygetwindow.getWindowsWithTitle('League of Legends')[0] # pega o codigo da janela do lol
                left, top, width, height = hwnd_lol.left, hwnd_lol.top, hwnd_lol.width, hwnd_lol.height

                x1, y1, x2, y2 = (l / 1024) * width, (t / 576) * height, (w / 1024) * width, (h / 576) * height
                self.region = (left + x1, top +y1, x2 - x1, y2 - y1)

                screenshot = pyautogui.screenshot(region=(self.region))
                pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
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

            


    def autopick(self):
        while True:
            if self.get_elements(344, 11, 478, 37, 'SELECIONE'):
                pass
            
            
                                
    
Start().verify()