from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.style_autoaccept = False
        self.style_autopick = False

        self.autoaccept = QPushButton('auto-accept', self)
        self.autoaccept.setObjectName('auto')
        self.autoaccept.setGeometry(10, 10, 130, 30)
        self.autoaccept.clicked.connect(self.autoaccept_action)

        self.autopick = QPushButton('auto-pick', self)
        self.autopick.setObjectName('auto')
        self.autoaccept.setGeometry(200, 10, 130, 30)
        self.autopick.clicked.connect(self.autopick_action) 

        self.setWindowTitle('p e p p a . j p e g')
        self.setGeometry(100, 100, 400, 300)
        self.setObjectName('body')
        with open('Interface\style.css', 'r') as f:
            css = f.read()     
        app.setStyleSheet(css)

    def autoaccept_action(self):
        self.style_autoaccept = not self.style_autoaccept

        if self.style_autoaccept:
            self.autoaccept.setStyleSheet('background-color: #537FE7;')
        else:
            self.autoaccept.setStyleSheet('background-color: black;')

    def autopick_action(self):
        self.style_autopick = not self.style_autopick

        if self.style_autopick:
            self.autopick.setStyleSheet('background-color: #537FE7;')
        else:
            self.autopick.setStyleSheet('background-color: black;')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())