import tkinter as tk
from tkinter import ttk


class TicTacToeApp:
    def __init__(self, on_user_move=None,
                       on_start_game=None,
                       on_new_game=None):
        #these are the function to notify of user's choice
        self.on_user_move = on_user_move
        self.on_start_game = on_start_game
        self.on_new_game = on_new_game

        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.root.geometry("400x450")

        # save player types
        self.player1_var = tk.StringVar(value="human")
        self.player2_var = tk.StringVar(value="hard")

        # create the two frames - menu and playboard
        self.menu_frame = tk.Frame(self.root)
        self.game_frame = tk.Frame(self.root)

        self.build_menu_frame()
        self.build_game_frame()

        # start with menu
        self.show_frame(self.menu_frame)

        # for grid cell sizes
        self.cell_width = None
        self.cell_height = None

    def build_menu_frame(self):
        """Menu frame with player type dropdowns and 'start' button"""
        tk.Label(self.menu_frame, text="Player 1:").pack(pady=10)
        player1_combo = ttk.Combobox(
            self.menu_frame,
            textvariable=self.player1_var,
            values=["human", "easy", "medium", "hard"]
        )
        player1_combo.pack()

        tk.Label(self.menu_frame, text="Player 2:").pack(pady=10)
        player2_combo = ttk.Combobox(
            self.menu_frame,
            textvariable=self.player2_var,
            values=["human", "easy", "medium", "hard"]
        )
        player2_combo.pack()

        start_button = tk.Button(self.menu_frame, text="Start Game",
                                 command=self.start_game)
        start_button.pack(pady=20)

        self.menu_frame.pack(fill="both", expand=True)

    def build_game_frame(self):
        """Game frame with canvas and control buttons"""
        control_frame = tk.Frame(self.game_frame)
        control_frame.pack(fill="x")

        new_game_btn = tk.Button(control_frame, text="New Game",
                                 command=self.new_game)
        new_game_btn.pack(side="left", padx=10, pady=10)

        back_btn = tk.Button(control_frame, text="Return to Menu",
                             command=lambda: self.show_frame(self.menu_frame))
        back_btn.pack(side="left", padx=10, pady=10)

        self.canvas = tk.Canvas(self.game_frame, bg="white")
        self.canvas.pack(fill="both", expand=True)
        self.canvas.bind("<Configure>", self.on_resize)
        self.canvas.bind("<Button-1>", self.on_click)

    def show_frame(self, frame):
        """Hide all frames and show the one passed in"""
        for f in (self.menu_frame, self.game_frame):
            f.pack_forget()
        frame.pack(fill="both", expand=True)
        if frame == self.game_frame:
            self.draw_grid()

    
    #notifys game logic game started
    def start_game(self):
        if self.on_start_game:
            self.on_start_game(self.player1_var.get(),
                               self.player2_var.get())
        self.show_frame(self.game_frame)
    
    #notifys game logic new game selected
    def new_game(self):
        if self.on_new_game:
            self.on_new_game()
        self.canvas.delete("mark")
        self.draw_grid()

    def draw_grid(self):
        """Draw Tic Tac Toe grid"""
        self.canvas.delete("grid")
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()
        self.cell_width = width / 3
        self.cell_height = height / 3
        for i in range(1, 3):
            x = i * self.cell_width
            y = i * self.cell_height
            self.canvas.create_line(x, 0, x, height, tags="grid")
            self.canvas.create_line(0, y, width, y, tags="grid")

    def on_resize(self, event):
        """Redraw grid when resized"""
        self.draw_grid()

    def on_click(self, event):
        """Handle mouse clicks on the board"""
        if not self.cell_width or not self.cell_height:
            return
        col = int(event.x // self.cell_width)
        row = int(event.y // self.cell_height)
        print(f"Clicked cell {row}, {col}")
        

        #notify gamelogic the selected move
        if self.on_user_move:
            self.on_user_move(row, col)

    def on_move(self, row, col, symbol):
        """Draw a symbol in the given cell"""
        if not self.cell_width or not self.cell_height:
            return
        x1 = col * self.cell_width
        y1 = row * self.cell_height
        x2 = x1 + self.cell_width
        y2 = y1 + self.cell_height
        self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2,
                                text=symbol,
                                font=("Arial", int(self.cell_height / 2)),
                                tags="mark")

    def on_game_over(self, message="Game tied!"):
        """Display a game-over message on the canvas."""
        # Clear any previous marks if you want, or keep them
        # self.canvas.delete("mark")  # optional

        # draw a semi-transparent overlay (optional)
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()
        self.canvas.create_rectangle(0, 0, width, height,
                                     fill="white", stipple="gray50",
                                     tags="game_over")

        # draw the message
        self.canvas.create_text(width/2, height/2,
                                text=message + "\nClick 'New Game' or 'Return to Menu'",
                                font=("Arial", 16),
                                fill="red",
                                justify="center",
                                tags="game_over")

    def on_game_winner(self, player):
        """Called by backend when a player wins. Displays winner message."""
        # Optional: clear previous marks if desired
        # self.canvas.delete("mark")

        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()

        # draw a semi-transparent overlay to make the message clear
        self.canvas.create_rectangle(0, 0, width, height,
                                     fill="white", stipple="gray50",
                                     tags="game_over")

        # draw the winner message in the center
        self.canvas.create_text(width/2, height/2,
                                text=f"Player {player} wins!\nClick 'New Game' or 'Return to Menu'",
                                font=("Arial", 16),
                                fill="green",
                                justify="center",
                                tags="game_over")



    def run(self):
        self.root.mainloop()

#for testeing porpuses
if __name__ == "__main__":
    app = TicTacToeApp()
    app.run()
