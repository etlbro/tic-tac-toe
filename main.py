import game_logic
import sys


def main():
    gl = game_logic.Game_logic(size=3)
    x = 'x'
    o = 'o'

    while True:
        while True:
            player_1_type = input("please enter the player type for player 1 (x)\n" \
            " options are- human, hard, medium , easy \n >>").strip().lower()        
            if player_1_type in ['human', 'hard', 'medium', 'easy']:
                break
            print("Invalid command. Accepted options: human, hard, medium, easy")      
        while True:
            player_2_type = input("please enter the player type for player 2 (o)\n" \
            " options are- human, hard, medium , easy\n >>").strip().lower()

            if player_2_type not in ['human', 'hard', 'medium', 'easy']:
                print("invalid command. accepted options are: 'human', 'hard', 'medium', 'easy") 
            else:
                break       
        while True:
            gl.run_game([player_1_type, x], [ player_2_type, o])
            
            new_game_options= input("good game! type-\n" \
            "y to play again\n" \
            "n to set new player settings\n" \
            "q to exit game\n>>").strip().lower()
            if new_game_options == 'y':
                pass
            elif new_game_options == 'n':
                break
            else:
                sys.exit()



if __name__ == "__main__":
    main()