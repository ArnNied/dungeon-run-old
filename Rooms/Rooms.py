from os import system
from time import sleep
from Functions.functions import rng, prompt, append_score, print1, print2, print3, print_s1, print_s2
from Enemy.Enemy import Enemy
from Weapon.Weapon import Sword, Rapier, Axe
from Apparel.Apparel import Armor, Shield
from Potion.Potion import LesserHealingPotion, HealingPotion
from Mechanics.Mechanics import weapon_drop, apparel_drop, battle

class Trigger(object):
    def __init__(self):
        self.mini1 = False
        self.mini2 = False
        self.boss = False

trigger = Trigger()

def death(player):
    print3("You ran out of health")
    print(f"Your score is: {player.score} has been added to the score.txt file")
    append_score("score.txt", player.score)
    print("Thank you for playing")
    action = input("Press ENTER to exit")

    return

def main_menu(player):
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

    action = prompt()
    if action == 1:
        return 'char_create'
    else:
        return 0

def char_create(player):
    stat_allocate = 22

    print("========================================================================================================")
    print1(f"You have {stat_allocate} Skill Points.")
    print1("STR affect your damage reduction and the damage you dealt.")
    while True:
        player.str = prompt("Enter a number between 0-8 for your STR.")
        if player.str < 0 or player.str > 8:
            print_s2("Error: Invalid input")
            continue
        stat_allocate -= player.str
        break

    print2("--------------------------------------------------------------------------------------------------------")
    print1(f"You have {stat_allocate} Skill Point(s) remaining.")
    print1("AGI affect your evade and hit chance.")
    while True:
        player.agi = prompt("Enter a number between 0-8 for your AGI.")
        if player.agi < 0 or player.agi > 8:
            print_s2("Error: Invalid input")
            continue
        stat_allocate -= player.agi
        break
    
    print2("--------------------------------------------------------------------------------------------------------")
    print1(f"You have {stat_allocate} Skill Point(s) remaining")
    print1("MISC skill will affect your chances of landing a critical, making a parry, and increase potion effectiveness.")
    while True:
        player.misc = prompt("Enter a number between 0-8 for your MISC.")
        if player.misc < 0 or player.misc > 8:
            print_s2("Error: Invalid input")
            continue
        stat_allocate -= player.misc
        break

    print("========================================================================================================")
    if stat_allocate < 0:
        print_s2("Error: Stat exceeding limit")
        return 'char_create'
    if stat_allocate > 0:
        action = prompt(f"You have {stat_allocate} skill points remaining. Do you want to restart?\n1. Yes   2. No")
        if action == 1:
            return 'char_create'
        else:
            pass
    
    print1(f"Your stats will be")
    print(f"STR: {player.str}   AGI: {player.agi}   MISC: {player.misc}")
    if prompt("Confirm?\n0. RESTART   1. CONFIRM"):
        print_s2("Starting...")
        return 'intro'
    else:
        return 'char_create'

def intro(player):

    print1("========================================================================================================")
    print1("\nYou wake up in a dark room")
    print1("You see an unfamiliar roof")
    print1("You try to get a grasp of your surrounding")
    print1("Only to be startled by a rat hissing at you")

    battle(player, 'rat1')
    if Sword('sword1').item_drop():
        weapon_drop(player, Sword('sword1'))
    if LesserHealingPotion().item_drop():
        player.add_potion('Potion.Potion', 'LesserHealingPotion')

    return 'room1'

def room1(player):

    print1("\nThe room is gloomy")
    print1("Extinguished torches attached to the walls")

    if Enemy('slime1').encounter():
        print2(f"You see a {Enemy('slime1').name} in the middle of the room")
        print1("It's jumping in place")

        battle(player, 'slime1')
        print1("Maybe the slime is not that bad?")

    elif Enemy('rat1').encounter():
        print2(f"A {Enemy('rat1').name} is hissing at you")

        battle(player, 'rat1')
        if Sword('sword1').item_drop():
            weapon_drop(player, Sword('sword1'))
        elif LesserHealingPotion().item_drop():
            player.add_potion('Potion.Potion', 'LesserHealingPotion')

    while True:
        action = prompt("You see 2 doors\n1. East Door   2. South Door")
        if action == 1:
            return 'room2'
        elif action == 2:
            return 'room6'
        else:
            print("Error: Invalid input")

