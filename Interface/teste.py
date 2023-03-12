from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QFrame, QWidget, QVBoxLayout, QScrollArea
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import sys
import os

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

        #Creating a widget with all content
        self.widget = QWidget(self)
        self.scroll_Qvbox = QVBoxLayout(self.widget)

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
                    button = QPushButton(self.widget)
                    layout = QVBoxLayout(button)
                    image = QPixmap(os.path.join(self.image_dir, self.images_files[c])).scaled(60, 60)
                    label = QLabel(self.widget)
                    label.setPixmap(image)
                    self.scroll_Qvbox.addWidget(label)
                    self.scroll_Qvbox.setContentsMargins(10, 0, 0, 0)
                    button.setGeometry(c*70, 10, image.width(), image.height())
                    contador +=1
                elif contador >= atingir-5:
                    print('oi')
                elif contador >=0:
                    button = QPushButton(self.widget)
                    layout = QVBoxLayout(button)
                    image = QPixmap(os.path.join(self.image_dir, self.images_files[contador+5])).scaled(60, 60)
                    label = QLabel(self.widget)
                    label.setPixmap(image)
                    self.scroll_Qvbox.addWidget(label)
                    self.scroll_Qvbox.setContentsMargins(10, 0, 0, 0)
                    button.setGeometry(c*70, contador2*75, image.width(), image.height())
                    contador +=1
            contador2+=1 
    
        
        # Create thhe scroll area and set its widget property
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidget(self.widget)

        # Add the scroll  area to the  parent widget's layout
        main_widget = QWidget()
        main_layout = QVBoxLayout(main_widget)
        main_layout.addWidget(self.scroll_area)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Change()
    window.show()
    sys.exit(app.exec_())