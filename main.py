import random

def roll_die():    
    return random.randint(1, 6)

while True:
    players = input("Enter the number of players (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 and 4 players!")
    else: 
        print("Invalid number of players. Try again!")

target_score = 50

while True:
    player_scores = [0 for _ in range(players)]

    while max(player_scores) < target_score:
        for player_idx in range(players):
            print("\n--> Player {}'s turn has started".format(player_idx + 1))
            print("Your total score is: {}".format(player_scores[player_idx]), "\n")
            current_score = 0

            while True:
                ask_to_roll = input("Would you like to roll? (y): ")
                if ask_to_roll.lower() != "y":
                    break
                value = roll_die()
            
                if value == 1:
                    print("You rolled a 1. Your turn is over!")
                    current_score = 0
                    break
                else: 
                    current_score += value
                    print("You rolled a {}!".format(value))
                    
                print("Current score: {}".format(current_score))
                
            player_scores[player_idx] += current_score
            print("Player {}'s score: {}".format(player_idx + 1, current_score))

    winning_score = max(player_scores)
    winning_players = [i for i, score in enumerate(player_scores) if score == winning_score]
    
    if len(winning_players) == 1:
        print("Congratulations! Player {} won the game with a total score of {}".format(winning_players[0] + 1, winning_score))
    else:
        players_str = ', '.join(str(player + 1) for player in winning_players)
        print("It's a tie! Players {} have the highest score of {}".format(players_str, winning_score))

    replay = input("Do you want to play again? (y/n): ")
    if replay.lower() != 'y':
        print("Thanks for playing!")
        break