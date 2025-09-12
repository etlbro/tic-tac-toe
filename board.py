
class Board:
    #init board and its grid size
    def __init__(self, size):
        self.size = size
        # tic-tac-toe 2D grid of size*size
        self.pieces_grid = [[' ']*size for _ in range (size)]

    def print_board(self):
        for piece in self.pieces_grid:
            print("|",end='')
            for p in piece:
                print(f"{p}|", end='')
            print()

    def is_valid(self, row, col):
        '''
        checks if player move is valid- with in the grid and empty
        '''
        if row <= self.size and col <= self.size and self.pieces_grid[row][col] == ' ':
            return True
        return False
    
    def make_move(self, row, col, player):
        '''
        mark players (O, X) move on the board
        '''
        self.pieces_grid[row][col] = player
        return


b = Board(3)
b.make_move(1,1,'x')
b.print_board()