def room2(player):

    print1("\nYou entered a hallway")
    print1("Your surroundings are dimly lit by a few torches")

    if Enemy('spider').encounter():
        print2(f"You encountered a {Enemy('spider').name}")

        battle(player, 'spider')
        if Armor('armor1').item_drop():
            apparel_drop(player, Armor('armor1'))
        elif LesserHealingPotion().item_drop():
            player.add_potion('Potion.Potion', 'LesserHealingPotion')

    elif Enemy('slime1').encounter():
        print2(f"You encountered a {Enemy('rat1').name}")

        battle(player, 'rat1')
        if LesserHealingPotion().item_drop():
            player.add_potion('Potion.Potion', 'LesserHealingPotion')

    while True:
        action = prompt('There are 2 doors\n1. South Door   2. West Door')
        if action == 1:
            return 'room5'
        elif action == 2:
            return 'room1'
        else:
            print("Error: Invalid input")

def room3(player):

    print1("\nYou entered a huge room, it is barely lit")
    print1("There are bones scattered across the floor")

    if Enemy('skeleton').encounter():
        print2(f"A {Enemy('skeleton').name} rose up from the pile")

        battle(player, 'skeleton')
        if Armor('armor2').item_drop():
            apparel_drop(player, Armor('armor2'))

        if Enemy('skeleton').encounter():
            print2(f"A second {Enemy('skeleton').name} rose up from the pile")
            
            battle(player, 'skeleton')
            if LesserHealingPotion().item_drop():
                player.add_potion('Potion.Potion', 'LesserHealingPotion')
                    
            if Enemy('skeleton').encounter():
                print2(f"A third {Enemy('skeleton').name} rose up from the pile")
                
                battle(player, 'skeleton')
                if HealingPotion().item_drop():
                    player.add_potion('Potion.Potion', 'HealingPotion')

                if Enemy('skeleton').encounter():
                    print2(f"A fourth {Enemy('skeleton').name} rose up from the pile")

                    battle(player, 'skeleton')
                    if LesserHealingPotion().item_drop():
                        player.add_potion('Potion.Potion', 'LesserHealingPotion')

    while True:
        action = prompt("There are 2 doors\n1. South Door   2. West Door")
        if action == 1:
            return 'room9'
        elif action == 2:
            return 'room5'
        else:
            print("Error: Invalid input")

def room4(player):

    print1("\nYou entered a small room")
    print1("There are cracks all over the wall")

    if Enemy('goblin').encounter():
        print2(f"You encountered a {Enemy('goblin').name} ready to attack")

        battle(player, 'goblin')
        if Armor('armor1').item_drop():
            apparel_drop(player, Armor('armor1'))
                
    elif Enemy('spider').encounter():
        print2(f"A {Enemy('spider').name} is blocking your path")
        print1("You prepared yourself to attack it")

        battle(player, 'spider')

    while True:
        action = prompt("You can go through 3 doors\n1. East Door   2. South Door   3. West Door")
        if action == 1:
            return 'room5'
        elif action == 2:
            return 'room7'
        elif action == 3:
            return 'room6'
        else:
            print("Error: Invalid input")

def room5(player):

    print1("\nYou entered a small room")
    print1("There are carvings on the walls")

    if Enemy('goblin').encounter():
        print2(f"You encountered a {Enemy('goblin').name}")

        battle(player, 'goblin')
        if Axe('axe1').item_drop():
            weapon_drop(player, Axe('axe1'))
        elif Shield('shield1').item_drop():
            apparel_drop(player, Shield('shield1'))

    elif Enemy('rat1').encounter():
        print2(f"A {Enemy('rat1').name} is hissing at you")

        battle(player, 'rat1')
        if LesserHealingPotion().item_drop():
            player.add_potion('Potion.Potion', 'LesserHealingPotion')
    
    while True:
        action = prompt("You see 3 doors\n1. North Door   2. East Door   3. West Door")
        if action == 1:
            return 'room2'
        elif action == 2:
            return 'room3'
        elif action == 3:
            return 'room4'
        else:
            print("Error: Invalid input")

