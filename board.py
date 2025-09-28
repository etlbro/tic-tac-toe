
class Board:
    #init board and its grid size
    def __init__(self, size):
        self.size = size
        # tic-tac-toe 2D grid of size*size
        self.pieces_grid = [[' ']*size for _ in range (size)]
        self.req_to_win = 3

    def print_board(self):
        for piece in self.pieces_grid:
            print("|",end='')
            for p in piece:
                print(f"{p}|", end='')
            print()


    def is_valid(self, row, col):
        '''
        checks if player move is valid- i.e. within the grid and empty
        '''
        if row < self.size and col < self.size and self.pieces_grid[row][col] == ' ':
            return True
        return False
    

    def update_board(self, player, row, col):
        '''
        mark players (O, X) move on the board
        '''
        self.pieces_grid[row][col] = player
        return


    def is_full(self):
        '''
        checks is board is full and therefore a tie.
        returns True if full
        '''
        if any(' ' in row for row in self.pieces_grid):
            return False
        return True
 

    def check_row(self, player,  row ):
        '''
        checks for a victory on the row 
        '''
        j = 0
        for cell in self.pieces_grid[row]:
            if cell == player:
                j += 1
                if j == self.req_to_win: # enough in the row for a win
                    return True
            else: # does not match 'player' pieace 
                j=0
        return False


    def check_col(self, player, col):
        '''
        checks for a victory on the col 
        '''
        j = 0 
        for i in range(self.size):
            if self.pieces_grid[i][col] == player:
                j += 1
                if j == self.req_to_win: # enough in the row for a win
                    return True
            else: # does not match 'player' pieace 
                j = 0
        return False


    def check_main_diagonal(self, player,  row , col):
        '''
        checks for a victory on the main diagonal
        '''
        #start from the first col/row(=0), depending on minimum 
        k = min(row, col)
        start_row = row - k
        start_col = col - k
        j = 0 
        while start_row < self.size and start_col < self.size:
            if self.pieces_grid[start_row][start_col] == player:
                j = j + 1
                if j == self.req_to_win: # enough in the row for a win
                    return True
            else: # does not match 'player' pieace 
                j = 0
            start_row += 1
            start_col += 1
        return False
    

    def check_sec_diagonal(self, player,  row , col):
        '''
        checks for a victory on the secondary diagonal
        '''
        #start from the first col/row(=0), depending on minimum distance from top row or max col(=size)
        k = min(row, self.size - 1 - col) 
        start_row = row - k
        start_col = col + k
        j = 0 
        while start_row < self.size and start_col >= 0 :
            if self.pieces_grid[start_row][start_col] == player:
                j = j + 1
                if j == self.req_to_win: # enough in the row for a win
                    return True
            else: # does not match 'player' pieace 
                j = 0
            start_row += 1
            start_col -= 1
        return False


    def victory_achived(self, player,  row , col):
            '''
            call the varios victory testers
            '''
            if(self.check_row(player,  row ) or self.check_col(player, col) or
                self.check_main_diagonal(player,  row , col) or self.check_sec_diagonal(player,  row , col) ):
                return True
            return False

    def reset_board(self):
        '''
        resets the board.
        '''
        self.pieces_grid = [[' ']* self.size for _ in range ( self.size)]



#b = Board(3)
#b.make_move(1,1,'x')
#b.print_board()














