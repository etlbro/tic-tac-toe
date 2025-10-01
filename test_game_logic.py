
import unittest
import game_logic as GL
import player
gl = GL.Game_logic(3)

class TestPiecePlacment(unittest.TestCase):
    def test_placement(self):
        gl.start_new_game()
        self.assertTrue(gl.make_move('x', 1,1),"failed- placment") #should place
        self.assertTrue(gl.make_move('O', 2,1),"failed- placment") #should place 

        self.assertFalse(gl.make_move('x', 1,1),"failed- occupied check") #shouldnt place- spot already taken
        self.assertFalse(gl.make_move('x', 3,1),"failed- out of grid check") #shouldnt place- out of grid

class TestGameEnding(unittest.TestCase):
   
    def test_full_board(self):
        '''
        test full board detection
        '''
        gl.start_new_game()
        gl.make_move('x', 0,0)   # X O X 
        gl.make_move('O', 0,1)   # O X O
        gl.make_move('x', 0,2)   # X O
        gl.make_move('O', 1,0)
        gl.make_move('x', 1,1)
        gl.make_move('O', 1,2)
        gl.make_move('x', 2,0)
        gl.make_move('O', 2,1)
        self.assertFalse(gl.game_ended())
        gl.make_move('X', 2,2)  #now full
        self.assertTrue(gl.game_ended())

    def test_for_diagonal_victory(self):
        '''
        test for diagonal victory detection
        '''
        gl.start_new_game()
        gl.make_move('x', 0,0)   # X O X 
        gl.make_move('O', 0,1)   # O X O
        gl.make_move('x', 0,2)   # X O
        gl.make_move('O', 1,0)
        gl.make_move('x', 1,1)
        gl.make_move('O', 1,2)

        self.assertFalse(gl.check_winner('O', 1,2)) 
        gl.make_move('x', 2,0) #now there is a winner, diagonal
        self.assertTrue(gl.check_winner('x', 2,0)) 

    def test_for_row_victory(self):
        '''
        test for row victory detection
        '''
        gl.start_new_game()
        gl.make_move('x', 1,0)   # 
        gl.make_move('x', 1,1)   # x x x 
                                 #                            
        self.assertFalse(gl.check_winner('x', 1,1))         
        gl.make_move('x', 1,2)   
        self.assertTrue(gl.check_winner('x', 1,2)) 


    def test_for_col_victory(self):
        '''
        test for col victory detection
        '''
        gl.start_new_game()
        gl.make_move('x', 0,1)   #  x
        gl.make_move('x', 1,1)   #  x 
                                 #  x
        self.assertFalse(gl.check_winner('x', 1,1))      
        gl.make_move('x', 2,1)   
        self.assertTrue(gl.check_winner('x', 2,1)) 

    #def test_player_input(Self):
    #    print()
    #    gl.start_new_game()
    #    player_1 = player.HumanPlayer('x')
    #    move = player_1.get_move(gl.board) #get input
    #    gl.make_move(player_1.get_symbol(), move[0], move[1])
    #    gl.board.print_board()


    #def test_rand_comp_player(self):
    #    print()
    #    gl.start_new_game()
    #    easy_player = player.EasyComPlayer('x')
    #    move = easy_player.get_move(gl.board) #get input
    #    gl.make_move(easy_player.get_symbol(), move[0], move[1])
    #    gl.board.print_board()



    def test_hard_comp_player(self):
        gl.start_new_game()
        #check that best move is made
        gl.make_move('x', 0,0) # x   o
        gl.make_move('x', 1,0) # x   o
        gl.make_move('o', 0,2) #
        gl.make_move('o', 1,2) # check tht it know to end the game and not block
        
        hard_player = player.HardPlayer('x')
        move = hard_player.get_move(gl.board)
        assert move == (2 , 0) # best move


    def test_full_game_easy(self):
        '''
        honestly not sure this will look
        '''
        gl.start_new_game()
        gl.run_game_test(['easy', 'x'], ['easy', 'o'])
        gl.board.print_board()

    def test_full_game_hard(self):
        '''
        tic-tac-toe is a sloved game. should be a tie
        '''
        gl.start_new_game()
        gl.run_game_test(['hard', 'x'], ['hard', 'o'])
        gl.board.print_board()


if __name__ == "__main__":
    unittest.main()