def room6(player):

    print1("\nYou entered a well-lit room")
    print1("Torches are attached along the walls")
    print1("There are symbols everywhere")

    if Enemy('spider').encounter():
        print2(f"A {Enemy('spider').name} is wandering around the room")

        battle(player, 'spider')
        if Rapier('rapier1').item_drop():
            weapon_drop(player, Rapier('rapier1'))

    elif Enemy('spider').encounter():
        print2(f"A {Enemy('goblin').name} is cleaning it's weapon in the corner")

        battle(player, 'goblin')
        if Shield('shield1').item_drop():
            apparel_drop(player, Shield('shield1'))
        elif LesserHealingPotion().item_drop():
            player.add_potion('Potion.Potion', 'LesserHealingPotion')

    while True:
        action = prompt("After looking around, You see 5 doors\n1. North Door   2. East Door #1   3. East Door #2   4. South Door #1   5. South Door #2")
        if action == 1:
            return 'room1'
        elif action == 2:
            return 'room4'
        elif action == 3:
            return 'room7'
        elif action == 4:
            return 'room10'
        elif action == 5:
            return 'room11'
        else:
            print("Error: Invalid input")

def room7(player):

    print1("\nYou entered a massive room")
    print1("Slimy substances are scattered across the floor")

    if Enemy('slime2').encounter():
        print2(f"You encountered a {Enemy('slime2').name}")

        battle(player, 'slime2')
        if LesserHealingPotion().item_drop():
            player.add_potion('Potion.Potion', 'LesserHealingPotion')

    elif Enemy('skeleton').encounter():
        print2(f"A {Enemy('skeleton').name} rose up from the ground")
        
        battle(player, 'skeleton')
        if Sword('sword2').item_drop():
            weapon_drop(player, Sword('sword2'))
    
    while True:
        action = prompt("You see 5 doors you can use\n1. North door   2. East Door   3. South Door   4. West Door #1   5. West Door #2")
        if action == 1:
            return 'room4'
        elif action == 2:
            return 'room8'
        elif action == 3:
            return 'room12'
        elif action == 4:
            return 'room6'
        elif action == 5:
            return 'room11'
        else:
            print("Error: Invalid input")

def room8(player):

    print1("\nDust is floating through the air")
    print1("Torches are attached along the walls")

    if Enemy('slime3').encounter():
        print2(f"A {Enemy('slime3').name} is lunging at you")

        battle(player, 'slime3')
        if Shield('shield2').item_drop():
            apparel_drop(player, Shield('shield2'))
        elif HealingPotion().item_drop():
            player.add_potion('Potion.Potion', 'HealingPotion')
    
    while True:
        action = prompt("There are 3 doors you can go through\n1. East Door   2. South Door   3. West Door")
        if action == 1:
            return 'room9'
        elif action == 2:
            return 'room12'
        elif action == 3:
            return 'room7'
        else:
            print("Error: Invalid input")

def room9(player):

    print1("\nThe room is massive")
    print1("A chandelier is hanging from the ceiling")
    print1("All the candles are lit")

    if Enemy('slime3').encounter():
        print2(f"You encountered a {Enemy('slime3').name}")

        battle(player, 'slime3')
        if Axe('axe2').item_drop():
            weapon_drop(player, Axe('axe2'))

    if Enemy('slime2').encounter():
        print2(f"A {Enemy('slime2').name} is charging at you from behind")

        battle(player, 'slime2')
        if HealingPotion().item_drop():
            player.add_potion('Potion.Potion', 'HealingPotion')

    elif Enemy('skeleton').encounter():
        print2(f"You encountered a {Enemy('skeleton').name}")

        battle(player, 'skeleton')
        if LesserHealingPotion().item_drop():
            player.add_potion('Potion.Potion', 'LesserHealingPotion')
    
    while True:
        action = prompt(f"You see 3 doors you can go through\n1. North Door   2. South Door (Mini Boss: {Enemy('mini1').name})   3. West Door")
        if action == 1:
            return 'room3'
        elif action == 2:
            return 'room13'
        elif action == 3:
            return 'room7'
        else:
            print("Error: Invalid input")

