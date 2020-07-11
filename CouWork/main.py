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
    """
    base.placelist.append(Market('shop'))
    base.playerlist.append(Player('hhf', base.placelist[0]))
    player1 = base.playerlist[0]
    base.placelist[0].broken = 1
    player1.BuyKnife()
    print(player1.knife)
    """

    #建立基础地点
    base.placelist.append(Market('shop'))
    base.placeListNum+=1


    #建立玩家以及玩家出生点
    base.playerNum = int(input('玩家人数:'))
    for i in range(0,base.playerNum):
        playerName = str(input('请输入%d号玩家的姓名:' % (i+1)))
        base.placelist.append(Home((i+1)))
        base.placeListNum+=1
        base.playerlist.append(Player(playerName, i, base.placelist[base.placeListNum-1]))
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
        tempCount=0
        print('优先级设置完成')
        for i in range(0,base.playerNum):
            if (base.playerDiceList[base.playerActionOrder[i]] == 0):
                continue
            #行动由hhf来写
            #base.playerActionOrder[i]是当前玩家的ID
            #base.RoundActionStep是当前行动力
            print('当前行动力为%d'%base.RoundActionStep)
            CommandIn = str(input('输入玩家%d的指令' % base.playerActionOrder[i]))
        print('指令输入完成')
        
if __name__ == '__main__':
    main()