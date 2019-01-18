def display_board(board):
    print("Type a number to place X or O in that spot")
    print('9' + '|' + '8' + '|' + '7' + '\t' + board[8] + '|' + board[7] + '|' + board[6])
    print('6' + '|' + '5' + '|' + '4' + '\t' + board[5] + '|' + board[4] + '|' + board[3])
    print('3' + '|' + '2' + '|' + '1' + '\t' + board[2] + '|' + board[1] + '|' + board[0])


def decide():
    spot = ''
    while spot not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        spot = (input("“What space will you choose?”"))
    return int(spot)


def win_check(board, _sign):
    global playing
    score = ''
    for i in board:
        score += str([0, 1][i == _sign])
    if '-' not in board:
        print('Tied!')
        playing = False
    win_combos = {'1': score[2:9:3], '2': score[3:6], '3': score[0:9:3], '4': score[2:7:2],
                  '5': score[1:9:3], '6': score[6:9], '7': score[0:9:4], '8': score[:3]}
    for i in win_combos.values():
        if i == '111':
            print(sign + ' wins')
            playing = False


while True:
    print("Welcome to Tic-Tac-Toe")
    counter = 0
    digits = ['-'] * 9
    display_board(digits)
    playing = True
    while playing:
        counter += 1
        sign = ['X', 'O'][counter % 2]
        position = decide()
        if digits[position - 1] == '-':
            digits[position - 1] = sign
        else:
            counter -= 1
        win_check(digits, sign)
        display_board(digits)
    if not input('Would you like to play again? Type yes or no').lower().startswith('y'):
        break
