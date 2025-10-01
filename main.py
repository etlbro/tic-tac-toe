# main.py
from gui import TicTacToeApp
from game_logic import Game_logic

def main():
    # --- create backend ---
    game = Game_logic(size=3)  # 3x3 board

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


    # --- register GUI as listener to backend events ---
    game.add_listener(app)

    # --- run GUI ---
    app.run()


if __name__ == "__main__":
    main()
