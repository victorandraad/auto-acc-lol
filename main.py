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
            Start().autoaccept()

    def autoaccept(self):
        while True:
            listWindow = pygetwindow.getAllTitles()  #lista nome de todos os apps ativos no windows
            if 'League of Legends (TM) Client' in listWindow:
                sleep(60)
            else:
                while True:
                    hwnd_lol = pygetwindow.getWindowsWithTitle('League of Legends')[0] # pega o codigo da janela do lol
                    left, top, width, height = hwnd_lol.left, hwnd_lol.top, hwnd_lol.width, hwnd_lol.height
                    x1, y1, x2, y2 = (475 / 1024) * width, (436 / 576) * height, (551 / 1024) * width, (453 / 576) * height
                    region = (left + x1, top +y1, x2 - x1, y2 - y1)
                    screenshot = pyautogui.screenshot(region=(region))
                    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
                    texto = pytesseract.image_to_string(screenshot)

                    sleep(5)
                    if 'ACEITAR' in texto:
                        pyautogui.moveTo(region)
                        # pyautogui.click()
                        break
                    
    
Start().verify()