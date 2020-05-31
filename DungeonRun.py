#########################################
#                                      #
#   Copyright 2019 Andrien Wiandyano   #
#                                      #
#########################################


from sys import exit
from random import randint, choice
from core import Player, Enemy, Weapon, Apparel, Potions, Trigger
import math
import time


#################################################################################################################
# Player
player = Player()

# Item Stats
items = {
    # Name, Attack, Hit Rate, Crit Rate, Drop Rate
    "punch": Weapon("Punch", range(2, 6), 75, 5, 100),

    "sword1": Weapon("Iron Sword", range(7, 13), 32, 4, 60),
    "sword2": Weapon("Steel Sword", range(14, 20), 42, 8, 50),
    "sword3": Weapon("Daedric Sword", range(22, 29), 52, 12, 40),

    "rapier1": Weapon("Iron Rapier", range(7, 10), 37, 3, 60),
    "rapier2": Weapon("Steel Rapier", range(12, 15), 50, 9, 50),
    "rapier3": Weapon("Daedric Rapier", range(17, 21), 63, 15, 40),

    "axe1": Weapon("Iron Axe", range(12, 33), 25, 6, 60),
    "axe2": Weapon("Steel Axe", range(18, 39), 30, 8, 50),
    "axe3": Weapon("Daedric Axe", range(24, 45), 35, 10, 40),

    # Name, Stats, Drop Rate
    "shield1": Apparel("Wooden Shield", 16, 50),
    "shield2": Apparel("Steel Shield", 21, 40),
    "shield3": Apparel("Daedric Shield", 26, 30),

    "armor1": Apparel("Iron Chainmail", 10, 50),
    "armor2": Apparel("Steel Plating", 15, 40),
    "armor3": Apparel("Daedric Armor", 20, 30),

    # Stats, Initial limit, Drop Rate 
    "potion1": Potions(30, 3, 70),
    "potion2": Potions(60, 1, 40)
}

# Enemy Stats
enemy = {
    # Name, HP, Attack, Hit Rate, Crit Rate, Evade Rate, EXP, Chance

    "slime1": Enemy("Blue Slime", range(10, 21), range(0, 1), 0, 0, 0, range(1, 3), range(5, 11)),

    # EASY
    "rat1": Enemy("Rat", range(10, 21), range(1, 4), 80, 3, 25, range(1, 6), range(70, 81)),
    "spider": Enemy("Giant Spider", range(30, 41), range(4, 7), 75, 5, 0, range(5, 9), range(10, 41)),
    "goblin": Enemy("Goblin", range(20, 31), range(2, 9), 70, 15, 5, range(7, 11), range(50, 71)),

    #INTERMEDIATE
    "slime2": Enemy("Red Slime", range(100, 121), range(4, 8), 80, 55, 10, range(10, 21), range(40, 61)),
    "slime3": Enemy("Green Slime", range(50, 81), range(10, 17), 80, 5, 10, range(5, 36), range(30, 51)),
    "skeleton": Enemy("Skeleton", range(80, 101), range(7, 11), 70, 2, 7, range(15, 21), range(40, 61)),

    # HARD
    "zombie": Enemy("Zombie", range(100, 151), range(10, 18), 70, 12, 0, range(20, 51), range(40, 51)),
    "knight": Enemy("Undead Knight", range(200, 281), range(10, 21), 80, 5, 9, range(25, 33), range(20, 41)),
    "paladin": Enemy("Fallen Paladin", range(250, 301), range(12, 16), 70, 2, 2, range(25, 33), range(20, 41)),

    # BOSS
    "mini1": Enemy("Minotaur", range(400, 601), range(14, 21), 80, 5, 10, range(50, 71), range(30, 41)),
    "mini2": Enemy("Stone Gargoryle", range(600, 801), range(15, 24), 85, 5, 15, range(80, 101), range(30, 41)),
    "boss": Enemy("Horned-Beast", range(1000, 1201), range(20, 31), 90, 8, 6, range(110, 151), range(5, 6))
}

# Trigger
trigger = Trigger()

#################################################################################################################

def rng():                                                                              # RNG
    return randint(1, 101)

def print1(text):                                                                       # Pause before printing
    time.sleep(0.5)
    print(text)

def exp_check(exp):                                                                     # Check player exp for level up

    print1(f"Gained {exp} EXP")
    player.exp += exp

    if player.str == 8 and player.agi == 8 and player.misc == 8:
        player.exp = player.expLimit
        print1("\nWarning: Max Level Reached!")

    elif player.exp >= player.expLimit:

        player.exp -= player.expLimit
        player.expLimit += 10
        player.level += 1
        player.maxHp += 10
        player.hp = player.maxHp
        
        print1(f"\nYou are now Level: {player.level}")

        if player.level % 4 == 0:
            items['potion1'].limit += 1
            print1("Potion limit increased")
            print1(f"You can hold {items['potion1'].limit} Potion")

        if player.level % 5 == 0:
            items['potion2'].limit += 1
            print1("Greater Potion limit increased")
            print1(f"You can hold {items['potion2'].limit} Greater Potion")

        level_up()

def level_up():                                                                         # Player level up

    loop = True
    print1("\nYou gained a skill point!")
    print1("Where do you want to allocate it?")

    while loop == True:
        print1(f"1.STR: {player.str}/8   2. AGI: {player.agi}/8   3. MISC: {player.misc}/8")
        action = input("> ")

        if action == "1":
            if player.str == 8:
                print("Error: Stat is already maxed")
            else:
                player.str += 1
                loop = False

        elif action == "2":
            if player.agi >= 8:
                print("Error: Stat is already maxed")
            else:
                player.agi += 1
                loop = False

        elif action == "3":
            if player.misc >= 8:
                print("Error: Stat is already maxed")
            else:
                player.misc += 1
                loop = False

        else:
            print("Error: Invalid input")

    if player.str == 8 and player.agi == 8 and player.misc == 8:
        player.exp = player.expLimit
        print1("\nWarning: Max Level Reached!")

