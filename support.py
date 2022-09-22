import random

E = 'Проблемы ввода!!!'

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
        num = convert_number_to_digits(cord)
    print(Field.LINES[num[0]-1][num[1]-1][0])
    try:
        if Field.LINES[num[0]-1][num[1]-1][0] == '#':  # если ставим на занятую клетку
            print(E + ' Эта позиция уже занята!')
            return False
    except IndexError:
        print()
    for i in range(-1, 2):
            for j in range(-1, 2):
                #if num[0] == num[1] or num[0] - num[1] == 0:# а надо ли?
                    #continue
                #else:
                    try:
                        cordindefsym = Field.LINES[num[0]+i-1][num[1]+j-1][0]# Проверка на выпадение за пределы поля


                    except IndexError:
                        continue

                    if len(coordinates) != 0:
                        print(len(coordinates))
                        prev = convert_number_to_digits(coordinates[-1])
                        print(coordinates[-1] + ' !!!  ' + str(num[0] + i - 1) + str(num[1] + j - 1))
                        if (num[0] - prev[0]) > 1 or (num[1] - prev[1]) > 1:
                            print(E + ' Не должно быть пробелов между палубами корабля!')
                            return False
                        if num[0] != prev[0] and num[1] != prev[1]:# проверка на диагональ
                            print(E + ' Нельзя ставить палубы по диагонали! ')
                            return False


                        if (num[0]) == prev[0] and (num[1]) == prev[1]:
                            raise UnboundLocalError
                            print(f'{num[0]} = {prev[0]}  {num[1]} = {prev[1]}')
                            print(E + ' Здесь предидущая палуба!')
                            return False  # если координаты совпадают с предидущей палубой


                        elif cordindefsym == Field.SHIP and coordinates[-1] != str(num[0]+i-1)+ str(num[1]+j-1):
                                 print(f'{coordinates[-1]} мммм {int(str(num[0]+i-1)+ str(num[1]+j-1))} ')
                                 if human:
                                     print(f'{num[0]+i} = {prev[0]}  {num[1] + j} = {prev[1]}')
                                     print(E + ' Рядом другой корабль !')
                                     return False


    return True
def convert_number_to_digits(num):
    character1 = int(list(str(num))[0])
    character2 = int(list(str(num))[1])
    return character1, character2
