import random

def random_word():
    words = ["программа", "енисей", "египет", "кодинг"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "*"
    return display

def hangman():
    print('Добро пожаловать в игру "Поле Чудес"!')
    secret_word = random_word()
    guessed_letters = []
    attempts = 7  # Количество попыток

    while attempts > 0:
        current_display = display_word(secret_word, guessed_letters)
        print(f"Слово: {current_display}")
        print(f"Оставшиеся попытки: {attempts}")

        guess = input("Введите букву: ").lower()

        if guess in guessed_letters:
            print("Вы уже вводили эту букву. Попробуйте другую.")
            continue

        guessed_letters.append(guess)

        if guess not in secret_word:
            attempts -= 1
            print("Неверная буква!")

        if guess not in secret_word:
            attempts -= 1
            print("Неверное слово!")

        if secret_word in guess or "*" not in display_word(secret_word, guessed_letters):
            print(f"Поздравляем! Вы угадали слово: '{secret_word}'. Вы победили!")
            break

    if "*" in display_word(secret_word, guessed_letters):
        print(f"Игра окончена. Загаданное слово было: '{secret_word}'.")

if __name__ == "__main__":
    hangman()