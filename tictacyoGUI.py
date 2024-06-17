import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'
        self.buttons = []
        self.play_mode = None
        self.create_mode_selection()

    def create_mode_selection(self):
        self.mode_frame = tk.Frame(self.root)
        self.mode_frame.pack()
        tk.Label(self.mode_frame, text="Choose a mode", font='normal 20 bold').pack()

        tk.Button(self.mode_frame, text="Player vs Player", font='normal 20 bold', command=self.start_pvp).pack(pady=10)
        tk.Button(self.mode_frame, text="Player vs Computer", font='normal 20 bold', command=self.start_pvc).pack(pady=10)

    def start_pvp(self):
        self.play_mode = 'PVP'
        self.mode_frame.pack_forget()
        self.create_board()

    def start_pvc(self):
        self.play_mode = 'PVC'
        self.mode_frame.pack_forget()
        self.create_board()

    def create_board(self):
        board_frame = tk.Frame(self.root)
        board_frame.pack()
        for i in range(9):
            button = tk.Button(board_frame, text=' ', font='normal 20 bold', height=3, width=6, background='black', fg = "white",
                               command=lambda i=i: self.make_move(i, self.current_player))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)

    def make_move(self, index, player):
        if self.board[index] == ' ':
            self.board[index] = player
            self.buttons[index].config(text=player)
            if self.check_win(player):
                messagebox.showinfo("Tic Tac Toe", f"Player {player} wins!")
                self.reset_game()
            elif ' ' not in self.board:
                messagebox.showinfo("Tic Tac Toe", "It's a tie!")
                self.reset_game()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
                if self.play_mode == 'PVC' and self.current_player == 'O':
                    self.computer_move()

    def computer_move(self):
        empty_cells = [i for i in range(9) if self.board[i] == ' ']
        move = random.choice(empty_cells)
        self.make_move(move, 'O')

    def check_win(self, player):
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
                          (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
                          (0, 4, 8), (2, 4, 6)]             # diagonals
        return any(all(self.board[i] == player for i in condition) for condition in win_conditions)

    def reset_game(self):
        self.board = [' ' for _ in range(9)]
        for button in self.buttons:
            button.config(text=' ')
        self.current_player = 'X'
        if self.play_mode == 'PVC' and self.current_player == 'O':
            self.computer_move()

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
