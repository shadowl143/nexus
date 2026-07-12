# main.py
from nexus_desktop.PyQt.views.layout.principal_layout import WindowsPrincipal
from PyQt6.QtWidgets import QApplication
import sys
from nexus_desktop.PyQt.services.multi_lenguage_service import MultiLanguageService

multilang = MultiLanguageService()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = WindowsPrincipal(language=multilang)
    main.show()
    sys.exit(app.exec())
