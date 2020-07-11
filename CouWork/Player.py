from Place import Home
from Place import OutsideHome
from Place import Car

import base

MAX_HP = 3

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

    def __init__(self, name, pid, plc, hp = MAX_HP, knife = 0, 
                 biscuit = 0, gun = 0, cardone = 0, aim = -1):
        """ pid       the id of the player           """
        """ cardone   whether finish the car driving """
        """ vislist   the visibility of each player  """
        """ aim       -1: no aim target   0 ~ playernum-1: the aim player id """
        super().__init__(name, plc)
        self.pid = pid
        self.hp = hp
        self.knife = knife
        self.biscuit = biscuit
        self.gun = gun
        self.cardone = cardone
        self.aim = aim
        self.vislist = [1] * base.playerNum

    def PrintInfo(self):
        print('Player%d: %s' % (self.pid, self.name))
        print('    place: ', end = '')
        self.plc.PrintName()
        print('    hp:%d  knife:%d  gun:%d  biscuit:%d  cardone:%d' % (self.hp, self.knife, self.gun, self.biscuit, self.cardone))
        if (self.aim == -1):
            print('    no aim target')
        else:
            print('    aim at Player%d: %s' % (self.aim.pid, self.aim.name))

    def MoveTo(self, plc):
        self.plc = plc

    def OpenDoor(self):
        if (self.plc.type == 0 and self.plc.door == 0): 
            self.plc.door = 1
            return
        if (self.plc.type == 2):
            for tmp in base.homelist:
                if (tmp.owner == self.plc.owner and tmp.door == 0):
                    tmp.door = 1
                    return
        print('Invalid action!')

    def CloseDoor(self):
        if (self.plc.type == 0 and self.plc.door == 1):
            self.plc.door = 0
            return
        if (self.plc.type == 2):
            for tmp in base.homelist:
                if (tmp.owner == self.plc.owner and tmp.door == 1):
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
            for tmp in base.homelist:
                if (tmp.owner == self.plc.owner and tmp.door == 2):
                    tmp.door = 0
                    return
        print('Invalid action!')

    def InstallWindow(self):
        if (self.plc.type == 0 and self.plc.window == 0):
            self.plc.window = 1
            return
        print('Invalid action!')

    def ShotWindow(self):
        if (self.gun > 0 and (self.plc.type == 2 or self.plc.type == 6)):
            for tmp in base.homelist:
                if (tmp.owner == self.plc.owner and tmp.window == 1):
                    tmp.window = 0
                    return 
        print('Invalid action!')

    def DigCellar(self):
        if (self.plc.type == 0):
            for tmp in base.cellarlist:
                if (tmp.owner == self.plc.owner and tmp.door == 3):
                    tmp.door = 1
                    return
        print('Invalid action!')

    def OpenCellarDoor(self):
        if (self.plc.type == 1 and self.plc.door == 0):
            self.plc.door = 1
            return
        if (self.plc.type == 0):
            for tmp in base.cellarlist:
                if (tmp.owner == self.plc.owner and tmp.door == 0):
                    tmp.door = 1
                    return
        print('Invalid action!')

    def CloseCellarDoor(self):
        if (self.plc.type == 1 and self.plc.door == 1):
            self.plc.door = 0
            return
        if (self.plc.type == 0):
            for tmp in base.cellarlist:
                if (tmp.owner == self.plc.owner and tmp.door == 1):
                    tmp.door = 0
                    return
        print('Invalid action!')

    def LockCellarDoor(self):
        if (self.plc.type == 1 and self.plc.door == 0):
            self.plc.door = 2
            return
        if (self.plc.type == 0):
            for tmp in base.cellarlist:
                if (tmp.owner == self.plc.owner and tmp.door == 0):
                    tmp.door = 2
                    return
        print('Invalid action!')

    def UnlockCellarDoor(self):
        if (self.plc.type == 1 and self.plc.door == 2):
            self.plc.door = 0
            return
        if (self.plc.type == 0):
            for tmp in base.cellarlist:
                if (tmp.owner == self.plc.owner and tmp.door == 2):
                    tmp.door = 0
                    return
        print('Invalid action!')

    def PushIntoCellar(self, target):
        if (self.plc.type == 0 and target.plc.type == 0 and self.plc.owner == target.plc.owner):
            for tmp in base.cellarlist:
                if (tmp.owner == self.plc.owner and tmp.door == 1):
                    target.plc = base.cellarlist[base.cellarlist.index(tmp)]
                    return
        print('Invalid action!')

    def PullOutCellar(self, target):
        if (self.plc.type == 0 and target.plc.type == 1 and self.plc.owner == target.plc.owner and target.door == 1):
            target.plc = self.plc
            return
        print('Invalid action!')

    def GetOnCar(self):
        car = base.carlist[self.pid - 1]
        if (self.cardone == 0):
            if (self.plc.type == 2 or self.plc.type == 6):
                self.plc = car
                return
            if (self.plc.type == 0 and self.plc.door == 1):
                self.plc = car
                return
        print('Invalid action!')

    def PullOffCar(self, target):
        if (target.plc.type == 5 and self.plc.type == 6 and self.plc.owner == target.name):
            target.plc = base.outcarlist[target.pid - 1]
            return
        print('Invalid action!')

    def PushIntoHome(self, target):
        if (target.plc.type == 2 and self.plc.type == 2 and self.plc.owner == target.plc.owner):
            for tmp in base.homelist:
                if (tmp.owner == self.plc.owner and tmp.door == 1):
                    target.plc = base.homelist[base.homelist.index(tmp)]
                    self.plc = target.plc
                    return
        if (target.plc.type == 6 and self.plc.type == 6 and self.plc.owner == target.plc.owner):
            for tmp in base.homelist:
                if (tmp.owner == self.plc.owner and tmp.door == 1):
                    target.plc = base.homelist[base.homelist.index(tmp)]
                    self.plc = target.plc
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

    def EatBiscuit(self):
        if (self.biscuit > 0):
            self.biscuit -= 1
            self.hp += 1
            if (self.hp > MAX_HP): self.hp = MAX_HP
            return
        print('Invalid action!')

    def BrokeMarket(self):
        if (self.plc.type == 3 and not self.plc.broken):
            self.plc.broken = 1
            return
        print('Invalid action!')

    def Stab(self, target):
        if (self.plc == target.plc and self.knife > 0):
            target.hp -= 1
            return 
        print('Invalid action!')

    def Shot(self, target):
        if (self.gun == 0):
            print('Invalid action!')
            return
        if (self.aim == target.pid):
            target.hp -= 1
            return
        print('Invalid action!')
    
    def Search(self, target):
        if (target.plc.type != 7 or self.gun == 0):
            print('Invalid action!')
            return
        if (target.plc.belong == self.plc):
            self.vislist[target.pid - 1] = 1
            return
        print('Invalid action!')
    
    def AimAt(self, target):
        if (self.gun == 0 or self.vislist[target.pid - 1] == 0):
            print('Invalid action!')
            return
        if (target.plc.type == 7 and target.plc.belong == self.plc):
            self.aim = target.pid
            return
        if (self.plc == target.plc):
            self.aim = target.pid
            return
        if (self.plc.type == 0 and (target.plc.type == 2 or target.plc.type == 6) and self.plc.owner == target.plc.owner):
            self.aim = target.pid
            return
        if (self.plc.type == 2 and (target.plc.type == 0 or target.plc.type == 6) and self.plc.owner == target.plc.owner):
            self.aim = target.pid
            return
        if (self.plc.type == 6 and (target.plc.type == 2 or target.plc.type == 0) and self.plc.owner == target.plc.owner):
            self.aim = target.pid
            return
        print('Invalid action!')

    def Ambush(self, targetplc):
        if (Move(self, targetplc)):
            newAmbushPoint = base.ambushlist[self.pid - 1]
            newAmbushPoint.belong = targetplc
            self.plc = newAmbushPoint
            return 
        print('Invalid action!')

    def NewAmbush(self):
        for tmp in base.playerlist:
            if (tmp.plc == self.plc):
                oldAmbushPoint = base.ambushlist[tmp.pid - 1]
                oldAmbushPoint.belong = self.plc.belong
                for tt in base.playerlist:
                    if (tt.plc == self.plc):
                        tt.plc = oldAmbushPoint
                break

def Move(plr, B):
    A = plr.plc
    if (A == B): return True
    if (B.type == 5): return False
    if (B.type == 6 and B.owner.plc.type != 5): return False
    if (A.type == 0):
        if (B.type == 1 and B.door == 1 and B.owner == A.owner): return True
        if (A.door == 1 and plr.cardone == 1):
            if (B.type > 1 or B.type == 0 and B.door == 1): return True
        return False
    if (A.type == 1):
        if (B.type == 0 and B.owner == A.owner and A.door == 1): return True
        return False
    if (A.type == 2 or A.type == 6):
        if (B.type == 0 and B.door == 1):
            if (B.owner == A.owner or plr.cardone == 1): return True
        if (B.owner == A.owner and (B.type == 2 or B.type == 6)): return True
        if (B.type > 1 and plr.cardone): return True
        return False
    if (A.type >= 3):
        if (B.type == 0 and B.door == 1): return True
        if (B.type > 1): return True
        return False
    return False

if __name__ == '__main__':
    pass
