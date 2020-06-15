
from Functions.functions import rng, open_data
from random import randint

class Weapon(object):
    def __init__(self, data=''):
        if not data:
            data = open_data('Weapon/weapons.json')['fist']
        
        self.name = data['name']
        self.atk = data['atk']
        self.hit = data['hit']
        self.crit = data['crit']
        self.drop = data['drop']

    def display_attack(self, player):
        return f"{min(self.atk) + player.str*2} - {max(self.atk) + player.str*2}"

    def attack(self, player):
        return randint(min(self.atk), max(self.atk)) + player.str*2

    def hit_rate(self, player):
        return self.hit + player.agi*2

    def crit_rate(self, player):
        return self.crit + player.misc*2

    def item_drop(self):
        return rng() <= self.drop

class Sword(Weapon):
    def __init__(self, weapon):
        data = open_data('Weapon/weapons.json')['sword'][weapon]
        super().__init__(data)

    def display_attack(self, player):
        return f"{min(self.atk) + player.str*3} - {max(self.atk) + player.str*3}"
    def attack(self, player):
        return randint(min(self.atk), max(self.atk)) + player.str*3

    def hit_rate(self, player):
        return self.hit + player.agi*3

    def crit_rate(self, player):
        return self.crit + player.misc*2

class Rapier(Weapon):
    def __init__(self, weapon):
        data = open_data('Weapon/weapons.json')['rapier'][weapon]
        super().__init__(data)

    def display_attack(self, player):
        return f"{min(self.atk) + player.str*2} - {max(self.atk) + player.str*2}"

    def attack(self, player):
        return randint(min(self.atk), max(self.atk)) + player.str*2

    def hit_rate(self, player):
        return self.hit + player.agi*4
        
    def crit_rate(self, player):
        return self.crit + player.misc*3

class Axe(Weapon):
    def __init__(self, weapon):
        data = open_data('Weapon/weapons.json')['axe'][weapon]
        super().__init__(data)

    def display_attack(self, player):
        return f"{min(self.atk) + player.str*4} - {max(self.atk) + player.str*4}"

    def attack(self, player):
        return randint(min(self.atk), max(self.atk)) + player.str*4

    def hit_rate(self, player):
        return self.hit + player.agi*2
        
    def crit_rate(self, player):
        return self.crit + player.misc*1

