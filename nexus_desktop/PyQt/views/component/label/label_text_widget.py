
from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
import nexus_core.design_tokens as design

class LabelTextWidget:
    def __init__(self, parent, text: str,
        pady: int = 20,
        padx: int = 0):

        self.label = QLabel(text, parent)

        font = QFont(
            design.TYPOGRAPHY["font.family.sans"],
            design.TYPOGRAPHY["font.size.body"]
        )

        self.label.setFont(font)

        self.label.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.label.setStyleSheet(f"""
            padding:{pady}px {padx}px;
        """)
    
    # 2. Creamos nuestro propio método pack
    def pack(self, **kwargs):
        # Configuramos valores por defecto si el usuario no los envía
        if "anchor" not in kwargs:
            kwargs["anchor"] = "w"
        if "pady" not in kwargs:
            kwargs["pady"] = 20
            
        self.label.pack(**kwargs)
        return self # Permite encadenar código si se desea

    # 3. Creamos nuestro propio método grid
    def grid(self, **kwargs):
        # Configuramos valores por defecto para grid si no los envían
        if "sticky" not in kwargs:
            kwargs["sticky"] = "w"
        if "pady" not in kwargs:
            kwargs["pady"] = 20
            
        self.label.grid(**kwargs)
        return self