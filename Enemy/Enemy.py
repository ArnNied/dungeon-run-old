
from random import randint
from Functions.functions import open_data, rng
 
class Enemy(object):
    def __init__(self, enemy):
        data = open_data('Enemy/enemies.json')[enemy]
        
        self.name = data['name']
        self.hp = randint(min(data['hp']), max(data['hp']))
        self.atk = data['atk']
        self.hit = data['hit']
        self.crit = data['crit']
        self.evade = data['evade']
        self.exp = data['exp']
        self.chance = randint(min(data['chance']), max(data['chance']))

    def encounter(self):
        return rng() <= self.chance
    
    def display_attack(self):
        return f"{min(self.atk)} - {max(self.atk)}"

    def hit_rate(self):
        return self.hit

    def crit_rate(self):
        return self.crit

    def evade_rate(self):
        return self.evade
    
    def attack_check(self):
        if not rng() <= self.hit_rate():
            print(f"{self.name}: Missed")
            return 0
        elif rng() <= self.crit_rate():
            print(f"{self.name}: Critical Hit")
            return randint(min(self.atk), max(self.atk))*2
        else:
            print(f"{self.name}: Hit")
            return randint(min(self.atk), max(self.atk))

    def evade_check(self):
        if rng() <= self.evade:
            return True

    def give_exp(self):
        return randint(min(self.exp), max(self.exp))
