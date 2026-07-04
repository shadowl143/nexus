import ttkbootstrap as tb

class RidesFrame():
    def __init__(self, contenedor_principal):
        self.contenedor_principal = contenedor_principal

    def crear_frame_inicio(self) -> tb.Frame:
        # Pantalla de Ajustes
        p_ajustes = tb.Frame(self.contenedor_principal)
        tb.Label(p_ajustes, text="Configuración del Sistema", font=("Arial", 16)).pack(pady=20)
        return p_ajustes