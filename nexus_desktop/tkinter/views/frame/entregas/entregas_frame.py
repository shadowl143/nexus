import ttkbootstrap as tb
from nexus_desktop.tkinter.views.component.label.label_tittle_widget import (
    LabelTittleWidget,
)
from nexus_desktop.tkinter.views.component.label.label_text_widget import (
    LabelTextWidget,
)
from nexus_desktop.tkinter.views.component.table.table_widget import TableFrame
from nexus_desktop.tkinter.views.component.button.button_component import WidgetButtons
from nexus_desktop.tkinter.views.component.messge_box.message_box import MessageBox
from nexus_desktop.tkinter.services.multi_lenguage.multi_lenguage_service import (
    MultiLanguageService,
)
from nexus_desktop.tkinter.controllers.entregas.entrega_controller import (
    EntregaController,
)
from nexus_desktop.tkinter.controllers.rider.rider_controller import (
    RiderController,
)
from nexus_desktop.tkinter.views.component.drop_down.drop_down_component import (
    DropDownComponent,
)
from nexus_desktop.tkinter.views.component.entries.numeric_entry import NumericEntry
from nexus_desktop.tkinter.views.component.entries.decimal_entry import DecimalEntry
from nexus_desktop.tkinter.view_model.entregas_vm import EntregaVm


class EntregasFrame:
    def __init__(
        self,
        contenedor_principal,
        entrega_controller: EntregaController,
        rider_controller: RiderController,
        multilanguage: MultiLanguageService,
    ):
        self.contenedor_principal = contenedor_principal
        self.rider_controller = rider_controller
        self.entrega_controller = entrega_controller
        self.data = entrega_controller.rider_list()
        self.info: list[EntregaVm] = self.rider_controller.rider_select()

        # texto
        self.lenguage = multilanguage.load_transaction()
        self.id = self.lenguage["id"]
        self.name = self.lenguage["name"]
        self.distance = self.lenguage["distance"]
        self.co2 = self.lenguage["co2_saved"]

        # controles
        self.txt_id: NumericEntry
        self.ddn_rider_id: DropDownComponent
        self.txt_distance: DecimalEntry
        self.txt_co2 = DecimalEntry

    def crear_frame_inicio(self) -> tb.Frame:
        # Pantalla de Ajustes
        p_entregas = tb.Frame(self.contenedor_principal)
        LabelTittleWidget(
            tbframe=p_entregas, text=self.lenguage["tittles"]["rider"]
        ).pack(pady=20)
        p_entregas.pack(fill="both", expand=True, padx=30)

        # Contenedor
        content_rider = tb.Frame(p_entregas)
        content_rider.pack(fill="both", expand=True)

        # configurar contenedores para que sea en 2 columnas
        content_rider.columnconfigure(0, weight=2)
        content_rider.columnconfigure(1, weight=1)

        # se configura la tabla
        columns = (self.id, self.name, self.distance, self.co2)

        self.table = TableFrame(content_rider, columns, self.data)
        self.table.grid(row=0, column=0, padx=20, sticky="NSEW")

        self.contend_form(content_rider)

        return p_entregas

    def contend_form(self, frame: tb.Frame):
        # se configura el formulario
        form_entregas = tb.Frame(frame)
        form_entregas.grid(row=0, column=1, padx=40, sticky="NSEW")

        LabelTextWidget(tbframe=form_entregas, text=self.name).grid(row=0, column=0)
        self.ddn_rider_id = DropDownComponent(
            form_entregas, options=[f"{info.name}" for info in self.info]
        ).select()
        self.ddn_rider_id.grid(row=0, column=1)

        LabelTextWidget(tbframe=form_entregas, text=self.distance).grid(row=1, column=0)
        self.txt_distance = DecimalEntry(parent=form_entregas)
        self.txt_distance.grid(row=1, column=1)

        LabelTextWidget(tbframe=form_entregas, text=self.co2).grid(row=2, column=0)
        self.txt_co2 = DecimalEntry(parent=form_entregas)
        self.txt_co2.grid(row=2, column=1)

        button = WidgetButtons(parent=form_entregas, command=self.crear_nuevo)
        button.grid(row=3, column=1, sticky="SE")

    def crear_nuevo(self):

        respuesta = MessageBox(
            self.contenedor_principal,
            message=self.lenguage["modal"]["save"],
            title=self.lenguage["modal"]["message"],
        ).msg_save()
        if respuesta == "Si":
            selected = self.ddn_rider_id.get()
            rider_id = next((e.id for e in self.info if e.name == selected))
            self.ddn_rider_id.get()
            modelo = EntregaVm(
                _id=len(self.data) + 1,
                _name=selected,
                _rider_id=rider_id,
                _distance=self.txt_distance.get(),
                _co2=self.txt_co2.get(),
            )
            self.entrega_controller.save_rider(modelo)
            self.data = self.entrega_controller.rider_list()
            self.table.reload_table(self.data)
        else:
            MessageBox(
                parent=self.contenedor_principal,
                title=self.lenguage["modal"]["cancel"],
                message=self.lenguage["modal"]["message_cancel"],
            ).msg_information()
