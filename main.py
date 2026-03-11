"""
Program: The Walking Code
Description: A text-based zombie survival game where the player moves between
locations, rests to recover stamina and health, and survives random zombie
encounters for as long as possible.

Author: Ashton Worcester
Date Created: March 9, 2026

"""

print("Welcome to The Walking Code survive as long as you can.")

import random
from the_walking_code import Player, Location, zombie_encounter


def show_status(player, loc):
    """Display the current player status and location information."""

    print("\n--- STATUS ---")
    print(f"Location: {loc.name}")
    print(f"Name: {player.name}")
    print(f"Health: {player.health}")
    print(f"Stamina: {player.stamina}")
    print(f"Survival Score (turns): {player.score}")
    print("-------------")


def main():
    """Main game loop that controls player actions and zombie encounters."""

    print("=== THE WALKING CODE ===")
    name = input("Enter survivor name: ")
    player = Player(name)

    locations = [
        Location("Abandoned Street", 0.30),
        Location("Grocery Store", 0.45),
        Location("Hospital", 0.55),
        Location("Police Station", 0.50),
        Location("Safehouse", 0.15),
    ]

    current = 0

    while player.alive():
        player.add_score()
        loc = locations[current]
        show_status(player, loc)

        print("\nActions:")
        print("1) Move")
        print("2) Rest")
        print("3) Quit")

        choice = input("Choose (1-3): ").strip()

        while choice not in ["1", "2", "3"]:
            print("Invalid option. Please choose 1, 2, or 3.")
            choice = input("Choose (1-3): ").strip()

        if choice == "1":

            print("\nWhere to?")
            for i, l in enumerate(locations, start=1):
                here = " (you)" if (i - 1) == current else ""
                print(f"{i}. {l.name}{here}")

            pick = input("Location number: ").strip()

            if pick.isdigit():
                idx = int(pick) - 1

                if 0 <= idx < len(locations):
                    current = idx
                else:
                    print("Not a valid location.")

            else:
                print("Not a valid number.")

        elif choice == "2":
            print("You rest for a bit.")
            player.stamina += 20
            player.health += 10

        elif choice == "3":
            print("You quit.")
            break

        # Keep health and stamina from exceeding limits
        if player.stamina > 100:
            player.stamina = 100

        if player.health > 100:
            player.health = 100

        # Random zombie encounter based on location danger level
        if random.random() < loc.danger:
            ok = zombie_encounter(player)

            if not ok:
                break

    print("\n=== GAME OVER ===")
    print(f"Final score: {player.score}")
    print(f"Final health: {player.health}")


if __name__ == "__main__":
    main()