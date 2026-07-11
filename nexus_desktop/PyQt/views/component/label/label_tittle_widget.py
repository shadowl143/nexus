from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
import nexus_core.design_tokens as design


class LabelTitleWidget(QLabel):

    DEFAULT_PADX = 15
    DEFAULT_PADY = 15

    def __init__(self, text: str, parent=None, pady: int = 20, padx: int = 0):
        super().__init__(text, parent)

        # ✅ Fuente
        font = QFont(
            design.TYPOGRAPHY["font.family.sans"], design.TYPOGRAPHY["font.size.h1"]
        )
        font.setBold(True)
        self.setFont(font)

        # ✅ Centrar texto
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # ✅ Padding interno
        self.setStyleSheet(f"""
            QLabel {{
                padding: {pady}px {padx}px;
            }}
        """)
