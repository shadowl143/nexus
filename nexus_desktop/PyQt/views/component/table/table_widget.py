# table_frame.py
from PyQt6.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout

class TableFrame(QWidget):
    def __init__(self, parent, columns, data, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        
        # Crear el widget de tabla
        self.table = QTableWidget(self)
        self.table.setColumnCount(len(columns))
        self.table.setHorizontalHeaderLabels(columns)
        
        # Insertar datos en la tabla
        self.table.setRowCount(len(data))
        for row_idx, row_data in enumerate(data):
            for col_idx, item in enumerate(row_data):
                self.table.setItem(row_idx, col_idx, QTableWidgetItem(str(item)))
        
        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.table)
        self.setLayout(layout)