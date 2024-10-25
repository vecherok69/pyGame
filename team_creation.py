from starship import Fighter, Bomber, Interceptor, Support

def default_teams():
    return [
        [Fighter("Alpha"), Bomber("Bravo"), Support("Charlie")],  # Team 1: Fighter, Bomber, Support
        [Interceptor("Delta"), Support("Echo"), Fighter("Foxtrot")],  # Team 2: Interceptor, Support, Fighter
        [Bomber("Golf"), Fighter("Hotel"), Support("India")],  # Team 3: Bomber, Fighter, Support
        [Support("Juliet"), Interceptor("Kilo"), Bomber("Lima")],  # Team 4: Support, Interceptor, Bomber
        [Fighter("Mike"), Support("November"), Interceptor("Oscar")],  # Team 5: Fighter, Support, Interceptor
        [Support("Papa"), Fighter("Quebec"), Bomber("Romeo")]  # Team 6: Support, Fighter, Bomber
    ]

def display_default_teams(teams):
    print("\nAvailable Default Teams:")
    for i, team in enumerate(teams):
        print(f"Team {i + 1}:")
        for ship in team:
            print(f"  - {ship}")

def create_team(team_name, predefined=False):
    if predefined:
        teams = default_teams()
        display_default_teams(teams)

        while True:
            try:
                choice = int(input(f"\nChoose a default team for {team_name} (1-6): ")) - 1
                if 0 <= choice < len(teams):
                    return teams[choice]
                else:
                    print("Invalid choice, please select a number between 1 and 6.")
            except ValueError:
                print("Invalid input, please enter a valid number.")
    else:
        team = []
        support_in_team = False

        print(f"Creating team {team_name}:")
        for i in range(3):
            ship_name = input(f"Enter name for {team_name} ship {i + 1}: ").strip()

            while True:
                ship_type = input(
                    f"Choose ship type for {team_name} ship {i + 1} (Fighter, Bomber, Interceptor, Support): ").strip().lower()

                if ship_type == "fighter":
                    team.append(Fighter(ship_name))
                    break
                elif ship_type == "bomber":
                    team.append(Bomber(ship_name))
                    break
                elif ship_type == "interceptor":
                    team.append(Interceptor(ship_name))
                    break
                elif ship_type == "support":
                    if support_in_team:
                        print("You can only have one Support ship in a team. Please choose another type.")
                    else:
                        team.append(Support(ship_name))
                        support_in_team = True  # Set the flag to True to prevent adding another Support ship
                        break
                else:
                    print("Invalid ship type. Please enter Fighter, Bomber, Interceptor, or Support.")

        return team

def ask_for_default_team():
    while True:
        use_default = input("Do you want to use a predefined team? (yes/no): ").strip().lower()
        if use_default == "yes":
            return True
        elif use_default == "no":
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
