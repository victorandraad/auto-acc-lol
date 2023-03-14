import pygetwindow
from time import sleep

class autoaccept():
    def __init__(self):
        super().__init__()
        sleep(2)
        
        list = pygetwindow.getAllTitles()
        for nome in list:
            nome = nome.upper()
            if 'LEAGUE OF LEGENDS' in nome:
                print(f'League of Legends encontrado nome completo da janela: {nome}')
                break
        window = pygetwindow.getActiveWindowTitle().upper()
        
        if window == nome:
            print('teste')

autoaccept()
efgh