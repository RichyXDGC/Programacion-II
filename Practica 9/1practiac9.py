import tkinter as tk
from tkinter import messagebox

class Boleto:
    def __init__(self, numero):
        self.numero = numero

    def obtener_precio(self):
        return 0.0

    def __str__(self):
        return f"Número: {self.numero}, Precio: {self.obtener_precio()}"

class Palco(Boleto):
    def obtener_precio(self):
        return 100.0

class Platea(Boleto):
    def __init__(self, numero, dias):
        super().__init__(numero)
        self.dias = dias

    def obtener_precio(self):
        return 50.0 if self.dias >= 10 else 60.0

class Galeria(Boleto):
    def __init__(self, numero, dias):
        super().__init__(numero)
        self.dias = dias

    def obtener_precio(self):
        return 25.0 if self.dias >= 10 else 30.0

class TeatroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Teatro Municipal")
        tk.Label(root, text="Teatro municipal", font=("Arial", 18)).pack()
        tk.Label(root, text="Datos del Boleto", font=("Arial", 10)).pack()

        self.tipo = tk.StringVar(value="Palco")
        tipos_frame = tk.Frame(root)
        tipos_frame.pack()
        for t in ["Palco", "Platea", "Galeria"]:
            tk.Radiobutton(tipos_frame, text=t, variable=self.tipo, value=t).pack(side=tk.LEFT)

        tk.Label(root, text="Número de Boleto:").pack()
        self.numero_entry = tk.Entry(root)
        self.numero_entry.pack()

        tk.Label(root, text="Días de Anticipación:").pack()
        self.dias_entry = tk.Entry(root)
        self.dias_entry.pack()

        botones_frame = tk.Frame(root)
        botones_frame.pack(pady=10)
        tk.Button(botones_frame, text="Vender", command=self.vender_boleto).pack(side=tk.LEFT, padx=10)
        tk.Button(botones_frame, text="Salir", command=root.quit).pack(side=tk.LEFT, padx=10)

        
        self.resultado = tk.Label(root, text="", font=("Arial", 12))
        self.resultado.pack(pady=10)

    def vender_boleto(self):
        try:
            numero = int(self.numero_entry.get())
            dias = self.dias_entry.get()
            dias = int(dias) if dias.strip() else 0

            tipo = self.tipo.get()
            if tipo == "Palco":
                boleto = Palco(numero)
            elif tipo == "Platea":
                boleto = Platea(numero, dias)
            elif tipo == "Galeria":
                boleto = Galeria(numero, dias)
            else:
                raise ValueError("Tipo inválido")

            self.resultado.config(text=str(boleto))

        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese datos válidos.")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x300")
    app = TeatroApp(root)
    root.mainloop()
