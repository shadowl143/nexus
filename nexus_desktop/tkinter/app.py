from nexus_desktop.tkinter.views.layout.principal_layout import WindowsPrincipal

from nexus_desktop.tkinter.views.frame.entregas import entregas_frame as entregas
from nexus_desktop.tkinter.views.frame.inicio import inicio_frame as inicio
from nexus_desktop.tkinter.views.frame.rider import rider_frame as frame

# Creamos funciones "fábrica" que WindowsPrincipal ejecutará pasándole el contenedor padre
dependencias_pantallas = {
    # 1. Instanciamos la clase pasando el contenedor y luego llamamos al método sin ejecutarlo en el main
    "Inicio": lambda contenedor: inicio.InicioFrame(contenedor).crear_frame_inicio(),
    
    # 2. Corregido para que apunte a sus módulos y clases correspondientes (asumiendo nombres estándar)
    "Entregas": lambda contenedor: entregas.EntregasFrame(contenedor).crear_frame_inicio(),
    
    "Riders": lambda contenedor: frame.RidesFrame(contenedor).crear_frame_inicio()
}
app = WindowsPrincipal(pantallas= dependencias_pantallas)
app.iniciar()