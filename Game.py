class Game:

    def __init__(self, p1, p2, b):
        self.p1 = p1
        self.p2 = p2
        self.board = b
        self.turn = p1

    def progress(self):
        return

    def win(self, p): #takes in a player
        b = self.board
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
        for i in self.b:
            if i is None:
                count += 1
        return not self.lose(self.turn) and not self.win(self.turn) and (count == 9)