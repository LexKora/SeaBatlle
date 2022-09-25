from support import *
from main import *

HumanField = Field()# где человек расставляет корабли и куда стреляет компьютер
HumanHideField = Field()
ComputerField = Field()
ComputerHideField = Field()
ComputerReservField = Field()

#HumanField.graphic_field()
print('Создаём Флот')
HumaneFleet = Fleet()
print('Вводим двухзначные чиисла где первая цифра горизонталь а вторая вертикаль ')
human = True
generator_of_ships(HumanField, HumanHideField, HumaneFleet, human)
ComputerFleet = Fleet()
human = False
generator_of_ships(ComputerHideField, ComputerReservField, ComputerFleet, human)
print('Поле компьютера')
print(ComputerHideField.graphic_field())
print('Поле игрока')
print(HumanField.graphic_field())
