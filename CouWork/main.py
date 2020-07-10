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

def main():
    placelist = []
    playerlist = []
    placelist.append(Market('shop'))
    playerlist.append(Player('hhf', placelist[0]))
    player1 = playerlist[0]
    placelist[0].broken = 1
    player1.BuyKnife()
    print(player1.knife)

if __name__ == '__main__':
    main()
