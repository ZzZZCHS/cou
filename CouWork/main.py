from Place import Place
from Place import Home
from Place import Cellar
from Place import OutsideHome
from Place import Market
from Place import BlackMarket
from Place import Car
from Place import OutsideCar
from Place import AmbushPoint

from Player import Player

from Print import PrintPlaceInfo
from Print import PrintPlayerInfo

import base

import random
import math


def main():

    #建立商店
    base.marketlist.append(Market('shop'))
    base.marketlist.append(Market('supermarket'))
    base.marketlist.append(Market('retail department'))
    base.marketlist.append(Market('shopping mall'))
    base.bmarketlist.append(BlackMarket())

    #建立玩家以及与玩家有关的地点
    base.playerNum = int(input('Number of players:'))
    for i in range(0, base.playerNum):
        playerName = str(input('Please input the Player%d\'s name:' % (i + 1)))

        base.playerlist.append(Player(playerName, i, base.bmarketlist[0]))
        nowPlayer = base.playerlist[i]

        base.homelist.append(Home(nowPlayer))
        nowPlayer.plc = base.homelist[i]
        base.outhomelist.append(OutsideHome(nowPlayer))
        base.cellarlist.append(Cellar(nowPlayer))
        base.carlist.append(Car(nowPlayer))
        base.outcarlist.append(OutsideCar(nowPlayer))
        base.ambushlist.append(AmbushPoint(base.homelist[i], nowPlayer))

        base.playerPriorityList.append(-1)
        base.playerDiceList.append(0)
        base.playerActionOrder.append(-1)

    #开启循环
    running = True
    while running:
        base.RoundActionStep = 0
        for i in range(0, base.playerNum):
            tempDouble = random.random()*2
            tempInt = math.floor(tempDouble)
            base.playerDiceList[i] = tempInt
            if tempInt == 0:
                base.RoundActionStep += 1
        if (base.RoundActionStep == 0 or base.RoundActionStep == base.playerNum):
            continue

        #回合优先级判断
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

        for i in range(0, base.playerNum):
            if (base.playerDiceList[base.playerActionOrder[i]] == 0):
                continue
            PrintPlaceInfo()
            PrintPlayerInfo()
            #base.playerActionOrder[i]是当前玩家的ID
            #base.RoundActionStep是当前行动力
            
            nowPlayer = base.playerlist[base.playerActionOrder[i]]
            for step in range(0, base.RoundActionStep):
                pass
            
            print('当前行动力为%d' % base.RoundActionStep)
            CommandIn = str(input('输入玩家%d的指令' % base.playerActionOrder[i]))
        print('指令输入完成')


if __name__ == '__main__':
    main()
