from support import *
from main import *

HumanField = Field()
ComputerField = Field()
ComputerHideField = Field()

#HumanField.graphic_field()
print('Создаём Флот')
HumaneFleet = Fleet()
print('Вводим двухзначные чиисла где первая цифра горизонталь а вторая вертикаль ')
human = True
generator_of_ships(HumanField, HumaneFleet, human)

print()
print(HumanField.graphic_field())