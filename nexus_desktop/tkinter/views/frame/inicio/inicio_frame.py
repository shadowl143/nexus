import ttkbootstrap as tb
from nexus_desktop.tkinter.views.component.label.label_tittle_widget import LabelTittleWidget

class InicioFrame():
    def __init__(self, contenedor_principal):
        self.contenedor_principal = contenedor_principal

    def crear_frame_inicio(self) -> tb.Frame:
        p_inicio = tb.Frame(self.contenedor_principal)
        LabelTittleWidget(tbframe= p_inicio, text="Bienvenido a la Pantalla de Inicio").grid(row=0, column= 0)
        return p_inicio
    