def room10(player):

    print1("\nYou entered a small hallway")
    print1("There are cobwebs on the ceiling")

    if Enemy('skeleton').encounter():
        print2(f"A {Enemy('skeleton').name} is blocking your path")
        
        battle(player, 'skeleton')
        if Rapier('rapier2').item_drop():
            weapon_drop(player, Rapier('rapier2'))

    elif Enemy('slime2').encounter():
        print2(f"You encountered a {Enemy('slime2').name}")
        
        battle(player, 'slime2')
        if HealingPotion().item_drop():
            player.add_potion('Potion.Potion', 'HealingPotion')
    
    while True:
        action = prompt("There are 2 doors you can use\n1. North Door   2. South Door")
        if action == 1:
            return 'room6'
        elif action == 2:
            return 'room14'
        else:
            print("Error: Invalid input")

def room11(player):

    print1("\nYou entered a small room")
    print1("There are weird symbols along the wall")
    print1("Dust are floating in the air")

    if Enemy('skeleton').encounter():
        print2(f"A {Enemy('skeleton').name} notice you walks in")
        
        battle(player, 'skeleton')
        if Shield('shield2').item_drop():
            apparel_drop(player, Shield('shield2'))

    elif Enemy('slime3').encounter():
        print2(f"You encountered a {Enemy('slime3').name}")

        battle(player, 'slime3')
        if LesserHealingPotion().item_drop():
            player.add_potion('Potion.Potion', 'LesserHealingPotion')

    while True:
        action = prompt("You see 3 doors\n1. North Door   2. East Door   3. South Door")
        if action == 1:
            return 'room6'
        elif action == 2:
            return 'room7'
        elif action == 3:
            return 'room14'
        else:
            print("Error: Invalid input")

def room12(player):

    print1("\nYou entered a massive room")
    print1("There are decaying corpses around the room")
    print1("The smell is horrible")

    if Enemy('zombie').encounter():
        print2("One of the corpses starts to move again")

        battle(player, 'zombie')
        if Armor('armor2').item_drop():
            apparel_drop(player, Shield('armor2'))
        if HealingPotion().item_drop():
            player.add_potion('Potion.Potion', 'HealingPotion')

        if Enemy('zombie').encounter():
            print2("A second one starts to move")
            
            battle(player, 'zombie')
            if Axe('axe3').item_drop():
                weapon_drop(player, Axe('axe3'))

            if Enemy('zombie').encounter():
                print2("A third one is coming")
                
                battle(player, 'zombie')
                if HealingPotion().item_drop():
                    player.add_potion('Potion.Potion', 'HealingPotion')

    while True:
        action = prompt("You see 4 doors you can use\n1. North Door #1   2. North Door #2   3. South Door   4. West Door")
        if action == 1:
            return 'room7'
        elif action == 2:
            return 'room8'
        elif action == 3:
            return 'room17'
        elif action == 4:
            return 'room14'
        else:
            print("Error: Invalid input")

def room13(player):

    if trigger.mini1 == False:
        print1("\nYou entered the room quietly")
        print1(f"You see a {Enemy('mini1').name} guarding a chest in the middle of the room")

        action = prompt("Do you want to fight it?\n1. Yes (Warning: Mini Boss fight)   2. No")
        if action == 1:
            print2("You convinced yourself that you are ready to face that creature")
            
            battle(player, 'mini1')
            trigger.mini1 = True
            apparel_drop(player, Shield('shield3'))
            player.add_potion('Potion.Potion', 'HealingPotion')

            print1(f"You killed the {Enemy('mini1').name}")
            print1("You opened the chest")
            print1("There is a key inside")
            print1("You decded to take it")
            print1("There's nothing left to see")
        else:
            print_s2("You go back the way you came")
            return 'room9'
    else:
        if Enemy('slime1').encounter():
            print2(f"\nA {Enemy('slime1').name} is jumping in place")

            battle(player, 'slime1')

        elif Enemy('mini1').encounter():
            print1(f"\nThe {Enemy('mini1').name} came back")

            action = prompt(f"The {Enemy('mini1').name} came back\nDo you want to fight it?\n1. Yes   2. No")
            if action == 1:
                print2("You decided to fight the minotaur again")
                
                battle(player, 'mini1')
                apparel_drop(player, Shield('shield3'))
                player.add_potion('Potion.Potion', 'HealingPotion')
            else:
                print_s2("You decided that it's a hassle to fight it again")
                return 'room9'

    print_s2("There's nothing left to see")
    return 'room9'

