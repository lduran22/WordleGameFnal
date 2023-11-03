import tkinter as tk
from tkinter import messagebox

class WordleGUI:
    def __init__(self, root, game):
        self.root = root
        self.root.title("Wordle")
        self.game = game
        self.definicion_disponible = False

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

        self.definition_button = tk.Button(self.frame, text="Ver Definición", command=self.ver_definicion, state="disabled")
        self.definition_button.pack()

        self.attempts_label = tk.Label(self.frame, text=f"Intentos restantes: {self.game.intentos_restantes}")
        self.attempts_label.pack()
        self.word_display_frame = tk.Frame(self.frame)
        self.word_display_frame.pack()

        self.word_display_labels = []
        for i in range(5):
            label = tk.Label(self.word_display_frame, text='', width=2, height=2, borderwidth=2, relief='ridge')
            label.grid(row=0, column=i, padx=5)
            self.word_display_labels.append(label)

    def realizar_intento(self):
        palabra = self.entry.get().strip()
        if len(palabra) != 5:
            messagebox.showwarning("Wordle", "La palabra debe tener exactamente 5 letras.")
            return

        self.game.realizar_intento(palabra)
        retroalimentacion = self.game.historial_intentos[-1][1]

        for i in range(5):
            self.word_display_labels[i].config(text=palabra[i])

            if palabra[i] == self.game.palabra_oculta[i]:
                self.word_display_labels[i].config(bg='green')
            elif palabra[i] in self.game.palabra_oculta:
                self.word_display_labels[i].config(bg='yellow')
            else:
                self.word_display_labels[i].config(bg='gray')

        retroalimentacion_message = f"Retroalimentación: " \
                                    f"{retroalimentacion.correctas_posicion} en posición correcta, " \
                                    f"{retroalimentacion.correctas_incorrectas_posicion} en posición incorrecta, " \
                                    f"{retroalimentacion.incorrectas} incorrectas."
        messagebox.showinfo("Wordle", retroalimentacion_message)

        if self.game.verificar_victoria():
            messagebox.showinfo("Wordle", "¡Has ganado!")
            self.definition_button.config(state="active")
        elif self.game.verificar_derrota():
            messagebox.showinfo("Wordle", f"Has perdido. La palabra oculta era: {self.game.palabra_oculta}")
            self.definition_button.config(state="active")

        self.attempts_label.config(text=f"Intentos restantes: {self.game.intentos_restantes}")

    def iniciar_nueva_partida(self):
        self.game.iniciar_nueva_partida()
        self.attempts_label.config(text=f"Intentos restantes: {self.game.intentos_restantes}")
        self.entry.delete(0, 'end')
        self.definition_button.config(state="disabled")

    def ver_definicion(self):
        palabra_oculta = self.game.palabra_oculta
        definicion = self.game.definiciones.get(palabra_oculta, "Definición no encontrada.")
        messagebox.showinfo("Definición de la Palabra Oculta", definicion)
