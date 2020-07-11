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

import Print
import Game
import base

import random
import math


def main():

    #建立商店
    base.marketList.append(Market('shop'))
    base.marketList.append(Market('supermarket'))
    base.marketList.append(Market('retail department'))
    base.marketList.append(Market('shopping mall'))
    base.bmarketList.append(BlackMarket())

    #建立玩家以及与玩家有关的地点
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

    #开启循环
    running = True
    Turn = 0
    while running:
        Turn += 1
        base.RoundActionStep = 0
        for i in range(0, base.playerNum):
            tempDouble = random.random()*2
            tempInt = math.floor(tempDouble)
            base.playerDiceList[i] = tempInt
            if (tempInt == 0 and base.playerList[i].hp > 0):
                base.RoundActionStep += 1
        if (base.RoundActionStep == 0 or base.RoundActionStep == base.alivePlayerNum):
            Turn -= 1
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
            nowID = base.playerActionOrder[i]
            nowPlayer = base.playerList[nowID]
            if (nowPlayer.hp <= 0 or base.playerDiceList[nowID] == 0):
                continue
            #base.playerActionOrder[i]是当前玩家的ID
            #base.RoundActionStep是当前行动力
            
            for step in range(0, base.RoundActionStep):
                Print.PrintInfo(Turn)
                print('Player%d: %s, it\'s your turn.' % (nowID + 1, base.playerList[nowID].name))
                print('You have %d step(s) left.' % (base.RoundActionStep - step))
                Game.GameDecision(nowID)
                CommandIn = int(input('Your option:'))
                Game.GameDecision(nowID, CommandIn)
                base.alivePlayerNum = Game.CountAlive()
        
        if (base.alivePlayerNum == 1):
            for plr in base.playerList:
                if (plr.hp > 0):
                    print('Winner: ', end = '')
                    plr.PrintName()
                    input()
            break

if __name__ == '__main__':
    main()
