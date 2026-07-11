from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QPushButton, QWidget, QHBoxLayout
from nexus_desktop.PyQt.services.multi_lenguage_service import MultiLanguageService
import nexus_core.design_tokens as desing


class WindowsPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.lenguage = MultiLanguageService().load_transaction()
        print(self.lenguage)
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle(self.lenguage.get("welcome", "App"))
        self.setGeometry(200, 200, 1000, 900)
        self.setMinimumSize(1000, 900)

        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout principal horizontal
        main_layout = QHBoxLayout()
        central_widget.setLayout(main_layout)

        # Agregar sidebar
        main_layout.addWidget(self.side_lateral())

        # Agregar área central vacía (por ahora)
        contenido = QWidget()
        contenido.setStyleSheet(f"background-color: {desing.COLORS["bg.primary"]};")
        main_layout.addWidget(contenido)

    def side_lateral(self) -> QWidget:
        sidebar_layout = QVBoxLayout()
        btn_text: dict = self.lenguage.get("menu", "App")
        windows = {
            btn_text.get("home", "App"),
            btn_text.get("delivered", "App"),
            btn_text.get("rider", "App"),
        }
        for window in windows:
            btn = QPushButton(window)
            sidebar_layout.addWidget(btn)
        sidebar_layout.addStretch()

        sidebar_widget = QWidget()
        sidebar_widget.setLayout(sidebar_layout)
        sidebar_widget.setFixedWidth(200)
        sidebar_widget.setStyleSheet(f"""
            background-color: {desing.COLORS["bg.surface"]};
            color: white;
        """)

        return sidebar_widget