def health_check():                                                                     # Check player health

    global trigger

    if player.hp <= 0:
        print1("You ran out of health")
        print1("Restart?")
        print("1. Yes   2. No")
        action = input("> ")

        if action == "1":

            trigger.start = False
            trigger.mini1 = False
            trigger.mini2 = False
            trigger.boss = False
            trigger.exit_key = False

            player.exp = 0
            player.expLimit = 20
            player.level = 1
            player.hp = 100
            player.maxHp = 100 

            player.str = 0 
            player.agi = 0 
            player.misc = 0

            player.weapon = "punch"
            player.apparel = "none"

            print1("Restarting...")
            time.sleep(1)
            char_create()

        else: 
            print1("Thank you for playing!")
            time.sleep(3)
            exit(0)

def atk():                                                                              # Check Player's weapon for damage

    if player.weapon == "sword1":
        return player.str*3 + choice(items['sword1'].atk)
    elif player.weapon == "sword2":
        return player.str*3 + choice(items['sword2'].atk)
    elif player.weapon == "sword3":
        return player.str*3 + choice(items['sword3'].atk)

    elif player.weapon == "rapier1":
        return player.str*2 + choice(items['rapier1'].atk)
    elif player.weapon == "rapier2":
        return player.str*2 + choice(items['rapier2'].atk)
    elif player.weapon == "rapier3":
        return player.str*2 + choice(items['rapier3'].atk)

    elif player.weapon == "axe1":
        return player.str*4 + choice(items['axe1'].atk)
    elif player.weapon == "axe2":
        return player.str*4 + choice(items['axe2'].atk)
    elif player.weapon == "axe3":
        return player.str*4 + choice(items['axe3'].atk)

    else:
        return player.str*2 + choice(items['punch'].atk)

def datk():                                                                             # Display minimum and maximum damage

    if player.weapon == "sword1":
        return (f"{min(items['sword1'].atk) + (player.str*3)} - {max(items['sword1'].atk) + (player.str*3)}")
    elif player.weapon == "sword2":
        return (f"{min(items['sword2'].atk) + (player.str*3)} - {max(items['sword2'].atk) + (player.str*3)}")
    elif player.weapon == "sword3":
        return (f"{min(items['sword3'].atk) + (player.str*3)} - {max(items['sword3'].atk) + (player.str*3)}")

    elif player.weapon == "rapier1":
        return (f"{min(items['rapier1'].atk) + (player.str*2)} - {max(items['rapier1'].atk) + (player.str*2)}")
    elif player.weapon == "rapier2":
        return (f"{min(items['rapier2'].atk) + (player.str*2)} - {max(items['rapier2'].atk) + (player.str*2)}")
    elif player.weapon == "rapier3":
        return (f"{min(items['rapier3'].atk) + (player.str*2)} - {max(items['rapier3'].atk) + (player.str*2)}")

    elif player.weapon == "axe1":
        return (f"{min(items['axe1'].atk) + (player.str*4)} - {max(items['axe1'].atk) + (player.str*4)}")
    elif player.weapon == "axe2":
        return (f"{min(items['axe2'].atk) + (player.str*4)} - {max(items['axe2'].atk) + (player.str*4)}")
    elif player.weapon == "axe3":
        return (f"{min(items['axe3'].atk) + (player.str*4)} - {max(items['axe3'].atk) + (player.str*4)}")

    else:
        return (f"{min(items['punch'].atk) + (player.str*2)} - {max(items['punch'].atk) + (player.str*2)}")    

def damage_reduction():                                                                 # Damage reduction

    if player.apparel == "armor1":
        return player.str*4 + items['armor1'].stat
    elif player.apparel == "armor2":
        return player.str*4 + items['armor2'].stat
    elif player.apparel == "armor3":
        return player.str*4 + items['armor3'].stat

    else:
        return player.str*4 + 0

def parry():                                                                            # Parry chance

    if player.apparel == "shield1":
        return player.misc*7 + items['shield1'].stat
    elif player.apparel == "shield2":
        return player.misc*7 + items['shield2'].stat
    elif player.apparel == "shield3":
        return player.misc*7 + items['shield3'].stat

    else:
        return player.misc*7 + 0

def hit_rate():                                                                         # Player hit rate
    
    if player.weapon == "sword1":
        return player.agi*3 + items['sword1'].hit
    elif player.weapon == "sword2":
        return player.agi*3 + items['sword2'].hit
    elif player.weapon == "sword3":
        return player.agi*3 + items['sword3'].hit

    elif player.weapon == "rapier1":
        return player.agi*4 + items['rapier1'].hit
    elif player.weapon == "rapier2":
        return player.agi*4 + items['rapier2'].hit
    elif player.weapon == "rapier3":
        return player.agi*4 + items['rapier3'].hit

    elif player.weapon == "axe1":
        return player.agi*2 + items['axe1'].hit
    elif player.weapon == "axe2":
        return player.agi*2 + items['axe2'].hit
    elif player.weapon == "axe3":
        return player.agi*2 + items['axe3'].hit

    else:
        return player.agi*2 + items['punch'].hit
    
def crit_rate():                                                                        # Player crit rate

    if player.weapon == "sword1":
        return player.misc*2 + items['sword1'].crit
    elif player.weapon == "sword2":
        return player.misc*2 + items['sword2'].crit
    elif player.weapon == "sword3":
        return player.misc*2 + items['sword3'].crit

    elif player.weapon == "rapier1":
        return player.misc*3 + items['rapier1'].crit
    elif player.weapon == "rapier2":
        return player.misc*3 + items['rapier2'].crit
    elif player.weapon == "rapier3":
        return player.misc*3 + items['rapier3'].crit

    elif player.weapon == "axe1":
        return player.misc*1 + items['axe1'].crit
    elif player.weapon == "axe2":
        return player.misc*1 + items['axe2'].crit
    elif player.weapon == "axe3":
        return player.misc*1 + items['axe3'].crit

    else:
        return player.misc*2 + items['punch'].crit

