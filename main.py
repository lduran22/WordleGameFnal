import tkinter as tk
from wordle_game import WordleGame
from wordle_gui import WordleGUI

if __name__ == "__main__":
    root = tk.Tk()
    game = WordleGame()
    gui = WordleGUI(root, game)
    root.mainloop()