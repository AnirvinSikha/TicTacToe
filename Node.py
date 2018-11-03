class Node:

    def __init__(self, position, grid, val, oppVal):
        self.position = position
        self.grid = grid
        self.val = val
        self.oppVal = oppVal

    def get_utility(self):

        util = 0

        test_grid = self.grid.copy()
        test_grid[self.position] = self.val
        if self.is_win(test_grid):
            return float('inf')

        num_val = self.grid.count(self.val)
        opp_val = self.grid.count(self.oppVal)

        util += 10 * num_val + 5 * opp_val

        return util

    def is_win(self, grid, val):
        b = grid
        return (b[0] == b[4] == b[8] == self.val \
                or b[2] == b[4] == b[6] == self.val \
                or b[0] == b[1] == b[2] == self.val \
                or b[3] == b[4] == b[5] == self.val \
                or b[6] == b[7] == b[8] == self.val \
                or b[0] == b[3] == b[6] == self.val \
                or b[1] == b[4] == b[7] == self.val \
                or b[2] == b[5] == b[8] == self.val)