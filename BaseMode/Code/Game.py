from Place import Place, Home, Cellar, OutsideHome, Market, BlackMarket, Car, OutsideCar, AmbushPoint
from Player import Player
import base

def GameDecision(plr, do = 0):
    now = 0
    FLAG = 1
    if (plr.OpenDoor()):
        now += 1
        if (do == 0):
            print('%2d: open the door' % now)
        if (do == now):
            plr.OpenDoor(1)
    if (plr.GetOnCar()):
        now += 1
        if (do == 0):
            print('%2d: get on the car' % now)
        if (do == now):
            plr.GetOnCar(1)
    if (plr.CloseDoor()):
        now += 1
        if (do == 0):
            print('%2d: close the door' % now)
        if (do == now):
            plr.CloseDoor(1)
    if (plr.LockDoor()):
        now += 1
        if (do == 0):
            print('%2d: lock the door' % now)
        if (do == now):
            plr.LockDoor(1)
    if (plr.UnlockDoor()):
        now += 1
        if (do == 0):
            print('%2d: unlock the door' % now)
        if (do == now):
            plr.UnlockDoor(1)
    if (plr.InstallWindow()):
        now += 1
        if (do == 0):
            print('%2d: install the window' % now)
        if (do == now):
            plr.InstallWindow(1)
    if (plr.ShotWindow()):
        now += 1
        if (do == 0):
            print('%2d: shot the window' % now)
        if (do == now):
            plr.ShotWindow(1)
    if (plr.DigCellar()):
        now += 1
        if (do == 0):
            print('%2d: dig the cellar' % now)
        if (do == now):
            plr.DigCellar(1)
    if (plr.OpenCellarDoor()):
        now += 1
        if (do == 0):
            print('%2d: open the cellar door' % now)
        if (do == now):
            plr.OpenCellarDoor(1)
    if (plr.CloseCellarDoor()):
        now += 1
        if (do == 0):
            print('%2d: close the cellar door' % now)
        if (do == now):
            plr.CloseCellarDoor(1)
    if (plr.LockCellarDoor()):
        now += 1
        if (do == 0):
            print('%2d: lock the cellar door' % now)
        if (do == now):
            plr.LockCellarDoor(1)
    if (plr.UnlockCellarDoor()):
        now += 1
        if (do == 0):
            print('%2d: unlock the cellar door' % now)
        if (do == now):
            plr.UnlockCellarDoor(1)
    for target in base.playerList:
        if (plr.PushIntoCellar(target)):
            now += 1
            if (do == 0):
                print('%2d: push ' % now, end = '')
                target.PrintName()
                print(' into the cellar')
            if (do == now):
                plr.PushIntoCellar(target, 1)
    for target in base.playerList:
        if (plr.PullOutCellar(target)):
            now += 1
            if (do == 0):
                print('%2d: pull ' % now, end = '')
                target.PrintName()
                print(' out of the cellar')
            if (do == now):
                plr.PullOutCellar(target, 1)
    for target in base.playerList:
        if (plr.PullOffCar(target)):
            now += 1
            if (do == 0):
                print('%2d: pull ' % now, end = '')
                target.PrintName()
                print(' off the car')
            if (do == now):
                plr.PullOffCar(target, 1)
    for target in base.playerList:
        if (plr.PushIntoHome(target)):
            now += 1
            if (do == 0):
                print('%2d: push ' % now, end = '')
                target.PrintName()
                print(' into the home')
            if (do == now):
                plr.PushIntoHome(target, 1)
    if (plr.BuyGun()):
        now += 1
        if (do == 0):
            print('%2d: buy a gun' % now)
        if (do == now):
            plr.BuyGun(1)
    if (plr.BuyKnife()):
        now += 1
        if (do == 0):
            print('%2d: buy a knife' % now)
        if (do == now):
            plr.BuyKnife(1)
    if (plr.BuyBiscuit()):
        now += 1
        if (do == 0):
            print('%2d: buy a biscuit' % now)
        if (do == now):
            plr.BuyBiscuit(1)
    if (plr.EatBiscuit()):
        now += 1
        if (do == 0):
            print('%2d: eat a biscuit' % now)
        if (do == now):
            plr.EatBiscuit(1)
    if (plr.BrokeMarket()):
        now += 1
        if (do == 0):
            print('%2d: broke the %s' % (now, plr.plc.name))
        if (do == now):
            plr.BrokeMarket(1)
    for target in base.playerList:
        if (plr.Stab(target)):
            now += 1
            if (do == 0):
                print('%2d: stab ' % now, end = '')
                target.PrintName()
                print()
            if (do == now):
                plr.Stab(target, 1)
    for target in base.playerList:
        if (plr.Shot(target)):
            now += 1
            if (do == 0):
                print('%2d: shot ' % now, end='')
                target.PrintName()
                print()
            if (do == now):
                FLAG = 0
                plr.Shot(target, 1)
    for target in base.playerList:
        if (plr.Search(target)):
            now += 1
            if (do == 0):
                print('%2d: search for ' % now, end='')
                target.PrintName()
                print()
            if (do == now):
                plr.Search(target, 1)
    for target in base.playerList:
        if (plr.AimAt(target)):
            now += 1
            if (do == 0):
                print('%2d: aim at ' % now, end='')
                target.PrintName()
                print()
            if (do == now):
                FLAG = 0
                plr.AimAt(target, 1)
    for placeList in (base.homeList,base.outhomeList,base.carList,base.outcarList,
                      base.marketList,base.bmarketList,base.cellarList,base.ambushList):
        for targetplc in placeList:
            if (plr.Move(targetplc)):
                now += 1
                if (do == 0):
                    print('%2d: move to ' % now, end = '')
                    targetplc.PrintName()
                    print()
                if (do == now):
                    plr.MoveTo(targetplc)
    for placeList in (base.homeList, base.outhomeList, base.carList, base.outcarList,
                      base.marketList, base.bmarketList, base.cellarList, base.ambushList):
        for targetplc in placeList:
            if (plr.Ambush(targetplc)):
                now += 1
                if (do == 0):
                    print('%2d: ambush around ' % now, end='')
                    targetplc.PrintName()
                    print()
                if (do == now):
                    plr.Ambush(targetplc, 1)
    if (plr.NewAmbush()):
        now += 1
        if (do == 0):
            print('%2d: change a nearby place to ambush' % now)
        if (do == now):
            plr.NewAmbush(1)
    if (FLAG and do > 0):
        plr.aim = -1
    now += 1
    if (do == 0):
         print('%2d: do nothing' % now)
    return now

def CountAlive():
    num = 0
    for plr in base.playerList:
        if (plr.hp > 0):
            num += 1
    return num

def UpdatePlayerTurnInfo():
    for i in range(0, base.playerNum):
        if (base.playerDiceList[i] == 1):
            base.playerList[i].turnwinner = 1
            base.playerList[i].leftstep = base.RoundActionStep
        else:
            base.playerList[i].turnwinner = 0
            base.playerList[i].leftstep = 0

def GameEndCheck():
    if (base.alivePlayerNum == 1):
        for plr in base.playerList:
            if (plr.hp > 0):
                print('Winner: ', end='')
                plr.PrintName()
                input()
        return True
    return False