def weapon_drop(weapon):                                                                # Prompt for dropped weapon

    print1(f"The enemy dropped a(n) '{items[weapon].name}'")
    print(f"'{items[weapon].name}' Stats:")
    print(f"Attack: {items[weapon].datk}   Hit Chance: {items[weapon].hit}%   Crit Chance: {items[weapon].crit}%")
    print1("Action:")
    print("1. Take it  2. Leave it")
    action = input("> ")

    if action == "1":
        player.weapon = weapon
        print1(f"You took the {items[weapon].name}")

    else:
        print1(f"You leave the {items[weapon].name}")

def apparel_drop(apparel):                                                                  # Prompt for dropped armor

    item = apparel[:-1]

    if item == "armor":
        print1(f"The enemy dropped a(n) '{items[apparel].name}'")
        print(f"'{items[apparel].name}' Stats:")
        print(f"Damage Reduction: {items[apparel].stat}%")
        print1("Action:")
        print("1. Take it (Warning: Will replace shield)  2. Leave it")
        action = input("> ")

        if action == "1":
            player.apparel = apparel
            print1(f"You took the {items[apparel].name}")

        else:
            print1(f"You leave the {items[apparel].name}")
    else:
        print1(f"The enemy dropped a(n) '{items[apparel].name}'")
        print(f"'{items[apparel].name}' Stats:")
        print(f"Parry Chance: {items[apparel].stat}%")
        print1("Action:")
        print("1. Take it (Warning: Will replace armor) 2. Leave it")
        action = input("> ")

        if action == "1":
            player.apparel = apparel
            print1(f"You took the {items[apparel].name}")

        else:
            print1(f"You leave the {items[apparel].name}")

def potion_drop(potion):                                                                # Prompt for dropped Potion

    if items[potion].count == items[potion].limit:
        if potion == "potion1":
            print("Warning: Max Potion Limit\n")
        else:
            print1("Warning: Max Greater Potion Limit\n")

    else:
        items[potion].count += 1
        if potion == "potion1":
            print1("The enemy dropped a Potion")
            print1(f"You have {items[potion].count}/{items[potion].limit} Potion\n")
        else:
            print1("The enemy dropped a Greater Potion")
            print1(f"You have {items[potion].count}/{items[potion].limit} Greater Potion\n")  

def battle(enemy):                                                                      # Battle sequence

    enemyHp = choice(enemy.hp)
    time.sleep(1)

    print("\n========================================================================================================")
    while enemyHp > 0:
        
        health_check()
        print1("\n--------------------------------------------------------------------------------------------------------")
        print(f"{enemy.name}'s Stats:")
        print(f"HP: {enemyHp}  Attack: {enemy.datk}")
        print(f"Hit Chance: {enemy.hit}%   Crit Chance: {enemy.crit}%   Evade: {enemy.evade}%\n")
        print("Your Stats:")
        print(f"Level: {player.level}   EXP: {player.exp}/{player.expLimit}   HP: {player.hp}/{player.maxHp}   Attack: {datk()}   Potion: {items['potion1'].count}/{items['potion1'].limit}   Greater Potion: {items['potion2'].count}/{items['potion2'].limit}")
        print(f"Hit Chance: {hit_rate()}%   Crit Chance: {crit_rate()}%   Parry Chance: {parry()}%   Damage Reduction: {damage_reduction()}%   Evade Chance: {player.agi*3}%")
        print("--------------------------------------------------------------------------------------------------------")
        print("Action:\n1. Attack   2. Parry   3. Use Potion")
        action = input("> ")
        

        if action == "1":
            if rng() <= enemy.evade or not rng() <= hit_rate():
                print("Miss!")

            elif rng() <= crit_rate():
                print("Critical Hit!")
                enemyHp -= atk()*2

            else:
                print("Succesful Hit!")
                enemyHp -= atk() 


            if rng() <= player.agi*3 or not rng() <= enemy.hit:
                print("Enemy Miss!")

            elif rng() <= enemy.crit and rng() <= enemy.hit:
                print("Enemy Critical Hit!")
                player.hp -= math.ceil((choice(enemy.atk)*2) * ((100 - damage_reduction()) / 100))

            else:
                print("You are hit!")
                player.hp -= math.ceil(choice(enemy.atk) * ((100 - damage_reduction()) / 100))


        elif action == "2":
            if rng() <= parry() and rng() <= enemy.evade and rng() <= enemy.crit and rng() <= enemy.hit:
                print("Critical Parry Evaded!")
                player.hp -= math.ceil((choice(enemy.atk)*2) * ((100 - damage_reduction()) / 100) * 0.1)

            elif rng() <= parry() and rng() <= enemy.evade and rng() <= enemy.hit and not rng() <= enemy.evade:
                print("Parry Evaded!")
                player.hp -= math.ceil(choice(enemy.atk) * ((100 - damage_reduction()) / 100) * 0.1)

            elif rng() <= parry() and rng() <= enemy.crit and rng() <= enemy.hit:
                print("Critical Parry!")
                enemyHp -= math.ceil((choice(enemy.atk)*2) * 0.8)
                player.hp -= math.ceil((choice(enemy.atk)*2) * ((100 - damage_reduction()) / 100) * 0.1)

            elif rng() <= parry() and rng() <= enemy.hit and not rng() <= enemy.evade:
                print("Parry Succesful!")
                enemyHp -= math.ceil(choice(enemy.atk)*0.8)
                player.hp -= math.ceil(choice(enemy.atk) * ((100 - damage_reduction()) / 100) * 0.1)

            else:
                print("Parry Failed!")

                if  rng() <= player.agi*3 or not enemy.hit:
                    print("Enemy Miss!")

                elif rng() <= enemy.crit and enemy.hit:
                    print("Enemy Critical Hit!")
                    player.hp -= math.ceil((choice(enemy.atk)*2) * ((100 - damage_reduction()) / 100))

                else:
                    print("You are hit!")
                    player.hp -= math.ceil(choice(enemy.atk) * ((100 - damage_reduction()) / 100))


        elif action == "3":
            if items['potion1'].count == 0 and items['potion2'].count == 0:
                print("Warning: You don't have any potion")

            else:
                print(f"\n1. Potion: {items['potion1'].count}/{items['potion1'].limit}  2. Greater Potion: {items['potion2'].count}/{items['potion2'].limit}")
                action = input("> ")

                if action == "1":
                    if items['potion1'].count != 0:
                        items['potion1'].count -= 1
                        print(f"Healed {items['potion1'].stat + (player.misc*4)} HP!\n{items['potion1'].count}/{items['potion1'].limit} Potion left.")
                        player.hp += items['potion1'].stat + (player.misc*4)
                        time.sleep(1)
                        
                    else:
                        print("You don't have that potion type")

                elif action == "2":
                    if items['potion2'].count != 0:
                        items['potion2'].count -= 1
                        print(f"Healed {items['potion2'].stat*6} HP!\n{items['potion2'].count}/{items['potion2'].limit} Greater Potion left.")
                        player.hp += items['potion2'].stat + (player.misc*6)
                        time.sleep(1)
                        
                    else:
                        print("You don't have that potion type")

                else:
                    print("Error: Invalid input")
        
        else:
            print("Error: Invalid input")

    health_check()
    print1(f"\n{enemy.name} killed")
    exp_check(choice(enemy.exp))
    print1(f"EXP: {player.exp}/{player.expLimit}")
    print1("========================================================================================================\n")

