import random

E = 'Проблемы ввода!!!'
PROBLEMSCOORDINATS = {'11': ['13', '31'], '16': ['14', '36'], '61': ['41', '63'], '66': ['46', '64']}
def random_6():
    return random.randint(1, 6)

def random_8():
    return random.randint(1, 8)

def number_check(num):
    if num == None:
        num = ()

    try:
        type(int(num)) == int
    except ValueError:
        print(E + " Введённое значение не является числом!!! ")
        return False
    else:
        for a in convert_number_to_digits(num):
            if not (0 < a < 7):
                print(E + ' Вы вышли за пределы поля!!!')
                return False
    num = None
    return True

def checking_or_ships_nearby(Field, cord, human, coordinates):

    if coordinates == None:
        coordinates = []
    num = None
    if num == None:
        num = convert_number_to_digits(cord)#введённые координаты

    if Field.LINES[num[0]-1][num[1]-1][0] == Field.SHIP:  # если ставим на занятую клетку
        print(E + ' Эта позиция уже занята!')
        return False
    def next_to_another_ship():
            if human:
                print(E + f' Рядом на {str(num[0]+i)+str(num[1]+j)} другой корабль !')
            return False

    for i in range(-1, 2):
        for j in range(-1, 2):
            try:
                cordindefsym = Field.LINES[num[0]+i-1][num[1]+j-1][0]# Проверка на выпадение за пределы поля
            except IndexError:
                continue

            if not len(coordinates):
                if cordindefsym == Field.SHIP:
                    return next_to_another_ship()
            else:
                prev = convert_number_to_digits(coordinates[-1])
                print(f'{num[0] - prev[0]}   +    {num[1] - prev[1]}')
                if len(coordinates) == 2:  # Что бы не был углом трёхпалубный
                    print(coordinates)
                    a = convert_number_to_digits(coordinates[0])
                    b = convert_number_to_digits(coordinates[1])
                    print(f'{a[0]}{min(a[1], b[1]) - 1}    {a[0]}{max(a[1], b[1]) + 1} num = {num}')
                    if a[0] == b[0]:
                        if cord == convert_digits_to_number(a[0], min(a[1], b[1])-1) or\
                            cord == convert_digits_to_number(a[0], max(a[1], b[1])+1):
                            print(f'{a[0]}{min(a[1], b[1])-1}    {a[0]}{max(a[1], b[1])+1} num = {num}')
                            return True
                    if a[1] == b[1]:
                        if cord == convert_digits_to_number(min(a[0], b[0])-1, a[1]) or\
                            cord == convert_digits_to_number(max(a[0], b[0])+1, a[1]):
                            return True
                    else:
                        print(E +' Трёхпалубный корабль должен быть расположен по прямой и без пробелов!')
                        return False

                if abs(num[0] - prev[0]) > 1 or abs(num[1] - prev[1]) > 1:
                    print(E + ' Не должно быть пробелов между палубами корабля!')
                    return False
                if num[0] != prev[0] and num[1] != prev[1]:# проверка на диагональ
                     print(E + ' Нельзя ставить палубы по диагонали! ')
                     return False
                if cordindefsym == Field.SHIP and coordinates[-1] != convert_digits_to_number(num[0] + i, num[1] + j):
                    print(cordindefsym)
                    print(f'{coordinates[-1]} -- {str(num[0] + i - 1) + str(num[1] + j - 1)}')
                    return next_to_another_ship()# если координаты совпадают с предидущей палубой

    return True
def space_for_two_decks(Field, coord, decks, numberofdecks, human):

    if decks == 2 and numberofdecks == 1 :
        for key, listok in PROBLEMSCOORDINATS.items():
            if key == coord:
                if Field.LINES[convert_number_to_digits(listok[0])[0]-1][convert_number_to_digits(listok[0])[1]-1][0] == Field.SHIP\
                    and Field.LINES[convert_number_to_digits(listok[1])[0]-1][convert_number_to_digits(listok[1])[1]-1][0] == Field.SHIP:
                    if human:
                        print(E + ' Здесь не поместится двухпалйбный корабль!')
                    return False
    return True

def convert_number_to_digits(num):
    character1 = int(list(str(num))[0])
    character2 = int(list(str(num))[1])
    return character1, character2
def convert_digits_to_number(a, b):
    number = str(a) + str(b)
    return number

