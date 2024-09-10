import PyQt5
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox,  QStackedWidget
from PyQt5.QtGui import QPixmap, QIcon
from generation_word import word_categories
from dictionary import word_categories_dictionary
from PyQt5.QtGui import QIcon
import random

class Ui_SecondaryWindows(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('картинки/иконка.jpg'))
        self.setStyleSheet("background-color: lightblue;")
        self.random_word = "" #случайно выбранное слово
        self.hidden_word_display = []   #стображение слова пользователю
        self.guessed_letters = []       #список использованных букв
        self.guessed_letters_in_word = []    #список отгаданных букв
        self.timer_host = QTimer(self)
        self.timer_host.setSingleShot(True)
        self.timer_host.timeout.connect(self.clear_label_host)

    def Menu(self):   #окно меню
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 400))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setMaximumSize(QtCore.QSize(16777215, 200))
        font = QtGui.QFont()
        font.setPointSize(45)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayout_4.addWidget(self.frame_2, 0, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setVerticalSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        self.Rules_Button = QtWidgets.QPushButton(self.frame)
        self.Rules_Button.setMaximumSize(QtCore.QSize(250, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Rules_Button.setFont(font)
        self.Rules_Button.setObjectName("Rules_Button")
        self.gridLayout.addWidget(self.Rules_Button, 1, 0, 1, 1)
        self.Play_Button = QtWidgets.QPushButton(self.frame)
        self.Play_Button.setMaximumSize(QtCore.QSize(250, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Play_Button.setFont(font)
        self.Play_Button.setObjectName("Play_Button")
        self.gridLayout.addWidget(self.Play_Button, 0, 0, 1, 1)
        self.Exit_Button = QtWidgets.QPushButton(self.frame)
        self.Exit_Button.setMaximumSize(QtCore.QSize(250, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Exit_Button.setFont(font)
        self.Exit_Button.setObjectName("Exit_Button")
        self.gridLayout.addWidget(self.Exit_Button, 2, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame, 1, 0, 1, 1)
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi_Menu()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi_Menu(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Поле чудес"))
        self.label.setText(_translate("MainWindow", "Поле чудес"))
        self.Rules_Button.setText(_translate("MainWindow", "Правила игры"))
        self.Rules_Button.clicked.connect(self.rules)
        self.Play_Button.setText(_translate("MainWindow", "Новая игра"))
        self.Play_Button.clicked.connect(self.game)
        self.Exit_Button.setText(_translate("MainWindow", "Выйти из игры"))
        self.Exit_Button.clicked.connect(self.exit_game)

    def Rules(self):     # окно правил
        self.centralwidget_2 = QtWidgets.QWidget(self)
        self.centralwidget_2.setObjectName("centralwidget_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.centralwidget_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget_2)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame_3.setCursor(QtGui.QCursor(QtCore.Qt.SizeAllCursor))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.gridLayout_6.addWidget(self.frame_3, 0, 0, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.centralwidget_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        self.label_2.setMinimumSize(QtCore.QSize(550, 300))
        self.label_2.setMaximumSize(QtCore.QSize(800, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.gridLayout_5.addWidget(self.label_2, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.frame_4, 1, 0, 1, 1)
        self.frame_5 = QtWidgets.QFrame(self.centralwidget_2)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.main_menu = QtWidgets.QPushButton(self.frame_5)
        self.main_menu.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.main_menu.setFont(font)
        self.main_menu.setObjectName("main_menu")
        self.gridLayout_7.addWidget(self.main_menu, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.frame_5, 2, 0, 1, 1)
        self.setCentralWidget(self.centralwidget_2)

        self.retranslateUi_Rules()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi_Rules(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Поле чудес"))
        self.label_3.setText(_translate("MainWindow", "Правила игры"))
        self.label_2.setStyleSheet('font:22pt')
        self.label_2.setAlignment(QtCore.Qt.AlignJustify)
        self.label_2.setText(_translate("MainWindow", "В начале игры будет выбрана случайная категория и будет загадано слово, относящееся к выбранной категории. Ваша задача: отгадать загаданное слово первее соперников(все слова написаны в именительном падеже). Если вы или соперник отгадали букву, она отобразится в загаданном слове на своём месте. Если же была указана неправильная буква, то ход переходит следующему участнику. Игра будет продолжаться, пока слово не будет отгадано. Так же у вас будет возможность один раз за игру воспользоваться подсказкой. Приятной игры!"))
        self.main_menu.setText(_translate("MainWindow", "На главное меню"))
        self.main_menu.clicked.connect(self.to_the_main_menu)

    def Win(self):
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setMaximumSize(QtCore.QSize(16777215, 200))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setContentsMargins(0, -1, -1, -1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setMaximumSize(QtCore.QSize(250, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_3.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMaximumSize(QtCore.QSize(250, 50))
        self.pushButton_2.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_3.addWidget(self.pushButton_2, 1, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_3)
        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.setCentralWidget(self.centralwidget)
        self.retranslateUi_win()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi_win(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Вы отгадали слово!"))
        self.pushButton.setText(_translate("MainWindow", "Новая игра"))
        self.pushButton.clicked.connect(self.game)
        self.pushButton_2.setText(_translate("MainWindow", "Главное меню"))
        self.pushButton_2.clicked.connect(self.to_the_main_menu)

    def Lose(self):
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setMaximumSize(QtCore.QSize(16777215, 200))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setContentsMargins(0, -1, -1, -1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setMaximumSize(QtCore.QSize(250, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_3.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMaximumSize(QtCore.QSize(250, 50))
        self.pushButton_2.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_3.addWidget(self.pushButton_2, 1, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_3)
        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.setCentralWidget(self.centralwidget)
        self.retranslateUi_lose()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi_lose(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Повезёт в следующий раз!"))
        self.pushButton.setText(_translate("MainWindow", "Новая игра"))
        self.pushButton.clicked.connect(self.game)
        self.pushButton_2.setText(_translate("MainWindow", "Главное меню"))
        self.pushButton_2.clicked.connect(self.to_the_main_menu)

    def exit_game(self):
        QApplication.quit()

    def to_the_main_menu(self):
        self.Menu()

    def rules(self):
        self.Rules()

    def game(self):
        self.GameWindow()

    def win(self):
        self.Win()

    def lose(self):
        self.Lose()

    def GameWindow(self):     # игровое окно
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setMaximumSize(QtCore.QSize(200, 225))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.gridLayout_2.addWidget(self.frame_3, 2, 0, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setMaximumSize(QtCore.QSize(200, 225))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.frame_4)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.gridLayout_2.addWidget(self.frame_4, 2, 2, 1, 1)
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_4 = QtWidgets.QGridLayout()

        # создание алфавита
        self.alphabet = [chr(i) for i in range(1040, 1072)]
        self.alphabet.insert(6, chr(1025))
        self.create_keyboard()

        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_5, 2, 1, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label_player = QtWidgets.QLabel(self.frame)
        self.label_player.setFont(font)
        self.label_player.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignBottom)
        self.gridLayout_2.addWidget(self.label_player, 1, 0, 1, 1)
        self.label_host = QtWidgets.QLabel(self.frame)
        self.label_host.setFont(font)
        self.label_host.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignBottom)
        self.gridLayout_2.addWidget(self.label_host, 1, 2, 1, 1)
        self.label_category = QtWidgets.QLabel(self.frame_2)
        self.label_category.setWordWrap(True)
        self.label_category.setFont(font)
        self.gridLayout_3.addWidget(self.label_category, 0, 0, 0, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label_word = QtWidgets.QLabel(self.frame_2)
        self.label_word.setFont(font)
        self.label_word.setObjectName("label_word")
        self.gridLayout_3.addWidget(self.label_word, 0, 0, 0, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom)
        self.horizontalLayout.addLayout(self.gridLayout_3)
        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 1, 3)
        self.frame_6 = QtWidgets.QFrame(self.frame)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_2.addWidget(self.frame_6, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.button_frame = QtWidgets.QFrame(self.frame)
        self.button_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.button_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.button_layout = QtWidgets.QHBoxLayout(self.button_frame)
        self.button_help = QtWidgets.QPushButton("подсказка", self.button_frame)
        self.button_help.setFixedSize(80, 50)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.button_help.setFont(font)
        self.button_layout.addWidget(self.button_help)
        self.gridLayout_2.addWidget(self.button_frame, 0, 2, 1, 1, QtCore.Qt.AlignTop | QtCore.Qt.AlignRight)
        self.setCentralWidget(self.centralwidget)
        self.retranslateUi_game()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi_game(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Поле чудес"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.label_3.setText(_translate("MainWindow", "Игрок"))
        self.label_4.setText(_translate("MainWindow", "TextLabel"))
        self.label_5.setText(_translate("MainWindow", "Ведущий"))
        pixmap1 = QPixmap('картинки/аватар.jpg')
        self.label_2.setPixmap(pixmap1)
        self.scaled_pixmap1 = pixmap1.scaled(250, 200)
        self.label_2.setPixmap(self.scaled_pixmap1)
        pixmap2 = QPixmap('картинки/ведущий.jpeg')
        self.label_4.setPixmap(pixmap2)
        self.scaled_pixmap2 = pixmap2.scaled(250, 200)
        self.label_4.setPixmap(self.scaled_pixmap2)
        self.button_help.clicked.connect(self.hint)
        app.setStyleSheet('#label_2, #label_4{ border: 1px solid black}; #label{ font-size: 26pt}')

        # выбор случайной подсказки
        self.random_category = random.choice(list(word_categories.keys()))
        self.label_category.setText(f"<center><span style='font-size: 28pt;'>{self.random_category}</span></center>")

        # выбор слова из выбранной подсказки
        self.hidden_word_display.clear()
        self.random_word = random.choice(word_categories[self.random_category])
        self.hidden_word_display = list("_" * len(self.random_word))

        self.label_word.setText(' '.join(self.hidden_word_display))  # установка скрытого слова в label

        self.input_locked = False
        self.guessed_letters.clear()
        self.guessed_letters_in_word.clear()

    def create_keyboard(self):
        for i in range(3):
            for j in range(11):
                btn = QtWidgets.QPushButton()
                btn.setText(self.alphabet[i * 11 + j])
                btn.clicked.connect(self.button_clicked)
                self.gridLayout_4.addWidget(btn, i, j)

    def button_clicked(self):   #функция для обработки нажатия кнопок на виртуальной клавиатуре
        button = self.sender()  # кнопка, которая была нажата
        if self.input_locked:
            return
        if button:
            self.label_host.clear()
            self.input_locked = True
            button.setEnabled(False)
            letter = button.text().lower()
            self.user_letter(letter)
            self.guessed_letters.append(letter)
            QTimer.singleShot(6000, self.clear_label_player)
            if letter in self.random_word:
                self.result = 1
                QTimer.singleShot(6500, self.unlock_input)
                QTimer.singleShot(2500, lambda: (self.there_letter(), QTimer.singleShot(3500, self.clear_label_host)))
                QTimer.singleShot(5000, lambda: (self.there_letter(), self.update_hidden_word_delayed(letter)))
                self.guessed_letters_in_word.append(letter)
            else:
                self.result = 0
                QTimer.singleShot(3000, lambda: (self.there_no_letter(), QTimer.singleShot(3000, self.clear_label_host)))
                self.input_locked = True
                QTimer.singleShot(7000, self.first_bot)
                QTimer.singleShot(8000, self.guess_letter_one)

    def keyPressEvent(self, event):      #функция обработки нажатия клавишь на клавиатуре
        if self.input_locked:
            return
        letter = event.text().lower()
        if event.key() == 16777216:  # Код клавиши Esc
            self.show_modal()
        if letter in self.guessed_letters:
            return
        if letter.isalpha() and len(letter) == 1:
            self.label_host.clear()
            self.input_locked = True
            self.user_letter(letter)
            self.guessed_letters.append(letter)
            button = self.find_button_by_letter(letter)
            if button:
                self.clear_keyboard(button)
            QTimer.singleShot(6000, self.clear_label_player)
            if letter in self.random_word:
                self.result = 1
                QTimer.singleShot(6500, self.unlock_input)
                QTimer.singleShot(2500, lambda: (self.there_letter(), QTimer.singleShot(3500, self.clear_label_host)))
                QTimer.singleShot(5000, lambda: (self.there_letter(), self.update_hidden_word_delayed(letter)))
                self.guessed_letters_in_word.append(letter)
            else:
                self.result = 0
                QTimer.singleShot(3000, lambda: (self.there_no_letter(), QTimer.singleShot(3000, self.clear_label_host)))
                self.input_locked = True
                QTimer.singleShot(8000, self.guess_letter_one)
                QTimer.singleShot(7000, self.first_bot)

    def clear_keyboard(self,button):
        button.setEnabled(False)

    def find_button_by_letter(self, letter):
        for i in range(3):
            for j in range(11):
                button = self.gridLayout_4.itemAtPosition(i, j).widget()
                if button and button.text().lower() == letter:
                    return button
        return None

    def guess_letter_one(self):   #Работа первого бота
        if "_" not in self.hidden_word_display:
            return
        self.guess_letters()
        possible_words = self.get_possible_words(self.label_word.text().replace(' ', ''))
        chance = random.randint(1,9)
        if possible_words:
            if len(self.random_word) <= 6 and len(list(set(self.random_word))) - len(self.guessed_letters_in_word) <= 1:
                random_word = random.choice(possible_words)
                letter = random.choice(random_word)
            elif len(self.random_word) > 6 and len(self.random_word) <= 8 and len(list(set(self.random_word))) - len(self.guessed_letters_in_word) <= 2:
                random_word = random.choice(possible_words)
                letter = random.choice(random_word)
            elif len(self.random_word) > 8 and len(list(set(self.random_word))) - len(self.guessed_letters_in_word) <= 3:
                random_word = random.choice(possible_words)
                letter = random.choice(random_word)
            elif chance in range(1,5):
                random_word = random.choice(possible_words)
                letter = random.choice(random_word)
            else:
                letter = random.choice(self.alphabet).lower()
        if letter in self.guessed_letters:
            QTimer.singleShot(100, self.guess_letter_one)
            return
        self.user_letter(letter)
        self.guessed_letters.append(letter)
        button = self.find_button_by_letter(letter)
        if button:
            self.clear_keyboard(button)
        QTimer.singleShot(6000, self.clear_label_player)
        if letter in self.random_word:
            QTimer.singleShot(2500, lambda: (self.there_letter(), QTimer.singleShot(3500, self.clear_label_host)))
            QTimer.singleShot(5000, lambda: (self.there_letter(), self.update_hidden_word_delayed(letter)))
            QTimer.singleShot(8000, self.guess_letter_one)
            self.guessed_letters_in_word.append(letter)
        else:
            QTimer.singleShot(3000, lambda: (self.there_no_letter(), QTimer.singleShot(3000, self.clear_label_host)))
            QTimer.singleShot(8000, self.guess_letter_two)
            QTimer.singleShot(7000, self.second_bot)

    def guess_letter_two(self):  #Работа второго бота
        if "_" not in self.hidden_word_display:
            return
        self.guess_letters()
        possible_words = self.get_possible_words(self.label_word.text().replace(' ', ''))
        chance = random.randint(1,9)
        if possible_words:
            if len(self.random_word) <= 6 and len(list(set(self.random_word))) - len(self.guessed_letters_in_word) <= 1:
                random_word = random.choice(possible_words)
                letter = random.choice(random_word)
            elif len(self.random_word) > 6 and len(self.random_word) <= 8 and len(list(set(self.random_word))) - len(self.guessed_letters_in_word) <= 2:
                random_word = random.choice(possible_words)
                letter = random.choice(random_word)
            elif len(self.random_word) > 8 and len(list(set(self.random_word))) - len(self.guessed_letters_in_word) <= 3:
                random_word = random.choice(possible_words)
                letter = random.choice(random_word)
            elif chance in range(1,4):
                random_word = random.choice(possible_words)
                letter = random.choice(random_word)
            else:
                letter = random.choice(self.alphabet).lower()
        if letter in self.guessed_letters:
            QTimer.singleShot(100, self.guess_letter_two)
            return
        self.user_letter(letter)
        self.guessed_letters.append(letter)
        button = self.find_button_by_letter(letter)
        if button:
            self.clear_keyboard(button)
        QTimer.singleShot(6000, self.clear_label_player)
        if letter in self.random_word:
            QTimer.singleShot(2500, lambda: (self.there_letter(), QTimer.singleShot(3500, self.clear_label_host)))
            QTimer.singleShot(5000, lambda: (self.there_letter(), self.update_hidden_word_delayed(letter)))
            QTimer.singleShot(8000, self.guess_letter_two)
            self.guessed_letters_in_word.append(letter)
        else:
            QTimer.singleShot(3000, lambda: (self.there_no_letter(), QTimer.singleShot(3000, self.clear_label_host)))
            QTimer.singleShot(7000, self.unlock_input)

    def update_hidden_word_delayed(self, letter):   # обновляем отображаемый пользователю текст загаданного слова
        for i in range(len(self.random_word)):
            if self.random_word[i] == letter:
                self.hidden_word_display[i] = letter
        self.label_word.setText(' '.join(self.hidden_word_display))
        self.player_win()
        self.player_lose()

    def player_win(self):
        if "_" not in self.hidden_word_display and self.result == 1:
            QTimer.singleShot(3500, self.win)

    def player_lose(self):
        if "_" not in self.hidden_word_display and self.result == 0:
            self.label_player.clear()
            self.label_host.clear()
            QTimer.singleShot(3500, self.lose)

    def guess_letters(self):     #создание шаблона слова для дальнейшей работы с ним
        pattern = self.label_word.text().replace(' ','')
        possible_words = self.get_possible_words(pattern)

    def get_possible_words(self, pattern):    #создаём список подходящих под щаблон слов
        dictionary = word_categories_dictionary
        possible_words = []

        for word in dictionary:
            if len(word) == len(pattern) and self.matches_pattern(word, pattern):
                possible_words.append(word)

        return possible_words

    def matches_pattern(self, word, pattern):   #сравниваем буквы шаблона с буквами из словаря
        for w_char, p_char in zip(word, pattern):
            if p_char != '_' and w_char != p_char:
                return False
        return True

    def user_letter(self, letter):   #Буква выбранная игроком/ботом
        self.chosen_letter = f"Буква \"{letter}\""
        self.label_player.setText(self.chosen_letter)

    def there_no_letter(self):   #Выбранной буквы нет в слове
        self.absent = f"Нет такой \n буквы"
        self.label_host.setText(self.absent)

    def there_letter(self):   #Выбранная буква есть в слове
        self.present = f"Откройте!"
        self.label_host.setText(self.present)

    def unlock_input(self):   #Разрешение игроку выбирать букву
        self.input_locked = False
        self.player = f"Игрок"
        self.label_3.setText(self.player)

    def clear_label_host(self):  #Очищение ответа ведущего
        self.label_host.clear()

    def clear_label_player(self):  #Очищение ответа игрока/бота
        self.label_player.clear()

    def first_bot(self):   #Ходит первый компьютер

        self.first = f"Первый компьютер"
        self.label_3.setText(self.first)

    def second_bot(self):   #Ходит второй компьютер
        self.second = f"Второй компьютер"
        self.label_3.setText(self.second)

    def hint(self):   #подсказка игроку
        if self.input_locked:
            return
        unopened_letters = set(self.random_word) - set(self.guessed_letters_in_word)
        if unopened_letters:
            letter = random.choice(list(unopened_letters))
            self.help = f"Назовите \n букву \"{letter}\""
            self.label_host.setText(self.help)
            self.button_help.setEnabled(False)

    def show_modal(self):
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle('Пауза')
        msg_box.setText('Вы хотите вернуться в главное меню?')
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        # Меняем текст кнопок после установки стандартных кнопок
        yes_button = msg_box.button(QMessageBox.Yes)
        yes_button.setText("Продолжить")

        no_button = msg_box.button(QMessageBox.No)
        no_button.setText("Главное меню")

        response = msg_box.exec_()
        if response == QMessageBox.No:
            # Создаем экземпляры окон
            self.menu = self.Menu()
            self.gamewindow = self.GameWindow()
            self.

            class changer_page(QStackedWidget):
                def __init__(self, parent=None):
                    super(changer_page, self).__init__(parent)

                    # Добавляем окна в QStackedWidget
                    self.addWidget(self.menu)
                    self.addWidget(self.gamewindow)

                    # Устанавливаем текущее окно (меню)
                    self.setCurrentIndex(0)

                def change(self):
                    if self.currentIndex() == 0:
                        self.setCurrentIndex(1)  # Переходим к игровому окну
                    else:
                        self.setCurrentIndex(0)  # Переходим к меню


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Ui_SecondaryWindows()
    MainWindow.setMinimumSize(1152, 864)
    MainWindow.Menu()
    MainWindow.showFullScreen()
    app.exec_()
