from PyQt6.QtWidgets import (
    QMainWindow,
    QVBoxLayout,
    QPushButton,
    QWidget,
    QHBoxLayout,
    QStackedWidget,
)
from nexus_desktop.PyQt.services.multi_lenguage_service import MultiLanguageService
from nexus_core.themepyqt import mode_dark
from nexus_desktop.PyQt.services.entregas.entrega_service import EntregaService
from nexus_desktop.PyQt.services.rider.rider_service import RiderService
from nexus_desktop.PyQt.controllers.entregas.entregas_controller import (
    EntregaController,
)
from nexus_desktop.PyQt.controllers.rider.rider_controller import RiderController
from nexus_desktop.PyQt.views.frame.entregas.entregas_widget import EntregasWidget
from nexus_desktop.PyQt.views.frame.rider.rider_widget import RiderWidget
from nexus_desktop.PyQt.views.frame.inicio.inicio_widget import InicioWidget
from nexus_desktop.PyQt.services.multi_lenguage_service import MultiLanguageService

rider_service = RiderService()
ridercontroller = RiderController(rider_service)

entregas_service = EntregaService()
entrega_controller = EntregaController(entregas_service)


class WindowsPrincipal(QMainWindow):
    def __init__(self, language: MultiLanguageService):
        super().__init__()
        self.multilan = language
        self.language = self.multilan.load_transaction()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle(self.language.get("welcome", "App"))
        self.setGeometry(200, 200, 1080, 900)
        self.setMinimumSize(1000, 900)
        mode_dark(self, False)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QHBoxLayout(central_widget)

        # Stack principal
        self.stack = QStackedWidget()

        # Crear pantallas reales
        self.frames = {
            "home": InicioWidget(),
            "delivered": EntregasWidget(controller=entrega_controller),
            "rider": RiderWidget(controller=ridercontroller, language=self.multilan),
        }

        # Agregarlas al stack
        for frame in self.frames.values():
            self.stack.addWidget(frame)

        # Sidebar
        sidebar = self.side_lateral()

        main_layout.addWidget(sidebar)
        main_layout.addWidget(self.stack)

        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        # Mostrar home por defecto
        self.stack.setCurrentWidget(self.frames["home"])

    def side_lateral(self) -> QWidget:
        sidebar_layout = QVBoxLayout()

        btn_text: dict = self.language.get("menu", {})

        botones = {
            "home": btn_text.get("home", "Home"),
            "delivered": btn_text.get("delivered", "Delivered"),
            "rider": btn_text.get("rider", "Rider"),
        }

        for key, text in botones.items():
            btn = QPushButton(text)

            # Conectar botón al frame correcto
            btn.clicked.connect(
                lambda _, k=key: self.stack.setCurrentWidget(self.frames[k])
            )

            sidebar_layout.addWidget(btn)

        sidebar_layout.addStretch()

        sidebar_widget = QWidget()
        sidebar_widget.setLayout(sidebar_layout)
        sidebar_widget.setFixedWidth(200)
        sidebar_widget.setObjectName("menu")

        sidebar_widget.setContentsMargins(0, 0, 0, 0)
        return sidebar_widget
