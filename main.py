import tkinter as tk
from tkinter import PhotoImage

class AppCoordenadasNether:
    def __init__(self, root):
        self.root = root
        self.root.title("Convertidor de Coordenadas Nether")
        self.root.geometry("1280x720")

        self.fondo_nether = PhotoImage(file="fondo2.png")
        self.fondo_superficie = PhotoImage(file="fondo1.png")

        self.label1 = tk.Label(root, text="Convertir Coordenadas:")
        self.label1.pack(pady=10)

        self.modo_var = tk.StringVar()
        self.modo_var.set("nether_a_superficie")

        self.marco_radio = tk.Frame(root)
        self.nether_a_superficie_radio = tk.Radiobutton(self.marco_radio, text="Convertir a Nether", variable=self.modo_var, value="nether_a_superficie", command=self.actualizar_fondo)
        self.nether_a_superficie_radio.pack(side="left", padx=10)
        self.superficie_a_nether_radio = tk.Radiobutton(self.marco_radio, text="Convertir a Superficie", variable=self.modo_var, value="superficie_a_nether", command=self.actualizar_fondo)
        self.superficie_a_nether_radio.pack(side="left", padx=10)
        self.marco_radio.pack()

        self.label2 = tk.Label(root, text="Ingrese X:")
        self.label2.pack()
        self.x_entrada = tk.Entry(root)
        self.x_entrada.pack()

        self.label3 = tk.Label(root, text="Ingrese Z:")
        self.label3.pack()
        self.z_entrada = tk.Entry(root)
        self.z_entrada.pack()

        self.boton_convertir = tk.Button(root, text="Convertir", command=self.convertir_coordenadas, bg="darkred", fg="white")
        self.boton_convertir.pack(pady=10)

        self.etiqueta_resultado = tk.Label(root, text="", font=("Helvetica", 14, "bold"))
        self.etiqueta_resultado.pack()

        self.imagen_fondo = tk.Label(root)
        self.imagen_fondo.pack(fill="both", expand=True) 

        self.actualizar_fondo()

    def actualizar_fondo(self):
        if self.modo_var.get() == "nether_a_superficie":
            self.root.config(bg="black")
            self.label1.config(bg="black", fg="white")
            self.marco_radio.config(bg="black")
            self.nether_a_superficie_radio.config(bg="black", fg="green")
            self.superficie_a_nether_radio.config(bg="black", fg="white")
            self.fondo_nether_resized = self.fondo_nether.subsample(int(self.fondo_nether.width() / 1280)) 
            self.imagen_fondo.config(image=self.fondo_nether_resized)
            
        else:
            self.root.config(bg="white")
            self.label1.config(bg="white", fg="black")
            self.marco_radio.config(bg="white")
            self.nether_a_superficie_radio.config(bg="white", fg="black")
            self.superficie_a_nether_radio.config(bg="white", fg="green")
            self.fondo_superficie_resized = self.fondo_superficie.subsample(int(self.fondo_superficie.width() / 1280))  
            self.imagen_fondo.config(image=self.fondo_superficie_resized)
            self.fondo_superficie_resized = self.fondo_superficie.subsample(int(self.fondo_superficie.width() / 1280))  
            self.imagen_fondo.config(image=self.fondo_superficie_resized)

    def convertir_coordenadas(self):
        try:
            x = float(self.x_entrada.get())
            z = float(self.z_entrada.get())

            if self.modo_var.get() == "nether_a_superficie":
                x /= 8
                z /= 8
            else:
                x *= 8
                z *= 8

            self.etiqueta_resultado.config(text=f"Coordenadas Convertidas: X = {x:.2f}, Z = {z:.2f}")
        except ValueError:
            self.etiqueta_resultado.config(text="Entrada no válida. Por favor ingrese números válidos.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AppCoordenadasNether(root)
    root.mainloop()
