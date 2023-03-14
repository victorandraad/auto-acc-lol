from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QFrame, QToolButton, QMenu, QScrollArea, QVBoxLayout
from PyQt5.QtGui import QPixmap, QIcon
import sys
import os

class Main(QMainWindow):
    def __init__(self):
        super().__init__()

        # Define o container do header, é importante "fixar" o uso do self para que seja acessível em todo o código,
        # cada variável criada com self é adicionada à lista de variáveis dentro de self(objeto)
        self.header_container = QFrame(self) 
        self.header_container.setObjectName('header_container')
        self.header_container.setGeometry(0, -7, self.width(), 40) 

        # Define a label e a label é atribuída ao header container:
        self.header = QLabel('p e p p a p e p p a p e p p a p e p p a', self.header_container)
        self.header.setObjectName('header')

        # Seta duas variáveis booleanas como False para que possam ser alteradas e identificadas em uma
        # função dinâmica, que pega esse valor como propriedade para realizar ações
        self.style_autoaccept = False
        self.style_autopick = False

        # Define autoaccept como botão atribuída a self (corpo do app), é legal informar que aqui eu seto "auto" como objectname para poder
        # usá-lo em um arquivo css
        self.autoaccept = QPushButton('auto-accept', self)
        self.autoaccept.setObjectName('auto')
        self.autoaccept.setGeometry(40, 40, 120, 40) # Geometry define as dimensões do botão
        self.autoaccept.clicked.connect(self.autoaccept_action) # Adiciona ação ao evento clicar no botão

        self.autopick = QPushButton('auto-pick', self)
        self.autopick.setObjectName('auto')
        self.autopick.setGeometry(185, 40, 120, 40)
        self.autopick.clicked.connect(self.autopick_action) 

        # Image container
        self.image_container = QFrame(self)
        self.image_container.setGeometry(65, 100, 200, 130)
        self.image_container.setObjectName('image_container')

        self.image = QLabel(self.image_container)
        self.champ_image = QPixmap('Interface\settings\champs\Aatrox.png')
        self.image.setPixmap(self.champ_image)
        self.image.setObjectName('champ_image')
        self.image.setGeometry(65, 0, 100, 110)

        # Change
        self.change_button = QToolButton(self)
        self.change_button.setText('Aatrox')
        self.change_button.setGeometry(130, 215, 100, 40)
        self.change_button.setPopupMode(QToolButton.InstantPopup)
        self.change_button.setObjectName('change_button')

        self.menu = QMenu(self)
        champs_dir = 'Interface\settings\champs'
        arquivos = [f for f in os.listdir(champs_dir) if os.path.isfile(os.path.join(champs_dir, f)) and f.endswith('.png')]
        arquivos = [os.path.splitext(f)[0] for f in arquivos]
        for arquivo in arquivos:
            arquivo = arquivo
            item = self.menu.addAction(arquivo)
            item.triggered.connect(lambda checked, arquivo=arquivo: self.champ_seleccionado(arquivo))

        self.menu.setObjectName('menu')
        self.change_button.setMenu(self.menu)

        # config
        self.config_button = QPushButton(self)
        self.config_image = QPixmap('Interface\settings\icon.png')
        self.config_button.setIcon(QIcon(self.config_image))
        self.config_button.setGeometry(310, 310, 30, 30)
        self.config_button.setObjectName('config_button')
        self.config_button.clicked.connect(self.config_button_action)


        # Define propriedades do app como título, estilo, tamanho, etc
        self.setWindowTitle('p e p p a . j p e g')
        self.setGeometry(20, 100, 350, 350)
        self.setObjectName('body')
        self.setMinimumSize(350, 350)
        self.setMaximumSize(350, 350)
        with open('Interface/style.css', 'r') as f:
            css = f.read()     
        app.setStyleSheet(css)

    def champ_seleccionado(self, x):
        self.champ_image = QPixmap(f'Interface\settings\champs\{x}.png')
        self.image.setPixmap(self.champ_image)
        self.image.setObjectName('champ_image')
        self.image.setGeometry(65, 0, 100, 110)
        self.change_button.setText(f'{x}')


    # Função chamada ao clicar no botão de autoaccept
    def autoaccept_action(self):
        self.style_autoaccept = not self.style_autoaccept

        if self.style_autoaccept:
            self.autoaccept.setStyleSheet('background-color: #537FE7;')
            
        else:
            self.autoaccept.setStyleSheet('background-color: black;')

    # Função chamada ao clicar no botão autopick
    def autopick_action(self):
        self.style_autopick = not self.style_autopick

        if self.style_autopick:
            self.autopick.setStyleSheet('background-color: #537FE7;')
        else:
            self.autopick.setStyleSheet('background-color: black;')
    
    def config_button_action(self):
        print('clicou1')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())