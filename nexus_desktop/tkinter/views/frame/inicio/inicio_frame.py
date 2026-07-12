import ttkbootstrap as tb
import tkinter as tk
from nexus_desktop.tkinter.views.component.label.label_tittle_widget import (
    LabelTittleWidget,
)
from nexus_desktop.tkinter.services.multi_lenguage.multi_lenguage_service import (
    MultiLanguageService,
)
from nexus_desktop.tkinter.views.component.drop_down.drop_down_component import (
    DropDownComponent,
)


class InicioFrame:
    def __init__(
        self,
        contenedor_principal,
        language: tk.StringVar,
        mode: tk.BooleanVar,
        toggle_callback,
        multilanguage_class: MultiLanguageService,
    ):
        self.contenedor_principal = contenedor_principal
        self.multilanguage_class = multilanguage_class
        self.language = language
        self.dark_var = mode
        self.toggle_callback = toggle_callback
        self.combo = DropDownComponent

        # cargar idioma inicial
        self.lenguage_value = self.multilanguage_class.load_transaction()

    def crear_frame_inicio(self) -> tb.Frame:
        p_inicio = tb.Frame(self.contenedor_principal)
        LabelTittleWidget(tbframe=p_inicio, text=self.lenguage_value["welcome"]).pack()
        self.mode_dark = tb.Checkbutton(
            p_inicio,
            text="modo oscuro",
            variable=self.dark_var,
            command=self.toggle_callback,
        )

        self.mode_dark.pack(padx=15, pady=15)
        self.combo = DropDownComponent(p_inicio, options=["es_Mx", "en_US"]).select()
        self.combo.bind(
            "<<ComboboxSelected>>", lambda e: self.change_language(self.combo.get())
        )
        self.combo.pack()
        return p_inicio

    def change_language(self, value: str):
        self.language.set(value)
        self.lenguage_value = self.multilanguage_class.load_transaction()
