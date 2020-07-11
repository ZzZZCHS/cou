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

def PrintPlaceInfo():
    N = base.playerNum
    for i in range(0, base.MarketNum):
        base.marketlist[i].PrintInfo()
    print('---------------------------------------------------------')
    for i in range(0, N):
        base.homelist[i].PrintInfo()
    print('---------------------------------------------------------')
    for i in range(0, N):
        base.cellarlist[i].PrintInfo()
    print('---------------------------------------------------------')

def PrintPlayerInfo():
    N = base.playerNum
    for i in range(0, N):
        base.playerlist[i].PrintInfo()
    print('---------------------------------------------------------')
    
