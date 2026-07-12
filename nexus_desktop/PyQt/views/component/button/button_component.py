from PyQt6.QtWidgets import QPushButton


class WidgetButton(QPushButton):

    def __init__(self, button_text: str = "Guardar", command=None):
        super().__init__(button_text)

        if command:
            self.clicked.connect(command)
