#!/usr/bin/env python3

from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
import pyglet


pyglet.resource.add_font("jbm.ttf")


class App:
    """Proyecto para la cátedra de 'Compiladores'. Consiste en un editor de
    texto el cual permitirá llevar a cabo los distintos análisis típicos de un
    lenguaje de programación al momento de su compilación"""

    def __init__(self) -> None:
        """Construye la app"""
        # Crear ventana principal
        self.root = ThemedTk(theme="black")
        # Establecer dimensiones de la ventana
        self.root.geometry("800x500")
        self.root.resizable(height=False, width=False)
        # Crear barra de menú
        self.menubar = Menu(
            self.root,
            background="white",
            activebackground="lightblue",
            border=0,
            relief="flat",
            activeborderwidth=0,
        )

        # Anexar a la barra de menú submenu 'Archivo'
        self.menubar.add_cascade(
            menu=self.create_cascade(
                {
                    "Abrir": self.open_file,
                    "Guardar": self.save_file,
                    "Salir": exit,
                }
            ),
            label="Archivo",
        )

        # Anexar a la barra de menú submenu 'Análisis'
        self.menubar.add_cascade(
            menu=self.create_cascade(
                {
                    "Léxico": lambda: None,
                    "Sintáctico": lambda: None,
                    "Árbol": lambda: None,
                }
            ),
            label="Análisis",
        )

        # Anexar a la barra de menú submenu 'Ver'
        self.menubar.add_cascade(
            menu=self.create_cascade(
                {
                    "Tabla de símbolos": lambda: None,
                    "Detección de errores": lambda: None,
                }
            ),
            label="Ver",
        )

        # Crear área principal de escritura de texto
        self.textbox = Text(self.root, font=("JetBrains Mono", 16))
        # Seleccionar todo el texto con Control + a/A
        self.textbox.bind("<Control-Key-a>", self.select_all)
        self.textbox.bind("<Control-Key-A>", self.select_all)

        self.textbox.pack()

        # Configurar menú en la ventana
        self.root.configure(menu=self.menubar)

    # https://stackoverflow.com/a/13808423
    # Seleccionar todo el texto en la caja de texto
    def select_all(self, event):
        self.textbox.tag_add(SEL, "1.0", END)
        self.textbox.mark_set(INSERT, "1.0")
        self.textbox.see(INSERT)
        return "break"

    # Crear submenú con las entradas `args` y agregarlo a la barra menú
    def create_cascade(self, args: dict) -> Menu:
        cascade = Menu(
            self.menubar,
            tearoff=0,
            background="lightgray",
            activebackground="lightblue",
            border=0,
            relief="flat",
            activeborderwidth=0,
        )

        for entry, command in args.items():
            cascade.add_command(label=entry, command=command)

        return cascade

    def open_file(self) -> None:
        """Abrir archivo"""
        # TODO
        print("abrir")

    def save_file(self) -> None:
        """Guardar archivo"""
        # TODO
        print("guardar")

    def run(self) -> None:
        """Ejecutar app"""
        self.root.mainloop()


if __name__ == "__main__":
    app = App()  # Crear app
    app.run()  # Ejecutar
