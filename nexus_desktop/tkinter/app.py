from nexus_desktop.tkinter.views.layout.principal_layout import WindowsPrincipal
from nexus_desktop.tkinter.views.frame.entregas import entregas_frame as entregas
from nexus_desktop.tkinter.views.frame.inicio import inicio_frame as inicio
from nexus_desktop.tkinter.views.frame.rider import rider_frame as frame
from nexus_desktop.tkinter.controllers.rider.rider_controller import RiderController
from nexus_desktop.tkinter.services.rider.rider_service import RiderService
from nexus_desktop.tkinter.services.entregas.entregas_service import EntregaService
from nexus_desktop.tkinter.controllers.entregas.entrega_controller import (
    EntregaController,
)
import os

rider_service = RiderService()
ridercontroller = RiderController(rider_service)

entregas_service = EntregaService()
entrega_controller = EntregaController(entregas_service)
import locale

if __name__ == "__main__":

    @staticmethod
    def get_system_language():
        # Obtiene el lenguaje del sistema
        lang, _ = locale.getdefaultlocale()
        return lang

    shared = get_system_language()
    dependencias_pantallas = {
        "Inicio": lambda contenedor: inicio.InicioFrame(
            contenedor, shared
        ).crear_frame_inicio(),
        "Entregas": lambda contenedor: entregas.EntregasFrame(
            contenedor, shared, entrega_controller
        ).crear_frame_inicio(),
        "Riders": lambda contenedor: frame.RidesFrame(
            contenedor, shared, ridercontroller
        ).crear_frame_inicio(),
    }

    app = WindowsPrincipal(pantallas=dependencias_pantallas)

    os.execl(app.iniciar())
