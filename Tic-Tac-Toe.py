def display_board(b):
    print(f'9|8|7\t{b[8]}|{b[7]}|{b[6]}\n6|5|4\t{b[5]}|{b[4]}|{b[3]}\n3|2|1\t{b[2]}|{b[1]}|{b[0]}\n')


def decide():
    spot = ''
    while spot not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        spot = (input("“Type a number to place X or O”"))
    return int(spot)


def win_check(board, _sign):
    global playing
    score = ''
    for i in board:
        score += str([0, 1][i == _sign])
    if '-' not in board:
        print('Tied!')
        playing = False
    match = [score[2:9:3], score[3:6], score[0:9:3], score[2:7:2], score[1:9:3], score[6:9], score[0:9:4], score[:3]]
    for i in match:
        if i == '111':
            print(sign + ' wins')
            playing = False


while True:
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
