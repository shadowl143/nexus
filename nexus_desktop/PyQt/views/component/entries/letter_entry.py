from PyQt6.QtWidgets import QLineEdit
from PyQt6.QtGui import QRegularExpressionValidator
from PyQt6.QtCore import QRegularExpression


class LettersEntry(QLineEdit):

    def __init__(self, parent=None):
        super().__init__(parent)

        # ✅ Expresión regular: solo letras (incluye acentos) y espacios
        regex = QRegularExpression("^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]*$")
        validator = QRegularExpressionValidator(regex)

        self.setValidator(validator)
