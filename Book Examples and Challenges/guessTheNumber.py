# This is a guess the number game.
import random

def startGame():
    secretNumber = random.randint(1, 20)
    print('I am thinking of a number between 1 and 20.')

    # Ask the player to guess up to 6 times
    for guessesTaken in range(1, 7):
        print('Take a guess.')
        try:
            guess = int(input())
            
            if guess < secretNumber:
                print('Your guess is too low.')
            elif guess > secretNumber:
                print('Your guess is too high.')
            else:
                break # This condition is the correct guess!
        except ValueError:
            print('Please select a number between 1 and 20.')
    try:
        if guess == secretNumber:
            print('Good Job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
        else:
            print('Nope. The number I was thinking of was ' + str(secretNumber))
    except UnboundLocalError:
         print('Nope. The number I was thinking of was ' + str(secretNumber))
    restart()

def restart():
    print('Do you want to play again? (yes or no)')
    choice = input()
    if choice == 'yes':
        startGame()
    elif choice == 'no':
        print('Ok...')
    else:
        print('Please choose yes or no')
        restart()


startGame()
