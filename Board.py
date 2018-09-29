class Board():



    def __init__(self):
        self.board = [None] * 9

    def visualize(self):

        return

    def position_visuaize(self):

        updated = [None] * 9
        for i in range(9):
            if self.board[i] == "X" or self.board[i] == "O":
                updated[i] = self.board[i]
            else:
                updated[i] = i





