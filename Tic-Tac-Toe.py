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


def decide(board):
    spot = ''
    while spot not in range(0, 9) or board[spot] != '-':
        try:
            spot = int(input("“What space will you choose?”"))
        except ValueError:
            print("Press numbers 1 - 9")
            continue
        return spot


def win_check(board):
    global sign
    global playing
    score = ''
    for i in board:
        if i == sign:
            score += '1'
        else:
            score += '0'
    if '-' not in board:
        print('Tied!')
        playing = False
    if score[:3] == '111' \
            or score[3:6] == '111' \
            or score[6:9] == '111' \
            or score[0:9:3] == '111' \
            or score[1:9:3] == '111' \
            or score[2:9:3] == '111' \
            or score[0:9:4] == '111' \
            or score[2:7:2] == '111':
        print(sign + ' wins')
        playing = False


while True:
    print("Welcome to Tic-Tac-Toe")
    digits = ['-'] * 9
    turn = True
    playing = True
    while playing:
        display_board(digits)
        if turn:
            sign = 'X'
            position = decide(digits)
            digits[position - 1] = sign
            win_check(digits)
        else:
            sign = 'O'
            display_board(digits)
            position = decide(digits)
            digits[position - 1] = sign
            win_check(digits)
    if not input('Would you like to play again? Type yes or no').lower().startswith('y'):
        break
