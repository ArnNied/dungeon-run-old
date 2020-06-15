from Functions.functions import open_data, rng

class Apparel(object):
    def __init__(self, data=''):
        if not data:
            data = open_data('Apparel/apparel.json')['cloth']

        self.name = data['name']
        self.stat = data['stat']
        self.drop = data['drop']

    def damage_reduction(self, player):
        return (100 - self.display_damage_reduction(player)) / 100

    def display_damage_reduction(self, player):
        return player.str*4

    def parry_rate(self, player):
        return player.misc*7

    def item_drop(self):
        return rng() <= self.drop

class Armor(Apparel):
    def __init__(self, armor):
        data = open_data('Apparel/apparel.json')['armor'][armor]
        super().__init__(data)

    def display_damage_reduction(self, player):
        return self.stat + player.str*4

class Shield(Apparel):
    def __init__(self, shield):
        data = open_data('Apparel/apparel.json')['shield'][shield]
        super().__init__(data)
    
    def parry_rate(self, player):
        return self.stat + player.misc*7
