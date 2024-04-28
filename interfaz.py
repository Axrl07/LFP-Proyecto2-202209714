import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

# archivo
ruta = ""

def nuevo(area):
    contenido = area.get("1.0", "end-1c")
    if len(contenido.strip()) > 0:
        respuesta = messagebox.askyesnocancel("Nuevo archivo", "¿Desea guardar los cambios en el archivo actual")
        if respuesta is None:
            return
        elif respuesta:
            guardarComo(area)
    area.delete("1.0", "end")

def abrir(area):
    global ruta
    nuevaRuta = filedialog.askopenfilename(filetypes=[("Archivos de texto", ".txt"), ("Archivos LFP", ".lfp"), ("Todos los archivos", ".*")])
    contenido = area.get("1.0", "end-1c")

    if len(contenido) > 10:
        respuesta = messagebox.askyesnocancel("Nuevo archivo", "¿Desea guardar los cambios en el archivo actual")
        if respuesta:
            guardarComo(area)

    if nuevaRuta:
        with open(nuevaRuta, "r", encoding="utf-8") as file:
            contenido = file.read()
            area.delete("1.0", "end")
            area.insert("1.0", contenido)
            ruta = nuevaRuta

def guardar(area):
    global ruta
    if ruta:
        contenido = area.get("1.0", "end-1c")
        with open(ruta, "w") as file:
            file.write(contenido)
    else:
        guardarComo(area)


def guardarComo(area):
    global ruta
    nuevaRuta = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt"), ("Archivos LFP", "*.lfp")])
    if nuevaRuta:
        contenido = area.get("1.0", "end-1c")
        with open(nuevaRuta, "w") as file:
            file.write(contenido)
        ruta = nuevaRuta

def salir(area, raiz):
    contenido = area.get("1.0", "end-1c")
    salir = messagebox.askyesno("Salir", "¿Está seguro que desea salir del programa?")
    if salir:
        if len(contenido.strip()) > 0:
            respuesta = messagebox.askyesnocancel("Nuevo archivo", "¿Desea guardar los cambios en el archivo actual")
            if respuesta:
                guardarComo(area)
                if salir:
                    raiz.destroy()
            elif respuesta is False:
                raiz.destroy()


# analisis

def generarSentencias(area):
    print("Generar sentencias MongoDB")
    pass


# listados

def tokens(area):
    print("Ver Tokens")
    global ruta
    print(ruta)
    directorio = ruta.split("/").pop(-1)
    print(directorio)

def errores(area):
    print( "Ver Errores")


# editor

def editor():
    root = tk.Tk()
    root.title('Editor de peudo-codigo a mongoDB en python')
    root.config(bg="#1C2833")

    ancho = root.winfo_reqwidth()
    alto = root.winfo_reqheight()
    pos_x = int(root.winfo_screenwidth() / 4 - ancho / 4)
    pos_y = int(root.winfo_screenheight() / 4 - alto / 4)
    root.geometry(f"900x550+{pos_x}+{pos_y}")
    root.resizable(False, False)

    # barra de menus
    barraMenus = tk.Menu(root)
    root.config(menu=barraMenus)

    # menus
    archivo = tk.Menu(barraMenus)
    analisis = tk.Menu(barraMenus)
    listados = tk.Menu(barraMenus)
    
    barraMenus.add_cascade(label='Archivo', menu=archivo)
    barraMenus.add_cascade(label='Analisis', menu=analisis)
    barraMenus.add_cascade(label='Listados', menu=listados)

    # opciones de archivo
    archivo.add_command(label='Nuevo', command=lambda:nuevo(area))
    archivo.add_command(label='Abrir', command=lambda:abrir(area))
    archivo.add_command(label='Guardar', command=lambda:guardar(area))
    archivo.add_command(label='Guardar Como', command=lambda:guardarComo(area))
    archivo.add_separator()
    archivo.add_command(label='Salir', command=lambda:salir(area, root))

    # opciones de analisis
    analisis.add_command(label='generar sentencias', command=lambda:generarSentencias(area))

    # opciones de listados
    listados.add_command(label='Tokens', command=lambda:tokens(area))
    listados.add_separator()
    listados.add_command(label='Errores', command=lambda:errores(area))

    # Area de texto
    texto = tk.Label(root, text="Ingrese el pseudo-codigo o abra un archivo:", bg="#1C2833", fg="white", font=("Bahnschrift", 20))
    texto.pack(anchor="w", padx=10, pady=5)
    area = tk.Text(root, font=("JetBrains Mono", 15))
    area.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    editor()
