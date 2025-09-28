
import board as b 

class Game_logic:
    '''
    class to handel general game logic:
     makes the moves on board, checks for winner, switches player's turn. 
    '''
    def __init__(self,size):
        self.board = b.Board(size)

    

    def make_move(self, player, row, col):
        '''
        checks move is valid and updates board accordingly
        '''
        if self.board.is_valid(row, col):
            self.board.update_board(player, row, col)
            return True
        return False    


    def game_ended(self):
        '''
        checks for full board i.e game ended
        '''
        if self.board.is_full():
            return True
        return False

    def check_winner(self, player, row, col):
        '''
        checks if some one has a winning position of any sort
        '''
        if(self.board.victory_achived(player, row, col)):
            return True
        return False

    def start_new_game(self):
        '''
        resets the board.
        '''
        self.board.reset_board()





