from Place import Home
from Place import OutsideHome

class Person(object):
    """人物"""

    def __init__(self, name, plc):
        self._name = name
        self._plc = plc

    @property
    def name(self):
        return self._name

    @property
    def plc(self):
        return self._plc

    @name.setter
    def name(self, name):
        self._name = name

    @plc.setter
    def setplc(self, position):
        self._plc = plc

    def PrintName(self):
        print(self.name, end = '')

    @name.setter
    def rename(self, name):
        self._name = name


class Player(Person):
    """玩家"""

    def __init__(self, name, plc, hp = 3, knife = 0, biscuit = 0, gun = 0):
        super().__init__(name, plc)
        self.hp = hp
        self.knife = knife
        self.biscuit = biscuit
        self.gun = gun

    def MoveTo(self, plc):
        self.plc = plc

    def BuyGun(self):
        if (self.plc.type == 3 and not self.plc.broken or self.plc.type == 4):
            self.gun += 1
        else:
            print('Invalid action!')

    def BuyKnife(self):
        if (self.plc.type == 3 and not self.plc.broken or self.plc.type == 4):
            self.knife += 1
        else:
            print('Invalid action!')

    def BuyBiscuit(self):
        if (self.plc.type == 3 and not self.plc.broken or self.plc.type == 4):
            self.biscuit += 1
        else:
            print('Invalid action!')

if __name__ == '__main__':
    pass