import ttkbootstrap as tb
import os
import sys
from nexus_core.theme import mode_dark
import tkinter as tk
from nexus_desktop.tkinter.views.frame.inicio import inicio_frame as inicio
from nexus_desktop.tkinter.views.frame.entregas import entregas_frame as entregas
from nexus_desktop.tkinter.views.frame.rider import rider_frame as rider
import locale

from nexus_desktop.tkinter.controllers.rider.rider_controller import RiderController
from nexus_desktop.tkinter.services.rider.rider_service import RiderService
from nexus_desktop.tkinter.services.entregas.entregas_service import EntregaService
from nexus_desktop.tkinter.controllers.entregas.entrega_controller import (
    EntregaController,
)

rider_service = RiderService()
ridercontroller = RiderController(rider_service)

entregas_service = EntregaService()
entrega_controller = EntregaController(entregas_service)


class WindowsPrincipal:
    def __init__(self, mode=False):
        # configuracion ventana principal
        self.root = tb.Window(themename="flatly")

        self.dark_var = tk.BooleanVar(master=self.root, value=mode)
        mode_dark(self.root, self.dark_var.get())

        self.languge = tk.StringVar(master=self.root, value=self.get_system_language())

        self.root.title("Proyecto integrador")
        self.root.minsize(2000, 900)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.pantallas = self.frames()
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

    def frames(self):

        frames = {
            "Inicio": lambda contenedor: inicio.InicioFrame(
                contenedor, self.languge, self.dark_var, self.toggle_theme
            ).crear_frame_inicio(),
            "Entregas": lambda contenedor: entregas.EntregasFrame(
                contenedor, self.languge.get(), entrega_controller, ridercontroller
            ).crear_frame_inicio(),
            "Riders": lambda contenedor: rider.RidesFrame(
                contenedor, self.languge.get(), ridercontroller
            ).crear_frame_inicio(),
        }
        return frames

    def toggle_theme(self):
        print(self.dark_var.get())
        mode_dark(self.root, self.dark_var.get())

    @staticmethod
    def get_system_language():
        # Obtiene el lenguaje del sistema
        lang, _ = locale.getdefaultlocale()
        return lang

    def iniciar(self):
        self.root.mainloop()

    def cerrar_limpio(self):
        # 1. Destruye la interfaz de Tkinter de forma segura
        self.root.destroy()
        # 2. Mata el proceso de Python de raíz, deteniendo cualquier hilo colgado
        sys.exit()
