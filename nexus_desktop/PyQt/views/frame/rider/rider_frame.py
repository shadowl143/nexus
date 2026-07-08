import ttkbootstrap as tb
from nexus_desktop.tkinter.views.component.label.label_tittle_widget import LabelTittleWidget
from nexus_desktop.tkinter.views.component.label.label_text_widget import LabelTextWidget
from nexus_desktop.tkinter.views.component.table.table_widget import TableFrame
from nexus_desktop.tkinter.views.component.button.button_component import WidgetButtons
from nexus_desktop.tkinter.services.multi_lenguage.multi_lenguage_service import MultiLanguageService

class RidesFrame():
    def __init__(self, contenedor_principal, language:str):
        self.contenedor_principal = contenedor_principal
        self.lenguage = MultiLanguageService(language= language).load_transaction()
        self.name = self.lenguage["name"]
        self.bike_type = self.lenguage["bike_type"]
        self.rider_id = self.lenguage["co2_saved"]

    def crear_frame_inicio(self) -> tb.Frame:
        # Pantalla de Ajustes
        p_rider = tb.Frame(self.contenedor_principal)
        LabelTittleWidget(tbframe= p_rider, text=self.lenguage["tittles"]["rider"]).pack(pady=20)
    
        p_rider.pack(fill="both", expand=True, padx=30)
        
        
        # Contenedor
        content_rider = tb.Frame(p_rider)
        content_rider.pack(fill="both", expand=True)
        # configurar contenedores para que sea en 2 columnas
        content_rider.columnconfigure(0, weight=2)
        content_rider.columnconfigure(1, weight=1)

        # se configura la tabla
        columns = (self.name, self.bike_type, self.rider_id)
        data = [
            ("Alice", 30, "USA"),
            ("Bob", 25, "UK"),
            ("Charlie", 35, "Canada"),
            ("Bob", 25, "UK"),
            ("Charlie", 35, "Canada"),
            ("Bob", 25, "UK"),
            ("Charlie", 35, "Canada")
        ]
        table1 = TableFrame(content_rider, columns, data)
        table1.grid(row=0, column=0, padx=20, sticky="NSEW")
        
        # se configura el formulario
        form_raider = tb.Frame(content_rider)
        campos = [self.name, self.bike_type, self.rider_id]
        form_raider.grid(row=0, column=1, padx=40, sticky="NSEW")
        
        for i, campo in enumerate(campos):

            LabelTextWidget(tbframe= form_raider, text=campo).grid(
                row=i,
                column=0,
                padx=15
            )

            tb.Entry(
                form_raider,
                width=25
            ).grid(
                row=i,
                column=1,
                padx=15
            )
        
        button = WidgetButtons(form_raider, self.hola_mundo)
        button.grid(row= 3, column= 0)
        return p_rider
    
    def hola_mundo(self):
        print("hola mundo")