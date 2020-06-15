
from abc import ABC, abstractmethod
from Functions.functions import open_data, rng
from math import floor

class Potion(ABC):
    def __init__(self, data):
        self.name = data['name']
        self.stat = data['stat']
        self.count = 1
        self.limit = data['limit']
        self.drop = data['drop']

    @abstractmethod
    def use(self, player):
        pass

    @abstractmethod
    def check_limit(self, player, perLevel):
        return self.limit + floor(player.level/perLevel)

    @abstractmethod
    def item_drop(self):
        return rng() <= self.drop

class LesserHealingPotion(Potion):
    def __init__(self):
        data = open_data('Potion/potions.json')['healing']['lesser']
        super().__init__(data)

    def use(self, player):
        print(f"{self.name}: Healed for {self.stat + player.misc*3}")
        player.hp += self.stat + player.misc*3
        self.count -= 1

    def check_limit(self, player):
        return super().check_limit(player, 3)

    def item_drop(self):
        return super().item_drop()

class HealingPotion(Potion):
    def __init__(self):
        data = open_data('Potion/potions.json')['healing']['normal']
        super().__init__(data)

    def use(self, player):
        print(f"{self.name}: Healed for {self.stat + player.misc*4}")
        player.hp += self.stat + player.misc*4
        self.count -= 1
    
    def check_limit(self, player):
        return super().check_limit(player, 4)

    def item_drop(self):
        return super().item_drop()