def end():                                                                              # End sequence

    print1("Do you want to use the key")
    print("1. Yes 2. No")
    action = input("> ")
    
    if action == "1":
        print1("You used the key")
        time.sleep(2)
        print("The door opened revealing a staircase leading up")
        time.sleep(2)
        print("You have no choice")
        time.sleep(2)
        print(".")
        time.sleep(2)
        print(".")
        time.sleep(2)
        print(".")
        time.sleep(4)
        print("It's been 10 minutes")
        time.sleep(2)
        print("You finally reached the top")
        time.sleep(2)
        print("There's a door blocking your way")
        time.sleep(2)
        print("You opened it")
        time.sleep(2)
        print("Only to be greeted with the same atmosphere when you wake up")
        time.sleep(2)
        print("With similar room, sound, perhaps everything")
        time.sleep(2)
        print('"Is there an end to this?" You said to yourself while desperate on the ground')
        time.sleep(1)
        print("The End", end='')
        time.sleep(1)
        print(".", end='')
        time.sleep(1)
        print(".", end='')
        time.sleep(1)
        print(".", end='')
        time.sleep(8)
        print("?")
        
        delay = input("Press ENTER to exit")
        exit(0)

    else:
        print("You decided to explore some more")
        room19()

###################################################################################################################


def main_menu():

    print("""
    |========\\   |         | |\\      |  /=======   |=========|  /=======\\  |\\      |
    |         \\  |         | | \\     | /           |           /         \\ | \\     |
    |          | |         | |  \\    | |           |           |         | |  \\    |
    |          | |         | |   \\   | |   =====|  |=======|   |         | |   \\   |
    |          | |         | |    \\  | |        |  |           |         | |    \\  |
    |         /   \\       /  |     \\ | \\        /  |           \\         / |     \\ |
    |========/     \\=====/   |      \\|  \\======/   |=========|  \\=======/  |      \\|


                            |========\\ |         | |\\      |
                            |        | |         | | \\     |
                            |        | |         | |  \\    |
                            |========/ |         | |   \\   |
                            |     \\    |         | |    \\  |
                            |      \\    \\       /  |     \\ |
                            |       \\    \\=====/   |      \\|


                                        How To Play:
                  Type in the number for the action you want and press ENTER
                  For more information please refer to the included .txt file

                            1. START                2. EXIT
    """)

    action = input("> ")

    if action == "1":
        char_create()
    else:
        exit()

def char_create():                                                                      # Point allocation

    global player
    stat_allocate = 24

    print("========================================================================================================")
    print1(f"You have {stat_allocate} Skill Points.")
    print1("STR affect your damage reduction and the damage you dealt.")
    print1("Each point will increase Damage Reduction by '4%'")
    print1("Enter a number between 0-8 for your STR.")
    action = input("> ")
    if action.isdecimal() == False:
        print("Error: Invalid input")
        print1("Restarting...")
        time.sleep(2)
        char_create()
    else:
        player.str = int(action)
        stat_allocate -= player.str

    print("--------------------------------------------------------------------------------------------------------")

    print1(f"You have {stat_allocate} Skill Point(s) remaining.")
    print1("AGI affect your evade and hit chance.")
    print1("Each AGI point will increase evade by '3%'")
    print1("Enter a number between 0-8 for your AGI.")
    action = input("> ")
    if action.isdecimal() == False:
        print("Error: Invalid input")
        print1("Restarting...")
        time.sleep(2)
        char_create()
    else:
        player.agi = int(action)
        stat_allocate -= player.agi

    print("--------------------------------------------------------------------------------------------------------")

    print1(f"You have {stat_allocate} Skill Point(s) remaining")
    print1("MISC skill will affect your chances of landing a critical, making a parry, and increase potion effectiveness.")
    print1("Each MISC point wil increase parry chance by '7%', Potion by 4 Points, and Greater Potion by 6 points.")
    print1("Enter a number between 0-8 for your MISC.")
    action = input("> ")
    if action.isdecimal() == False:
        print("Error: Invalid input")
        print1("Restarting...")
        time.sleep(2)
        char_create()
    else:
        player.misc = int(action)
        stat_allocate -= player.misc

    print("========================================================================================================")

    if stat_allocate > 0:
        print("You have", stat_allocate, "Skill points remaining. Do you want to restart?\n1. Yes\n2. No")
        action = input("> ")

        if action == "1":
            print("Restarting...")
            time.sleep(1)
            char_create()

        else:
            print("Starting...")
            time.sleep(1)
            room1()

    elif stat_allocate < 0:
        print("Error: Stat exceed maximum")
        print("Restarting...")
        time.sleep(1)
        char_create()

    else:
        print("Starting...")
        time.sleep(1)
        room1()

