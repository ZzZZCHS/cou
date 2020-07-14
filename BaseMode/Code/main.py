from Place import Place, Home, Cellar, OutsideHome, Market, BlackMarket, Car, OutsideCar, AmbushPoint
from Player import Player
import Print
import Game
import base
import Prepare

import random
import math

def main():

    #建立商店
    Prepare.PrepareShop()

    #建立玩家以及与玩家有关的地点
    Prepare.PreparePlayer()

    #开启循环
    Turn = 0
    while (True):
        Turn += 1

        #随机胜负，统计步数
        Prepare.PrepareStep()
        if (base.RoundActionStep == 0 or base.RoundActionStep == base.alivePlayerNum):
            Turn -= 1
            continue

        #回合优先级判断
        Prepare.PreparePriority()

        #更新玩家的回合信息
        Game.UpdatePlayerTurnInfo()

        #游戏进程
        for i in range(0, base.playerNum):
            #base.RoundActionStep是当前回合行动力
            nowID = base.playerActionOrder[i]
            nowPlayer = base.playerList[nowID]
            if (nowPlayer.hp <= 0 or base.playerDiceList[nowID] == 0):
                continue
            
            for step in range(0, base.RoundActionStep):
                Print.PrintInfo(Turn)
                print('Player%d: %s, it\'s your turn.' % (nowID + 1, base.playerList[nowID].name))
                print('You have %d step(s) left.' % (base.RoundActionStep - step))
                NothingID = Game.GameDecision(nowPlayer)
                CommandIn = int(input('Your option:'))
                if (CommandIn == NothingID):
                    break
                Game.GameDecision(nowPlayer, CommandIn)
                base.alivePlayerNum = Game.CountAlive()
                base.playerList[i].leftstep -= 1
        
        #游戏结束判断
        if (Game.GameEndCheck()):
            break

if __name__ == '__main__':
    main()
