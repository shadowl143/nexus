from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QFont
import nexus_core.design_tokens as design


def apply_theme(app: QApplication, colors: dict, typography: dict):
    qss = f"""
    QWidget {{
        background-color: {colors["bg.primary"]};
        color: {colors["text.primary"]};
    }}

    QWidget#menu {{
        background-color: {colors["bg.menu"]};
        color: {colors["text.primary"]};
    }}

    QFrame {{
        background-color: {colors["bg.primary"]};
    }}
    QLabel {{
        background-color: transparent;
        color: {colors["text.primary"]};
    }}

    QComboBox {{
        background-color: {colors["bg.surface"]};
        color: {colors["text.primary"]};
        border: 1px solid {colors["accent.primary"]};
        padding: 4px;
    }}

    QCheckBox {{
        background-color: transparent;
        color: {colors["text.primary"]};
    }}

    QPushButton {{
        background-color: {colors["accent.primary"]};
        color: white;
        padding: 6px 12px;
        border-radius: 6px;
        font-weight: bold;
    }}

    QPushButton#btnCancel {{
        background-color: {colors["accent.danger"]};
    }}
    QPushButton:hover {{
        background-color: {colors["bg.surface"]};
        opacity: 0.85;
    }}

    QPushButton:pressed {{
        background-color: {colors["text.muted"]};
        opacity: 0.85;
    }}

    QLineEdit {{
        background-color: {colors["bg.surface"]};
        color: {colors["text.primary"]};
        border: 1px solid {colors["accent.primary"]};
        padding: 4px;
    }}
    """

    app.setStyleSheet(qss)

    # Fuente global
    font = QFont(typography["font.family.sans"], typography["font.size.body"])
    app.setFont(font)


def mode_dark(app, value: bool):
    if value:
        apply_theme(app, design.COLORS_DARK, design.TYPOGRAPHY_BLACK)
    else:
        apply_theme(app, design.COLORS, design.TYPOGRAPHY_BLACK)
