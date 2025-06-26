import math
import random

# initialize player data
class Player:
    def __init__(self, health=100, heal_amount=25, attack_power=12, critical_chance=0.10, critical_multiplier=2):
        self.health = health
        self.heal_amount = heal_amount
        self.attack_power = attack_power
        self.critical_chance = critical_chance
        self.critical_multiplier = critical_multiplier

    def is_alive(self):
        return self.health > 0    

    # player action choices, (1 = attack, 2 = heal)
    def action_choice(self):
        while True:
            try:
                choice = int(input("Choose your action: (1) Attack, (2) Heal: "))
                if choice in [1, 2]:
                    return choice
                else:
                    print("Invalid choice. Please choose 1 or 2.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    
# initialize enemy data
class Enemy:
    def __init__(self, health=140, attack_power=10, critical_chance=0.8, critical_multiplier=2):
        self.health = health
        self.attack_power = attack_power
        self.critical_chance = critical_chance
        self.critical_multiplier = critical_multiplier
        
    def is_alive(self):
        return self.health > 0    
            