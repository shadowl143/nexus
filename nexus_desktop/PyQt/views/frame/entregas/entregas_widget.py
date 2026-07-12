from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QFormLayout
from nexus_desktop.PyQt.views.component.table.table_widget import TableFrame
from nexus_desktop.PyQt.views.component.entries.letter_entry import LettersEntry
from nexus_desktop.PyQt.views.component.entries.decimal_entry import DecimalEntry
from nexus_desktop.PyQt.views.component.button.button_component import WidgetButton
from nexus_desktop.PyQt.services.multi_lenguage_service import MultiLanguageService
from nexus_desktop.PyQt.controllers.entregas.entregas_controller import (
    EntregaController,
)
from nexus_desktop.PyQt.views.component.label.label_tittle_widget import (
    LabelTitleWidget,
)
from nexus_desktop.PyQt.views.component.messge_box.message_box import MessageBoxWidget
from nexus_desktop.PyQt.view_model.entregas_vm import EntregaVm


class EntregasWidget(QWidget):
    def __init__(self, controller: EntregaController, language="es_MX"):
        super().__init__()
        language = MultiLanguageService(language).load_transaction()
        self.title = language.get("tittles", "titulo")
        layout_principal = QVBoxLayout(self)
        title_label = LabelTitleWidget(text=self.title["delivered"])
        layout_principal.addWidget(title_label)

        layout_horizontal = QHBoxLayout()
        left_layout = QVBoxLayout()
        right_layout = QFormLayout()
        self.id = language.get("id", "Id")
        self.name = language.get("name", "Nombre")
        self.rider_type = language.get("bike_type", "bike_type")
        self.distance = language.get("distance", "distance")
        self.co2_saved = language.get("co2_saved", "co2_saved")
        self.entregas_controller = controller
        # left
        self.table = TableFrame(
            columns=[
                self.id,
                self.name,
                self.distance,
                self.co2_saved,
            ],
            data=self.entregas_controller.entregas_list(),
        )
        left_layout.addWidget(self.table)
        self.txt_name = LettersEntry()
        self.txt_rider_type = LettersEntry()
        self.txt_distance = DecimalEntry()
        self.txt_co2_saved = DecimalEntry()
        # rigth
        right_layout.addRow(self.name, self.txt_name)
        right_layout.addRow(self.rider_type, self.txt_rider_type)
        right_layout.addRow(self.distance, self.txt_distance)
        right_layout.addRow(self.co2_saved, self.txt_co2_saved)
        layout_btns = QHBoxLayout()
        layout_btns.addStretch()
        btnSuccess = WidgetButton(command=self.save)
        btnCancel = WidgetButton(button_text="Cancelar", command=self.cancel)
        btnCancel.setObjectName("btnCancel")
        layout_btns.addWidget(btnCancel)
        layout_btns.addWidget(btnSuccess)
        right_layout.addRow(layout_btns)

        layout_horizontal.addLayout(left_layout)
        layout_horizontal.addLayout(right_layout)
        layout_principal.addLayout(layout_horizontal)

    def save(self):
        try:
            respuesta = MessageBoxWidget.confirm(
                self, title="Seguro?", message="Guardar nuevos datos"
            )

            if respuesta:
                entregavm = EntregaVm(
                    _id=1,
                    _rider_id=1,
                    _name=self.txt_name.text(),
                    _distance=float(self.txt_distance.text()),
                    _co2=float(self.txt_co2_saved.text()),
                )
                self.entregas_controller.save_entrega(entregavm)
                self.table.load_data(self.entregas_controller.entregas_list())
            else:
                self.cancel()
        except Exception as e:
            MessageBoxWidget.error_critical(self, "Error", str(e))

    def cancel(self):
        MessageBoxWidget.information(self, "Cancelado", "Cancelado por el usuario")
