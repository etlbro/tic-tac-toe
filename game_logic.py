
import board as b 
import player
from  itertools import cycle


class Game_logic:
    '''
    class to handel general game logic:
     makes the moves on board, checks for winner, switches player's turn. 
    '''
    def __init__(self,size):
        self.board = b.Board(size)
        self.listeners = []
    
    def add_listener(self, listener):
        '''
        add to listeners
        '''
        self.listeners.append(listener)

    def make_move(self, player, row, col):
        '''
        checks move is valid and updates board accordingly
        '''
        if self.board.is_valid(row, col):
            self.board.update_board(player, row, col)
            return True
        return False    

    def notify_move(self, row, col, symbol):
        '''
        every lisntener must implement the on_move function
          '''
        for listener in self.listeners:
            listener.on_move(row, col, symbol)



    def game_ended(self):
        '''
        checks for full board i.e game ended
        '''
        if self.board.is_full():
            return True
        return False

    def notify_game_over(self):
        '''
        every lisntener must implement the notify_game_over function
        '''
        for listener in self.listeners:
            listener.on_game_over()

    
    def check_winner(self, player, row, col):
        '''
        checks if some one has a winning position of any sort
        '''
        if(self.board.victory_achived(player, row, col)):
            return True
        return False
    

    def notify_game_winner(self, player):
        '''
        every lisntener must implement the notify_game_over function
        '''
        for listener in self.listeners:
            listener.on_game_winner(player)


    def start_new_game(self):
        '''
        resets the board.
        '''
        self.board.reset_board()

    #test function. in actuallity lpayer will have a few options for players (pvp, pvc) so we'll need the factory. for now still with this
    def init_player(self):
        player_1 = player.HumanPlayer('x') #make instance of human player with selected symbol
        player_2 = player.HardPlayer('o')



    def run_game_test(self,player_1_data, player_2_data):
        '''
        main function to run game, handle player turns and checkfor game endings
        '''
        try:
            player_1 = player.PlayerFactory.creat_player(player_1_data) #make instance of human player with selected symbol
            player_2 = player.PlayerFactory.creat_player(player_2_data) 
        except Exception as e:
            print("invalid player type or symbol")
            return
        players = [player_1, player_2] 
        turns = cycle(players)
            #player.HardPlayer("x"), player.HardPlayer("o")
        for current_player in turns:
            while True: # makes sure move is valid, keep trying until set (= make move return true)
                move = current_player.get_move(self.board) 
                if(self.make_move(current_player.get_symbol(),move[0], move[1])):
                    break # need to rewrite make_move so it only update listener
            self.board.print_board()                   
            if self.game_ended():
                print("game over") # update listens of ending 
                break
            if self.check_winner(current_player.get_symbol(), move[0],move[1]):
                print(f"{current_player.get_symbol()} wins! well played!")
                break #// update listners of winner 


    def run_game(self,player_1_data, player_2_data):
        '''
        main function to run game, handle player turns and checkfor game endings
        '''
        try:
            player_1 = player.PlayerFactory.creat_player(player_1_data) #make instance of human player with selected symbol
            player_2 = player.PlayerFactory.creat_player(player_2_data) 
        except Exception as e:
            print("invalid player type or symbol")
            return
        players = [player_1, player_2] 
        turns = cycle(players)
            #player.HardPlayer("x"), player.HardPlayer("o")
        for current_player in turns:
            while True: # makes sure move is valid, keep trying until set (= make move return true)
                move = current_player.get_move(self.board) 
                if(self.make_move(current_player.get_symbol(),move[0], move[1])):
                    break 
            # update listeners board has changed
            self.board.print_board()                   
            if self.game_ended():
                # update listens of tie ending 
                self.notify_game_over()
                break
            if self.check_winner(current_player.get_symbol(), move[0],move[1]):
                # update listners of winner 
                self.notify_game_winner(current_player)
                break 

                