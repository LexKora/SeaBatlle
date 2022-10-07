from support import *
from main import *

gameflag = True
CONTROLLIST = ['Y', 'y', 'N', 'n']
while gameflag:
    HumanField = Field()# где человек расставляет корабли и куда стреляет компьютер
    HumanReservField = Field()
    HumanFireField = Field()
    ComputerField = Field()
    ComputerFireField = Field()
    ComputerReservField = Field()
    print('Создаём Флот')
    HumaneFleet = Fleet()
    print('Вводим двухзначные чиисла где первая цифра горизонталь а вторая вертикаль ')
    human = True
    generator_of_ships(HumanField, HumanReservField, HumaneFleet, human)
    ComputerFleet = Fleet()
    human = False
    generator_of_ships(ComputerField, ComputerReservField, ComputerFleet, human)
    print('Поле компьютера')
    print(ComputerField.graphic_field())
    print('Поле игрока')
    print(HumanField.graphic_field())
    print('Начнём бой!!!')
    fire_to_ship(HumanField, HumanFireField, ComputerField, ComputerFireField, HumaneFleet, ComputerFleet)
    q = None
    while not (q in CONTROLLIST):
        q = input('Ещё одну партию?(да-"Y" нет -"N") ')

    if q == 'Y' or q == 'y':
        gameflag = True
    else:gameflag = False