def room1():                                                                            # EASY          | Rat1, Slime1      | Sword1, Potion1
    
    if trigger.start == False:
        print1("\n\n========================================================================================================")
        print1("\nYou wake up in a dark room")
        print1("You see an unfamiliar roof")
        print1("You try to get a grasp of your surrounding")
        print1("Only to be startled by a rat hissing at you")
        time.sleep(1)
        battle(enemy['rat1'])
        trigger.start = True

        if rng() <= items['sword1'].drop:
            weapon_drop("sword1")
        
        elif rng() <= items['potion1'].drop:
            potion_drop("potion1")

    else:
        print1("\nThe room is gloomy")
        print1("Extinguished torches attached to the walls")

        if rng() <= choice(enemy['slime1'].chance):

            print1(f"You see a {enemy['slime1'].name} in the middle of the room")
            print1("It's jumping in place")
            battle(enemy['slime1'])
            print1("Maybe the slime is not that bad?")
            time.sleep(1)

        elif rng() <= choice(enemy['rat1'].chance):
            print1(f"A {enemy['rat1'].name} is hissing at you")
            battle(enemy['rat1'])

            if rng() <= items['sword1'].drop:
                weapon_drop("sword1")

            elif rng() <= items['potion1'].drop:
                potion_drop("potion1")

    while True:
        print1("You see 2 doors")
        print("1. East Door\n2. South Door")
        action = input("> ")

        if action == "1":
            room2()
        elif action == "2":
            room6()
        else:
            print("Error: Invalid input")

def room2():                                                                            # EASY          | Rat1, Spider      | Armor1, Potion1 x2

    print1("\nYou entered a hallway")
    print1("Your surroundings are dimly lit by a few torches")

    if rng() <= choice(enemy['spider'].chance):
        print1(f"You encountered a {enemy['spider'].name}")
        battle(enemy['spider'])

        if rng() <= items['armor1'].drop:
            apparel_drop("armor1")

        elif rng() <= items['potion1'].drop:
            potion_drop("potion1")

    elif rng() <= choice(enemy['rat1'].chance):
        print1(f"You encountered a {enemy['rat1'].name}")
        battle(enemy['rat1'])

        if rng() <= items['potion1'].drop:
            potion_drop("potion1")

    while True:
        print1("There are 2 doors")
        print("1. South Door\n2. West Door")
        action = input("> ")

        if action == "1":
            room5()
        elif action == "2":
            room1()
        else:
            print("Error: Invalid input")

def room3():                                                                            # INTERMEDIATE  | Skeleton x4       | Armor2, Potion1 x2, Potion2

    print1("\nYou entered a huge room, it is barely lit")
    print1("There are bones scattered across the floor")

    if rng() <= choice(enemy['skeleton'].chance):
        print1(f"A {enemy['skeleton'].name} rose up from the pile")
        battle(enemy['skeleton'])

        if rng() <= items['armor2'].drop:
            apparel_drop("armor2")

        if rng() <= choice(enemy['skeleton'].chance):
            print1(f"A second {enemy['skeleton'].name} rose up from the pile")
            battle(enemy['skeleton']) 

            if rng() <= items['potion1'].drop:
                potion_drop("potion1")
                    
            if rng() <= choice(enemy['skeleton'].chance):
                print1(f"A third {enemy['skeleton'].name} rose up from the pile")
                battle(enemy['skeleton'])

                if rng() <= items['potion2'].drop:
                    potion_drop("potion2")

                if rng() <= choice(enemy['skeleton'].chance):
                    print1(f"A fourth {enemy['skeleton'].name} rose up from the pile")
                    battle(enemy['skeleton'])

                    if rng() <= items['potion1'].drop:
                        potion_drop("potion1")

    while True:
        print1("There are 2 doors")
        print("1. South Door\n2. West Door")
        action = input("> ")

        if action == "1":
            room9()
        elif action == "2":
            room5()
        else:
            print("Error: Invalid input")

def room4():                                                                            # EASY          | Spider, Goblin    | Armor1  

    print1("\nYou entered a small room")
    print1("There are cracks all over the wall")

    if rng() <= choice(enemy['goblin'].chance):
        print1(f"You encountered a {enemy['goblin'].name} ready to attack")
        battle(enemy['goblin'])

        if rng() <= items['armor1'].drop:
            apparel_drop("armor1")
                
    elif rng() <= choice(enemy['spider'].chance):
        print1(f"A {enemy['spider'].name} is blocking your path")
        print1("You prepared yourself to attack it")
        battle(enemy['spider'])

    while True:
        print1("You can go through 3 doors")
        print("1. East Door\n2. South Door\n3. West Door")
        action = input("> ")

        if action == "1":
            room5()
        elif action == "2":
            room7()
        elif action == "3":
            room6()
        else:
            print("Error: Invalid input")

def room5():                                                                            # EASY          | Rat1, Goblin      | Shield1, Axe1, Potion1

    print1("\nYou entered a small room")
    print1("There are carvings on the walls")

    if rng() <= choice(enemy['goblin'].chance):
        print1(f"You encountered a {enemy['goblin'].name}")
        battle(enemy['goblin'])

        if rng() <= items['axe1'].drop:
            weapon_drop("axe1")

        elif rng() <= items['shield1'].drop:
            apparel_drop("shield1")

    elif rng() <= choice(enemy['rat1'].chance):
        print1(f"A {enemy['rat1'].name} is hissing at you")
        battle(enemy['rat1'])

        if rng() <= items['potion1'].drop:
            potion_drop("potion1")
    
    while True:
        print1("You see 3 doors")
        print("1. North Door\n2. East Door\n3. West Door")
        action = input("> ")

        if action == "1":
            room2()
        elif action == "2":
            room3()
        elif action == "3":
            room4()
        else:
            print("Error: Invalid input")

