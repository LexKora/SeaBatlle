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
            print('')

    def character_replacement(self, place, symbol):#сюда подаём координаты без исправлений
        try:
            self.LINES[convert_number_to_digits(place)[0]-1][convert_number_to_digits(place)[1]-1][0] = symbol
        except IndexError:
            pass



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
        for n, thisship in enumerate(self.orderoffleet):
            if thisship is ship:
                self.orderoffleet.pop(n)
                print('Корабль потоплен!!!')


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
                    if not enough_space_for_ships(HField, humship, p):
                        if human:
                            print('Корабли не поместятся! Переставьте последний корабль!')
                        remove_last_points(Field, humship.coordinates, Field.EMPTY)
                    else: flag = False
                Fleet.add_in_fleet(humship)


def fire_to_ship(Field, FireField, CField, CFireField, Fleet, CFleet):
    fire_to_ship.computerhit = [False, 0, 0, 0]
    firelist = []

    def character_match_check(num):
        cord1, cord2 = convert_number_to_digits(num)
        return True if (7 > cord1 > 0 and 7 > cord2 > 0 and return_character(CFireField, cord1, cord2) == CFireField.EMPTY) else False

    while len(Fleet.orderoffleet) and len(CFleet.orderoffleet):
        print(f'{len(Fleet.orderoffleet)} кораблей игрока и {len(CFleet.orderoffleet)} кораблей компьютера')
        human = True
        computer = True

        while human and len(CFleet.orderoffleet):
            print('Ваше поле для стрельбы.')
            FireField.graphic_field()
            hufire = input('Введите координаты выстрела: ')
            if number_check(hufire):
                fire1, fire2 = convert_number_to_digits(hufire)
                if return_character(FireField, fire1, fire2) == FireField.EMPTY:#проверка на огонь по ненужным координатам
                    human = dmg_(CField, FireField, CFleet, convert_digits_to_number(fire1, fire2), computerflag=False)
                else: print(' Нет смысла сюда стрелять! Попробуйте ещё раз!')


        while computer and len(Fleet.orderoffleet) and len(CFleet.orderoffleet):
            if fire_to_ship.computerhit[1] == 0:
                firelist = []
            if fire_to_ship.computerhit[0] and fire_to_ship.computerhit[1] != 0:
                fire1, fire2 = convert_number_to_digits(comfire)
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if abs(i) != abs(j) and 7 > (fire1+i) > 0 and 7 > (fire2+j) > 0 \
                                and return_character(CFireField, fire1+i, fire2+j) == Field.EMPTY:
                            firelist.append(convert_digits_to_number(fire1+i, fire2+j))
                if fire_to_ship.computerhit[1] == 2 and len(firelist) > 1:#стрельба компьютера по трёхпалубному после двух попаданей
                    firstwreck1number, firstwreck2number = convert_number_to_digits(fire_to_ship.computerhit[2])
                    sekondwreck1number, sekondwreck2number = convert_number_to_digits(fire_to_ship.computerhit[3])
                    firelist = []
                    if line_check(firstwreck1number, sekondwreck1number):
                        firelist.append(convert_digits_to_number(firstwreck1number, min(firstwreck2number, sekondwreck2number)-1))
                        firelist.append(convert_digits_to_number(firstwreck1number, max(firstwreck2number, sekondwreck2number)+1))
                        firelist = [x for x in firelist if character_match_check(x)]
                    if line_check(firstwreck2number, sekondwreck2number):
                        firelist.append(convert_digits_to_number(min(firstwreck1number, sekondwreck1number)-1, firstwreck2number))
                        firelist.append(convert_digits_to_number(max(firstwreck1number, sekondwreck1number)+1, firstwreck2number))
                        firelist = [x for x in firelist if character_match_check(x)]

                comfire = random_list(firelist)
                firelist.remove(comfire)
            elif not fire_to_ship.computerhit[0] and fire_to_ship.computerhit[1] != 0:
                comfire = random_list(firelist)
                firelist.remove(comfire)
            else:
                comfire = convert_digits_to_number(random_num(6), random_num(6))
            if return_character(CFireField, *comfire) == CFireField.EMPTY:
                print(f'Компьютер стреляет {comfire}!')
                computer = dmg_(Field, CFireField, Fleet, comfire, computerflag=True)
                fire_to_ship.computerhit[0] = computer# флаг того что компьютер попал
                if computer and fire_to_ship.computerhit[1] > 0:
                    if fire_to_ship.computerhit[1] == 1:
                        fire_to_ship.computerhit[2] = comfire
                    if fire_to_ship.computerhit[1] == 2:
                        fire_to_ship.computerhit[3] = comfire
                print('Поле для стрельбы компьютера: ')
                CFireField.graphic_field()

    if not len(Fleet.orderoffleet):
        print('Победил компьютер!')
        print('Флот компьютера: ')
        CField.graphic_field()
    else:print('Вы победили!')


def dmg_(EnemyField, Field, EnemyFleet, fire, computerflag):
    for ship in EnemyFleet.orderoffleet:
        for n, deck in enumerate(ship.coordinates):
            if deck == fire:
                ship.coordinates[n] = deck + Field.WRECK
                Field.character_replacement(fire, Field.WRECK)
                EnemyField.character_replacement(fire, Field.WRECK)
                print('Попадание!!!')
                if computerflag:
                    fire_to_ship.computerhit[0] = True
                    fire_to_ship.computerhit[1] = fire_to_ship.computerhit[1]+1

                count = 0
                for d in ship.coordinates:
                    if Field.WRECK in list(d):
                        count += 1
                if len(ship.coordinates) == count:#помечаем все точки вокруг потопленного корабля взрывами
                    for dd in ship.coordinates:
                        num = convert_number_to_digits(dd)
                        for i in range(-1, 2):
                            for j in range(-1, 2):
                                try:
                                    cordindefsym = return_character(Field, num[0] + i, num[1] + j)
                                except IndexError:
                                    continue
                                if cordindefsym == Field.EMPTY and (num[0] + i) > 0 and (num[1] + j) > 0:
                                    Field.character_replacement(convert_digits_to_number(num[0] + i, num[1] + j), Field.EXPLOSION)
                    EnemyFleet.del_in_fleet(ship)
                    if computerflag:
                        fire_to_ship.computerhit[1] = 0
                        fire_to_ship.computerhit[0] = True

                return True
    Field.character_replacement(fire, Field.EXPLOSION)
    fire_to_ship.computerhit[0] = False
    print('Промах... ')
    return False






