class Player():
    def __init__(self):

        self.str = 0
        self.agi = 0
        self.misc = 0

        self.level = 1
        self.exp = 0
        self.expLimit = 20

        self.hp = 100
        self.maxHp = 100

        self.weapon = "punch"
        self.apparel = "none"

class Enemy():
    def __init__(self, name, hp, atk, hit, crit, evade, exp, chance):
        
        self.name = name
        self.datk = f"{min(atk)} - {max(atk)}"
        self.hp = hp
        self.atk = atk
        self.hit = hit
        self.crit = crit
        self.evade = evade
        self.exp = exp
        self.chance = chance

class Weapon():
    def __init__(self, name, atk, hit, crit, drop):
        
        self.name = name
        self.datk = f"{min(atk)} - {max(atk)}"
        self.atk = atk
        self.hit = hit
        self.crit = crit
        self.drop = drop


class Apparel():
    def __init__(self, name, stat, drop):

        self.name = name
        self.stat = stat
        self.drop = drop

class Potions():
    def __init__(self, stat, limit, drop):

        self.stat = stat
        self.limit = limit
        self.drop = drop
        self.count = 0

class Trigger():
    def __init__(self):
        self.start = False
        self.mini1 = False
        self.mini2 = False
        self.boss = False
        self.exitKey = False