import pygetwindow, pyautogui
from time import sleep

class function():
    def verify(self):
        cont = 0
        while cont == 0:
            listWindow = pygetwindow.getAllTitles()
        
            if 'League of Legends' in listWindow:
                print(f'League of Legends encontrado.')
                cont = 1

        while cont == 1:
            self.active = pygetwindow.getActiveWindow()
            self.hwnd_lol = pygetwindow.getWindowsWithTitle('League of Legends')[0]
            if self.active._hWnd == self.hwnd_lol._hWnd:
                break
    

    def stop(self):
        pass