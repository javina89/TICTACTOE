def display_board(b):
    print(f'9|8|7\t{b[8]}|{b[7]}|{b[6]}\n6|5|4\t{b[5]}|{b[4]}|{b[3]}\n3|2|1\t{b[2]}|{b[1]}|{b[0]}\n')


def decide():
    spot = ''
    while spot not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        spot = (input("“Type a number to place X or O”"))
    return int(spot)


def win_check(board, _sign):
    global playing
    xo = ''
    for i in board:
        xo += str([0, 1][i == _sign])
    if '-' not in board:
        print('Tied!')
        playing = False
    if {xo[2:9:3], xo[3:6], xo[0:9:3], xo[2:7:2], xo[1:9:3], xo[6:9], xo[0:9:4], xo[:3]} & {'111'}:
        print(sign + ' wins')
        playing = False


while True:
    turn = 0
    digits = ['-'] * 9
    display_board(digits)
    playing = True
    while playing:
        turn += 1
        sign = ['X', 'O'][turn % 2]
        position = decide()
        if digits[position - 1] == '-':
            digits[position - 1] = sign
        else:
            turn -= 1
        display_board(digits)
        win_check(digits, sign)
    if not input('Would you like to play again? Type yes or no').lower().startswith('y'):
        break
