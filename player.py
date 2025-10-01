from abc import ABC, abstractmethod
import random

'''
class Symbol:
    def __init__(self, symbol):
        self.symbol = symbol

    def switch_symbol(self,symbol):
         if symbol == 'x':
              self.symbol = 'o'
         else:
              self.symbol = 'x'     

    def get_symbol(self):
         return self.symbol
'''

class AbsPlayer(ABC):
    '''
    abstarct player class for factory design pattern
    '''
    def __init__(self, symbol):
            
        self.symbol = symbol

    def get_symbol(self):   
        return self.symbol
    # helper resursive function to find actuall best move
    def find_best_move(self, board, analysis_depth,  symbol):
        if board.is_full() or  analysis_depth < 0:
             return 0, None
        valid_moves  = board.get_valid_moves()
        best_score = float('-inf') if (self.symbol == symbol) else float('inf')
        best_move = None

        #trial and error. i want a pruunig score s.t. if reached return it as best path
        #pruning_score = 2*(board.get_size() - analysis_depth) 

        for move in valid_moves: # go over all moveds, find best one (highest 'score')
            board.update_board( symbol, move[0], move[1])
            if board.victory_achived(symbol, move[0], move[1]):
                score = (10 if self.symbol == symbol else -10) * (analysis_depth + 1)
            else:
                next_symbol = 'o' if symbol == 'x' else 'x'
                score,_ = self.find_best_move(board, analysis_depth - 1, next_symbol)

            board.undo(move[0],move[1])    
            #check if move has highest score yet
            if self.symbol == symbol and score > best_score:
                best_score = score
                best_move = move 
                #if best_score >= pruning_score:
                #     break
            elif self.symbol != symbol and score < best_score:
                best_score = score
                best_move = move 
                #if best_score <= -pruning_score:
                #     break
                
        return best_score, best_move  
    
    @abstractmethod
    def get_move(self, board):
        '''
        abstract method for makeing a move, must be implamented
        '''
        pass
 

# temp function befor i implament the gui
class HumanPlayer(AbsPlayer):
      
    def get_move(self, board):
        row = int(input("row:"))
        col = int(input("col:"))
        return row,col
            


class EasyPlayer(AbsPlayer):
     
    def get_move(self, board):
        valid_moves  = board.get_valid_moves()
        return random.choice(valid_moves)
    


class MidPlayer(AbsPlayer):

    def get_move(self, board):
          _,move = self.find_best_move(board,1, self.get_symbol())
          return move

    

class HardPlayer(AbsPlayer):

    def get_move(self, board):
          _,move = self.find_best_move(board,9, self.get_symbol())
          return move



class PlayerFactory:
    '''
    will return two player objects, based on user input
      '''
    _player_map = {
        "easy"   : EasyPlayer,
        "medium" : MidPlayer,
        "hard"   : HardPlayer,
        "human"  : HumanPlayer
    }

    @classmethod
    def creat_player(cls, player_data):
        '''
        req a list with (player_type, symbol)
        '''
        player_type = cls._player_map.get(player_data[0])
        #check player tyoe and sign is valid
        if not player_type or player_data[1] not in ['x', 'o'] :
            raise ValueError(f"Unknown player type: {player_type}")
        return player_type(player_data[1])
        















