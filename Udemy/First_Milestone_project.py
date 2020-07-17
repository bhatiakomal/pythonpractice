'''from IPython.display import clear_output
def display_board(board):
    print(board[7]+'|'+board[8]+'|'+board[9]+'|')
    print(board[4] + '|' + board[5] + '|' + board[6] + '|')
    print(board[1] + '|' + board[2] + '|' + board[3] + '|')
test_board=['#','X','O','X','O','X','O','X','O','X',]
display_board(test_board)'''


from IPython.display import clear_output
def display_board(board):
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])
test_board=['#','X','O','X','O','X','O','X','O','X', ]
display_board(test_board)

def player_input():
    #Output=player 1 marker,player 2 marker
    marker=' '
    while marker!='O' and marker !='X':
        marker=input('Player1:choose X or O').upper()
    if marker=='X':
        return ('X','O')
    else:
        return ('O','X')
player1_marker,player2_marker=player_input()
print(player1_marker)
print(player2_marker)

def place_marker(board,marker,position):
    board[position]=marker
place_marker(test_board,'$',8)
display_board(test_board)

def win_check(board,mark):
    #Wintic tae Toe
    return ((board[7]==board[8]==board[9]==mark) or
    (board[4] == board[5] == board[6] == mark) or
    (board[7] == board[4] == board[1] == mark) or
    (board[8] == board[5] == board[2] == mark) or
    (board[9] == board[6] == board[3] == mark) or
    (board[7] == board[5] == board[3] == mark) or
    (board[9]==board[5]==board[1]==mark))
display_board(test_board)
print(win_check(test_board,'X'))

import random
def choose_first():
    flip=random.randint(0,1)
    if flip==0:
        return 'player 1'
    else:
        return 'player 2'

def  space_check(board, position):
    return board[position]==' '
def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True
def player_choice(board):
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position=int(input("choose a postion:(1-9)"))
    return position
def replay():
    choice=input("Play again?..Yes or No")
    return choice=='Yes'

#while loop to kepp running the game
print("Welcome to the TIC TAC TOE GAME")
while True:
    #play the game
    #Set everything up(Board ,whos first,choose marker X,O)
    the_board=[' ']*10
    player1_marker,player2_marker=player_input()
    turn=choose_first()
    play_game=input('Ready to play? Y or N')
    if play_game=='y':
        game_on=True
    else:
        game_on=False

    #play game
    while game_on:
        if turn=='Player 1':
            #Show the board
            display_board(the_board)
            #Choose a position
            position=player_choice(the_board)
            #Place the marker on the position
            place_marker(the_board,player1_marker,position)
            #Check if they won
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('Player 1 has won!!')
                game_on=False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME')
                    game_on=False
                else:
                    turn='Player 2'
            #or check if there is a tie
            #no tie or no win? Then next player turn

    #Player one turn
    else:
        # Show the board
        display_board(the_board)
        # Choose a position
        position = player_choice(the_board)
        # Place the marker on the position
        place_marker(the_board, player2_marker, position)
        # Check if they won
        if win_check(the_board, player2_marker):
            display_board(the_board)
            print('Player 2 has won!!')
            game_on = False
        else:
            if full_board_check(the_board):
                display_board(the_board)
                print('TIE GAME')
                game_on = False
            else:
                turn = 'Player 1'
    #Player two turn

    if not replay():
        break
