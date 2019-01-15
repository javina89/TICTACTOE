import random

digits = ['-'] * 9
sign = ''

def display_board(digits):
    print('\n' * 100)
    print(digits[8] + '|' + digits[7] + '|' + digits[6])
    print(digits[5] + '|' + digits[4] + '|' + digits[3])
    print(digits[2] + '|' + digits[1] + '|' + digits[0])

# TEST
# test_board = ['#','X','O','X','O','X','O','X','O','X']
# display_board(test_board)

def player_input():
    marker = ''

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

    return player1, player2

# player_input()

def place_marker(digits, marker, position):
    digits[position - 1] = marker
    return digits

# Test
# place_marker(digits,'X',1)
# place_marker(digits,'X',4)
# place_marker(digits,'X',7)
# display_board(digits)

def win_check(board, mark):
    score = ''
    if full_board_check(board):
        for i in board:
            if i == mark:
                score += '1'
            else:
                score += '0'

        if score[:3] == '111' \
                or score[3:7] == '111' \
                or score[7:10] == '111' \
                or score[0:10:3] == '111' \
                or score[1:10:3] == '11' \
                or score[2:10:3]:
            print(mark + ' wins')


# win_check(digits,'X')


def choose_first():
    return ['Player1', 'Player2'][random.randint(0,1)]

# print(choose_first())

def space_check(board, position):
    return board[position - 1] == '-'

def full_board_check(board):
    return '-' not in board

def player_choice(board):
    turn = 'unfinished'

    while turn != 'finished':
        position = int(input("“Where do you want put your marker?”"))
        if not space_check(board, position):
            place_marker(digits, sign, position)
            if sign == 'X':
                sign = 'O'
                return sign
            else:
                sign = 'X'
                return sign


def replay():
    print("Would you like to play again?")
    x = input("Enter 1 to play or 2 to stop")
    return x == 1


while True:
    print("Welcome to TICTACTOE")

    players = player_input()

    if choose_first() == 'Player1':
        print('Player1, you go first')
        sign = 'X'
    else:
        print('Player2, you go first')
        sign = 'O'

    game_on = True

    while game_on:
        display_board(digits)
        player_choice(digits)

        if win_check(digits,'X') == True or win_check(digits,'O') == True:
            if not replay():
                break

# Set the game up here
# pass

# while game_on:
# Player 1 Turn


# Player2's turn.

# pass

# if not replay():
# break
