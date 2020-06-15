from os import system
from time import sleep
from math import ceil
from random import randint
from Functions.functions import prompt, print1, print2, print3, print_s1, print_s2
from Enemy.Enemy import Enemy

class PlayerDead(Exception):
    pass

def exp_check(player, exp):
    print3(f"Gained {exp} EXP")
    player.exp += exp
    player.score += exp
    
    if player.str >= 8 and player.agi >= 8 and player.misc >= 8:
        player.str = 8
        player.agi = 8
        player.misc = 8

        player.exp = player.expLimit
        print_s2("\nWarning: Max Level Reached!")

    elif player.exp >= player.expLimit:
        level_up(player)

def level_up(player):
    while player.exp >= player.expLimit:
        player.exp -= player.expLimit
        player.expLimit += 10
        player.level += 1
        player.maxHp += 10
        player.hp = player.maxHp
        
        print1(f"\nYou are now Level: {player.level}")

        while True:
            action = prompt(f"1.STR: {player.str}/8   2. AGI: {player.agi}/8   3. MISC: {player.misc}/8")

            if action == 1 and player.str < 8:
                    player.str += 1
            elif action == 2 and player.agi < 8:
                    player.agi += 1
            elif action == 3 and player.misc < 8:
                    player.misc += 1
            else:
                print_s1("Error: Invalid input")
                continue
            break

        if player.str >= 8 and player.agi >= 8 and player.misc >= 8:
            player.exp = player.expLimit
            print_s2("\nWarning: Max Level Reached!")
            return
    return

def health_check(player):
    if player.hp >= player.maxHp:
        player.hp = player.maxHp
    elif player.hp <= 0:
        raise PlayerDead
    else:
        return

def battle(player, enemyKey):
    enemy = Enemy(enemyKey)
    sleep(1)
    while enemy.hp > 0:
        sleep(1.75)
        system('cls')
        print("\n========================================================================================================")
        print(f"{enemy.name}'s Stats:")
        print(f"HP: {enemy.hp}  Attack: {enemy.display_attack()}")
        print(f"Hit Chance: {enemy.hit_rate()}%   Crit Chance: {enemy.crit_rate()}%   Evade: {enemy.evade_rate()}%\n")
        print(f"Your Stats")
        print(f"HP: {player.hp}/{player.maxHp}   Attack: {player.display_attack()}   Level: {player.level}   EXP: {player.exp}/{player.expLimit}   Score: {player.score}")
        print(f"Hit Chance: {player.hit_rate()}%   Crit Chance: {player.crit_rate()}%   Parry Chance: {player.parry_rate()}%   Damage Reduction: {player.display_damage_reduction()}%   Evade Chance: {player.evade_rate()}%")
        print("========================================================================================================")
        
        action = prompt("Action:\n1. Attack   2. Parry   3. Use Potion")

        if action == 1:
            if not enemy.evade_check():
                enemy.hp -= player.attack_check()
            else:
                print(f"{enemy.name}: Evade")

            if not player.evade_check():
                player.hp -= ceil(enemy.attack_check() * player.damage_reduction())
            else:
                print("Attack Evaded")

        elif action == 2:
            enemyatk = enemy.attack_check()
            if enemyatk: 
                if player.parry_check():
                    enemy.hp -= enemyatk*0.9
                    player.hp -= enemyatk*0.1 * player.damage_reduction()
                else:
                    player.hp -= enemyatk * player.damage_reduction()

        elif action == 3:
            player.potion_check()

            if player.potion:
                potions = '0. BACK   '
                potionKeys = list(player.potion.keys())
                for i in range(1, len(potionKeys)+1):
                    current = player.potion[potionKeys[i-1]]
                    potions += f"{i}. {current.name} {current.count}/{current.check_limit(player)}   "

                while True:
                    try:
                        action = prompt(f"Available potion(s)\n{potions}")
                        if action == 0:
                            pass
                        elif action < 0:
                            print_s1("Error: Invalid input")
                        else:
                            key = potionKeys[action-1]
                            player.use_potion(key)
                        break
                    except IndexError:
                        print_s1("Error: Invalid input")
                        continue
            else:
                print("Warning: You don't have any potion")
        else:
            print("Error: Invalid input")
        health_check(player)

    exp_check(player, enemy.give_exp())
    sleep(2)
    system('cls')

def weapon_drop(player, weapon):
    system('cls')

    print1("--------------------------------------------------------------------------------------------------------")
    print(f"The enemy dropped a(n) '{weapon.name}'")
    print(f"'{weapon.name}' Stats:")
    print(f"Attack: {weapon.display_attack(player)}   Hit Chance: {weapon.hit_rate(player)}%   Crit Chance: {weapon.crit_rate(player)}%")
    print("\nCurrent weapon:")
    print(f"'{player.weapon.name}' stats:")
    print(f"Attack: {player.display_attack()}   Hit Chance: {player.hit_rate()}%   Crit Chance: {player.crit_rate()}%")
    print("--------------------------------------------------------------------------------------------------------")

    action = prompt(f"Action:\n1. Take {weapon.name}   2. Leave")
    if action == 1:
        player.change_weapon(weapon)
    else:
        print1(f"You leave the {weapon.name}")
    system('cls')

def apparel_drop(player, apparel):
    system('cls')

    print1("--------------------------------------------------------------------------------------------------------")
    print(f"The enemy dropped a(n) '{apparel.name}'")
    print(f"'{apparel.name}' Stats:")
    print(f"Damage Reduction: {apparel.display_damage_reduction(player)}%   Parry Chance: {apparel.parry_rate(player)}%")
    print("\nCurrent Apparel:")
    print(f"'{player.apparel.name}' stats:")
    print(f"Damage Reduction: {player.display_damage_reduction()}%   Parry Chance: {player.parry_rate()}%")
    print("--------------------------------------------------------------------------------------------------------")

    action = prompt(f"Action:\n1. Take {apparel.name}   2. Leave {apparel.name}")
    if action == 1:
        player.change_apparel(apparel)
    else:
        print1(f"You leave the {apparel.name}")
    system('cls')