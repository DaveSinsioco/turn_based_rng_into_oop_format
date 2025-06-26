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
        if self.health > 100:  # Assuming max health is 100
            self.health = 100
            print("Your health is at maximum (100).")    
    
# initialize enemy data
class Enemy:
    def __init__(self, health=140, attack_power=10, critical_chance=0.8, critical_multiplier=2):
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

# main loop
def main():
    player = Player()
    enemy = Enemy()

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