from PyQt6.QtWidgets import QMessageBox


class MessageBoxWidget:

    @staticmethod
    def confirm(parent, title="Información", message="Mensaje del usuario") -> bool:
        respuesta = QMessageBox.question(
            parent,
            title,
            message,
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        )
        return respuesta == QMessageBox.StandardButton.Yes

    @staticmethod
    def information(parent, title="Información", message="Mensaje del usuario") -> None:
        QMessageBox.information(parent, title, message)

    @staticmethod
    def error_critical(parent, title="Error", error_messge="Error inesperado"):
        QMessageBox.critical(parent, title, error_messge)
