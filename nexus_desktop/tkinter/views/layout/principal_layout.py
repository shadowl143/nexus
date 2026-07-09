import ttkbootstrap as tb
import os
import sys
from nexus_core.design_tokens import TYPOGRAPHY


class WindowsPrincipal:
    def __init__(self, pantallas: dict[str, tb.Frame]):
        # configuracion ventana principal
        self.root = tb.Window(themename="flatly")
        self.root.title("Proyecto integrador")
        self.root.minsize(2000, 900)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.pantallas = pantallas
        self.menu_lateral = tb.Frame(self.root, width=150, relief="solid")
        self.root.protocol("WM_DELETE_WINDOW", self.cerrar_limpio)
        local_path = os.path.join("nexus_desktop", "tkinter", "assets", "icon.ico")
        self.root.iconbitmap(local_path)

        # configuración menu lateral.
        self.menu_lateral.pack_propagate(False)
        self.menu_lateral.pack(side="left", fill="y", padx=(0, 10))
        self.windows = ""

        # metodos uso menu
        self.mostrar_pantalla("Inicio")
        self.crear_botones_menu()

    def crear_botones_menu(self):
        for nombre_pantalla in self.pantallas.keys():
            boton = tb.Button(
                self.menu_lateral,
                text=nombre_pantalla,
                bootstyle="link",
                command=lambda name=nombre_pantalla: self.select_frame(name),
            )
            boton.pack(fill="x", padx=15, pady=8, anchor="w")

    def mostrar_pantalla(self, nombre_pantalla):
        for nombre, creador_frame in self.pantallas.items():
            self.pantallas[nombre] = creador_frame(self.root)
            self.pantallas[nombre].pack_forget()
        self.windows = nombre_pantalla
        self.pantallas[nombre_pantalla].pack(fill="both", expand=True)

    def select_frame(self, name):
        self.pantallas[self.windows].pack_forget()
        self.pantallas[name].pack(fill="both", expand=True)
        self.windows = name

    def iniciar(self):
        self.root.mainloop()

    def cerrar_limpio(self):
        # 1. Destruye la interfaz de Tkinter de forma segura
        self.root.destroy()
        # 2. Mata el proceso de Python de raíz, deteniendo cualquier hilo colgado
        sys.exit()