def room6():                                                                            # EASY          | Spider, Goblin    | Shield1, Rapier1, Potion1

    print1("\nYou entered a well-lit room")
    print1("Torches are attached along the walls")
    print1("There are symbols everywhere")

    if rng() <= choice(enemy['spider'].chance):
        print1(f"A {enemy['spider'].name} is wandering around the room")
        battle(enemy['spider'])

        if rng() <= items['rapier1'].drop:
            weapon_drop("rapier1")

    elif rng() <= choice(enemy['goblin'].chance):
        print1(f"A {enemy['goblin'].name} is cleaning it's weapon in the corner")
        battle(enemy['goblin'])

        if rng() <= items['shield1'].drop:
            apparel_drop("shield1")

        elif rng() <= items['potion1'].drop:
            potion_drop("potion1")

    while True:
        print1("After looking around, You see 5 doors")
        print("1. North Door\n2. East Door #1\n3. East Door #2\n4. South Door #1\n5. South Door #2")
        action = input("> ")
        
        if action == "1":
            room1()
        elif action == "2":
            room4()
        elif action == "3":
            room7()
        elif action == "4":
            room11()
        elif action == "5":
            room10()
        else:
            print("Error: Invalid input")

def room7():                                                                            # INTERMEDIATE  | Slime2, Skeleton  | Sword2, Potion1

    print1("\nYou entered a massive room")
    print1("Slimy substances are scattered across the floor")

    if rng() <= choice(enemy['slime2'].chance):
        print1(f"You encountered a {enemy['slime2'].name}")
        battle(enemy['slime2'])

        if rng() <= items['potion1'].drop:
            potion_drop("potion1")

    elif rng() <= choice(enemy['skeleton'].chance):
        print1(f"A {enemy['skeleton'].name} rose up from the ground")
        battle(enemy['skeleton'])

        if rng() <= items['sword2'].drop:
            weapon_drop("sword2")
    
    while True:
        print1("You see 5 doors you can use")
        print("1. North door\n2. East Door\n3. South Door\n4. West Door #1\n5. West Door #2")
        action = input("> ")

        if action == "1":
            room4()
        elif action == "2":
            room8()
        elif action == "3":
            room12()
        elif action == "4":
            room6()
        elif action == "5":
            room11()
        else:
            print("Error: Invalid input")

def room8():                                                                            # INTERMEDIATE  | Slime3            | Shield2, Potion2
    
    print1("\nDust is floating through the air")
    print1("Torches are attached along the walls")

    if rng() <= choice(enemy['slime3'].chance):
        print1(f"A {enemy['slime3'].name} is lunging at you")
        battle(enemy['slime3'])
        
        if rng() <= items['shield2'].drop:
            apparel_drop("shield2")

        elif rng() <= items['potion2'].drop:
            potion_drop("potion2")
    
    while True:
        print1("There are 3 doors you can go through")
        print("1. East Door\n2. South Door\n3. West Door")
        action = input("> ")

        if action == "1":
            room9()
        elif action == "2":
            room12()
        elif action == "3":
            room7()
        else:
            print("Error: Invalid input")

def room9():                                                                            # INTERMEDIATE  | Slime3, Slime2    | Axe2, Potion1, Potion2
    
    print1("\nThe room is massive")
    print1("A chandelier is hanging from the ceiling")
    print1("All the candles are lit")

    if rng() <= choice(enemy['slime3'].chance):
        print1(f"You encountered a {enemy['slime3'].name}")
        battle(enemy['slime3'])

        if rng() <= items['axe2'].drop:
            weapon_drop("axe2")

        if rng() <= choice(enemy['slime2'].chance):
            print1(f"A {enemy['slime2'].name} is charging at you from behind")
            battle(enemy['slime2'])

            if rng() <= items['potion2'].drop:
                potion_drop("potion2")

    elif rng() <= choice(enemy['skeleton'].chance):
        print1(f"You encountered a {enemy['skeleton'].name}")
        battle(enemy['skeleton'])

        if rng() <= items['potion1'].drop:
            potion_drop("potion1")
    
    while True:
        print1("You see 3 doors you can go through")
        print(f"1. North Door\n2. South Door (Mini Boss: {enemy['mini1'].name})\n3. West Door")
        action = input("> ")

        if action == "1":
            room3()
        elif action == "2":
            room13()
        elif action == "3":
            room7()
        else:
            print("Error: Invalid input")

def room10():                                                                           # INTERMEDIATE  | Slime2, Skeleton  | Rapier2, Potion2
    
    print1("\nYou entered a small hallway")
    print1("There are cobwebs on the ceiling")

    if rng() <= choice(enemy['skeleton'].chance):
        print1(f"A {enemy['skeleton'].name} is blocking your path")
        battle(enemy['skeleton'])

        if rng() <= items['rapier2'].drop:
            weapon_drop("rapier2")

    elif rng() <= choice(enemy['slime2'].chance):
        print1(f"You encountered a {enemy['slime2'].name}")
        battle(enemy['slime2'])

        if rng() <= items['potion2'].drop:
            potion_drop("potion2")
    
    while True:
        print1("There are 2 doors you can use")
        print("1. North Door\n2. South Door")
        action = input("> ")

        if action == "1":
            room6()
        elif action == "2":
            room14()
        else:
            print("Error: Invalid input")

def room11():                                                                           # INTERMEDIATE  | Slime2, Skeleton  | Shield2, Potion1

    print1("\nYou entered a small room")
    print1("There are weird symbols along the wall")
    print1("Dust are floating in the air")

    if rng() <= choice(enemy['skeleton'].chance):
        print1(f"A {enemy['skeleton'].name} notice you walks in")
        battle(enemy['skeleton'])

        if rng() <= items['shield2'].drop:
            apparel_drop("shield2")

    elif rng() <= choice(enemy['slime3'].chance):
        print1(f"You encountered a {enemy['slime3'].name}")
        battle(enemy['slime3'])

        if rng() <= items['potion1'].drop:
            potion_drop("potion1")

    while True:
        print1("You see 3 doors")
        print("1. North Door\n2. East Door\n3. South Door")
        action = input("> ")

        if action == "1":
            room6()
        elif action == "2":
            room7()
        elif action == "3":
            room14()
        else:
            print("Error: Invalid input")

