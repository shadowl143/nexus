import ttkbootstrap as tb
import nexus_core.design_tokens as design

class LabelTextWidget:
    def __init__(self, tbframe: tb.Frame, text:str):
       self.label = tb.Label(
           tbframe, 
           text= text, 
           font=(design.TYPOGRAPHY["font.family.sans"], design.TYPOGRAPHY['font.size.body']),
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
    def grid(self, **kwargs):
        # Configuramos valores por defecto para grid si no los envían
        if "sticky" not in kwargs:
            kwargs["sticky"] = "w"
        if "pady" not in kwargs:
            kwargs["pady"] = 20
            
        self.label.grid(**kwargs)
        return self