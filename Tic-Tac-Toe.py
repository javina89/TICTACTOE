def display_board(board):
    print("Type a number to place X or O in that spot")
    print('9' + '|' + '8' + '|' + '7' + '\t' + board[8] + '|' + board[7] + '|' + board[6])
    print('6' + '|' + '5' + '|' + '4' + '\t' + board[5] + '|' + board[4] + '|' + board[3])
    print('3' + '|' + '2' + '|' + '1' + '\t' + board[2] + '|' + board[1] + '|' + board[0])


def decide():
    spot = 100
    while spot not in range(1, 10):
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
        score += str([0, 1][i == sign])
    if '-' not in board:
        print('Tied!')
        playing = False
    win_combos = {'6': score[2:9:3], '2': score[3:6], '4': score[0:9:3], '8': score[2:7:2],
                  '5': score[1:9:3], '3': score[6:9], '7': score[0:9:4], '1': score[:3]}
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
        win_check(digits)
        display_board(digits)
    if not input('Would you like to play again? Type yes or no').lower().startswith('y'):
        break
