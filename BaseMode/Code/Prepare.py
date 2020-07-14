from Place import Place, Home, Cellar, OutsideHome, Market, BlackMarket, Car, OutsideCar, AmbushPoint
from Player import Player
import base

import random
import math

def PrepareShop():
    base.marketList.append(Market('shop'))
    base.marketList.append(Market('supermarket'))
    base.marketList.append(Market('retail department'))
    base.marketList.append(Market('shopping mall'))
    base.bmarketList.append(BlackMarket())

def PreparePlayer():
    base.playerNum = int(input('Number of players:'))
    base.alivePlayerNum = base.playerNum
    for i in range(0, base.playerNum):
        playerName = str(input('Please input the Player%d\'s name:' % (i + 1)))

        base.playerList.append(Player(playerName, i, base.bmarketList[0]))
        nowPlayer = base.playerList[i]

        base.homeList.append(Home(nowPlayer))
        nowPlayer.plc = base.homeList[i]
        base.outhomeList.append(OutsideHome(nowPlayer))
        base.cellarList.append(Cellar(nowPlayer))
        base.carList.append(Car(nowPlayer))
        base.outcarList.append(OutsideCar(nowPlayer))
        base.ambushList.append(AmbushPoint(base.homeList[i], nowPlayer))

        base.playerPriorityList.append(-1)
        base.playerDiceList.append(0)
        base.playerActionOrder.append(-1)

def PrepareStep():
    base.RoundActionStep = 0
    for i in range(0, base.playerNum):
        tempDouble = random.random()*2
        tempInt = math.floor(tempDouble)
        base.playerDiceList[i] = tempInt
        if (tempInt == 0 and base.playerList[i].hp > 0):
            base.RoundActionStep += 1

def PreparePriority():
    for i in range(0, base.playerNum):
        base.playerPriorityList[i] = -1
    tempCount = 0
    while tempCount < base.playerNum:
        tempDouble = random.random()*base.playerNum
        tempInt = math.floor(tempDouble)
        if (base.playerPriorityList[tempInt] == -1):
            base.playerPriorityList[tempInt] = tempCount
            base.playerActionOrder[tempCount] = tempInt
            tempCount += 1
