from random import randrange


def chek_int(txt):
    numbers = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
    while True:
        obj = str(input(txt))
        for i in obj:
            if i not in numbers:
                print('! Потрібно вести додатнє число !')
                break
            else:
                return int(obj)


def info():
    print('--- Info ---')
    print('Кількість паролів: (числом)')
    number = chek_int('-> ')
    print('Кількості символів: (числом)')
    symbols = chek_int('-> ')
    print('-------------')
    input('Натисніть Enter для продовження!')
    print()
    return number, symbols


def logic(data):    # data = (number, symbols)
    char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-_/\\*+!@#$%:;&'
    list_password = []
    len_char = len(char)
    for ps in range(data[0]):
        psw = ''
        for ch in range(data[1]):
            psw += char[randrange(0, len_char)]
        list_password.append(psw)
    return list_password


def password(data):     # data = (number, symbols)
    print('--- Password ---')
    lst_psw = logic(data)
    for psw in lst_psw:
        print(psw)
    print('----------------')
    input('Натисніть Enter для закінчення!')
    print()


def main():
    information = info()
    password(information)



if __name__ == '__main__':
    main()
