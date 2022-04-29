import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
swap = 1

'''Function creates random card hit, then returns card to hand that funct. is being called upon.
'''
def hit():
    new_card = int(random.choice(cards))
    return new_card

'''Function primarily used for funct. player_turn, draws starting hand. 
    takes player_hand list as parameter to add into list. 
    '''
def first_hand(user):
    for _ in range(2):
        new_card = hit()
        user.append(new_card)

'''Function that serves as player's turn. 
    - Starts with list with 2 'cards' already inserted then starts while loop to finish turn.
    - While loop checks player's total, then determines if total's sum end's loop if total is over 21.
        - If required number not reached, then player input controls rest.
    -RETURNS player_hand list of cards that were added.
    '''
def player_turn(comp_card):
    player_hand = []
    first_hand(player_hand)
    print("Player goes first.")
    comp_first_card = comp_card

    player_go = True

    while player_go:

        print(f"Computer's first card is: {comp_first_card}\n")
        
        print("Player's Turn.")
        player_sum = sum(player_hand)
   
        if player_sum == 21:
            print("Blackjack!!\n")
            return player_hand

        elif player_sum > 21:
            if 11 in player_hand:
                print("Switching 11 for 1")
                player_hand[player_hand.index(11)] = swap
                player_sum += swap
                continue

            else:
                print("Player Busts!\n")
                return player_hand
            
        player_ans = input(f"Your hand: {player_hand}, your total: {player_sum}. Take a hit? Type 'y' or 'n': ").lower()

        if player_ans == 'y':
            print("Player is taking another hit.")
            player_hit = hit()
            player_hand.append(player_hit)
            player_sum += player_hit
            continue
        
        else:
            print("Player finishes turn\n")
            return player_hand
                
'''Function for computer's turn:
    - Starts with list to hold computer's hand and inserts 2 cards.
    - While loop to calculate computer's sum and determine next actions:
        - Computer hand is required to take more cards if sum is < 17.
    -RETURNS computer_hand list of cards added. '''
def computer_turn(comp_card):
    
    computer_hand = []
    comp_first_card = comp_card
    computer_hand.append(comp_first_card)

    for _ in range(1):
        new_card = hit()
        computer_hand.append(new_card)

    computer_go = True

    while computer_go:
        print("Computer's turn.")

        computer_sum = sum(computer_hand)

        # print(f"Computer Hand: {computer_hand}.")
        print(f"Computer first card: {computer_hand[0]}")
    
        if computer_sum == 21:
            print(f"Blackjack!!\n")
            return computer_hand

        elif computer_sum > 21:
            if 11 in computer_hand:
                print('Computer switching 11 to 1.')
                computer_hand[computer_hand.index(11)] = swap
                computer_sum += swap
                continue

            else:
                print("Computer's gone over.\n")
                return computer_hand
        
        elif computer_sum < 17:
            print(f"Computer's hand under 17. comp hand: {computer_hand}, total: {computer_sum}.")
            while computer_sum < 17:
                print("Computer's taking hit until over 17.")
                computer_hit = hit()
                computer_hand.append(computer_hit)
                computer_sum += computer_hit
                continue
            print(f"Over 17. Comp hand: {computer_hand}, total: {computer_sum}.\n")
            continue

        else:
            print("computer turn ends.\n")
            return computer_hand

'''Function that ties player_turn funct. and computer_turn funct. together.
    - Uses RETURN values of both player_hand and computer_hand list's to then use SUM function to
        run numbers through Blackjack logic to determine winner.'''
def play_game():

    computer_first_card = hit()

    player_final_hand = player_turn(computer_first_card)
    computer_final_hand = computer_turn(computer_first_card)

    player_final_total = sum(player_final_hand)
    computer_final_total = sum(computer_final_hand)

    print(f"Player's final hand: {player_final_hand}")
    print(f"Computer's final hand: {computer_final_hand}\n")

    if player_final_total == 21 and computer_final_total == 21:
        print("Its a Tie!! Both player's have 21.")
    
    elif player_final_total > 21 or computer_final_total > 21:
        if computer_final_total > 21:
            print(f"Player Wins!! Your total: {player_final_total}. Computer Busts with a hand of:{computer_final_hand}, a total of: {computer_final_total}")
        else:
            print(f"Computer Wins!! Their total: {computer_final_total}. Player Busts with a hand of:{player_final_hand}, a total of: {player_final_total}")
    
    elif player_final_total > computer_final_total or computer_final_total > player_final_total:
        if player_final_total > computer_final_total:
            print(f"Player Wins!! Your total: {player_final_total}. Computer Busts with a hand of:{computer_final_hand}, a total of: {computer_final_total}")
        else:
            print(f"Computer Wins!! Their total: {computer_final_total}. Player Busts with a hand of:{player_final_hand}, a total of: {player_final_total}")
    
    elif player_final_total == computer_final_total:
        print(f"It's a Tie!! Player hand: {player_final_total}, Computer hand: {computer_final_total}.") 

    else:
        print(f"Found edge case:\nplayer hand: {player_final_hand}\nplayer total: {player_final_total}\n\ncomputer hand: {computer_final_hand}\ncomp total: {computer_final_total}")



''' MAIN PROGRAM STARTS HERE:'''
game_on = True

while game_on:

    question = input("Want to play a hand? Press 'y' or 'n': ").lower()

    if question == 'y':
        print("\n")
        play_game()

    else:
        break

