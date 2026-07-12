from PyQt6.QtWidgets import QComboBox


class DropDownComponent(QComboBox):

    def __init__(self, options=None):
        super().__init__()
        if options:
            self.addItems(options)

        self.setEditable(False)  # Equivalente a state="readonly"
        self.setCurrentIndex(0)
