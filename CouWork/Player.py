from Person import Person
from Place import Place
from Place import Home

class Player(Person):
    """玩家"""

    def __init__(self, name):
        position = Home(self, 0, 0, 0)
        super().__init__(name,position)
        #应该把position加入list中
        self._knife=0
        self._zuoChe=0
        self._gun=0

    def moveTo(self, position):
        self._position = position

    def buyGun(self):
        #if position 在超市或者什么，就可以gun++
        self._gun += 1

    def buyKnife(self):
        #if position 在超市或者什么，就可以gun++
        self._knife += 1