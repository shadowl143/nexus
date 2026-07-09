import ttkbootstrap as tb
import tkinter as tk
import locale
from nexus_desktop.tkinter.views.component.label.label_tittle_widget import (
    LabelTittleWidget,
)
from nexus_desktop.tkinter.services.multi_lenguage.multi_lenguage_service import (
    MultiLanguageService,
)


class InicioFrame:
    def __init__(self, contenedor_principal, language: str):
        self.contenedor_principal = contenedor_principal
        self.lenguage = MultiLanguageService(language=language).load_transaction()

    def crear_frame_inicio(self) -> tb.Frame:
        p_inicio = tb.Frame(self.contenedor_principal)
        LabelTittleWidget(tbframe=p_inicio, text=self.lenguage["welcome"]).pack()
        return p_inicio
