from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt
import sys

app = QApplication(sys.argv)
def on_button():
    print('Arrumou')
    
button = QPushButton()
layout = QVBoxLayout(button)
image = QPixmap('Interface\settings\champs\Yorick.png')
label = QLabel()
label.setPixmap(image)
layout.addWidget(label)
layout.setContentsMargins(0, 0, 0, 0)
button.clicked.connect(on_button)
button.show()


sys.exit(app.exec_())
