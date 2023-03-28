import pygetwindow, pyautogui
import pytesseract
from time import sleep

class Start(): 
    def verify(self):
        cont = 0
        while cont == 0:
            listWindow = pygetwindow.getAllTitles()  #lista nome de todos os apps ativos no windows
            #procura League of Legendds em listWindow
            if 'League of Legends' in listWindow:
                print(f'League of Legends encontrado.')
                cont = 1


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

        if self.escolha  == 1:
            Start().autoaccept()

    def autoaccept(self):
        hwnd_lol = pygetwindow.getWindowsWithTitle('League of Legends')[0] # pega o codigo da janela do lol
        left, top, width, height = hwnd_lol.left, hwnd_lol.top, hwnd_lol.width, hwnd_lol.height
        x1, y1, x2, y2 = (475 / 1024) * width, (436 / 576) * height, (551 / 1024) * width, (453 / 576) * height
        while True:
            try:
                region = (left + x1, top +y1, x2 - x1, y2 - y1)
                break
            except:
                input("[ERRO] Pressione enter e tente novamente!")
                sleep(1)
        sleep(2)
        screenshot = pyautogui.screenshot(region=(region))
        screenshot.save("image.png")

Start().verify()