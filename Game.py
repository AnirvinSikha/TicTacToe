from Board import Board
from Player import Player

class Game:
    def __init__(self, p1, p2, b):
        self.p1 = p1
        self.p2 = p2
        self.board = b
        self.grid = b.grid
        self.turn = p1

    def progress(self):
        return

    def win(self, p): #takes in a player
        b = self.grid
        return (b[0] == b[4] == b[8] == p.val \
                or b[2] == b[4] == b[6] == p.val \
                or b[0] == b[1] == b[2] == p.val \
                or b[3] == b[4] == b[5] == p.val \
                or b[6] == b[7] == b[8] == p.val \
                or b[0] == b[3] == b[6] == p.val \
                or b[1] == b[4] == b[7] == p.val \
                or b[2] == b[5] == b[8] == p.val)

    def lose(self, player):
        if player == self.p1:
            return self.win(self.p2)
        else:
            return self.win(self.p1)

    def tie(self):
        count = 0
        for i in self.grid:
            if i is None:
                count += 1
        return not self.lose(self.turn) and not self.win(self.turn) and (count == 0)

    def finished(self):
        return self.win(self.p1) or self.win(self.p2) or self.tie()

def 1v1():
    b = Board()
    p1 = Player(b, 'x')
    p2 = Player(b, 'o')
    g = Game(p1, p2, b)
    while not g.finished():
        p1.play()
        if not g.finished():
            p2.play()
    if g.win(p1):
        print("Player 1 is the winner!")
    if g.win(p2):
        print("Plyaer 2 is the winner!")
    if g.tie():
        print("It's a tie!")
#1v1()