def room14(player):

    print1("\nYou entered a room")
    print1("There are vines all over the walls")

    if Enemy('skeleton').encounter():
        print2(f"You encountered a {Enemy('skeleton').name}")

        battle(player, 'skeleton')
        if HealingPotion().item_drop():
            player.add_potion('Potion.Potion', 'HealingPotion')

    elif Enemy('slime3').encounter():
        print2(f"A {Enemy('slime3').name} fell from the roof")

        battle(player, 'slime3')
        if LesserHealingPotion().item_drop():
            player.add_potion('Potion.Potion', 'HealingPotion')

    while True:
        action = prompt("You see 3 doors you can use\n1. North Door #1   2. North Door #2   3. East Door")
        if action == 1:
            return 'room10'
        elif action == 2:
            return 'room11'
        elif action == 3:
            return 'room12'
        else:
            print("Error: Invalid input")

def room15(player):

    if trigger.mini2 == False:
        print1("\nYou notices there's a lot of statue")
        print1("Your instinct tells you to stay away from the statue")
        print1("There is a chest in the middle of the room")

        action = prompt("Do you want to continue?\n1. Yes (Warning: Mini Boss fight)   2. No")
        if action == 1:
            print2("\nYou continue to walk to the chest")
            print1("In the middle of your way, one of the statue starts to move")
            print1("You prepared yourself")

            battle(player, 'mini2')
            trigger.mini2 = True
            apparel_drop(player, Armor('armor3'))
            player.add_potion('Potion.Potion', 'HealingPotion')

            print1(f"You defeated the {Enemy('mini2').name}")
            print1("You proceed to walk to the chest and take the key inside")
        else:
            print1("You go back the way you came")
            return 'room16'

    else:
        if Enemy('slime1').encounter():
            print2(f"\nA {Enemy('slime1').name} is jumping in place")

            battle(player, 'slime1')

        elif Enemy('mini2').encounter():
            print2(f"\nOne of the statues starts to move again")

            action = prompt("Do you want to fight it\n1. Yes   2. No")
            if action == 1:
                print1(f"You decided to fight the {Enemy['mini2'].name} again")

                battle(player, 'mini2')                
                print1("You managed to kill it")
                apparel_drop(player, Armor('armor3'))
                player.add_potion('Potion.Potion', 'HealingPotion')
            else:
                print_s2("You decided that it's a hassle to fight it again")
                return 'room16'

    print1("There's nothing left to see")
    print_s2("You go back the way you came")
    return 'room16'

def room16(player):

    print1("\nYou entered a small room")
    print1("A single torch is enough to lit the room")

    if Enemy('zombie').encounter():
        print2(f"You encountered a {Enemy('zombie').name}")

        battle(player, 'zombie')
        if HealingPotion().item_drop:
            player.add_potion('Potion.Potion', "HealingPotion")
        elif LesserHealingPotion().item_drop:
            player.add_potion('Potion.Potion', "LesserHealingPotion")

    while True:
        action = prompt(f"There are 3 doors available\n1. East Door   2. South Door   3. West Door (Mini Boss: {Enemy('mini2').name})")
        if action == 1:
            return 'room17'
        elif action == 2:
            return 'room18'
        elif action == 3:
            return 'room15'
        else:
            print("Error: Invalid input")

def room17(player):

    print1("\nYou entered a long hallway")
    print1("There are lot of equipment attached on the walls")

    if Enemy('paladin').encounter():
        print2("Something walks up from the darkness")
        print1("It grabbed some of the equipments")

        battle(player, 'paladin')
        if Rapier('rapier3').item_drop():
            weapon_drop(player, Rapier('rapier3'))
        elif HealingPotion().item_drop():
            player.add_potion('Potion.Potion', 'HealingPotion')

    elif Enemy('zombie').encounter():
        print2(f"You encountered a {Enemy('zombie').name}")

        battle(player, 'zombie')
        if HealingPotion().item_drop():
            player.add_potion('Potion.Potion', 'HealingPotion')
    
    while True:
        action = prompt("There are 3 doors you can use\n1. North door   2. South Door   3. West Door")
        if action == 1:
            return 'room12'
        elif action == 2:
            return 'room19'
        elif action == 3:
            return 'room16'
        else:
            print("Error: Invalid input")

