from Place import Home
from Place import OutsideHome
from Place import Car

import base

MAX_HP = 3

class Person(object):
    """人物"""

    def __init__(self, name, plc):
        self.name = name
        self.plc = plc


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

    def PrintName(self):
        print('Player%d: %s' % (self.pid + 1, self.name), end = '')

    def PrintInfo(self):
        print('Player%d: %s' % (self.pid + 1, self.name))
        print('    place: ', end = '')
        self.plc.PrintName()
        print()
        print('    hp:%d  knife:%d  gun:%d  biscuit:%d  cardone:%d' % (self.hp, self.knife, self.gun, self.biscuit, self.cardone))
        if (self.aim == -1):
            print('    no aim target')
        else:
            print('    aim at Player%d: %s' % (self.aim + 1, base.playerList[self.aim].name))

    def OpenDoor(self, do = 0):
        if (self.plc.type == 0 and self.plc.door == 0): 
            if (do):
                self.plc.door = 1
            return True
        if (self.plc.type == 2):
            for tmp in base.homeList:
                if (tmp.owner == self.plc.owner and tmp.door == 0):
                    if (do):
                        tmp.door = 1
                    return True
        #print('Invalid action!')
        return False

    def CloseDoor(self, do = 0):
        if (self.plc.type == 0 and self.plc.door == 1):
            if (do):
                self.plc.door = 0
            return True
        if (self.plc.type == 2):
            for tmp in base.homeList:
                if (tmp.owner == self.plc.owner and tmp.door == 1):
                    if (do):
                        tmp.door = 0
                    return True
        #print('Invalid action!')
        return False

    def LockDoor(self, do = 0):
        if (self.plc.type == 0 and self.plc.door == 0):
            if (do):
                self.plc.door = 2
            return True
        #print('Invalid action!')
        return False

    def UnlockDoor(self, do = 0):
        if (self.plc.type == 2):
            for tmp in base.homeList:
                if (tmp.owner == self.plc.owner and tmp.door == 2):
                    if (do):
                        tmp.door = 0
                    return True
        if (self.plc.type == 1 and self.plc.door == 2):
            if (do):
                self.plc.door = 0
            return True
        #print('Invalid action!')
        return False

    def InstallWindow(self, do = 0):
        if (self.plc.type == 0 and self.plc.window == 0):
            if (do):
                self.plc.window = 1
            return True
        #print('Invalid action!')
        return False

    def ShotWindow(self, do = 0):
        if (self.gun > 0 and (self.plc.type == 2 or self.plc.type == 6)):
            for tmp in base.homeList:
                if (tmp.owner == self.plc.owner and tmp.window == 1):
                    if (do):
                        tmp.window = 0
                    return True
        #print('Invalid action!')
        return False

    def DigCellar(self, do = 0):
        if (self.plc.type == 0):
            for tmp in base.cellarList:
                if (tmp.owner == self.plc.owner and tmp.door == 3):
                    if (do):
                        tmp.door = 1
                    return True
        #print('Invalid action!')
        return False

    def OpenCellarDoor(self, do = 0):
        if (self.plc.type == 1 and self.plc.door == 0):
            if (do):
                self.plc.door = 1
            return True
        if (self.plc.type == 0):
            for tmp in base.cellarList:
                if (tmp.owner == self.plc.owner and tmp.door == 0):
                    if (do):
                        tmp.door = 1
                    return True
        #print('Invalid action!')
        return False

    def CloseCellarDoor(self, do = 0):
        if (self.plc.type == 1 and self.plc.door == 1):
            if (do):
                self.plc.door = 0
            return True
        if (self.plc.type == 0):
            for tmp in base.cellarList:
                if (tmp.owner == self.plc.owner and tmp.door == 1):
                    if (do):
                        tmp.door = 0
                    return True
        #print('Invalid action!')
        return False

    def LockCellarDoor(self, do = 0):
        if (self.plc.type == 1 and self.plc.door == 0):
            if (do):
                self.plc.door = 2
            return True
        if (self.plc.type == 0):
            for tmp in base.cellarList:
                if (tmp.owner == self.plc.owner and tmp.door == 0):
                    if (do):
                        tmp.door = 2
                    return True
        #print('Invalid action!')
        return False

    def UnlockCellarDoor(self, do = 0):
        if (self.plc.type == 1 and self.plc.door == 2):
            if (do):
                self.plc.door = 0
            return True
        if (self.plc.type == 0):
            for tmp in base.cellarList:
                if (tmp.owner == self.plc.owner and tmp.door == 2):
                    if (do):
                        tmp.door = 0
                    return True
        #print('Invalid action!')
        return False

    def PushIntoCellar(self, target, do = 0):
        if (self == target):
            return False
        if (self.plc.type == 0 and target.plc.type == 0 and self.plc.owner == target.plc.owner):
            for tmp in base.cellarList:
                if (tmp.owner == self.plc.owner and tmp.door == 1):
                    flag = 0
                    for plr in base.playerList:
                        if (plr.plc == tmp): flag += 1
                    if (flag == 0):
                        if (do):
                            target.plc = base.cellarList[base.cellarList.index(tmp)]
                    return True
        #print('Invalid action!')
        return False

    def PullOutCellar(self, target, do = 0):
        if (self == target):
            return False
        if (self.plc.type == 0 and target.plc.type == 1 and self.plc.owner == target.plc.owner and target.plc.door == 1):
            if (do):
                target.plc = self.plc
            return True
        #print('Invalid action!')
        return False

    def GetOnCar(self, do = 0):
        car = base.carList[self.pid]
        if (self.cardone == 0):
            if (self.plc.type == 2 or self.plc.type == 6):
                if (do):
                    self.plc = car
                return True
            if (self.plc.type == 0 and self.plc.door == 1):
                if (do):
                    self.plc = car
                return True
        #print('Invalid action!')
        return False

    def PullOffCar(self, target, do = 0):
        if (self == target):
            return False
        if (target.plc.type == 5 and self.plc.type == 6 and self.plc.owner == target):
            if (do):
                target.plc = base.outcarList[target.pid]
            return True
        #print('Invalid action!')
        return False

    def PushIntoHome(self, target, do = 0):
        if (self == target):
            return False
        if (target.plc.type == 2 and self.plc.type == 2 and self.plc.owner == target.plc.owner):
            for tmp in base.homeList:
                if (tmp.owner == self.plc.owner and tmp.door == 1):
                    if (do):
                        target.plc = base.homeList[base.homeList.index(tmp)]
                        self.plc = target.plc
                    return True
        if (target.plc.type == 6 and self.plc.type == 6 and self.plc.owner == target.plc.owner):
            for tmp in base.homeList:
                if (tmp.owner == self.plc.owner and tmp.door == 1):
                    if (do):
                        target.plc = base.homeList[base.homeList.index(tmp)]
                        self.plc = target.plc
                    return True
        #print('Invalid action!')
        return False

    def BuyGun(self, do = 0):
        if (self.plc.type == 3 and not self.plc.broken or self.plc.type == 4):
            if (do):
                self.gun += 1
            return True
        #print('Invalid action!')
        return False

    def BuyKnife(self, do = 0):
        if (self.plc.type == 3 and not self.plc.broken or self.plc.type == 4):
            if (do):
                self.knife += 1
            return True
        #print('Invalid action!')
        return False

    def BuyBiscuit(self, do = 0):
        if (self.plc.type == 3 and not self.plc.broken):
            if (do):
                self.biscuit += 1
            return True
        #print('Invalid action!')
        return False

    def EatBiscuit(self, do = 0):
        if (self.biscuit > 0):
            if (do):
                self.biscuit -= 1
                self.hp += 1
                if (self.hp > MAX_HP): self.hp = MAX_HP
            return True
        #print('Invalid action!')
        return False

    def BrokeMarket(self, do = 0):
        if (self.plc.type == 3 and not self.plc.broken):
            if (do):
                self.plc.broken = 1
            return True
        #print('Invalid action!')
        return False

    def Stab(self, target, do = 0):
        if (self == target):
            return False
        if (self.plc == target.plc and self.knife > 0):
            if (do):
                target.hp -= 1
                if (target.hp <= 0):
                    base.alivePlayerNum -= 1
            return True
        #print('Invalid action!')
        return False

    def Shot(self, target, do = 0):
        if (self == target):
            return False
        if (self.gun == 0):
            #print('Invalid action!')
            return False
        if (self.aim == target.pid):
            if (do):
                target.hp -= 1
                if (target.hp <= 0):
                    base.alivePlayerNum -= 1
            return True
        #print('Invalid action!')
        return False
    
    def Search(self, target, do = 0):
        if (self == target):
            return False
        if (target.plc.type != 7 or self.gun == 0):
            #print('Invalid action!')
            return False
        if (target.plc.belong == self.plc):
            if (do):
                self.vislist[target.pid] = 1
            return True
        #print('Invalid action!')
        return False
    
    def AimAt(self, target, do = 0):
        if (self == target):
            return False
        if (self.gun == 0 or self.vislist[target.pid] == 0):
            #print('Invalid action!')
            return False
        if (self.plc.type == 7 and target.plc == self.plc.belong):
            if (do):
                self.aim = target.pid
            return True
        if (target.plc.type == 7 and target.plc.belong == self.plc):
            if (do):
                self.aim = target.pid
            return True
        if (self.plc == target.plc):
            if (do):
                self.aim = target.pid
            return True
        if (self.plc.type == 0 and (target.plc.type == 2 or target.plc.type == 6) and self.plc.owner == target.plc.owner):
            if (do):
                self.aim = target.pid
            return True
        if (self.plc.type == 2 and (target.plc.type == 0 or target.plc.type == 6) and self.plc.owner == target.plc.owner):
            if (do):
                self.aim = target.pid
            return True
        if (self.plc.type == 6 and (target.plc.type == 2 or target.plc.type == 0) and self.plc.owner == target.plc.owner):
            if (do):
                self.aim = target.pid
            return True
        #print('Invalid action!')
        return False

    def Ambush(self, targetplc, do = 0):
        if (self.plc.type == 5):
            return False
        if (targetplc.type <= 1):
            return False
        if (self.Move(targetplc) or self.plc == targetplc):
            if (do):
                newAmbushPoint = base.ambushList[self.pid]
                newAmbushPoint.belong = targetplc
                self.plc = newAmbushPoint
                for plr in base.playerList:
                    plr.vislist[self.pid] = 0
            return True
        #print('Invalid action!')
        return False

    def NewAmbush(self, do = 0):
        if (self.plc.type != 7): return False
        if (not do): return True
        for tmp in base.playerList:
            if (tmp.plc == self.plc):
                oldAmbushPoint = base.ambushList[tmp.pid - 1]
                oldAmbushPoint.belong = self.plc.belong
                for tt in base.playerList:
                    if (tt.plc == self.plc):
                        tt.plc = oldAmbushPoint
                for plr in base.playerList:
                    plr.vislist[self.pid] = 0
                break
    
    def MoveTo(self, plc):
        if (self.plc.type == 5):
            self.cardone = 1
        self.plc = plc
    
    def Move(self, B):
        A = self.plc
        if (A == B):
            return False
        if (B.type == 1):
            for plr in base.playerList:
                if (plr.plc == B):
                    return False
        if (B.type == 5):
            return False
        if (B.type == 6 and (B.owner.plc.type != 5 or B.owner == A.owner)):
            return False
        if (B.type == 7 and B.owner.plc != B):
            return False
        if (A.type == 0):
            if (B.type == 1 and B.door == 1 and B.owner == A.owner):
                return True
            if (A.door == 1 and self.cardone == 1):
                if (B.type > 1 or B.type == 0 and B.door == 1):
                    return True
            return False
        if (A.type == 1):
            if (B.type == 0 and B.owner == A.owner and A.door == 1):
                return True
            return False
        if (A.type == 2 or A.type == 6):
            if (B.type == 0 and B.door == 1):
                if (B.owner == A.owner or self.cardone == 1):
                    return True
            if ((B.type == 2 or B.type == 6) and B.owner == A.owner):
                return True
            if (B.type > 1 and self.cardone):
                return True
            return False
        if (A.type >= 3):
            if (B.type == 0 and B.door == 1):
                return True
            if (B.type > 1):
                return True
            return False
        return False

if __name__ == '__main__':
    pass
