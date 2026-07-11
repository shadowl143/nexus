from PyQt6.QtWidgets import QComboBox


class DropDownComponent(QComboBox):

    DEFAULT_PADX = 15
    DEFAULT_PADY = 15

    def __init__(self, parent=None, options=None):
        super().__init__(parent)

        if options:
            self.addItems(options)

        self.setEditable(False)  # Equivalente a state="readonly"
        self.setCurrentIndex(0)

        self.apply_style()

    def apply_style(self):
        self.setStyleSheet("""
            QComboBox {
                padding: 5px 10px;
                border: 1px solid #ccc;
                border-radius: 6px;
                background-color: white;
            }

            QComboBox::drop-down {
                border: none;
            }
        """)
