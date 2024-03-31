# # ? Step-1
# import random


# def display_board(board):
#     print(board[7]+"|"+board[8]+"|"+board[9])
#     print(board[4]+"|"+board[5]+"|"+board[6])
#     print(board[1]+"|"+board[2]+"|"+board[3])


# test_board = ["#", "X", "O", "X", "O", "X", "O", "X", "O", "X"]

# # display_board(test_board)

# # ? Step-2


# def player_input():
#     '''
#     output=(Player 1 marker,Player 2 marker)
#     '''
#     marker = ''
#     # // keep asking player 1 to choose X or O
#     while marker != 'X' and marker != "O":
#         marker = input("Player 1,choose X or O:")
#     # // Assign player 2,the opposie marker

#     player1 = marker

#     if player1 == "X":
#         player2 = "O"
#     else:
#         player2 = "X"

#     return (player1, player2)


# # ? Step 3

# def place_marker(board, marker, position):
#     board[position] = marker


# # place_marker(test_board, "$", 8)
# # display_board(test_board)


# def win_check(board, mark):
#     # ? win tic tac toe?
#     # ?all rows,and check to see if they al share the same marker
#     return (board[1] == mark and board[2] == mark and board[3] == mark) or (board[4] == mark and board[5]
#                                                                             == mark and board[6] == mark) or (board[7] == mark and board[8] == mark and board[9] == mark) or (board[7] == mark and board[4] == mark and board[1] == mark) or (board[8] == mark and board[5] == mark and board[2] == mark) or (board[9] == mark and board[6] == mark and board[3] == mark) or (board[7] == mark and board[5] == mark and board[3] == mark) or (board[1] == mark and board[5] == mark and board[9] == mark)


# display_board(test_board)
# # print(win_check(test_board, "X"))


# # ? step 5
# def choose_first():
#     flip = random.randint(0, 1)

#     if flip == 0:
#         return "Player 1"
#     else:
#         return "Player 2"

# # ? step 6


# def space_check(board, position):
#     return board[position] == ' '

# # ? step 7


# def full_board_check(board):
#     for i in range(1, 10):
#         if space_check(board, i):
#             return False
#     return True


# # ? step8

# def player_choice(board):
#     position = 0
#     while position not in range(1, 10) or not space_check(board, position):
#         position = int(input("Choose a position : (1-9)"))
#     return position

# # ? step 9


# def replay():
#     choice = input("Play again? Enter Yes or No")
#     return choice == "Yes"


# # ? step 10
# # // while loop for keep running the game
# print("....Welcome to Tic Tac Toe....")

# while True:
#     # ? play the game

#     # ? set everything up (board,whos first,choose markers x,o)
#     the_board = ['']*10
#     player1_marker, player2_marker = player_input()

#     turn = choose_first()
#     print(turn + ' will go first!')

#     play_game = input("Ready to play? Yes or No")
#     if play_game.lower()[0] == 'y':
#         game_on = True
#     else:
#         game_on = False

#     while game_on:
#         if turn == "Player 1":
#             # ? show the board
#             display_board(the_board)
#             # ? choose the position
#             position = player_choice(the_board)
#             # ? place the marker
#             place_marker(the_board, player1_marker,  position)
#             # ? check if they win
#             if win_check(the_board, player1_marker):
#                 display_board(the_board)
#                 print("Player 1 has won!")
#                 game_on = False
#             # ?check for tie
#             else:
#                 if full_board_check(the_board):
#                     display_board(the_board)
#                     print("Tie Game!")
#                     game_on = False
#                 else:
#                     turn == "Player 2"
#         else:
#             # ? show the board
#             display_board(the_board)
#             # ? choose the position
#             position = player_choice(the_board)
#             # ? place the marker
#             place_marker(the_board, player2_marker, position)
#             # ? check if they win
#             if win_check(the_board, player2_marker):
#                 display_board(the_board)
#                 print("Player 2 has won!")
#                 game_on = False
#             # ?check for tie
#             else:
#                 if full_board_check(the_board):
#                     display_board(the_board)
#                     print("Tie Game!")
#                     game_on = False
#                 else:
#                     turn == "Player 1"
#     if not replay():
#         break


import random


def display_board(board):

    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


def player_input():
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):

    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            # across the middle
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            # across the bottom
            (board[1] == mark and board[2] == mark and board[3] == mark) or
            # down the middle
            (board[7] == mark and board[4] == mark and board[1] == mark) or
            # down the middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or
            # down the right side
            (board[9] == mark and board[6] == mark and board[3] == mark) or
            # diagonal
            (board[7] == mark and board[5] == mark and board[3] == mark) or
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal


def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


def space_check(board, position):

    return board[position] == ' '


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))

    return position


def replay():

    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')

    play_game = input('Are you ready to play? Enter Yes or No.')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
