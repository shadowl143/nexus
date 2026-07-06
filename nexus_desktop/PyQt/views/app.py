
# main.py
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

class SimpleApp(QWidget):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana
        self.setWindowTitle('Aplicación Básica PyQt')
        self.setGeometry(200, 200, 300, 200)
        # Crear un botón
        self.button = QPushButton('Haz clic aquí', self)
        self.button.clicked.connect(self.on_click)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        self.setLayout(layout)

    def on_click(self):
        print('¡Botón clicado!')

def main():
    app = QApplication(sys.argv)
    window = SimpleApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()