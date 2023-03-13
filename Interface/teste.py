from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QFrame, QWidget, QVBoxLayout, QScrollArea
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon
import sys
import os

class Change(QWidget):
    def __init__(self):
        super().__init__()
        # Define propriedades do app como título, estilo, tamanho, etc
        self.setWindowTitle('p e p p a . j p e g')
        self.setGeometry(20, 100, 360, 350)
        self.setObjectName('body')
        self.setFixedSize(350, 350)

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
                    button.setGeometry(c*70, contador2*70, image.width(), image.height())
                    contador +=1
                    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Change()
    window.show()
    sys.exit(app.exec_())