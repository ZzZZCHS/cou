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

import base

import random
import math

def main():
    base.placelist.append(Market('shop'))
    base.playerlist.append(Player('hhf', base.placelist[0]))
    player1 = base.playerlist[0]
    base.placelist[0].broken = 1
    player1.BuyKnife()
    print(player1.knife)

    #建立基础地点
    base.placelist.append(Market('shop'))
    base.placeListNum+=1


    #建立玩家以及玩家出生点
    base.playerNum = int(input('玩家人数:'))
    for i in range(0,base.playerNum):
        playerName = str(input('请输入%d号玩家的姓名:' % (i+1)))
        base.placelist.append(Home((i+1)))
        base.placeListNum+=1
        base.playerlist.append(Player(playerName, base.placelist[base.placeListNum-1]))
        base.playerPriorityList.append(-1)
        base.playerDiceList.append(0)
        base.playerActionOrder.append(-1)

    #开启循环
    running = True
    while running:
        base.RoundActionStep=0
        for i in range(0,base.playerNum):
            tempDouble = random.random()*2
            tempInt = math.floor(tempDouble)
            base.playerDiceList[i]=tempInt
            if tempInt == 0:
                base.RoundActionStep+=1

        #回合优先级判断
        for i in range(0,base.playerNum):
            base.playerPriorityList[i] = -1
        tempCount=0
        while tempCount<base.playerNum:
            tempDouble = random.random()*base.playerNum
            tempInt = math.floor(tempDouble)
            if (base.playerPriorityList[tempInt] == -1):
                base.playerPriorityList[tempInt] = tempCount
                base.playerActionOrder[tempCount] = tempInt
                tempCount+=1
        
if __name__ == '__main__':
    main()
