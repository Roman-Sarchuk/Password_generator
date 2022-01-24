from random import randrange


class INFO:
    def __init__(self):
        self._number = 0
        self._type_symbols = [0, 0, '']
        self._list_char = [False, False, False, False]

    @staticmethod
    def __chek_y_n():
        while True:
            obj = str(input('-> '))
            if obj == 'y' or obj == 'yes':
                return True
            elif obj == 'n' or obj == 'no':
                return False
            else:
                print('! Ведіть y (yes) чи n (no) !')

    @staticmethod
    def __chek_int(txt):
        numbers = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
        while True:
            obj = str(input(txt))
            for i in obj:
                if i not in numbers:
                    print('! Потрібно вести число !')
                    break
                else:
                    return int(obj)

    def info(self):
        print('--- Info ---')

        print('Кількість паролів: (числом)')
        self._number = self.__chek_int('-> ')

        print('''Тип кількості символів: 1/2
1) Стала
2) Зміна''')
        while True:
            type_counter_symbols = str(input('-> '))
            if type_counter_symbols == '1':
                print('Кількість символів: (одним числом)')
                symbols_statistic = self.__chek_int('-> ')
                self._type_symbols[1] = symbols_statistic
                self._type_symbols[2] = 'statistical'
                break
            elif type_counter_symbols == '2':
                print('Кількість символів: (два числа)')
                self._type_symbols[2] = 'dynamic'
                while True:
                    symbol_dynamic_1 = self.__chek_int('Від: ')
                    symbol_dynamic_2 = self.__chek_int('До:  ')
                    if symbol_dynamic_2 <= symbol_dynamic_1:
                        print('! "Від" повино бути меншим, ніж "До" !')
                    else:
                        break
                self._type_symbols[0], self._type_symbols[1] = symbol_dynamic_1, symbol_dynamic_2
                break
            else:
                print('! Ведіть 1 чи 2 !')

        print('''Вид символів у паролі: Y/N
(Ведіть всі види з яких 
складатимется пароль!)''')
        print('1) Нижній регістер')
        low_reg = self.__chek_y_n()
        print('2) Верхній регістер')
        upr_reg = self.__chek_y_n()
        print('3) Цифри')
        num = self.__chek_y_n()
        print('4) Спеціальні символи')
        spec_char = self.__chek_y_n()
        self._list_char = [low_reg, upr_reg, num, spec_char]

        print('-------------')
        input('Натисніть Enter для продовження!')
        print()


class PASSWORD(INFO):
    def __init__(self):
        # self._number = 0
        # self._type_symbols = [0, 0, '']
        # self._list_char = [False, False, False, False]
        super().__init__()
        self.info()
        self._char = ''
        if self._list_char[0] is True:
            self._char += 'abcdefghijklmnopqrstuvwxyz'
        if self._list_char[1] is True:
            self._char += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if self._list_char[2] is True:
            self._char += '1234567890'
        if self._list_char[3] is True:
            self._char += '-_/\\*+!@#$%:;&'

        self._type_print = ''
        if self._type_symbols[2] == 'statistical':
            self._type_print = f'[{self._type_symbols[1]}]'
        else:
            self._type_print = f'[{self._type_symbols[0]} - {self._type_symbols[1]}]'

    def __logic(self):
        list_password = []
        len_char = len(self._char)
        cycle = self._type_symbols[0]
        for ps in range(0, self._number):
            password = ''
            if self._type_symbols[2] == 'statistical':
                for ch in range(0, self._type_symbols[1]):
                    password += self._char[randrange(0, len_char)]
            elif self._type_symbols[2] == 'dynamic':
                for ch in range(cycle):
                    password += self._char[randrange(0, len_char)]
                if cycle == self._type_symbols[1]:
                    cycle = self._type_symbols[0]
                else:
                    cycle += 1
            else:
                print('! Error !')
            list_password.append(password)
        return list_password

    def resume(self):
        print(f'''--- Resume ---
Number :: {self._number}
Type symbols :: ({self._type_symbols[2]}) :: {self._type_print}
Char :: {self._char}
--------------''')
        input('Натисніть Enter для продовження!')
        print()

    def password(self):
        lst_psw = self.__logic()
        print('--- Password ---')
        for psw in lst_psw:
            print(psw)
        print('----------------')
        input('Натисніть Enter для закінчення!')
        print()


def main():
    psw = PASSWORD()
    psw.resume()
    psw.password()


if __name__ == '__main__':
    main()