def room12():                                                                           # HARD          | Zombie x3         | Armor2, Axe3, Potion2 x2

    print1("\nYou entered a massive room")
    print1("There are decaying corpses around the room")
    print1("The smell is horrible")

    if rng() <= choice(enemy['zombie'].chance):
        print1("One of the corpses starts to move again")
        battle(enemy['zombie'])

        if rng() <= items['armor2'].drop:
            apparel_drop("armor2")

        elif rng() <= items['potion2'].drop:
            potion_drop("potion2")

        if rng() <= choice(enemy['zombie'].chance):
            print1("A second one starts to move")
            battle(enemy['zombie'])

            if rng() <= items['axe3'].drop:
                weapon_drop("axe3")

            if rng() <= choice(enemy['zombie'].chance):
                print1("A third one is coming")
                battle(enemy['zombie'])

                if rng() <= items['potion2'].drop:
                    potion_drop("potion2")

    while True:
        print1("You see 4 doors you can use")
        print("1. North Door #1\n2. North Door #2\n3. South Door\n4. West Door")
        action = input("> ")

        if action == "1":
            room7()
        elif action == "2":
            room8()
        elif action == "3":
            room17()
        elif action == "4":
            room14()
        else:
            print("Error: Invalid input")

def room13():                                                                           # MINI BOSS     | MINOTAUR, Slime1  | Shield3

    time.sleep(1)

    if trigger.mini1 == False:

        print1("\nYou entered the room quietly")
        print1(f"You see a {enemy['mini1'].name} guarding a chest in the middle of the room")
        print1("Do you want to fight it?")
        print("1. Yes (Warning: Mini Boss fight)\n2. No")
        action = input("> ")

        if action == "1":

            print1("You convinced yourself that you are ready to face that creature")
            battle(enemy['mini1'])
            trigger.mini1 = True

            print1(f"You killed the {enemy['mini1'].name}")
            print1("You opened the chest")
            print1(f"There is a {items['shield3'].name} inside")
            print1("Do you want to equip it?")
            print("1. Yes (Warning: Will dequip equipped armor)\n2. No")
            action = input("> ")

            if action == "1":
                print(f"You equipped the {items['shield3'].name}\n")
                player.apparel = "shield3"

            else:
                print(f"You leave the {items['shield3'].name}\n")

            potion_drop("potion2")

            if trigger.mini1 == trigger.mini2:

                time.sleep(1)
                trigger.exitKey = True
                print1("A key phased itself right in front of you")
                print1("Thinking it might be important, you decided to take it")
                time.sleep(1)
            
            print1("You go back the way you came")
            room9()

        else:
            print1("There's nothing left to see")
            print1("You go back the way you came")
            room9()
    else:

        if rng() <= choice(enemy['slime1'].chance):

            print1(f"\nA {enemy['slime1'].name} is inside the chest")
            print1("You decide to kill it")
            battle(enemy['slime1'])
            print1("Maybe the slime isn't that bad?")

        elif rng() <= choice(enemy['mini1'].chance):

            print1(f"\nThe {enemy['mini1'].name} came back")
            print1("Do you want to fight it?")
            print("1. Yes\n2. No")
            action = input("> ")

            if action == "1":

                print("You decided to fight the minotaur again")
                battle(enemy['mini1'])

                print("You managed to kill it")
                apparel_drop("shield3")
                potion_drop("potion2")

            else:
                print("You decided that it's a hassle to fight it again")
                room9()

        print1("There's nothing left to see")
        room9()

def room14():                                                                           # INTERMEDIATE  | Skeleton, Slime3  | Potion1, Potion2

    print1("\nYou entered a room")
    print1("There are vines all over the walls")

    if rng() <= choice(enemy['skeleton'].chance):
        print1(f"You encountered a {enemy['skeleton'].name}")
        battle(enemy['skeleton'])

        if rng() <= items['poiton2'].drop:
            potion_drop("potion2")

    elif rng() <= choice(enemy['slime3'].chance):
        print1(f"A {enemy['slime3'].name} fell from the roof")
        battle(enemy['slime3'])

        if rng() <= items['potion1'].drop:
            potion_drop("potion1")

    while True:
        print1("You see 3 doors you can use")
        print("1. North Door #1\n2. North Door #2\n3. East Door")
        action = input("> ")

        if action == "1":
            room10()
        elif action == "2":
            room11()
        elif action == "3":
            room12()
        else:
            print("Error: Invalid input")

def room15():                                                                           # MINI BOSS     | GARGOYLE, Slime1  | Armor3

    time.sleep(1)
    if trigger.mini2 == False:

        print1("\nYou notices there's a lot of statue")
        print1("Your instinct tells you to stay away from the statue")
        print1("There is a chest in the middle of the room")
        print1("Do you want to continue?")
        print("1. Yes (Warning: Mini Boss fight)\n2. No")
        action = input("> ")

        if action == "1":

            print1("\nYou continue to walk to the chest")
            print1("In the middle of your way, one of the statue starts to move")
            print1("You prepared yourself")
            battle(enemy['mini2'])
            trigger.mini2 = True

            print1(f"You defeated the {enemy['mini2'].name}")
            print1("You proceed to walk to the chest")
            print1(f"There is a {items['armor3'].name} inside")
            print1("Do you want to equip it?")
            print("1. Yes (Warning: Will dequip equipped shield)\n2. No")
            action = input("> ")

            if action == "1":
                player.apparel = "armor3"
                print(f"You equipped the {items['armor3'].name}\n")

            else:
                print(f"You leave the {items['armor3'].name}\n")

            potion_drop("potion2")

            if trigger.mini1 == trigger.mini2:
                trigger.exitKey = True
                print1("A key phased itself right in front of you")
                print1("Thinking it might be important, you decided to take it")
                time.sleep(2)

            print("You go back the way you came")
            room16()

        else:
            print1("There's nothing left to see")
            print1("You go back the way you came")
            room16()

    else:
        if rng() <= choice(enemy['slime1'].chance):
            print1(f"\nA {enemy['slime1'].name} is inside the chest")
            print1("You decide to kill it")
            battle(enemy['slime1'])
            print1("Maybe the slime isn't that bad?")

        elif rng() <= choice(enemy['mini2'].chance):
            print1(f"\nOne of the statues starts to move again")
            print1("Do you want to fight it?")
            print("1. Yes\n2. No")
            action = input("> ")

            if action == "1":
                print(f"You decided to fight the {enemy['mini2'].name} again")
                battle(enemy['mini2'])
                
                print1("You managed to kill it")
                apparel_drop("armor3")
                potion_drop("potion2")

            else:
                print("You decided that it's a hassle to fight it again")
                room16()

        print1("There's nothing left to see")
        print1("You go back the way you came")
        room16()
    
