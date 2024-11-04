import random


def roll():

    min_value = 1
    max_value = 6

    roll = random.randint(1, 6)

    return roll


while True:

    players = input("Enter the number of players (2 - 4): ")

    if players.isdigit():

        players = int(players)

        if players in range(2, 5):

            break

        print("Must be between 2 - 4 players.")

    else:

        print("Invalid, try again.")


max_score = 50

players_scores = [0] * players


while max(players_scores) < max_score:

    for player_index in range(players):

        print(f"\nPlayer {player_index+1} turn has just started!")

        print("Your total score till this turn is", players_scores[player_index], "\n")

        current_score = 0

        while True:

            should_roll = input("Would you like to roll (y)? ").lower()

            if should_roll != 'y':

                break

            value = roll()

            if value == 1:

                print("You rolled a 1! Turn done!")

                current_score = 0

                break

            current_score += value

            print("You rolled a:", value)

            print("Your score is:", current_score)

        players_scores[player_index] += current_score


winner_ind = players_scores.index(max(players_scores))

winner = winner_ind + 1

print(f"\nCongrats, Player {winner}!!!! \nYou won the game.\n\nTotal scores are:\n")

for player_index in range(len(players_scores)):

    print(f"Player {player_index+1}: {players_scores[player_index]}")

print()
