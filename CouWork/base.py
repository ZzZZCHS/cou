from enum import IntEnum, unique

@unique
class PlaceType(IntEnum):
    Home = 0
    Cellar = 1
    OutsideHome = 2
    Market = 3
    BlackMarket = 4
    Car = 5
    OutsideCar = 6
    AmbushPoint = 7

@unique
class Door(IntEnum):
    Closed = 0
    Open = 1
    Locked = 2
    NotExist = 3

@unique
class Window(IntEnum):
    Empty = 0
    Installed = 1


homeList = []
outhomeList = []
cellarList = []
marketList = []
bmarketList = []
carList = []
outcarList = []
ambushList = []

playerList = []
playerPriorityList = []  # 数字表示优先级
playerActionOrder = []  # 内存ID，表示行动的顺序
playerDiceList = []  # 0或1表示回合是否行动

MarketNum = 4
BMarketNum = 1

playerNum = 0
alivePlayerNum = 0
RoundActionStep = 0  # 回合行动力
