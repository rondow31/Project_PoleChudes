import PyQt5
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPixmap
import random


def random_word(self):
    words = ["программа", "енисей", "египет", "кодинг"]
    return random.choice(words)


def display_word(self, word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "*"
    return display


def update_word(self):
    self.secret_word = self.random_word()
    self.guessed_letters = []
    self.word_parts = self.display_word(self.secret_word, self.guessed_letters)
    for i, part in enumerate(self.word_parts):
        self.label_word.setText(part)


def guess_letter(self, letter):
    if letter in self.guessed_letters:
        print("Вы уже вводили эту букву. Попробуйте другую.")
    else:
        self.guessed_letters.append(letter)
        if letter in self.secret_word:
            print("Вы угадали букву!")
        else:
            print("Вы не угадали букву.")
        self.update_word()