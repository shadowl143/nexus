from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QFormLayout
from nexus_desktop.PyQt.views.component.table.table_widget import TableFrame
from nexus_desktop.PyQt.views.component.entries.letter_entry import LettersEntry
from nexus_desktop.PyQt.views.component.button.button_component import WidgetButton
from nexus_desktop.PyQt.services.multi_lenguage_service import MultiLanguageService
from nexus_desktop.PyQt.controllers.rider.rider_controller import RiderController


class RiderWidget(QWidget):
    def __init__(self, controller: RiderController, language="es_MX"):
        super().__init__()
        language = MultiLanguageService(language).load_transaction()
        layout = QHBoxLayout(self)
        left_layout = QVBoxLayout()
        right_layout = QFormLayout()

        # left
        table = TableFrame(
            columns=[
                language.get("Id", "Id"),
                language.get("name", "Nombre"),
                language.get("rider_type", "Tipo rider"),
            ],
            data=controller.rider_list(),
        )
        left_layout.addWidget(table)

        # rigth
        right_layout.addRow("Nombre", LettersEntry())
        right_layout.addRow("tipo de rider", LettersEntry())
        layout_btns = QHBoxLayout()
        layout_btns.addStretch()
        btnSuccess = WidgetButton()
        btnCancel = WidgetButton(button_text="Cancelar")
        layout_btns.addWidget(btnCancel)
        layout_btns.addWidget(btnSuccess)
        right_layout.addRow(layout_btns)

        layout.addLayout(left_layout)
        layout.addLayout(right_layout)
