import random

class The_hanged_man():

    def __init__(self):
       self.life = 6
       self.dictionary = ['гуала', 'хоуми', 'блок', 'чаппа', 'лейм', 'гэнг', 'флоу', 'вайб', 'снич', 'шутер', 'факбой', 'хасл']
       self.the_word = 'ккыыыааа'
       self.hidden_word = "□" * len(self.the_word)
       self.wrong_letters = []
       self.wrong_letters_count = 0
       ## random.choice(self.dictionary)
    def letter_check(self, letter): # алгоритм показывания букв
        self.the_word_list = list(self.the_word)
        for l in range(len(self.the_word_list)):
            if self.the_word_list[l] == letter:
                hidden_word_list = list(self.hidden_word) 
                hidden_word_list[l] = letter
                self.hidden_word = "".join(hidden_word_list)
    
    def end_game(self):
        if self.life == 0:
            print(f'Вы проиграли. Загаданное слово - {self.the_word}')
        elif self.hidden_word == self.the_word:
            print('Поздравляем, вы выиграли!')
    
    def attempt_checker(self, letter): # проверка на наличие буквы в слове
        if len(letter) > 1 or letter not in 'абвгдеёжзиклмнопрстиуфхцчшщъыьэюя':
            print('Введите букву русского алфавита!')
        else:
            if letter not in self.the_word:
                if letter not in self.wrong_letters: # проверка на наличие буквы в использованном списке
                    self.life -= 1
                    self.wrong_letters.append(letter)
                    self.wrong_letters_count = len(self.wrong_letters)
                    string_wrong_letters = ', '.join(self.wrong_letters) 
                    print(f'Спрятанное слово: {self.hidden_word}')
                    print(f'Этой буквы нет в слове, осталось жизней: {self.life}')
                    print(f'Ошибки ({self.wrong_letters_count}): {string_wrong_letters if len(self.wrong_letters) != 0 else ""}') # ради красоты в выводе
                else:
                    print('Вы уже пробовали эту букву, попробуйте другую.')
            else:
                if letter not in self.hidden_word:
                    self.letter_check(letter)
                    print(f'Вы угадали букву! Спрятанное слово: {self.hidden_word}')
                    print(f'Ошибки ({self.wrong_letters_count}): {string_wrong_letters if len(self.wrong_letters) != 0 else ""}')
                else: 
                    print('Вы уже угадали эту букву.')
            self.end_game()
        

    def attempt(self):
        print(f'Спрятанное слово: {self.hidden_word}')
        while self.hidden_word != self.the_word and self.life > 0:
            letter = input('Введите букву: ').lower()
            self.attempt_checker(letter)
        return

def main():
    game = The_hanged_man()
    game.attempt()
main()