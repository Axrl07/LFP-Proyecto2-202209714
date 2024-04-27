import tkinter as tk
from tkinter import filedialog
from tkinter import font
from tkinter import messagebox

class Ventana:
    def __init__(self, root=tk.Tk()):
        self.root = root
        self.data = []
        self.root.title("Proyecto 1 - Lenguajes Formales y de Programacion")
        ancho_ventana, alto_ventana = self.root.winfo_reqwidth(), self.root.winfo_reqheight()
        pos_x = int(self.root.winfo_screenwidth() / 4 - ancho_ventana / 4)
        pos_y = int(self.root.winfo_screenheight() / 4 - alto_ventana / 4)
        self.root.geometry(f"900x550+{pos_x}+{pos_y}")
        self.root.resizable(False, False)

        self.boton_abrir = tk.Button(self.root, text="Abrir archivo", command=self.abrir_explorador)
        self.boton_abrir.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.boton_borrar_entrada = tk.Button(self.root, text="Borrar entrada",
                                              command=lambda: self.area_entrada.delete("1.0", "end"))
        self.boton_borrar_entrada.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        self.boto_borrar_salida = tk.Button(self.root, text="Borrar salida", command=self.borrar)
        self.boto_borrar_salida.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        self.entrada = tk.Label(self.root, text="Texto de entrada")
        self.entrada.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.salida = tk.Label(self.root, text="Traduccion")
        self.salida.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        self.area_entrada = tk.Text(self.root, width=50, height=20)
        self.area_entrada.grid(row=4, column=0, padx=10, pady=10)

        self.area_salida = tk.Text(self.root, width=50, height=20, state="disabled")
        self.area_salida.grid(row=4, column=1, padx=10, pady=10)

        self.boton_traducir = tk.Button(self.root, text="Traducir", command=self.traducir)
        self.boton_traducir.grid(row=6, column=0, padx=10, pady=10, sticky="e")

    def borrar(self):
        self.area_salida.config(state="normal")
        self.area_salida.delete("1.0", "end")
        self.area_salida.config(state="disabled")

    def abrir_explorador(self):
        filepath = filedialog.askopenfilename(
            initialdir="/",
            title="Selecciona un archivo",
            filetypes=(
                ("Archivos de texto", "*.json"),
                ("Archivos de texto", "*.lfp"),
                ("Todos los archivos", "*.*")
            )
        )
        self.data = [filepath, filepath.split("/")[-1], open(filepath, "r").read()]
        self.area_entrada.delete("1.0", "end")
        self.area_entrada.insert("1.0", str(self.data[2]))

    def traducir(self):
        entrada = len(str(self.area_entrada.get("1.0", "end")))

        if entrada <= 21:
            return messagebox.showerror("Error", "No hay contenido para traducir")
        else:
            # configurando contenido
            aux, nombre, contenido_archivo = self.data
            contenido_area = str(self.area_entrada.get("1.0", "end"))
            if contenido_archivo != contenido_area:
                contenido = contenido_area
            else:
                contenido = contenido_archivo
            print(contenido)
            # ejecutamos main.py


if __name__ == "__main__":
    app = Ventana()
    app.root.mainloop()
