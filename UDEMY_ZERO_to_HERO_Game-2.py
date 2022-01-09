#from IPython.display import clear_output

def display_board(board):
    #clear_output()
    print('\n' * 100)
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
    marker = ' '
    while marker != 'O' or marker != 'X':
        marker = input("Player: Do you want to be X or O?:  ").upper()
        if marker == 'O':
            return ('O', 'X')
        else:
            return ('X', 'O')


def place_marker(board, marker, position):
    board[position] = marker.upper()


def win_check(board, mark):
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[7] == mark and board[4] == mark and board[1] == mark) or
            (board[8] == mark and board[5] == mark and board[2] == mark) or
            (board[9] == mark and board[6] == mark and board[3] == mark) or
            (board[1] == mark and board[5] == mark and board[9] == mark) or
            (board[7] == mark and board[5] == mark and board[3] == mark))


import random
def choose_first():
    if random.randint(1, 2) == 1:
        return 'The First Player - Player_1'
    else:
        return 'The First Player - Player_2'

# STEP 6 ok
def space_check(board, position):
    return board[position] == ' '

# STEP 7
def full_board_check(board):
    return ' ' not in board

# STEP 8 ok
def player_choice(board):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose your next position among 1 - 9:  '))
    return position


# STEP 9
# def replay():
#     choice = 'wrong'
#     while choice not in ['Yes', 'No']:
#         choice = input("Do you want to play again? Enter Yes or No: ").capitalize()
#
#         if choice not in ['Yes', 'No']:
#             print("Sorry, I don't understand, please choose Y or N!")
#
#     if choice == 'Yes':
#         return True
#     else:
#         return False


def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


def game_on():
    test_board_d = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    a = True
    while a == True:
        test_board = test_board_d
        print('Welcome to Tic Tac Toe!')
        print(choose_first())
        print(player_input())
        display_board(test_board)
        while ' ' in test_board:
            position = player_choice(test_board)
            marker = input('Choose "X" or "O"  ')
            place_marker(test_board, marker, position)
            print(display_board(test_board))
            if win_check(test_board, 'X'):
                print('"X" is the winner')
                a = replay()
            elif win_check(test_board, 'Y'):
                print('"Y" is the winner')
                a = replay()
            else:
                pass
        print('Nobody is winner')
    a = replay()


print(game_on())
