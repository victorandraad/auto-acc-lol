from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QFrame, QWidget, QVBoxLayout, QScrollArea
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
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
        self.autoaccept.setGeometry(40, 20, 120, 40) # Geometry define as dimensões do botão
        self.autoaccept.clicked.connect(self.autoaccept_action) # Adiciona ação ao evento clicar no botão

        self.autopick = QPushButton('auto-pick', self)
        self.autopick.setObjectName('auto')
        self.autopick.setGeometry(185, 20, 120, 40)
        self.autopick.clicked.connect(self.autopick_action) 

        # Image container
        self.image_container = QFrame(self)
        self.image_container.setGeometry(65, 100, 200, 130)
        self.image_container.setObjectName('image_container')

        self.image = QLabel(self.image_container)
        self.champ_image = QPixmap('Interface\settings\champs\Kayn.png')
        self.image.setPixmap(self.champ_image)
        self.image.setObjectName('champ_image')
        self.image.setGeometry(65, 0, 100, 110)

        # Change
        self.change_button = QPushButton('change', self)
        self.change_button.setGeometry(130, 215, 100, 40)
        self.change_button.clicked.connect(self.change_champ)
        self.change_button.setObjectName('change_button')

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
    
    # Função chamada ao clicar em change
    def change_champ(self):

        self.change_page = Change()
        self.change_page.show()
        
    
    def config_button_action(self):
        print('clicou1')

class Change(QWidget):
    def __init__(self):
        super().__init__()
        # Define propriedades do app como título, estilo, tamanho, etc
        self.setWindowTitle('p e p p a . j p e g')
        self.setGeometry(20, 100, 360, 350)
        self.setObjectName('body')

        with open('Interface/style.css', 'r') as f:
            css = f.read()     
        app.setStyleSheet(css)

        # Botões imagem
        self.image_dir = 'Interface\settings\champs'
        self.images_files = [f for f in os.listdir(self.image_dir) if os.path.isfile(os.path.join(self.image_dir,  f)) and f.endswith('.png')]
        

        # Lista todos os campeões
        contador = -5
        contador2 = 0
        atingir = len(self.images_files)
        for c in range(0, atingir, 5):
            for c in range(0, 5):
                if contador < 0:
                    button = QPushButton(self)
                    layout = QVBoxLayout(button)
                    image = QPixmap(os.path.join(self.image_dir, self.images_files[c])).scaled(60, 60)
                    label = QLabel(self)
                    label.setPixmap(image)
                    layout.addWidget(label)
                    layout.setContentsMargins(10, 0, 0, 0)
                    button.setGeometry(c*70, 10, image.width(), image.height())
                    contador +=1
                elif contador >= atingir-5:
                    print('oi')
                elif contador >=0:
                    button = QPushButton(self)
                    layout = QVBoxLayout(button)
                    image = QPixmap(os.path.join(self.image_dir, self.images_files[contador+5])).scaled(60, 60)
                    label = QLabel(self)
                    label.setPixmap(image)
                    layout.addWidget(label)
                    layout.setContentsMargins(10, 0, 0, 0)
                    button.setGeometry(c*70, contador2*75, image.width(), image.height())
                    contador +=1
            contador2+=1 

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Change()
    window.show()
    sys.exit(app.exec_())