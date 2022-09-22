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
        previous = None
        while len(self.coordinates) < self.deck:
            Field.graphic_field()
            print(f' палуба № {len(self.coordinates)+1}')
            a = input('Вводиим координаты : ')
            if number_check(a) and checking_or_ships_nearby(Field, a, human, self.coordinates):
                self.coordinates.append(a)
                Field.character_replacement(a, Field.SHIP)
                previous = a
        print(self.coordinates)

class Fleet():

    def __init__(self):
        self.ship = []
        self.orderoffleet = []
    def add_in_fleet(self, ship):
        self.orderoffleet.append(ship)

    def del_in_fleet(self, ship):
        if not len(ship):
            self.orderoffleet.pop(ship)


def generator_of_ships(Field , Fleet, human ):
    for i in range(1, 4): # количество кораблей

            j = 4 - i
            for p in range(1, 5 - j):# палубы кораблей
                humship = Ship(j)
                print(f'{j} палубный №{p} ', end='')
                humship.ship_installation(Field, human)
                Fleet.add_in_fleet(humship)




