from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit, QTextEdit
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from googletrans import Translator


class GoogleTranslator(QWidget):
    ''' основное окно, в котором располагается приветствие и кнопки для выбора действий '''
    def __init__(self, window):
        super().__init__()
        self.main_window = window
        self.initUI() # создаём и настраиваем графические эелементы
        self.set_appear() # устанавливаем, как будет выглядеть окно (надпись, размер, место)
        self.setStyles() # устанавливаем визуальное оформление окна (цвета, шрифт, размеры элементов)
        self.connects() # устанавливаем связи между элементами
        self.show() # старт

    def initUI(self):
        ''' создаем графические элементы '''
        self.label = QLabel("Для поиска информации \n\t введи запрос")
        self.request = QLineEdit()
        self.request.setPlaceholderText("Слово или фраза для перевода")
        self.info = QTextEdit()
        self.info.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.info.setReadOnly(True)
        self.button_start = QPushButton("Перевести")
        self.button_clear = QPushButton("Очистить")
        self.button_back = QPushButton("Назад")

        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.label, alignment=Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addWidget(self.request)
        self.main_layout.addWidget(self.info)
        self.main_layout.addWidget(self.button_start)
        self.main_layout.addWidget(self.button_clear)
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
        # self.label.setStyleSheet("font-size: 24px;")
        self.request.setStyleSheet("background-color: #FFF; font-size: 16px;")
        self.info.setStyleSheet("background-color: #FFF; font-size: 12px; width: 150px; height: 80px;")
        self.button_start.setStyleSheet(button_style)
        self.button_clear.setStyleSheet(button_style)
        self.button_back.setStyleSheet(button_style)

    def connects(self):
        '''устанавливаем связи между элементами'''
        self.button_back.clicked.connect(self.back_click)
        self.button_start.clicked.connect(self.get_translate)
        self.button_clear.clicked.connect(self.clear)

    def back_click(self):
        '''создаем экземпляры классов для перехода между окнами'''
        self.main_window.show()
        self.hide()

    def get_translate(self):
        if self.request.text():
            try:
                self.result = Translator().translate(self.request.text(), src='ru', dest='en').text
                self.info.setText(self.result)
            except:
                self.info.setText("Ошибка запроса")
        else:
            self.info.setText("Введите текст запроса")

    def clear(self):
        self.request.clear()
        self.info.clear()

