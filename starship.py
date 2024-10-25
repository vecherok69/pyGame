import random

class Starship:
    def __init__(self, name, health, attack_damage):
        self.name = name
        self.health = health
        self.max_health = health
        self.attack_damage = attack_damage

    def attack(self, target):
        print(f"{self.name} attacks {target.name} for {self.attack_damage} damage!")
        target.health -= self.attack_damage
        if target.health < 0:
            target.health = 0

    def is_destroyed(self):
        return self.health <= 0

    def __str__(self):
        return f"{self.name} (HP: {self.health}/{self.max_health}, ATK: {self.attack_damage})"


class Fighter(Starship):
    def __init__(self, name):
        super().__init__(name, health=50, attack_damage=30)
        self.max_health = 50

    def attack(self, target):
        crit_chance = 0.13
        if random.random() < crit_chance:
            crit_damage = int(self.attack_damage * 1.5)
            print(f"CRITICAL STRIKE! {self.name} deals {crit_damage} damage to {target.name}!")
            target.health -= crit_damage
        else:
            super().attack(target)

    def __str__(self):
        return f"Fighter {self.name} - HP: {self.health}/{self.max_health}, ATK: {self.attack_damage}"


class Bomber(Starship):
    def __init__(self, name):
        super().__init__(name, health=100, attack_damage=20)
        self.max_health = 100
        self.bomb_cooldown = 0

    def attack(self, target):
        if self.bomb_cooldown == 0:
            print(f"{self.name} uses Heavy Bomb!")
            double_damage = self.attack_damage * 2
            target.health -= double_damage
            print(f"{self.name} deals {double_damage} damage!")
            self.bomb_cooldown = 2
        else:
            print(f"{self.name}'s Heavy Bomb is on cooldown, performing normal attack.")
            super().attack(target)

    def end_turn(self):
        if self.bomb_cooldown > 0:
            self.bomb_cooldown -= 1

    def __str__(self):
        return f"Bomber {self.name} - HP: {self.health}/{self.max_health}, ATK: {self.attack_damage}"


class Interceptor(Starship):
    def __init__(self, name):
        super().__init__(name, health=75, attack_damage=25)
        self.max_health = 75

    def dodge(self):
        dodge_chance = 0.25
        return random.random() < dodge_chance

    def take_damage(self, damage):
        if self.dodge():
            print(f"{self.name} dodges the attack!")
        else:
            self.health -= damage
            if self.health < 0:
                self.health = 0

    def __str__(self):
        return f"Interceptor {self.name} - HP: {self.health}/{self.max_health}, ATK: {self.attack_damage}"


class Support(Starship):
    def __init__(self, name):
        super().__init__(name, health=80, attack_damage=10)
        self.max_health = 80
        self.heal_cooldown = 2

    def heal(self, team):
        if not team:
            return

        if self.heal_cooldown > 0:
            print(f"{self.name}'s healing is on cooldown. Cooldown remaining: {self.heal_cooldown} turns.")
            return

        healable_ships = [ship for ship in team if ship != ship.is_destroyed() and ship.health < ship.max_health]

        if not healable_ships:
            print(f"{self.name} has no allies to heal!")
            return

        lowest_hp_ship = min(healable_ships, key=lambda ship: ship.health)

        heal_amount = 10
        new_health = min(lowest_hp_ship.health + heal_amount, lowest_hp_ship.max_health)
        actual_heal = new_health - lowest_hp_ship.health

        lowest_hp_ship.health = new_health
        print(f"{self.name} heals {lowest_hp_ship.name} for {actual_heal} HP!")

        self.heal_cooldown = 2

    def attack(self, target):
        super().attack(target)

    def end_turn(self):
        if self.heal_cooldown > 0:
            self.heal_cooldown -= 1

    def __str__(self):
        return f"Support {self.name} - HP: {self.health}/{self.max_health}, ATK: {self.attack_damage}"
