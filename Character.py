import cmd
import textwrap
import sys
import time
import random

screen_width =100

###player setup###
class Character:
    def __init__(self, name, hp, kt, level, points):
        #Stats
        self.name = name
        self.hp = self.hp
        self.kt = kt
        self.level = level
        self.points = points
        #Inventory
#myPlayer = player()


class Player(Character):
    def __init__(self, gender, _class, name, hp, kt, level, points):
        super().__init__(name, hp, kt, level, points)
        self._class = _class
        self.gender = gender
            

###title Screan ###

def title_selection():
    option = input("> ")

