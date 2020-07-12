import base

class Place(object):
    def __init__(self, type):
        self.type = type
    
class Home(Place):
    def __init__(self, owner, type = base.PlaceType.Home, door = base.Door.Closed, window = base.Window.Empty):
        super().__init__(type)
        self.owner = owner
        self.door = door
        self.window = window

    def PrintName(self):
        print(self.owner.name + '\'s home', end = '')

    def PrintInfo(self):
        self.PrintName()
        print(':')
        if (self.door == base.Door.Closed):
            print('    Door is closed.')
        elif (self.door == base.Door.Open):
            print('    Door is open.')
        else:
            print('    Door is locked.')
        if (self.window == base.Window.Empty):
            print('    Window is empty.')
        else:
            print('    Window is complete.')


class Cellar(Place):
    def __init__(self, owner, type = base.PlaceType.Cellar, door = base.Door.NotExist):
        super().__init__(type)
        self.owner = owner
        self.door = door
    
    def PrintName(self):
        print(self.owner.name + '\'s cellar', end = '')

    def PrintInfo(self):
        self.PrintName()
        print(':')
        if (self.door == base.Door.Closed):
            print('    Cellar door is closed.')
        elif (self.door == base.Door.Open):
            print('    Cellar door is open.')
        elif (self.door == base.Door.Locked):
            print('    Cellar door is locked.')
        else:
            print('    Cellar not exist.')

class OutsideHome(Place):
    def __init__(self, owner, type = base.PlaceType.OutsideHome):
        super().__init__(type)
        self.owner = owner

    def PrintName(self):
        print('outside ' + self.owner.name + '\'s home', end = '')

class Market(Place):
    def __init__(self, name, type = base.PlaceType.Market, broken = 0, owner = 'God'):
        super().__init__(type)
        self.name = name
        self.broken = broken
        self.owner = owner

    def PrintName(self):
        print(self.name, end = '')
    
    def PrintInfo(self):
        self.PrintName()
        if (self.broken):
            print(' is broken.')
        else:
            print(' is open.')

class BlackMarket(Place):
    def __init__(self, name = 'Black Market', type = base.PlaceType.BlackMarket, owner = 'God'):
        super().__init__(type)
        self.name = name
        self.owner = owner
    
    def PrintName(self):
        print(self.name, end = '')

class Car(Place):
    def __init__(self, owner, type = base.PlaceType.Car):
        self.owner = owner
        super().__init__(type)
        
    def PrintName(self):
        print(self.owner.name + '\'s car', end = '')

class OutsideCar(Place):
    def __init__(self, owner, type = base.PlaceType.OutsideCar):
        self.owner = owner
        super().__init__(type)

    def PrintName(self):
        print('outside ' + self.owner.name + '\'s car', end = '')
    
class AmbushPoint(Place):
    def __init__(self, belong, owner, type = base.PlaceType.AmbushPoint):
        super().__init__(type)
        self.belong = belong
        self.owner = owner

    def PrintName(self):
        print(self.owner.name + '\'s ambush point (belong to ', end = '')
        self.belong.PrintName()
        print(')', end = '')

def main():
    A = Home("hhf")
    A.PrintInfo()
    pass

if __name__ == '__main__':
    main()
