import ttkbootstrap as tb
from nexus_desktop.tkinter.views.component.label.label_tittle_widget import LabelTittleWidget
from nexus_desktop.tkinter.views.component.label.label_text_widget import LabelTextWidget
from nexus_desktop.tkinter.views.component.table.table_widget import TableFrame
from nexus_desktop.tkinter.views.component.button.button_component import WidgetButtons
from nexus_desktop.tkinter.services.multi_lenguage.multi_lenguage_service import MultiLanguageService
from nexus_desktop.tkinter.controllers.rider.rider_controller import RiderController
from nexus_desktop.tkinter.views.component.entries.letter_entry import LettersEntry
class RidesFrame():
    def __init__(self, contenedor_principal, language:str, rider_controller: RiderController):
        self.contenedor_principal = contenedor_principal
        self.rider_controller = rider_controller
        self.data = rider_controller.rider_list()
        self.lenguage = MultiLanguageService(language= language).load_transaction()
        self.name = self.lenguage["name"]
        self.bike_type = self.lenguage["bike_type"]
        self.rider_id = self.lenguage["co2_saved"]
        self.txt_name = tb.Entry
        self.txt_bike_type = ""
        self.txt_rider_id= ""

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
       
        table1 = TableFrame(content_rider, columns, self.data)
        table1.grid(row=0, column=0, padx=20, sticky="NSEW")
        
        self.contend_form(content_rider)
        
        return p_rider
    
    def contend_form(self, frame:tb.Frame):
        # se configura el formulario
        form_raider = tb.Frame(frame)
        form_raider.grid(row=0, column=1, padx=40, sticky="NSEW")
        
        LabelTextWidget(tbframe= form_raider, text=self.name).grid(
                row=0,
                column=0,
                padx=15
            )
        self.txt_name = LettersEntry(parent= form_raider).grid(
                row=0,
                column=1,
                padx=15
            )
        LabelTextWidget(tbframe= form_raider, text=self.bike_type).grid(
                row=1,
                column=0,
                padx=15
            )
        self.txt_rider_id = LettersEntry(parent= form_raider).grid(
                row=1,
                column=1,
                padx=15
            )
        
        LabelTextWidget(tbframe= form_raider, text=self.rider_id).grid(
                row=2,
                column=0,
                padx=15
            )
        self.txt_rider_id = LettersEntry(parent= form_raider).grid(
                row=2,
                column=1,
                padx=15
            )
        button = WidgetButtons(form_raider, self.hola_mundo)
        button.grid(row= 3, column= 0)
    
    def hola_mundo(self):
        print(self.txt_name.get())