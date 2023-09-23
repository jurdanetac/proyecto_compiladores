#!/usr/bin/env python3

"""Proyecto para la cátedra de 'Compiladores'. Consiste en un editor de
texto el cual permita llevar a cabo los distintos análisis típicos de un
lenguaje de programación al momento de su compilación"""


# Imports #####################################################################

import tkinter as tk

from pathlib import Path
from tkinter import filedialog
from tkinter import messagebox

###############################################################################

# Variables ###################################################################

# Crear ventana principal
root: tk.Tk = tk.Tk()

# Crear área principal de escritura de texto
textbox = tk.Text(root)

# directorio del archivo
filedir: Path = Path("archivos").resolve()

# directorio del archivo
filename: tk.StringVar = tk.StringVar()
filename.set(str(filedir / "Sin-titulo.txt"))

###############################################################################

# Functions ###################################################################


def open_file() -> None:
    """Abrir archivo"""

    # Archivo a abrir
    file = filedialog.askopenfile(
        initialdir="archivos",
        filetypes=(("text files", "*.txt"), ("all files", "*.*")),
    )

    # Si se seleccionó un archivo correctamente
    if file is not None:
        text = file.read()

        textbox.delete(0.0, tk.END)
        textbox.insert(0.0, text)

        filename.set(file.name)


def new_file() -> None:
    """Nuevo archivo"""

    # Actualizar nombre del archivo actual
    filename.set(str(filedir / "Sin-titulo.txt"))

    # Vaciar editor
    textbox.delete(0.0, tk.END)


# Crear submenú con las entradas `args` y agregarlo a la barra menú
def create_cascade(args: dict, menubar: tk.Menu) -> tk.Menu:
    """Crear submenu para la barra de menú principal"""

    # Crear submenú
    cascade = tk.Menu(
        menubar,
        tearoff=0,
        background="lightgray",
        activebackground="lightblue",
        border=0,
        relief="flat",
        activeborderwidth=0,
    )

    # Añadir opciones al submenú
    for entry, command in args.items():
        cascade.add_command(label=entry, command=command)

    return cascade


# https://stackoverflow.com/a/13808423
# Seleccionar todo el texto en la caja de texto
def select_all(event):
    textbox.tag_add(tk.SEL, "1.0", tk.END)
    textbox.mark_set(tk.INSERT, "1.0")
    textbox.see(tk.INSERT)
    return "break"


def save_file_as() -> None:
    text = textbox.get(0.0, tk.END)

    file = filedialog.asksaveasfile(
        initialdir="archivos",
        filetypes=(("text files", "*.txt"), ("all files", "*.*")),
        mode="w",
        defaultextension=".txt",
    )

    if file is not None:
        try:
            with open(file.name, "w") as archivo:
                archivo.write(text)

            filename.set(file.name)
        except:
            messagebox.showerror(title="Oops", message="Error")


def save_file(event) -> None:
    """Wrapper para guardar archivo como"""
    text = textbox.get(0.0, tk.END)

    # Guardar archivo
    Path(filedir).mkdir(exist_ok=True)  # crear directorio si no existe

    with open(Path(filedir).resolve() / filename.get(), "w") as archivo:
        archivo.write(text)


def setup_tk() -> tk.Tk:
    """Construye la app"""
    root.wm_title("Preprocesador")

    # Crear título dinámico que indica qué archivo está abierto
    title = tk.Label(root, textvariable=filename)
    title.pack()

    # Seleccionar todo el texto con Control + a/A
    textbox.bind("<Control-Key-a>", select_all)
    textbox.bind("<Control-Key-A>", select_all)
    # Guardar con Control + s/S
    textbox.bind("<Control-Key-s>", save_file)
    textbox.bind("<Control-Key-S>", save_file)
    textbox.pack()

    root.geometry("800x500")  # dimensiones de la ventana
    root.resizable(height=False, width=False)  # no redimension

    # Crear barra de menú
    menubar = tk.Menu(
        root,
        background="white",
        activebackground="lightblue",
        border=0,
        relief="flat",
        activeborderwidth=0,
    )

    # Anexar a la barra de menú submenu 'Archivo'
    menubar.add_cascade(
        menu=create_cascade(
            {
                "Nuevo": new_file,
                "Abrir": open_file,
                "Guardar": save_file,
                "Guardar Como": save_file_as,
                "Salir": exit,
            },
            menubar,
        ),
        label="Archivo",
    )

    # Anexar a la barra de menú submenu 'Análisis'
    menubar.add_cascade(
        menu=create_cascade(
            {
                "Léxico": lambda: None,
                "Sintáctico": lambda: None,
                "Árbol": lambda: None,
            },
            menubar,
        ),
        label="Análisis",
    )

    # Anexar a la barra de menú submenu 'Ver'
    menubar.add_cascade(
        menu=create_cascade(
            {
                "Tabla de símbolos": lambda: None,
                "Detección de errores": lambda: None,
            },
            menubar,
        ),
        label="Ver",
    )

    # Configurar menú en la ventana
    root.configure(menu=menubar)

    return root


###############################################################################

if __name__ == "__main__":
    app: tk.Tk = setup_tk()
    app.mainloop()
