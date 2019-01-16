import sys
import random

digits = ['-'] * 9
sign = ''
sign2 = ''
player1 = ''
player2 = ''
won = False


def display_board(board):
    print('\n' * 100)
    print("Type a number to place X or O in that spot")
    print('9' + '|' + '8' + '|' + '7')
    print('6' + '|' + '5' + '|' + '4')
    print('3' + '|' + '2' + '|' + '1')
    print('\n' * 1)
    print(board[8] + '|' + board[7] + '|' + board[6])
    print(board[5] + '|' + board[4] + '|' + board[3])
    print(board[2] + '|' + board[1] + '|' + board[0])
    print('\n' * 1)
    win_check(digits, sign2)

# TEST
# test_board = ['#','X','O','X','O','X','O','X','O','X']
# display_board(test_board)


def player_input():
    marker = ''
    global player1
    global player2

    while marker != 'X' and marker != 'O':
        print("Player 1:")
        marker = input("Please pick a marker 'X' or 'O'")
        marker = marker.upper()

    if marker == 'X':
        player1 = 'X'
        player2 = 'O'
    else:
        player1 = 'O'
        player2 = 'X'


def place_marker(board, marker, position):
    board[position - 1] = marker


# Test
# place_marker(digits,'X',1)
# place_marker(digits,'X',4)
# place_marker(digits,'X',7)
# display_board(digits)


def win_check(board, mark):
    score = ''
    global won
    for i in board:
        if i == mark:
            score += '1'
        else:
            score += '0'

    if score[:3] == '111' \
            or score[3:6] == '111' \
            or score[6:9] == '111' \
            or score[0:9:3] == '111' \
            or score[1:9:3] == '111' \
            or score[2:9:3] == '111' \
            or score[0:9:4] == '111' \
            or score[2:7:2] == '111':
        print(mark + ' wins')

        won = True


# win_check(digits,'X')


def choose_first():
    return ['Player1', 'Player2'][random.randint(0, 1)]


def space_check(board, position):
    return board[position - 1] == '-'


def full_board_check(board):
    return '-' not in board


def player_choice(board):
    turn = 'unfinished'
    global sign
    global sign2
    while turn != 'finished':
        try:
            position = int(input(f"“Where do you want to place {sign}?”"))
        except ValueError:
            print("Press numbers 1 - 9")
            continue
        if space_check(board, position):
            place_marker(digits, sign, position)
            if sign == 'X':
                sign = 'O'
                sign2 = 'X'
                turn = 'finished'
            else:
                sign = 'X'
                sign2 = 'O'
                turn = 'finished'
        else:
            turn = 'finished'


def replay():
    print("Would you like to play again?")
    x = int(input("Enter 1 to play or 2 to stop"))
    return x == 1


while True:
    print("Welcome to TICTACTOE")

    player_input()
    display_board(digits)
    if choose_first() == 'Player1':
        print('Player1, you go first')
        sign = 'X'
    else:
        print('Player2, you go first')
        sign = 'O'

    game_on = True

    while game_on:
        player_choice(digits)
        display_board(digits)

        if full_board_check(digits):
            print('It is a tie!')
            if not replay():
                sys.exit("Thanks for playing")
            else:
                digits = ['-'] * 9
                sign = ''
                sign2 = ''
                player1 = ''
                player2 = ''
                won = False
                break

        if won:
            if not replay():
                sys.exit("Thanks for playing")
            else:
                digits = ['-'] * 9
                sign = ''
                sign2 = ''
                player1 = ''
                player2 = ''
                won = False
                break
