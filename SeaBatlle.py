
from main import *

gameflag = True
CONTROLLIST = ['Y', 'y', 'N', 'n']
T = 'Вводите двухзначные чиисла где первая цифра горизонталь а вторая вертикаль '
while gameflag:
    HumanField = Field()
    HumanReservField = Field()
    HumanFireField = Field()
    ComputerField = Field()
    ComputerFireField = Field()
    ComputerReservField = Field()
    print('Создаём Флот')
    HumaneFleet = Fleet()
    print(T)
    print('Корабли не могут распологатся вплотную друг к другу и по диагонали.')
    human = True
    generator_of_ships(HumanField, HumanReservField, HumaneFleet, human)
    ComputerFleet = Fleet()
    human = False
    generator_of_ships(ComputerField, ComputerReservField, ComputerFleet, human)
    fire_to_ship(HumanField, HumanFireField, ComputerField, ComputerFireField, HumaneFleet, ComputerFleet)
    q = None
    while not (q in CONTROLLIST):
        q = input('Ещё одну партию?(да-"Y" нет -"N") ')

    if q == 'Y' or q == 'y':
        gameflag = True
    else:
        gameflag = False

