import ttkbootstrap as tb
import nexus_desktop.tkinter.views.component.label.label_tittle_widget as title
import nexus_desktop.tkinter.views.component.label.label_text_widget as text

class EntregasFrame():
    def __init__(self, contenedor_principal):
        self.contenedor_principal = contenedor_principal

    def crear_frame_inicio(self) -> tb.Frame:
        # Pantalla de Perfil
        p_perfil = tb.Frame(self.contenedor_principal)
        title.LabelTittleWidget(p_perfil, "Entregas")
        text.LabelTextWidget(p_perfil, "Gestion de datos para obtener entregas")
        tb.Entry(p_perfil).pack(pady=5)  # Campo de ejemplo
        return p_perfil
    
    def crear_tabla(self):
        pass