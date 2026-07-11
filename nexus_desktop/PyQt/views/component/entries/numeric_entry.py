from PyQt6.QtWidgets import QLineEdit
from PyQt6.QtGui import QIntValidator


class NumericEntry(QLineEdit):

    DEFAULT_PADX = 15
    DEFAULT_PADY = 15

    def __init__(self, parent=None, min_value=0, max_value=999999):
        super().__init__(parent)

        # ✅ Validador entero
        validator = QIntValidator(min_value, max_value)
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
        """Devuelve el valor como int"""
        text = self.text()
        return int(text) if text else 0
