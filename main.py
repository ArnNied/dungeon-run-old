# from Mechanics import *
from os import system
from time import time
from Player.Player import Player
from Rooms import Rooms
from Mechanics.Mechanics import PlayerDead 

if __name__ == '__main__':
    player = Player()
    try:
        while player.location:
            system('cls')
            player.location = getattr(Rooms, player.location)(player)
    except PlayerDead:
        Rooms.death(player)