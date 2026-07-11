from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
import nexus_core.design_tokens as design


class LabelTextWidget(QLabel):

    def __init__(self, text: str, parent=None, pady: int = 20, padx: int = 0):
        super().__init__(text, parent)

        font = QFont(
            design.TYPOGRAPHY["font.family.sans"], design.TYPOGRAPHY["font.size.body"]
        )
        self.setFont(font)

        self.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setStyleSheet(f"""
            QLabel {{
                padding: {pady}px {padx}px;
            }}
        """)
