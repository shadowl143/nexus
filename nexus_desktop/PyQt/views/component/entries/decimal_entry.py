from PyQt6.QtWidgets import QLineEdit
from PyQt6.QtGui import QDoubleValidator
from PyQt6.QtCore import QLocale


class DecimalEntry(QLineEdit):

    DEFAULT_PADX = 15
    DEFAULT_PADY = 15

    def __init__(self, parent=None, decimals=2):
        super().__init__(parent)

        # ✅ Crear validador decimal
        validator = QDoubleValidator()
        validator.setDecimals(decimals)
        validator.setNotation(QDoubleValidator.Notation.StandardNotation)

        # Opcional: Forzar punto como separador decimal
        validator.setLocale(QLocale(QLocale.Language.English))

        self.setValidator(validator)

        self.setStyleSheet("""
            QLineEdit {
                padding: 6px;
                border: 1px solid #ccc;
                border-radius: 6px;
                font-size: 12px;
            }
        """)

    def value(self):
        """Devuelve el valor como float"""
        text = self.text()
        return float(text) if text else 0.0
