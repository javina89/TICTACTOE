import textwrap


class Board:
    def __init__(self, space):
        self.space = space
        self.state = [self.space] * 9
        self.game = True

    def __str__(self):
        return textwrap.dedent(f"""
            9|8|7\t{self.state[8]}|{self.state[7]}|{self.state[6]}
            6|5|4\t{self.state[5]}|{self.state[4]}|{self.state[3]}
            3|2|1\t{self.state[2]}|{self.state[1]}|{self.state[0]}
        """)

    def change_state(self, move, name):
        if self.state[move - 1] == '-':
            self.state[move - 1] = name
            return True
        else:
            return False

    def run(self, player1, player2):
        print(self)
        while self.game:
            while not player1.make_move(player1.take_input(), self):
                print("Invalid move, try again")
            print(self)
            if self.win(player1, player2):
                print(self.win(player1, player2) + 'wins')
                self.exit_game()
            if self.tie():
                print('Tied')
                self.exit_game()
            player1, player2 = player2, player1

    def win(self, player1, player2):
        for name in [player1.name, player2.name]:
            xo = ''
            for i in self.state:
                xo += str([0, 1][i == name])
            if {xo[2:9:3], xo[3:6], xo[0:9:3], xo[2:7:2], xo[1:9:3], xo[6:9], xo[0:9:4], xo[:3]} & {'111'}:
                return name
            else:
                return None

    def tie(self):
        if '-' not in self.state:
            return True
        else:
            return False

    def exit_game(self):
        self.game = False


class Player:
    def __init__(self, name):
        self.name = name

    def make_move(self, move, board):
        return board.change_state(move, self.name)

    def take_input(self):
        spot = ''
        while spot not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            spot = (input(f"“Type a number to place {self.name}”"))
        return int(spot)


ttt = Board('-')
x = Player('X')
o = Player('O')
ttt.run(x, o)
