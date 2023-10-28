from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QDesktopWidget,
    QTextEdit
)
from PyQt5 import QtGui
import json, sys
from random import choice
from pathlib import Path


class Quote(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
        self.gen_quote = QLabel("""""")
        self.gen_quote.setStyleSheet("font-size: 18px; font-family: Arial; padding-left: 350px;")
        

        self.quote = QTextEdit('Хотите ли вы сгенерировать цитату?')
        self.quote.setFixedSize(int(self.width_win/1.5), int(self.height_win/2.5))
        self.quote.setStyleSheet("font-size: 30px; font-family: Times; background-color: lightblue; border-radius: 30%;")
        self.quote.setAlignment(Qt.AlignCenter)
        self.quote.setTextInteractionFlags(Qt.NoTextInteraction)

        self.font_btn = QtGui.QFont("Times", 17, QtGui.QFont.Bold)
        self.push_button = QPushButton('Сгенерировать')
        self.push_button.setFont(self.font_btn)
        self.push_button.clicked.connect(self.new_quotes)
        self.push_button.setFixedSize(int(self.width_win/4), int(self.height_win/11))
        self.push_button.setStyleSheet("QPushButton {background-color: #79b6c9; color: white; border-radius: 10px;} QPushButton:hover {background-color: #5A8896;}")

        self.img = QLabel()

        self.layout_main = QVBoxLayout()
        self.layout_main.setSpacing(85)
        self.layout_quote = QHBoxLayout()
        self.layout_middle = QHBoxLayout()
        self.layout_push = QHBoxLayout()

        self.layout_quote.addWidget(self.quote, alignment=Qt.AlignCenter)
        self.layout_push.addWidget(self.push_button, alignment=Qt.AlignHCenter)
        self.layout_middle.addWidget(self.gen_quote, alignment=Qt.AlignRight)
        self.layout_middle.addWidget(self.img, alignment=Qt.AlignRight)

        self.layout_main.addLayout(self.layout_quote)
        self.layout_main.addLayout(self.layout_middle)
        self.layout_main.addLayout(self.layout_push)
        self.gen_quote.setVisible(False)
        self.img.setVisible(False)
        self.setLayout(self.layout_main)


    def initUI(self):
        self.setWindowTitle('Генератор цитат')
        self.width_screen = QDesktopWidget().screenGeometry(-1).width()
        self.height_screen = QDesktopWidget().screenGeometry(-1).height()
        self.width_win = int(QDesktopWidget().screenGeometry(-1).width()*0.5)
        self.height_win = int(QDesktopWidget().screenGeometry(-1).height()*0.6)
        self.setFixedSize(self.width_win, self.height_win)
        self.move((self.width_screen-self.width())//2, (self.height_screen-self.height())//2)
        self.setStyleSheet("background-color: lightblue;")


    def keyPressEvent(self, e):
        if e.key() == Qt.Key(16777220): 
            self.push_button.click()
        elif e.key() == Qt.Key(16777216): 
            self.close()


    def new_quotes(self):
        with open('цитаты.json', 'r', encoding="utf-8") as file:
            data = json.load(file)
        self.author = choice(list(data))
        self.quote.setText('“'+choice(data[self.author])+'„')
        self.gen_quote.setText(self.author)
        self.quote.setFixedSize(int(self.width_win/1.5), int(self.height_win/2.5))
        self.quote.setStyleSheet("font-size: 30px; font-family: Arial; font-style: italic; background-color: lightblue; border-radius: 30%;")
        self.quote.setAlignment(Qt.AlignCenter)
        self.pixmap = QtGui.QPixmap(str(Path("изображения", self.author+".png")))
        self.pixmap = self.pixmap.scaled(int(self.width_win/3.5), int(self.height_win/3.5))
        self.img.setPixmap(self.pixmap)
        self.gen_quote.setVisible(True)
        self.img.setVisible(True)

def main():
    app = QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('icon.png'))
    quote = Quote()
    quote.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()