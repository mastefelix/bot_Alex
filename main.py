from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QHBoxLayout,
                             QVBoxLayout, QLineEdit, QTextEdit)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
import wiki, google_trans, weather, game

class ChatBotApp(QWidget):
    ''' основное окно, в котором располагается приветствие и кнопки для выбора действий '''
    def __init__(self):
        super().__init__()
        self.initUI() # создаём и настраиваем графические эелементы
        self.set_appear() # устанавливаем, как будет выглядеть окно (надпись, размер, место)
        self.setStyles() # устанавливаем визуальное оформление окна (цвета, шрифт, размеры элементов)
        self.connects() # устанавливаем связи между элементами
        self.show() # старт

    def initUI(self):
        ''' создаем графические элементы '''
        self.hello_text = QLabel("Привет! Это чат бот Алекс!\n\tДобро пожаловать!")
        self.description_text = QLabel("Для перехода к действию, нажми кнопку!")
        self.button_wiki = QPushButton("Википедия")
        self.button_translate = QPushButton("Переводчик")
        self.button_weather = QPushButton("Погода")
        self.button_game = QPushButton("Игра")
        self.button_back = QPushButton("Выход")

        self.main_layout = QVBoxLayout()
        self.h1_layout = QHBoxLayout()
        self.h2_layout = QHBoxLayout()

        self.main_layout.addWidget(self.hello_text, alignment=Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addWidget(self.description_text, alignment=Qt.AlignmentFlag.AlignCenter)
        self.h1_layout.addWidget(self.button_wiki)
        self.h1_layout.addWidget(self.button_translate)
        self.h2_layout.addWidget(self.button_weather)
        self.h2_layout.addWidget(self.button_game)
        self.main_layout.addLayout(self.h1_layout)
        self.main_layout.addLayout(self.h2_layout)
        self.main_layout.addWidget(self.button_back)
        self.setLayout(self.main_layout)

    def set_appear(self):
        ''' устанавливаем, как будет выглядеть окно (надпись, размер, место) '''
        self.setWindowTitle("Чат-бот")
        self.setWindowIcon(QIcon("bot.png"))
        self.resize(450, 500)

    def setStyles(self):
        '''устанавливаем визуальное оформление окна (цвета, шрифт, размеры элементов)'''
        self.setStyleSheet("background-color: #7192BE; color: #000; font-family: fantasy, Comic Sans MS;"
                           "font-size: 18px;")
        button_style = "background-color: #70BDB5; border-radius: 10px;"
        self.hello_text.setStyleSheet("font-size: 24px;")
        self.description_text.setStyleSheet("")
        self.button_wiki.setStyleSheet(button_style)
        self.button_translate.setStyleSheet(button_style)
        self.button_weather.setStyleSheet(button_style)
        self.button_game.setStyleSheet(button_style)
        self.button_back.setStyleSheet(button_style)

    def show_wiki(self):
        '''создаем экземпляры классов для перехода между окнами'''
        self.win_wiki = wiki.Wiki(self)
        self.hide()

    def show_translator(self):
        self.win_translator = google_trans.GoogleTranslator(self)
        self.hide()

    def show_weather(self):
        self.win_weather = weather.Weather(self)
        self.hide()

    def show_game(self):
        self.win_game = game.Game(self)
        self.hide()

    def connects(self):
        '''устанавливаем связи между элементами'''
        self.button_back.clicked.connect(exit)
        self.button_wiki.clicked.connect(self.show_wiki)
        self.button_translate.clicked.connect(self.show_translator)
        self.button_weather.clicked.connect(self.show_weather)
        self.button_game.clicked.connect(self.show_game)


if __name__ == "__main__":
    app = QApplication([])
    chat_bot = ChatBotApp()
    app.exec()
