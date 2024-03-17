from art import logo
import random

EASY_DIFFICULTY = 10
HARD_DIFFICULTY = 5

def play_game():
    print(logo)
    number = random.randint(1, 100)
    print(f"welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\nPssst, the correct answer is {number}")
    difficulty_level = input("Choose a difficulty. Type 'easy' to or 'hard' to: ").casefold()

    if difficulty_level == 'hard':
        lives = HARD_DIFFICULTY
    else: 
        lives = EASY_DIFFICULTY

    print(f"You have {lives} attempts")

    while lives != 0 or number == guess:
        guess = int(input("Make a guess: "))
        if guess < number:
            lives -= 1
            if lives == 0:
                print(f"You've run out of guesses, you lose.")
            else:    
                print(f"Too low\nGuess again.\nYou have {lives} attempts remaining to guess the number")
        elif guess > number:
            lives -= 1
            if lives == 0:
                print(f"You've run out of guesses, you lose.")
            else:
                print(f"Too high\nGuess again.\nYou have {lives} attempts remaining to guess the number")
        else:
            print(f"You got it! The answer was {number}")
            break

while input("Do you want to play the Number Guessing Game? 'y'/'n': ") == 'y':
    if __name__ == '__main__':
        play_game()