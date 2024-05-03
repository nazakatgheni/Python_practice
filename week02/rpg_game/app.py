import random
from classes.food import Food
from classes.player import Player
from classes.weapon import Weapon


player = Player("Fred")

is_playing = True

print(f"Welcome to the game, {player.name}!")
print("Type 'help' for a list of commands.")

# our game loop
while is_playing:

    print(f"\nYour strength is {player.strength}.")
    # build-in function
    # we passing info in terminal and it will pass info
    command = input("Enter a command: ")

    if command == "quit":
        is_playing = False

    elif command == "help":
        print("\nAvailable commands:")
        print("\nquit - quits the game")
        print("help - prints this help message")
        
        
        # validate
    elif command == "walk":
        """
        choose a direction
        distance/speed
        energy reduction
        feedback - "you walked"
        """
        direction = input("Which direction? (e, w, n, s): ")
        if direction not in "ewns":
            print("\nYou can not walk that way")
            continue
        print("\n You Walk"
            + {
                "e": "East",
                "w": "West",
                "n": "North",
                "s": "South"
            }[direction])
        
        if player.walk() == 0:
            print("You died")
            
            
        
print("Thanks for playing!")