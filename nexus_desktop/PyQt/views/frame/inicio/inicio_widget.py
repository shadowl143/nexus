from PyQt6.QtWidgets import QWidget, QVBoxLayout, QFormLayout
from nexus_desktop.PyQt.views.component.label.label_tittle_widget import (
    LabelTitleWidget,
)
from nexus_desktop.PyQt.views.component.label.label_text_widget import (
    LabelTextWidget,
)
from nexus_desktop.PyQt.views.component.drop_down.drop_down_component import (
    DropDownComponent,
)
from nexus_desktop.PyQt.services.multi_lenguage_service import MultiLanguageService


class InicioWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.language = MultiLanguageService().load_transaction()
        layout = QVBoxLayout(self)
        optionsddr = QFormLayout()

        title = LabelTitleWidget(text=self.language.get("welcome", "app"))

        text = LabelTextWidget(text="lenguaje")
        ddr = DropDownComponent(options=["es_MX", "en_US"])

        layout.addWidget(title)
        optionsddr.addWidget(text)
        optionsddr.addWidget(ddr)
        layout.addLayout(optionsddr)
