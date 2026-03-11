"""
Program: The Walking Code
Description: This file contains the Player and Location classes, along with
the zombie encounter function used in the game.

Author: Ashton Worcester
Date Created: March 9, 2026

"""

import random


class Player:
    """Represent the player and track their survival stats."""

    def __init__(self, name):
        """Initialize a player with a name, health, stamina, and score."""
        self._name = name.strip() if name.strip() else "Survivor"
        self._health = 100
        self._stamina = 100
        self._score = 0

    @property
    def name(self):
        """Return the player's name."""
        return self._name

    @name.setter
    def name(self, v):
        """Set the player's name, or use 'Survivor' if blank."""
        if v.strip() == "":
            self._name = "Survivor"
        else:
            self._name = v

    @property
    def health(self):
        """Return the player's health."""
        return self._health

    @health.setter
    def health(self, v):
        """Set the player's health between 0 and 100."""
        if v < 0:
            self._health = 0
        elif v > 100:
            self._health = 100
        else:
            self._health = v

    @property
    def stamina(self):
        """Return the player's stamina."""
        return self._stamina

    @stamina.setter
    def stamina(self, v):
        """Set the player's stamina between 0 and 100."""
        if v < 0:
            self._stamina = 0
        elif v > 100:
            self._stamina = 100
        else:
            self._stamina = v

    @property
    def score(self):
        """Return the player's survival score."""
        return self._score

    def add_score(self):
        """Increase the player's score by one turn."""
        self._score += 1

    def alive(self):
        """Return True if the player is still alive."""
        return self._health > 0


class Location:
    """Represent a game location and its danger level."""

    def __init__(self, name, danger):
        """Initialize a location with a name and danger value."""
        self._name = name
        self._danger = danger

    @property
    def name(self):
        """Return the location name."""
        return self._name

    @property
    def danger(self):
        """Return the danger level of the location."""
        return self._danger


def zombie_encounter(player):
    """Run a zombie encounter and return True if the player survives."""
    zombie_hp = random.randint(20, 40)
    print("\nZombie encounter!")

    while zombie_hp > 0 and player.alive():
        print(f"Zombie HP: {zombie_hp} | Your HP: {player.health} | Stamina: {player.stamina}")
        choice = input("Fight (f) or Run (r)? ").strip().lower()

        while choice not in ["f", "r"]:
            print("Invalid option. Please enter 'f' to fight or 'r' to run.")
            choice = input("Fight (f) or Run (r)? ").strip().lower()

        if choice == "r":
            if player.stamina < 10:
                print("You're too tired to run!")
            else:
                player.stamina -= 10
                if random.random() < 0.6:
                    print("You got away.")
                    return True
                else:
                    print("You failed to escape and got grabbed!")

        if player.stamina >= 5:
            player.stamina -= 5
            dmg = random.randint(8, 15)
        else:
            dmg = random.randint(1, 4)

        zombie_hp -= dmg
        print(f"You hit for {dmg}!")

        if zombie_hp > 0:
            z_dmg = random.randint(6, 14)
            player.health -= z_dmg
            print(f"The zombie hits you for {z_dmg}!")

    if player.alive():
        print("You survived.")
        return True

    print("You died.")
    return False