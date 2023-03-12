from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('p e p p a')
        self.setGeometry(100, 100, 400, 300)
        self.setStyleSheet('background-color: black;')

        button = QPushButton('Botão', self)
        button.setGeometry(150, 100, 100, 50)

        webview = QWebEngineView(self)
        self.setCentralWidget(webview)
        webview.load(QUrl(''))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())