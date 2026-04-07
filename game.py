#BEGIN Guess the Number Game
# SETUP
    #- The computer picks a random number between 1 and 100 (player tries to guess it)
   # - Create a variable to count how many guesses the player makes
   # - return score at the end
# GAMEPLAY
  #  - Keep asking the player for a guess until they get it right
   # - After each wrong guess, tell them if their guess was too high or too low
#- Add 1 to the guess count every time they guess
# END OF GAME
   # - When they guess correctly, tell them their scores
   #   returns the score
# SAMPLE OUTPUT
  #  Enter your name: Alex
  #  Guess a number between 1 and 100: 40
  #  Too low, try again
  #  Guess a number between 1 and 100: 82
  #  Too high, try again
  #  Guess a number between 1 and 100: 62
  #  Yor score was 3


def game():
    import random
    import json

    # SETUP
    print("Welcome to the Guess the Number Game!")
    name = input("Enter your name: ")

    # Computer picks a random number
    secret_number = random.randint(1, 100)

    # Create variable to count guesses
    guesses = 0

    # GAMEPLAY
    while True:
        # Get player's guess
        guess = int(input("Guess a number between 1 and 100: "))
        
        # Add 1 to guess count
        guesses = guesses + 1
        
        # Check if guess is correct
        if guess == secret_number:
            # END OF GAME
            print("Yor score was " + str(guesses))
            
            # SAVE TO CSV
            # Open the file in append mode
            file = open("scores.json", "a")
            
            # Write the name and score to the file
            file.write(name + "," + str(guesses) + "\n")
            
            # Close the file
            file.close()
            
            print("Your score has been saved to scores.json!")
            break
        
        # Give hints if wrong
        elif guess < secret_number:
            print("Too low, try again")
        
        else:
            print("Too high, try again")

    # OPTIONAL: Show all previous scores
    print("\nDo you want to see all past scores? (yes/no)")
    see_scores = input()

    if see_scores == "yes":
        try:
            file = open("scores.json", "r")
            print("\n=== PAST SCORES ===")
            for line in file:
                # Split each line into name and score
                parts = line.strip().split(",")
                if len(parts) == 2:
                    print(parts[0] + ": " + parts[1] + " guesses")
            file.close()
        except:
            print("No scores found yet!")

    #can be saved to JSON FILE

game()
