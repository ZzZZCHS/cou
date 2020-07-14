from Place import Place, Home, Cellar, OutsideHome, Market, BlackMarket, Car, OutsideCar, AmbushPoint
from Player import Player
import base

import os

def PrintPlaceInfo():
    N = base.playerNum
    for i in range(0, base.MarketNum):
        base.marketList[i].PrintInfo()
    print('------------------------------------------------------------')
    for i in range(0, N):
        base.homeList[i].PrintInfo()
    print('------------------------------------------------------------')
    for i in range(0, N):
        base.cellarList[i].PrintInfo()
    print('------------------------------------------------------------')

def PrintPlayerInfo():
    N = base.playerNum
    for i in range(0, N):
        if (base.playerList[i].hp > 0):
            base.playerList[i].PrintInfo()
    print('------------------------------------------------------------')
    
def PrintInfo(turn):
    #os.system('clear')
    print('############################################################')
    print('Turn %d' % turn)
    print('------------------------------------------------------------')
    PrintPlaceInfo()
    PrintPlayerInfo()
