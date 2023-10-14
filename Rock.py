
def take_rounds_input(name):
    text_promt = "Hey " + name + " How many rounds would you like to play ?"
    while True:
        rounds = int(input(text_promt))
        if rounds % 2 == 1:
            # print("wow its an odd number")
            if rounds > 2 and rounds < 10:
                # print("Yay !! we got a perfect odd number")
                return rounds
                break
            else:
                print("Your number is not the range of 3 to 9, please enter again")
        else:
            print("No it's a even number, enter again")
         
import random
def comp_choice():
    option_list = ('rock','paper','scissor')
    return random.choice(option_list)

def play_option():
    option = input("R = Rock, P = Paper, S = Scissor : ")

    if option == 'R' or option == 'r':
        return 'rock'
    elif option == 'P' or option == 'p':
        return 'paper'
    elif option == 'S' or option == 's':
        return 'scissor'
    else:
        print("Wrong input , Enter again")
        return play_option()
def who_winning(comp_choice,play_option):
    if play_option == 'scissor' and comp_choice == 'scissor':
        return 'draw'
    elif play_option == 'rock' and comp_choice == 'scissor':
        return 'player'
    elif play_option == 'paper' and comp_choice == 'scissor':
        return 'computer'
    elif play_option == 'scissor' and comp_choice == 'rock':
        return 'computer'
    elif play_option == 'rock' and comp_choice == 'rock':
        return 'draw'
    elif play_option == 'paper' and comp_choice == 'rock':
        return 'player'
    elif play_option == 'scissor' and comp_choice == 'paper':
        return 'player'
    elif play_option == 'rock' and comp_choice == 'paper':
        return 'computer'
    elif play_option == 'paper' and comp_choice == 'paper':
        return 'draw'
    else:
        return 'Some error is there in spellings'
    

def final_win(round_list):
    player = round_list.count('player')
    computer = round_list.count('computer')
    cdraw = round_list.count('draw')

    if player > computer:
        return "player"
    elif computer>player:
        return "computer"
    else:
        return "draw"
    



name = input("Hey there! What's Your good name? ")
rounds = take_rounds_input(name)
sub_lst = []

for i in range(rounds):
    player_choice = play_option()
    print("Player Choice: ", player_choice)
    com_choice = comp_choice()
    print("Computer Choice: ", com_choice)
    sub_round_winner = who_winning(player_choice,com_choice)
    sub_lst.append(sub_round_winner)

print("Winner of sub rounds ",sub_lst)
if ( final_win == 'draw' ):
    print(" Game Draw ! ")
else:    
    print(final_win(sub_lst), "Win the Game!")