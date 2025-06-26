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

# initialize enemy data
class Enemy:
    def __init__(self, health=140, attack_power=10, critical_chance=0.8, critical_multiplier=2):
        self.health = health
        self.attack_power = attack_power
        self.critical_chance = critical_chance
        self.critical_multiplier = critical_multiplier
        
    def is_alive(self):
        return self.health > 0    
            