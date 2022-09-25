from support import *


class Field():
    EMPTY = '-'
    SHIP = '#'
    WRECK = 'X'
    EXPLOSION = '*'

    def __init__(self):
        self.LINES = [[[Field.EMPTY] for j in range(1, 7)] for i in range(1, 7)]


    def graphic_field(self):
        print('')
        print('   |1|2|3|4|5|6| ')
        for i in range(6):
            print(f'  {i + 1}|', end='')
            for j in range(6):
                print(self.LINES[i][j][0] + '|', end='')
            print()

    def character_replacement(self, place, symbol):
       self.LINES[convert_number_to_digits(place)[0]-1][convert_number_to_digits(place)[1]-1][0] = symbol



class Ship():

    def __init__(self, deck):
        self.deck = deck
        self.Field = Field
        self.coordinates = []
    def ship_installation(self, Field, human):

        while len(self.coordinates) < self.deck:
            if human:
                print(f' палуба № {len(self.coordinates) + 1}')
                Field.graphic_field()
                a = input('Вводиим координаты : ')
            else: a = convert_digits_to_number(random_num(6),random_num(6))
            if number_check(a) and checking_or_ships_nearby(Field, a, human, self.coordinates) and\
                    space_for_two_decks(Field, a, self.deck, len(self.coordinates)+1, human):
                self.coordinates.append(a)
                Field.character_replacement(a, Field.SHIP)


class Fleet():

    def __init__(self):
        self.ship = []
        self.orderoffleet = []
    def add_in_fleet(self, ship):
        self.orderoffleet.append(ship)

    def del_in_fleet(self, ship):
        if not len(ship):
            self.orderoffleet.pop(ship)


def generator_of_ships(Field , HField, Fleet, human ):
    for i in range(1, 4): # количество кораблей

            j = 4 - i
            for p in range(1, 5 - j):# палубы кораблей
                flag = True
                while flag:
                    humship = Ship(j)
                    if human:
                        print(f'{j} палубный №{p} ', end='')
                    humship.ship_installation(Field, human)
                    if enough_space_for_ships(HField, humship, p) == False:
                        if human:
                            print('Корабли не поместятся!!! Переставьте последний корабль!!!')
                            print(HField.graphic_field())
                        remove_last_points(Field, humship.coordinates, Field.EMPTY)
                    else: flag = False
                Fleet.add_in_fleet(humship)

def computer_layout(Field, HField):
    generator_of_ships()

def fire_to_ship(Field, HField, CField, CHField, Fleet, CFleet):
    while not len(Fleet.orderoffleet) or not len(CFleet.orderoffleet):
        human = True
        while human:
            fire = input('Введите координаты выстрела! ')
            if CField.LINES[convert_number_to_digits(fire)[0],convert_number_to_digits(fire)[1]][0] == CField.EMPTY:
                human = dmg_(CField, HField, CFleet, fire)


def dmg_(EnemyField, Field, EnemyFleet, fire):
    for ship in EnemyFleet:
        for deck, n in enumerate(ship):
            if deck == fire:
                ship[n] = deck + Field.WRECK
                Field.character_replacement(fire, Field.WRECK)
                EnemyField.character_replacement(fire, Field.WRECK)
                count = 0
                for d in ship:
                    if Field.WRECK in list(d):
                        count += 1
                if len(ship) == count:

                    for dd in ship:#помечаем все точки вокруг потопленного корабля взрывами
                        num = convert_number_to_digits(dd)
                        for i in (-1, 2):
                            for j in (-1, 2):
                                try:
                                    cordindefsym = Field.LINES[num[0] + i - 1][num[1] + j - 1][
                                        0]  # Проверка на выпадение за пределы поля
                                except IndexError:  # убрать?
                                    continue
                                if cordindefsym == Field.EMPTY:
                                    Field.character_replacement(convert_digits_to_number(num[0] + i - 1, num[1] + j - 1),\
                                                                Field.EXPLOSION)
                    EnemyFleet.del_in_fleet(ship)
                return True
    return False






