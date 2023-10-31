import tkinter as tk
from tkinter import messagebox


class WordleGUI:
    def __init__(self, root, game):
        self.root = root
        self.root.title("Wordle")
        self.game = game

        self.frame = tk.Frame(root)
        self.frame.pack(padx=20, pady=20)

        self.label = tk.Label(self.frame, text="Adivina la palabra oculta de 5 letras:")
        self.label.pack()

        self.entry = tk.Entry(self.frame, width=10)
        self.entry.pack()

        self.submit_button = tk.Button(self.frame, text="Intentar", command=self.realizar_intento)
        self.submit_button.pack()

        self.new_game_button = tk.Button(self.frame, text="Nueva partida", command=self.iniciar_nueva_partida)
        self.new_game_button.pack()

        self.attempts_label = tk.Label(self.frame, text=f"Intentos restantes: {self.game.intentos_restantes}")
        self.attempts_label.pack()

    def realizar_intento(self):
        palabra = self.entry.get().strip()
        if len(palabra) != 5:
            messagebox.showwarning("Wordle", "La palabra debe tener exactamente 5 letras.")
            return

        self.game.realizar_intento(palabra)
        retroalimentacion = self.game.historial_intentos[-1][1]
        palabra_con_aciertos = []
        for i in range(5):
            if palabra[i] == self.game.palabra_oculta[i]:
                palabra_con_aciertos.append(palabra[i])
            else:
                palabra_con_aciertos.append("-")
        palabra_con_aciertos = "".join(palabra_con_aciertos)

        retroalimentacion_message = f"Intento: {palabra} - Retroalimentación: {retroalimentacion.correctas_incorrectas_posicion} correctas en posición incorrecta, " \
              f"{retroalimentacion.incorrectas} incorrectas. Palabra con aciertos: {palabra_con_aciertos}"
        messagebox.showinfo("Wordle", retroalimentacion_message)

        if self.game.verificar_victoria():
            messagebox.showinfo("Wordle", "¡Has ganado!")
        elif self.game.verificar_derrota():
            messagebox.showinfo("Wordle", f"Has perdido. La palabra oculta era: {self.game.palabra_oculta}")

        self.attempts_label.config(text=f"Intentos restantes: {self.game.intentos_restantes}")

    def iniciar_nueva_partida(self):
        self.game.iniciar_nueva_partida()
        self.attempts_label.config(text=f"Intentos restantes: {self.game.intentos_restantes}")
        self.entry.delete(0, 'end')

