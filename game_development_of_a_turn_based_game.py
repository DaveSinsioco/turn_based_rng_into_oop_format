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