import pygetwindow, pyautogui
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

        while cont == 1:
            active = pygetwindow.getActiveWindow() #janela que está ativa, retorna
            hwnd_lol = pygetwindow.getWindowsWithTitle('League of Legends')[0] # pega o codigo da janela do lol
            try:
                if active._hWnd == hwnd_lol._hWnd:
                    cont = 2
            except AttributeError:
                input("[AVISO] Erro ao encontrar uma propriedade do League of Legends, por favor, tente abri-lo ou maximiza-lo novamente e pressione ENTER no app: ")
        print("Digite o número que corresponde ao seu desejo: ")
        print("[1] APENAS AUTO ACCEPT")
        print("[2] APENAS AUTO PICK")
        print("[3] AUTO PICK E AUTO ACCEPT")
        while True:
            try:
                self.escolha = int(input())
                break
            except ValueError:
                print("[ERRO] Escolha um número inteiro, caso queira encerrar o app, escolha um número não mencionado!")

        if self.escolha  == 1:
            Start().autoaccept()

    def autoaccept(self):
        sleep(2)
        hwnd_lol = pygetwindow.getWindowsWithTitle('League of Legends')[0] # pega o codigo da janela do lol
        while True:
            try:
                region = ( hwnd_lol.left, hwnd_lol.top, hwnd_lol.width, hwnd_lol.height)
                break
            except:
                input("[ERRO] Pressione enter e tente novamente!")
                sleep(1)
        screenshot = pyautogui.screenshot(region=(region))
        screenshot.save('image.png')
        print(screenshot)



Start().verify()