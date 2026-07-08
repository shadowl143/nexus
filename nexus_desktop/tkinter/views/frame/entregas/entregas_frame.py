import ttkbootstrap as tb
from nexus_desktop.tkinter.views.component.label.label_tittle_widget import LabelTittleWidget
from nexus_desktop.tkinter.views.component.label.label_text_widget import LabelTextWidget
from nexus_desktop.tkinter.views.component.table.table_widget import TableFrame
from nexus_desktop.tkinter.views.component.button.button_component import WidgetButtons
from nexus_desktop.tkinter.services.multi_lenguage.multi_lenguage_service import MultiLanguageService

class EntregasFrame():
    def __init__(self, contenedor_principal, language: str):
        self.contenedor_principal = contenedor_principal
        self.lenguage = MultiLanguageService(language= language).load_transaction()

    def crear_frame_inicio(self) -> tb.Frame:
       # Pantalla de Ajustes
        p_entregas = tb.Frame(self.contenedor_principal)
        LabelTittleWidget(tbframe= p_entregas, text=self.lenguage["tittles"]["delivered"]).pack(pady=20)
        self.distance = self.lenguage["distance"]
        self.bike_type = self.lenguage["bike_type"]
        self.id = self.lenguage["id"]

        p_entregas.pack(fill="both", expand=True, padx=30)
        
        
        # Contenedor
        contenido_entregas = tb.Frame(p_entregas)
        contenido_entregas.pack(fill="both", expand=True)
        # configurar contenedores para que sea en 2 columnas
        contenido_entregas.columnconfigure(0, weight=2)
        contenido_entregas.columnconfigure(1, weight=1)

        # se configura la tabla
        columns = (self.distance, self.bike_type, self.id)
        data = [
            ("Alice", 30, "USA"),
            ("Bob", 25, "UK"),
            ("Charlie", 35, "Canada"),
            ("Bob", 25, "UK"),
            ("Charlie", 35, "Canada"),
            ("Bob", 25, "UK"),
            ("Charlie", 35, "Canada")
        ]
        table1 = TableFrame(contenido_entregas, columns, data)
        table1.grid(row=0, column=0, padx=20, sticky="NSEW")
        
        # se configura el formulario
        frame_formulario_entregas = tb.Frame(contenido_entregas)
        campos = [self.distance, self.bike_type, self.id]
        frame_formulario_entregas.grid(row=0, column=1, padx=40, sticky="NSEW")
        
        for i, campo in enumerate(campos):

            LabelTextWidget(tbframe= frame_formulario_entregas, text=campo).grid(
                row=i,
                column=0,
                padx=15
            )

            tb.Entry(
                frame_formulario_entregas,
                width=25
            ).grid(
                row=i,
                column=1,
                padx=15
            )
        
        button = WidgetButtons(frame_formulario_entregas, self.hola_mundo)
        button.grid(row= 3, column= 0)
        return p_entregas
    
    def hola_mundo(self):
        print("hola mundo")