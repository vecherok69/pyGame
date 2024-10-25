from starship import Fighter, Bomber, Interceptor, Support

def battle(team1, team2):
    print("\n--- Battle Begins! ---")
    round_count = 1
    team1_index = 0
    team2_index = 0

    while team1 and team2:
        print(f"\n========== Round {round_count} ==========")
        round_count += 1

        print("\nTeam 1's Turn:")
        attacker = team1[team1_index]
        team1_index = (team1_index + 1) % len(team1)

        if isinstance(attacker, Support):
            if attacker.heal_cooldown > 0:
                print(f"{attacker.name}'s heal is on cooldown. Performing attack instead.")
                defender = team2[team2_index]
                attacker.attack(defender)
            else:
                attacker.heal(team1)
        else:
            defender = team2[team2_index]
            if isinstance(defender, Interceptor) and defender.dodge():
                print(f"{defender.name} dodged the attack from {attacker.name}!")
            else:
                attacker.attack(defender)

        if defender.is_destroyed():
            #print(f"{defender.name} has been destroyed!")
            if defender in team2:
                #print(f"Removing {defender.name} from team 2")
                team2.remove(defender)
                if len(team2) > 0:
                    team2_index %= len(team2)
            elif defender in team1:
                #print(f"Removing {defender.name} from team 1")
                team1.remove(defender)
                if len(team1) > 0:
                    team1_index %= len(team1)

        if not team2:
            print("\n========== Team 1 Wins the Battle! ==========")
            break

        print("\nTeam 2's Turn:")
        attacker = team2[team2_index]
        team2_index = (team2_index + 1) % len(team2)

        if isinstance(attacker, Support):
            if attacker.heal_cooldown > 0:
                print(f"{attacker.name}'s heal is on cooldown. Performing attack instead.")
                defender = team1[team1_index]
                attacker.attack(defender)
            else:
                attacker.heal(team2)
        else:
            defender = team1[team1_index]
            if isinstance(defender, Interceptor) and defender.dodge():
                print(f"{defender.name} dodged the attack from {attacker.name}!")
            else:
                attacker.attack(defender)

        if defender.is_destroyed():
            #print(f"{defender.name} has been destroyed!")
            if defender in team2:
                #print(f"Removing {defender.name} from team 2")
                team2.remove(defender)
                if len(team2) > 0:
                    team2_index %= len(team2)
            elif defender in team1:
                #print(f"Removing {defender.name} from team 1")
                team1.remove(defender)
                if len(team1) > 0:
                    team1_index %= len(team1)

        if not team1:
            print("\n========== Team 2 Wins the Battle! ==========")
            break

        for ship in team1 + team2:
            if isinstance(ship, Support):
                ship.end_turn()

        print("\n--- Team 1 Status ---")
        for ship in team1:
            print(ship)

        print("\n--- Team 2 Status ---")
        for ship in team2:
            print(ship)

    # Battle Result
    if team1:
        print("\n========== Battle Result ==========")
        print("Team 1 wins!")
        print("Surviving ships in Team 1:")
        for ship in team1:
            print(f"  - {ship}")
    elif team2:
        print("\n========== Battle Result ==========")
        print("Team 2 wins!")
        print("Surviving ships in Team 2:")
        for ship in team2:
            print(f"  - {ship}")

    print("\n========== Battle Over ==========")