def room16():                                                                           # HARD          | Zombie            | Potion1, Potion2

    print1("\nYou entered a small room")
    print1("A single torch is enough to lit the room")

    if rng() <= choice(enemy['zombie'].chance):
        print1(f"You encountered a {enemy['zombie'].name}")
        battle(enemy['zombie'])

        if rng() <= items['potion2'].drop:
            potion_drop("potion2")

        elif rng() <= items['potion1'].drop:
            potion_drop("potion1")

    while True:
        print1("There are 3 doors available")
        print(f"1. East Door\n2. South Door\n3. West Door (Mini Boss: {enemy['mini2'].name})")
        action = input("> ")

        if action == "1":
            room17()
        elif action == "2":
            room18()
        elif action == "3":
            room15()
        else:
            print("Error: Invalid input")

def room17():                                                                           # HARD          | Paladin, Zombie   | Rapier3, Potion1, Potion2

    print1("\nYou entered a long hallway")
    print1("There are lot of equipment attached on the walls")

    if rng() <= choice(enemy['paladin'].chance):
        print1("Something walks up from the darkness")
        print1("It grabbed some of the equipments")
        battle(enemy['paladin'])
        
        if rng() <= items['rapier3'].drop:
            weapon_drop("rapier3")

        elif rng() <= items['potion2'].drop:
            potion_drop("potion2")

    elif rng() <= choice(enemy['zombie'].chance):
        print1(f"You encountered a {enemy['zombie'].name}")
        battle(enemy['zombie'])

        if rng() <= items['potion2'].drop:
            potion_drop("potion1")
    
    while True:
        print1("There are 3 doors you can use")
        print("1. North door\n2. South Door\n3. West Door")
        action = input("> ")

        if action == "1":
            room12()
        elif action == "2":
            room19()
        elif action == "3":
            room16()
        else:
            print("Error: Invalid input")

def room18():                                                                           # HARD          | Knight, Zombie    | Sword3, Potion1, Potion2

    print1("\nYou entered a long hallway")
    print1("There are Knight armor along the wall")

    if rng() <= choice(enemy['knight'].chance):
        print1("One of them started to move")
        battle(enemy['knight'])

        if rng() <= items['sword3'].drop:
            weapon_drop("sword3")

        elif rng() <= items['potion2'].drop:
            potion_drop("potion2")
        
    elif rng() <= choice(enemy['zombie'].chance):
        print1(f"A {enemy['zombie'].name} appears between the armor")
        battle(enemy['zombie'])

        if rng() <= items['potion1'].drop:
            potion_drop("potion1")
    
    while True:
        print1("You see 2 doors")
        print("1. North Door\n2. East Door")
        action = input("> ")

        if action == "1":
            room16()
        elif action == "2":
            room19()
        else:
            print("Error: Invalid input")

def room19():                                                                           # HARD          | Zombie            | Potion1, Poiton2
    
    print1("\nYou entered a small room")
    print1("Old books are scattered on the floor")

    if rng() <= choice(enemy['zombie'].chance):
        print1(f"You encountered a {enemy['zombie'].name}")
        battle(enemy['zombie'])

        if rng() <= items['potion2'].drop:
            potion_drop("potion2")

        elif rng() <= items['potion1'].drop:
            potion_drop("potion1")

    while True:
        print1("You can use 3 doors")
        print(f"1. North Door\n2. East Door (BOSS: {enemy['boss'].name})\n3. West Door")
        action = input("> ")

        if action == "1":
            room17()
        elif action == "2":
            room20()
        elif action == "3":
            room18()
        else:
            print("Error: Invalid input")

def room20():                                                                           # BOSS

    if trigger.boss == False:

        print1("\nYou entered the room and notices a creature guarding a door")
        print1("The door looks different from the rest of the doors you have seen")
        print1("You feel a glimpse of hope")
        print1("You need to fight that creature to get to that door")
        print("1. Fight (Warning: Boss fight)\n2. Leave")
        action = input("> ")

        if action == "1":

            print1("You want to get out of here")
            print1("You charged yourself at that monster")
            battle(enemy['boss'])
            trigger.boss = True

            print1("You killed it")
            print1("You can finally get out of this hell hole")
            print1("You approached the door an notice a keyhole")

            if trigger.exitKey == True:
                print1(f"You remember that you got yourself a key from killing the {enemy['mini1'].name} and {enemy['mini2'].name}")
                end()

            else:
                print1("You have no choice but to come back when you got a key")
                room19()
        else:
            print1("You thought that you are not strong enough to face it")
            print1("You go back the way you came")
            room19()

    elif trigger.exit_key == True:
        print1(f"\nYou finally got the key after killing the {enemy['mini1'].name} and the {enemy['mini2'].name}")
        end()

    else:
        print1("You still don't have a key")
        print1("You have no choice but to come back later")
        room19()

main_menu()