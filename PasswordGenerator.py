import random
import array
import re


class Password:
    def __init__(self) -> None:
        self.DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.LOWERCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                                     'z']

        self.UPPERCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                                     'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                                     'Z']

        self.SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
                        '*', '(', ')', '<']

        self.COMBINED_LIST = self.DIGITS + self.UPPERCASE_CHARACTERS + self.LOWERCASE_CHARACTERS + self.SYMBOLS

    def generate(self, length):
        rand_digit = random.choice(self.DIGITS)
        rand_upper = random.choice(self.UPPERCASE_CHARACTERS)
        rand_lower = random.choice(self.LOWERCASE_CHARACTERS)
        rand_symbol = random.choice(self.SYMBOLS)

        temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

        for x in range(length - 4):
            temp_pass = temp_pass + random.choice(self.COMBINED_LIST)

            temp_pass_list = array.array('u', temp_pass)
            random.shuffle(temp_pass_list)

        password = ""
        for x in temp_pass_list:
            password = password + x

        return password

    @staticmethod
    def check(password):
        flag = True

        while True:
            if len(password) <= 8:
                flag = False
                break
            elif not re.search("[a-z]", password):
                flag = False
                break
            elif not re.search("[A-Z]", password):
                flag = False
                break
            elif not re.search("[0-9]", password):
                flag = False
                break
            elif not re.search("[_@$]", password):
                flag = False
                break
            elif re.search(r"\s", password):
                flag = False
                break
            else:
                return "Итс окэй... Вернись в главное меню"
                break

        if not flag:
            return "Ну... Может в следующий раз получится! Вернись в главное меню"
