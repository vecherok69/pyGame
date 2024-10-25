from team_creation import create_team, ask_for_default_team
from battle import battle

def show_ascii_spaceship():
    spaceship_art = """
                 .
                .:.
               .::.
              .:::.
             .::::.
         ***.:::::::.***
      ****** ::::::: ****** 
   ******** ::::::::: ********
 *********** ::::::::: ***********
************* ::::::::: *************
 ************ ::::::::: ************
  *********** ::::::::: ***********
   ********** ::::::::: **********
     *******  :::::::::  *******
       *****   :::::::   *****
        ***     :::::     ***
                 :::::
                  ::::
                  :::
                   :
    """
    print(spaceship_art)

def show_welcome_message():
    print("===============================================")
    print("  Welcome to the Space Battle Simulation Game!  ")
    print("===============================================\n")
    print("In this game, you'll create a team of 3 starships and battle against another team.")
    print("Here are the available ship types and their abilities:\n")

    print("1. Fighter (Fast attack ship)")
    print("   - HP: 50, ATK: 30")
    print("   - Ability: Critical Strike")
    print("     -> 13% chance to deal 150% damage on an attack.\n")

    print("2. Bomber (High-health heavy attacker)")
    print("   - HP: 100, ATK: 20")
    print("   - Ability: Heavy Bomb")
    print("     -> Deals double damage but has a 2-turn cooldown.\n")

    print("3. Interceptor (Ship with dodge ability)")
    print("   - HP: 75, ATK: 25")
    print("   - Ability: Dodge")
    print("     -> 25% chance to dodge attacks.\n")

    print("4. Support (Healer of the team)")
    print("   - HP: 80, ATK: 10")
    print("   - Ability: Heal")
    print("     -> Heals the ship with the lowest HP on its team for 10 health.")
    print("        Have a 2-turn cooldown.\n")

    print("Your goal is to choose ships strategically and defeat the opposing team. Good luck!\n")

def main():
    show_ascii_spaceship()

    show_welcome_message()

    if ask_for_default_team():
        team1 = create_team("Team 1", predefined=True)
        team2 = create_team("Team 2", predefined=True)
    else:
        team1 = create_team("Team 1")
        team2 = create_team("Team 2")

    battle(team1, team2)

if __name__ == "__main__":
    main()
