from PyQt6.QtWidgets import (
    QWidget,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QHeaderView,
)
from PyQt6.QtCore import Qt


class TableFrame(QWidget):
    def __init__(self, parent=None, columns=None, data=None):
        super().__init__(parent)

        columns = columns or []
        data = data or []

        self.table = QTableWidget()
        self.table.setColumnCount(len(columns))
        self.table.setHorizontalHeaderLabels(columns)

        # ✅ No editable
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)

        # ✅ Selección por fila
        self.table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)

        # ✅ Ajustar columnas automáticamente
        self.table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )

        # Insertar datos
        self.load_data(data)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.table)
        self.setLayout(layout)

    # ✅ Método reutilizable para recargar datos
    def load_data(self, data):
        self.table.setRowCount(len(data))

        for row_idx, row_data in enumerate(data):
            for col_idx, item in enumerate(row_data):
                cell = QTableWidgetItem(str(item))
                cell.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                self.table.setItem(row_idx, col_idx, cell)
