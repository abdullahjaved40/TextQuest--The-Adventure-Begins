# Ask the player for their name
name = input("Hey type your name: ")
print("Hello " + name + " welcome to my game!")

# Ask if the player wants to play the game
should_we_play = input("Do you want to play? ").lower()

# If player agrees to play, proceed
if should_we_play == "y" or should_we_play == "yes":
    print("We are gonna play!")

    # First decision: direction choice
    direction = input("Do you want to go left or right? (left/right) ").lower()

    if direction == "left":
        # Player chose left and loses
        print("You went left and fell of a cliff, game over, try again.")
    elif direction == "right":
        # Player chose right, now another choice
        choice = input(
            "Okay, you now see a bridge, do you want to swim under it or cross it? (swim/cross) ")
        if choice == "swim":
            # Player swims and loses
            print("You got eaten by an alligator, you die, the end!")
        else:
            # Player crosses and wins
            print("You found the gold and won!")
    else:
        # Invalid direction input
        print("Sorry not a valid reply, you die!")

else:
    # Player chose not to play
    print("We are NOT playing...")
