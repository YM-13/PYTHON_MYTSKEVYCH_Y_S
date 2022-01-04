import board as board
from IPython.display import clear_output

def display_board(board):
    #clear_output()
    #print('\n' * 100)
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

board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
display_board(board)


def player_input():
    marker = ' '
    while marker != 'O' or marker != 'X':
        marker = input("Player 1: Do you want to be X or O?:  ").upper()
        if marker == 'O':
            return ('O', 'X')
        else:
            return ('X', 'O')

player_input()


def place_marker(board, marker, position= ' '):
    # board = display_board()
    # marker = player_input()
    free_positions = [num.index() for num in board if num == ' ']
    position = ' '
    while position.isdigit == False or position not in free_positions:
        position = input(f"Choose your position in range of {free_positions}:  ")
    return position

print(place_marker(display_board, player_input()))
    # if
    # if position.isdigit == False:
    #         position = input("Choose your position i range of 1-9:  ")
    #     position = int(position)
    #     if position in
