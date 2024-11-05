# PyGame

Task: Terminal-Based Space Battle Simulation
Objective:
Create a simple terminal-based game where two teams of space fighters (starships) engage in a battle. The teams will consist of different types of starships, each with varying attributes such as health, attack damage, and special abilities. The battle will be simulated by randomly determining the outcome of attacks until one team is victorious.

Concepts Covered:

Classes and Objects
Inheritance
Functions and Methods
Randomization
Game Details
Starship Classes:

Create a base class called Starship.
Each starship has attributes:
name (string)
health (integer)
attack_damage (integer)
Each starship has a method attack(target) which reduces the target's health by the starship's attack damage.
Starship Types:

Create subclasses for different starship types:
Fighter: A fast, low-health ship with high attack damage.
Bomber: A slow, high-health ship with moderate attack damage.
Interceptor: A balanced ship with moderate health and attack damage but has a 50% chance to dodge an attack.
Special Abilities:

Implement unique methods for special abilities:
Interceptor: Override the attack() method to include a dodge mechanic where it avoids an attack 50% of the time.
Bomber: Introduce a method heavy_bomb() that deals double damage but has a cooldown of 2 turns.
Teams:

Create two teams of starships. Each team should have a mix of the three types.
The teams will take turns attacking each other until all ships on one team are destroyed.
Battle Logic:

Write a function battle(team1, team2) that runs the battle simulation:
The function should print the status of each starship after every round.
The function should randomly decide which starship attacks which on the opposing team.
Continue until all starships on one team are destroyed.
Declare the winning team.
Game Loop:

Allow the user to create and customize their teams by selecting types of starships.
Start the battle when teams are ready.