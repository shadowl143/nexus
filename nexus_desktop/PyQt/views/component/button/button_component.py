from PyQt6.QtWidgets import QPushButton
from PyQt6.QtCore import Qt
import nexus_core.design_tokens as design


class WidgetButton(QPushButton):

    DEFAULT_PADX = 15
    DEFAULT_PADY = 15

    def __init__(self, parent=None, button_text: str = "Guardar", command=None):
        super().__init__(button_text, parent)

        if command:
            self.clicked.connect(command)

        self.apply_style()

        # Padding interno del botón
        self.setContentsMargins(
            self.DEFAULT_PADX, self.DEFAULT_PADY, self.DEFAULT_PADX, self.DEFAULT_PADY
        )

    def apply_style(self):
        self.setStyleSheet(f"""
            QPushButton {{
                background-color: {design.COLORS["bg.primary"]};
                color: {design.COLORS["text.primary"]};
                font-family: {design.TYPOGRAPHY["font.family.sans"]};
                font-size: {design.TYPOGRAPHY["font.size.body"]}px;
                font-weight: bold;
                border-radius: 6px;
                padding: 10px 20px;
            }}

            QPushButton:hover {{
                opacity: 0.85;
            }}

            QPushButton:pressed {{
                background-color: {design.COLORS["text.muted"]};
            }}
        """)
