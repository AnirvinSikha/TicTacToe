import Board
class Player:

    def __init__(self, b, v):
        self.board = b
        self.grid = b.grid
        self.val = v

    def play(self):
        self.board.position_visualize()
        self.board.visualize()
        position = int(input("What position would you like to play? "))
        while self.grid[position] is not None:
            self.board.position_visualize()
            self.board.visualize()
            position = int(input("Invalid Position. What position would you like to play? "))
        self.grid[position] = self.val


def main():
    b = Board.Board()
    p1 = Player(b, 'x')
    p2 = Player(b, 'o')


