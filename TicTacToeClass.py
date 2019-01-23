import textwrap


class Board:
    def __init__(self):
        self.state = ['-'] * 9
        self.game = True
        self.queue = []
        self.sign = ['X', 'O']

    def __str__(self):
        return textwrap.dedent(f"""
            9|8|7\t{self.state[8]}|{self.state[7]}|{self.state[6]}
            6|5|4\t{self.state[5]}|{self.state[4]}|{self.state[3]}
            3|2|1\t{self.state[2]}|{self.state[1]}|{self.state[0]}
        """)

    def add_player(self, player):
        if not self.sign:
            raise Exception("only two players are supported at a time")
        player.sign = self.sign.pop(0)
        self.queue.append(player)

    def change_state(self, move):
        if self.state[move - 1] == '-':
            self.state[move - 1] = self.queue[0].sign
            return True
        else:
            return False

    def run(self):
        print(self)
        while self.game:
            while not self.change_state(self.queue[0].take_input()):
                print("Invalid move, try again")
            print(self)
            if self.win() or self.tie():
                self.game = False
            else:
                self.change_turn()

    def change_turn(self):
        self.queue.append(self.queue.pop(0))

    def win(self):
        check_win = (self.state[2:9:3], self.state[3:6],
                     self.state[0:9:3], self.state[2:7:2],
                     self.state[1:9:3], self.state[6:9],
                     self.state[0:9:4], self.state[:3])

        if [self.queue[0].sign] * 3 in check_win:
            print(self.queue[0].sign, "wins")
            return True

    def tie(self):
        if '-' not in self.state:
            print('Tied')
            return True
        else:
            return False


class Player:
    def __init__(self):
        self.sign = None

    def take_input(self):
        spot = ''
        while spot not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            spot = (input(f"“Type a number to place {self.sign}” "))
        return int(spot)


ttt = Board()
x = ttt.add_player(Player())
o = ttt.add_player(Player())
ttt.run()
