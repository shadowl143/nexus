from nexus_desktop.tkinter.views.layout.principal_layout import WindowsPrincipal
import tkinter as tk
from nexus_desktop.tkinter.views.frame.entregas import entregas_frame as entregas
from nexus_desktop.tkinter.views.frame.inicio import inicio_frame as inicio
from nexus_desktop.tkinter.views.frame.rider import rider_frame as frame
import locale


@staticmethod
def get_system_language():
    # Obtiene el lenguaje del sistema
    lang, _ = locale.getdefaultlocale()
    return lang
shared = get_system_language()
dependencias_pantallas = {
    "Inicio": lambda contenedor: inicio.InicioFrame(contenedor, shared).crear_frame_inicio(),
    "Entregas": lambda contenedor: entregas.EntregasFrame(contenedor, shared).crear_frame_inicio(),
    "Riders": lambda contenedor: frame.RidesFrame(contenedor, shared).crear_frame_inicio()
}

app = WindowsPrincipal(pantallas= dependencias_pantallas)


app.iniciar()


