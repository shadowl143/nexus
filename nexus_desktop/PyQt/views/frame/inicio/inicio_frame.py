from PyQt6.QtWidgets import QFrame
from nexus_desktop.PyQt.services.multi_lenguage_service import MultiLanguageService


class InicioFrame(QFrame):
    def __init__(self, contenedor_principal, language: str):
        super().__init__()
        self.contenedor_principal = contenedor_principal
        self.lenguage = MultiLanguageService(language=language).load_transaction()

    def crear_frame_inicio(self) -> QFrame:
        self.setFrameShape(QFrame.Shape.Box)
        self.setFrameShadow(QFrame.Shadow.Raised)
        self.setLineWidth(2)
