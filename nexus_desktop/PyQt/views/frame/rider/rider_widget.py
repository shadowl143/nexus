from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QFormLayout
from nexus_desktop.PyQt.views.component.table.table_widget import TableFrame
from nexus_desktop.PyQt.views.component.entries.letter_entry import LettersEntry
from nexus_desktop.PyQt.views.component.button.button_component import WidgetButton
from nexus_desktop.PyQt.services.multi_lenguage_service import MultiLanguageService
from nexus_desktop.PyQt.controllers.rider.rider_controller import RiderController
from nexus_desktop.PyQt.views.component.label.label_tittle_widget import (
    LabelTitleWidget,
)


class RiderWidget(QWidget):
    def __init__(self, controller: RiderController, language: MultiLanguageService):
        super().__init__()
        self.multi = language
        self.language = self.multi.load_transaction()
        self.layout_principal = QVBoxLayout(self)
        self.layout_horizontal = QHBoxLayout()
        layout_btns = QHBoxLayout()
        self.left_layout = QVBoxLayout()
        self.right_layout = QFormLayout()

        self.title = LabelTitleWidget(text=self.language["tittles"]["rider"])
        self.name = self.language["name"]
        # left
        table = TableFrame(
            columns=[
                self.language.get("Id", "Id"),
                self.language.get("name", "Nombre"),
                self.language.get("rider_type", "Tipo rider"),
            ],
            data=controller.rider_list(),
        )
        self.left_layout.addWidget(table)

        # rigth
        self.right_layout.addRow(self.name, LettersEntry())
        self.right_layout.addRow("tipo de rider", LettersEntry())
        layout_btns.addStretch()
        btnSuccess = WidgetButton()
        btnCancel = WidgetButton(button_text="Cancelar")
        btnCancel.setObjectName("btnCancel")
        layout_btns.addWidget(btnCancel)
        layout_btns.addWidget(btnSuccess)
        self.right_layout.addRow(layout_btns)

        self.layout_horizontal.addLayout(self.left_layout)
        self.layout_horizontal.addLayout(self.right_layout)

        self.layout_principal.addWidget(self.title)
        self.layout_principal.addLayout(self.layout_horizontal)
