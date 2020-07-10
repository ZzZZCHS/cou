from Place import Home
from Place import OutsideHome

import base

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

    def OpenDoor(self):
        if (self.plc.type == 0 and self.plc.door == 0): 
            self.plc.door = 1
            return
        if (self.plc.type == 2):
            for tmp in base.placelist:
                if (tmp.type == 0 and tmp.owner == self.plc.owner and tmp.door == 0):
                    tmp.door = 1
            return
        print('Invalid action!')

    def CloseDoor(self):
        if (self.plc.type == 0 and self.plc.door == 1):
            self.plc.door = 0
            return
        if (self.plc.type == 2):
            for tmp in base.placelist:
                if (tmp.type == 0 and tmp.owner == self.plc.owner and tmp.door == 1):
                    tmp.door = 0
            return 
        print('Invalid action!')

    def LockDoor(self):
        if (self.plc.type == 0 and self.plc.door == 0):
            self.plc.door = 2
            return
        print('Invalid action!')

    def UnlockDoor(self):
        if (self.plc.type == 2):
            for tmp in base.placelist:
                if (tmp.type == 0 and tmp.owner == self.plc.owner and tmp.door == 2):
                    tmp.door = 0
            return
        print('Invalid action!')

    def InstallWindow(self):
        if (self.plc.type == 0 and self.plc.window == 0):
            self.plc.window = 1
            return
        print('Invalid action!')

    def ShotWindow(self):
        if (self.plc.type == 2 or self.plc.type == 6):
            for tmp in base.placelist:
                if (tmp.type == 0 and tmp.owner == self.plc.owner and tmp.window == 1):
                    tmp.window = 0
            return 
        print('Invalid action!')

    def OpenCellarDoor(self):
        if (self.plc.type == 1 and self.plc.door == 0):
            self.plc.door = 1
            return
        if (self.plc.type == 0):
            for tmp in base.placelist:
                if (tmp.type == 1 and tmp.owner == self.plc.owner and tmp.door == 0):
                    tmp.door = 1
            return
        print('Invalid action!')

    def CloseCellarDoor(self):
        if (self.plc.type == 1 and self.plc.door == 1):
            self.plc.door = 0
            return
        if (self.plc.type == 0):
            for tmp in base.placelist:
                if (tmp.type == 1 and tmp.owner == self.plc.owner and tmp.door == 1):
                    tmp.door = 0
            return
        print('Invalid action!')

    def LockCellarDoor(self):
        if (self.plc.type == 1 and self.plc.door == 0):
            self.plc.door = 2
            return
        if (self.plc.type == 0):
            for tmp in base.placelist:
                if (tmp.type == 1 and tmp.owner == self.plc.owner and tmp.door == 0):
                    tmp.door = 2
            return
        print('Invalid action!')

    def UnlockCellarDoor(self):
        if (self.plc.type == 1 and self.plc.door == 2):
            self.plc.door = 0
            return
        if (self.plc.type == 0):
            for tmp in base.placelist:
                if (tmp.type == 1 and tmp.owner == self.plc.owner and tmp.door == 2):
                    tmp.door = 0
            return
        print('Invalid action!')

    def BuyGun(self):
        if (self.plc.type == 3 and not self.plc.broken or self.plc.type == 4):
            self.gun += 1
            return
        print('Invalid action!')

    def BuyKnife(self):
        if (self.plc.type == 3 and not self.plc.broken or self.plc.type == 4):
            self.knife += 1
            return
        print('Invalid action!')

    def BuyBiscuit(self):
        if (self.plc.type == 3 and not self.plc.broken or self.plc.type == 4):
            self.biscuit += 1
            return
        print('Invalid action!')

if __name__ == '__main__':
    pass
