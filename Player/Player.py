from os import system
from time import sleep
from importlib import import_module
from Functions.functions import open_data, rng, print_s1, print_s2
from Weapon.Weapon import Weapon
from Apparel.Apparel import Apparel

class Player(object):
    def __init__(self):
        self.str = 0
        self.agi = 0
        self.misc = 0

        self.level = 1
        self.exp = 0
        self.expLimit = 20

        self.hp = 200
        self.maxHp = 100

        self.weapon = Weapon()
        self.apparel = Apparel()

        self.potion = {}

        self.location = 'main_menu'
        self.score = 0

    def display_attack(self):
        return self.weapon.display_attack(self)

    def hit_rate(self):
        return self.weapon.hit_rate(self)

    def crit_rate(self):
        return self.weapon.crit_rate(self)

    def evade_rate(self):
        return self.agi*3

    def parry_rate(self):
        return self.apparel.parry_rate(self)

    def attack_check(self):
        if not rng() <= self.hit_rate():
            print("Miss!")
            return 0
        elif rng() <= self.crit_rate():
            print("Critical Hit!")
            return self.weapon.attack(self)*2
        else:
            print("Hit!")
            return self.weapon.attack(self)

    def evade_check(self):
        if rng() <= self.evade_rate():
            return True

    def parry_check(self):
        if rng() <= self.parry_rate():
            print("Parry Successful")
            return self.parry_rate()
        else:
            print("Parry Failed")

    def damage_reduction(self):
        return self.apparel.damage_reduction(self)

    def display_damage_reduction(self):
        return self.apparel.display_damage_reduction(self)

    def use_potion(self, potionKey):
        self.potion[potionKey].use(self)
            
    def change_weapon(self, weapon):
        print_s2(f"You took the {weapon.name}")
        self.weapon = weapon

    def change_apparel(self, apparel):
        print_s2(f"You took the {apparel.name}")
        self.apparel = apparel

    def add_potion(self, module, potionClass):
        item = getattr(import_module(module), potionClass)()
        print_s2(f"\nThe enemy dropped a(n) {item.name}")
        if not item.name in self.potion:
            self.potion[item.name] = item
        elif self.potion[item.name].count >= self.potion[item.name].check_limit(self):
            print_s2(f"{self.potion[item.name].name} is already maxed")
        else:
            self.potion[item.name].count += 1
        system('cls')

    def potion_check(self):
        potionKeys = list(self.potion.keys())

        for i in range(1, len(potionKeys)+1):
            current = self.potion[potionKeys[i-1]]
            if current.count == 0:
                del self.potion[potionKeys[i-1]]
