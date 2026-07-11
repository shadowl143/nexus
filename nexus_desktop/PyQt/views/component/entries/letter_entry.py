from PyQt6.QtWidgets import QLineEdit
from PyQt6.QtGui import QRegularExpressionValidator
from PyQt6.QtCore import QRegularExpression
import nexus_core.design_tokens as design


class LettersEntry(QLineEdit):

    DEFAULT_PADX = 15
    DEFAULT_PADY = 15

    def __init__(self, parent=None):
        super().__init__(parent)

        # ✅ Expresión regular: solo letras (incluye acentos) y espacios
        regex = QRegularExpression("^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]*$")
        validator = QRegularExpressionValidator(regex)

        self.setValidator(validator)

        self.setStyleSheet(f"""
            QLineEdit {{
                padding: 6px;
                border: 1px solid #ccc;
                border-radius: 6px;
                font-family: {design.TYPOGRAPHY["font.family.sans"]};
                font-size: {design.TYPOGRAPHY["font.size.body"]}px;
            }}
        """)
