#  Tic-Tac-Toe

A modern, object-oriented Tic-Tac-Toe game implemented in **Python**.  
It supports human vs. human, human vs. computer, and computer vs. computer matches, and can be run either with a GUI or in the console.

---

##  Features

- **Clean OOP architecture** using an abstract `AbsPlayer` base class and concrete player types.
- **Multiple player modes:** Human, Random AI, (future) Minimax AI.
- **GUI support** via a `gui` module (Tkinter/PyQt/etc.), plus optional console mode.
- **Factory pattern** for easily adding new player types.
- **Validations** for moves and board states.
- **Scalable grid size** (default 3×3).

---

##  How It Works

- The `Board` class manages the grid, checks for valid moves, and detects wins/draws.
- The `AbsPlayer` abstract base class defines the interface for all players.
- `HumanPlayer`, `RandomPlayer`, and other computer classes inherit from `AbsPlayer`.
- The `game_logic` class ties everything together: it sets up players, alternates turns, and updates the GUI/console.

---

##  Project Structure

tic-tac-toe/

│
├── main.py           # Entry point

├── board.py          # basic board logic, 

├── game_logic.py     # game rules and management

├── player.py         # Player classes (human + AI) 

└── README.md



##  How to Run

Clone the repository and run:

```bash
python main.py
```

## How to Play (CLI)

### Choose player types
On startup, you’ll be asked to enter the type of each player:

please enter the player type for player 1 (x) options are- human or computer: hard, medium, easy >> human
please enter the player type for player 2 (o) options are- human or computer: hard, medium, easy >> hard

### Take turns making moves
The game prints which player’s turn it is:

x's turn

If you’re a human player, the program will prompt you to enter the row and column of your move:

select row: 1
select column: 2

(Rows and columns are numbered starting at 0.)

### Board display
After each move, the board prints to the console so you can see the updated game state.

### Winning and ending
When someone wins, the game prints:

x wins! well played!

### When the board is full with no winner, it prints:

game over

### post game options
After a game
You’ll be prompted to:
- y — play again with the same players
- n — set up new player settings
- q — quit the program


## Future Plans

- Graphical User Interface (GUI):
A Tkinter-based interface to click on cells instead of typing moves.

- Packaging as an Executable (.exe):
So the game can run without Python installed.