def room18(player):

    print1("\nYou entered a long hallway")
    print1("There are Knight armor along the wall")

    if Enemy('knight').encounter():
        print2("One of them started to move")

        battle(player, 'knight')
        if Sword('sword3').item_drop():
            weapon_drop(player, Sword('sword3'))
        elif HealingPotion().item_drop():
            player.add_potion('Potion.Potion', 'HealingPotion')
        
    elif Enemy('zombie').encounter():
        print2(f"A {Enemy('zombie').name} appears between the armor")

        battle(player, 'zombie')
        if LesserHealingPotion().item_drop():
            player.add_potion('Potion.Potion', 'LesserHealingPotion')
    
    while True:
        action = prompt("You see 2 doors\n1. North Door   2. East Door")
        if action == 1:
            return 'room16'
        elif action == 2:
            return 'room19'
        else:
            print("Error: Invalid input")

def room19(player):

    print1("\nYou entered a small room")
    print1("Old books are scattered on the floor")

    if Enemy('zombie').encounter():
        print2(f"You encountered a {Enemy['zombie'].name}")

        battle(player, 'zombie')
        if HealingPotion().item_drop():
            player.add_potion('Potion.Potion', 'HealingPotion')
        elif LesserHealingPotion().item_drop():
            player.add_potion('Potion.Potion', 'LesserHealingPotion')

    while True:
        action = prompt(f"You can use 3 doors\n1. North Door   2. East Door (BOSS: {Enemy('boss1').name})   3. West Door")
        if action == 1:
            return 'room17'
        elif action == 2:
            return 'room20'
        elif action == 3:
            return 'room18'
        else:
            print("Error: Invalid input")

def room20(player):

    if trigger.boss == False:
        print1("\nYou entered the room and notices a creature guarding a door")
        print1("The door looks different from the rest of the doors you have seen")
        print1("Beside it, two keyhole can be seen")
        print1("You feel a glimpse of hope")
        
        action = prompt("You need to fight that creature to get to that door\n1. Fight (Warning: Boss fight)   2. Leave")
        if action == 1:
            print2("You want to get out of here")
            print1("You charged yourself at that monster")

            battle(player, 'boss')
            trigger.boss = True

            print1("You killed it")
            print1("You can finally get out of this place")
            print1("You approached the door and realized it's a keyhole")
        else:
            print2("You thought that you are not strong enough to face it")
            print_s2("You go back the way you came")
            return 'room19'

    if trigger.mini1 == trigger.mini2:
        action = prompt("Do you want to escape?\n1. Yes   2.No")
        if action == 1:
            return 'end1'
        elif action == 2:
            return 'room19'

    print_s2("You have no choice but to come back when you got a key")
    return 'room19'

def end1(player):
    sleep(2)

    print3(f"You used the key you got from killing {Enemy('mini1').name} and {Enemy('mini2').name}")
    print3("The door opened revealing a spiral staircase leading up")
    print3("Escaping is the only thing you can think of")
    print3(".")
    print3(".")
    print3(".")
    print3("It's been 10 minutes")
    print3("You finally reached the top")
    print3("There's a door blocking your way")
    print3("You opened it")
    print3("Only to be greeted with a vast open space covered in snow")
    print3("You sit desperately")
    print3("Thinking of what's your next action")
    print3("With nothing but empty space")
    sleep(4)
    print3("The End")
    print3(".")
    print3(".")
    print3(".")
    print_s2("?")

    return 'credits'
    
def end2(player):
    return 'credits'

def credits(player):
    print3("\nDungeon Run")
    print3("A \"game\" made by someone who got too much time during COVID-19 quarantine")
    print3("Andrien \"ArnNied\" Wiandyano")
    print3("Thank you for playing\n\n")
    sleep(2)
    print2(f"Your score is: {player.score} has been added to the score.txt file")
    append_score("score.txt", player.score)
    delay = input("Press ENTER to exit")