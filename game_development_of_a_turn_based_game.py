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

    # player attack
    def attack(self, enemy):
        if random.random() < self.critical_chance:
            damage = self.attack_power * self.critical_multiplier
            print(f"Critical hit! Dealt {damage} damage.")
        else:
            damage = self.attack_power
            print(f"Normal hit! Dealt {damage} damage.")

        enemy.health -= damage
        print(f"Enemy health is now {enemy.health}.")

    # player heal
    def heal(self):
        self.health += self.heal_amount
        print(f"You healed for {self.heal} health. Your health is now {self.health}.")
        if self.health > 100: 
            self.health = 100
            print("Your health is at maximum (100).")    
    
# initialize enemy data
class Enemy:
    def __init__(self, health, attack_power, critical_chance, critical_multiplier):
        self.health = health
        self.attack_power = attack_power
        self.critical_chance = critical_chance
        self.critical_multiplier = critical_multiplier
        
    def is_alive(self):
        return self.health > 0    
    
    # enemy attack
    def attack(self, player):
        if random.random() < self.critical_chance:
            damage = self.attack_power * self.critical_multiplier
            print(f"Enemy deals critical hit! Dealt {damage} damage.")
        else:
            damage = self.attack_power
            print(f"Enemy deals normal hit! Dealt {damage} damage.")

        player.health -= damage
        print(f"Your health is now {player.health}.")

# stats for ogre
class Ogre(Enemy):
    def __init__(self):
        super().__init__(health=120, attack_power=10, critical_chance=0.08, critical_multiplier=2)

# stats for troll
class Troll(Enemy):
    def __init__(self):
        super().__init__(health=150, attack_power=7, critical_chance=0.12, critical_multiplier=3)        
    # troll heal every turn
    def attack(self, player):
        super().attack(player)
        self.health += 5
        print(f"Troll heals for 5 health. Troll's health is now {self.health}.")
        if self.health > 150: 
            self.health = 150
            print("Troll's health is at maximum (150).")

def main():
    player = Player()
    # Choose an enemy type
    enemy_choice = input("Choose your enemy: (1) Ogre, (2) Troll: ")
    if enemy_choice == '1':
        enemy = Ogre()
    elif enemy_choice == '2':
        enemy = Troll()
    else:
        print("Invalid choice. Defaulting to Ogre.")
        enemy = Ogre()

    while player.is_alive() and enemy.is_alive():
        action = player.action_choice()

        if action == 1:
            player.attack(enemy)
        elif action == 2:
            player.heal()

        if enemy.is_alive():
            enemy.attack(player)

    if player.is_alive():
        print("Congratulations! You defeated the enemy.")
    else:
        print("Game over! You were defeated by the enemy.")

if __name__ == "__main__":
    main()             