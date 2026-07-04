import ttkbootstrap as tb
import nexus_core.design_tokens as design

class LabelTittleWidget:
    def __init__(self, tbframe: tb.Frame, text:str, pady:int = 20, padx : int=0):
       self.label = tb.Label(
            tbframe, 
            text= text, 
            font=(design.TYPOGRAPHY["font.family.sans"],
            design.TYPOGRAPHY['font.size.h1']),
            justify="center",  # 🎯 Asegura que el texto se mantenga centrado internamente
            anchor="center",    # 🎯 Centra el contenido dentro del bloque del Label
            padding= 5
       )
    
    # 2. Creamos nuestro propio método pack
    def pack(self, **kwargs):
        # Configuramos valores por defecto si el usuario no los envía
        if "anchor" not in kwargs:
            kwargs["anchor"] = "w"
        if "pady" not in kwargs:
            kwargs["pady"] = 20
            
        self.label.pack(**kwargs)
        return self # Permite encadenar código si se desea

    # 3. Creamos nuestro propio método grid
    def grid(self, row: int = 0, column: int = 0, rowspan: int = 1, columnspan: int = 1, **kwargs):
        """Posicionamiento estructurado con Grid (Soporta filas y columnas combinadas)"""
        # Configuraciones de alineación por defecto si el usuario no las envía
        if "sticky" not in kwargs:
            kwargs["sticky"] = ""
        if "pady" not in kwargs:
            kwargs["pady"] = 20

        # Inyectar los parámetros estructurados dentro de la ejecución de Tkinter
        self.label.grid(
            row=row, 
            column=column, 
            rowspan=rowspan, 
            columnspan=columnspan, 
            **kwargs
        )
        return self