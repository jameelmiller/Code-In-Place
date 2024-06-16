import random

def main():
    # Gather player information 
    name = input("What is your name? ")
    team_name = input("What is the name of your team? ")
    print("Hello " + name + ", With the 1st pick of the Draft, you have been selected by " + team_name + "!")

    # Explain the rules of the game
    print("Rules of the Game:")
    print("1. You will play 3 rounds against Lebrobot James.")
    print("2. In each round, you can choose one of the following moves:")
    print("   - Pass: Beats Kick")
    print("   - Run: Beats Pass")
    print("   - Kick: Beats Run")
    print("3. The computer will also choose a move.")
    print("4. The winner of each round is determined by the rules above.")
    print("5. The scores will be updated after each round.")
    print("6. The game ends after 3 rounds, and the player with the highest score wins.")
    print("7. If the scores are tied after 3 rounds, the game is a tie.")
    print("8. After the game, you will have the option to play again.")
    
    choices = ['Pass', 'Run', 'Kick']
    rounds = 3

    while True:
        player_score = 0
        computer_score = 0

        for round_number in range(1, rounds + 1):
            # Implement Player Input and Validation
            print("Round " + str(round_number))
            print("Choose one of the following:")
            print("1. Pass")
            print("2. Run")
            print("3. Kick")
            
            user_choice = input("Enter the number of your choice: ")
            
            if user_choice not in ['1', '2', '3']:
                print("Invalid choice. Please enter 1, 2, or 3.")
                continue
            
            user_choice = int(user_choice) - 1
            player_move = choices[user_choice]

            # Generate Computer Move
            computer_choice = random.randint(0, 2)
            computer_move = choices[computer_choice]
            
            print("You chose: " + player_move)
            print("Lebrobot chose: " + computer_move)

            # Determine Round Outcome
            if player_move == computer_move:
                print("It's a tie!")
            elif (player_move == 'Pass' and computer_move == 'Kick') or \
                 (player_move == 'Run' and computer_move == 'Pass') or \
                 (player_move == 'Kick' and computer_move == 'Run'):
                print(name + " from " + team_name + " wins this round!")
                player_score += 1
            else:
                print("Lebrobot wins this round!")
                computer_score += 1

            # Display Round Results
            print("Scores => " + name + ": " + str(player_score) + ", Lebrobot: " + str(computer_score))

        # Declare Overall Winner
        print("Game Over!")
        print("Final Scores => " + name + ": " + str(player_score) + ", Lebrobot: " + str(computer_score))
        if player_score > computer_score:
            print(name + " from " + team_name + " wins the game!")
        elif player_score < computer_score:
            print("Lebrobot wins the game!")
        else:
            print("The game is a tie!")

        # Replay Option
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == '__main__':
    main()

