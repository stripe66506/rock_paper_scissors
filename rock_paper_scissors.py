import random
import time
import sys

print("""The rules of the game: 
Rock beats Scissors, Scissors beats Paper, Paper beats Rock""")

print('\n1 = Rock\n2= Paper\n3= Scissors')
user = input("What is your name?: ")

def the_game():
    print("LET THE GAMES BEGIN!")

    player_score = 0
    computer_score = 0
    games_played = 0

    while True:
        while True:
            try:
                player = int(input('Rock(1), Paper(2), Scissors(3)....shoot!: '))
                if player not in [1, 2, 3]:
                    print('Enter a valid choice please! :-)')
                else:
                    break
            except ValueError:
                print('Please enter a valid number! :-)')

        if player == 1:
            player_choice = 'rock'
        elif player == 2:
            player_choice = 'paper'
        else:
            player_choice = 'scissors'

        print(f'\nYou chose {player_choice}!')

        print('The computer is thinking...', end='', flush=True)
        for _ in range(10):  # 10 cycles of spinner
            for cursor in '|/-\\':  # Spinner characters
                sys.stdout.write(cursor)
                sys.stdout.flush()
                time.sleep(0.1)  # Short delay
                sys.stdout.write('\b')  # Use backspace to remove the previous character

        computer_choice = random.randint(1,3)

        if computer_choice == 1:
            comp_choice = 'rock'
        elif computer_choice == 2:
            comp_choice = 'paper'
        else:
            comp_choice = 'scissors'

        print(f'\nThe computer chose {comp_choice}')

        print(f'Human:{player_choice} vs Computer:{comp_choice}')

        if player_choice == comp_choice:
            print('\nDraw')
            print(f'Round ' + str(games_played + 1)  + ' out of 10.')
            print(f'Your score is {player_score}, computer core is {computer_score}.')

        elif (player_choice == 'rock' and comp_choice == 'paper'):
                print('\nPaper covers rock.(Computer wins!)')
                print(f'Round ' + str(games_played + 1)  + ' out of 10.')
                computer_score += 1
                print(f'Your score is {player_score}, computer core is {computer_score}.')
        elif (player_choice == 'rock' and comp_choice == 'scissors'):
                print('\nRock beats Scissors.(You win!)')
                print(f'Round ' + str(games_played + 1)  + ' out of 10.')
                player_score += 1
                print(f'Your score is {player_score}, computer core is {computer_score}.')

        elif (player_choice == 'paper' and comp_choice == 'rock'):
                print('\nPaper covers Rock.(You win!)')
                print(f'Round ' + str(games_played + 1)  + ' out of 10.')
                player_score += 1
                print(f'Your score is {player_score}, computer core is {computer_score}.')

        elif (player_choice == 'paper' and comp_choice == 'scissors'):
                print('\nScissors cut Paper.(Computer wins!)')
                print(f'Round ' + str(games_played + 1)  + ' out of 10.')
                computer_score += 1
                print(f'Your score is {player_score}, computer core is {computer_score}.')

        elif (player_choice == 'scissors' and comp_choice == 'rock'):
                print('\nRock beats Scissors.(Computer wins!)')
                print(f'Round ' + str(games_played + 1)  + ' out of 10.')
                computer_score += 1
                print(f'Your score is {player_score}, computer core is {computer_score}.')

        elif (player_choice == 'scissors' and comp_choice == 'paper'):
                print('\nScissors cut Paper.(You win!)')
                print(f'Round ' + str(games_played + 1)  + ' out of 10.')
                player_score += 1
                print(f'Your score is {player_score}, computer core is {computer_score}.')

        games_played += 1

        if games_played == 10:  # Break the loop after 10 rounds
            break

    while True:
        ans = input('Do you want to play again? (Y/N) ').lower()
        if ans in ['y', 'n']:
            break
        else:
            print("Invalid input! Please enter either 'Y' for yes or 'N' for no.")

    if ans == 'n':
        print(f'\n{user} scored {player_score}.')
        print(f'Computer score {computer_score}')

        if player_score > computer_score:
            print('\nYou win!')

        elif player_score == computer_score:
            print('\nDraw!')

        else:
            print('\nComputer wins!')

    else:
        the_game()

the_game()

