class Board:
    def __init__(self, space):
        self.space = space
        self.state = [self.space] * 9
        self.game = True

    def __str__(self):
        return f'9|8|7\t{self.state[8]}|{self.state[7]}|{self.state[6]}\n' \
               f'6|5|4\t{self.state[5]}|{self.state[4]}|{self.state[3]}\n' \
               f'3|2|1\t{self.state[2]}|{self.state[1]}|{self.state[0]}\n'

    def change_state(self, move, name):
        if self.state[move - 1] == '-':
            self.state[move - 1] = name

    def exit_game(self):
        self.game = False


class Player:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def make_move(move, name, board):
        board.change_state(move, name)

    def take_input(self):
        spot = ''
        while spot not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            spot = (input(f"“Type a number to place {self.name}”"))
        return int(spot)


def win(board, name1, name2):
    for name in [name1.name, name2.name]:
        xo = ''
        for i in board.state:
            xo += str([0, 1][i == name])
        if '-' not in board.state:
            print(name + ' Tied!')
            board.exit_game()
        if {xo[2:9:3], xo[3:6], xo[0:9:3], xo[2:7:2], xo[1:9:3], xo[6:9], xo[0:9:4], xo[:3]} & {'111'}:
            print(name + ' wins')
            board.exit_game()


ttt = Board('-')
x = Player('X')
o = Player('O')

while ttt.game:
    print(ttt)
    x.make_move(x.take_input(), 'X', ttt)
    win(ttt, x, o)
    if not ttt.game:
        print(ttt)
        break
    print(ttt)
    o.make_move(o.take_input(), 'O', ttt)
    win(ttt, x, o)
