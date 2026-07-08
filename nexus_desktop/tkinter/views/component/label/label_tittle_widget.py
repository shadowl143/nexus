import ttkbootstrap as tb
import nexus_core.design_tokens as design

class LabelTittleWidget(tb.Label):
    def __init__(self, tbframe: tb.Frame, text:str, pady:int = 20, padx : int=0):
       super().__init__(
            tbframe, 
            text= text, 
            font=(design.TYPOGRAPHY["font.family.sans"],
            design.TYPOGRAPHY['font.size.h1']),
            justify="center",  # 🎯 Asegura que el texto se mantenga centrado internamente
            anchor="center",    # 🎯 Centra el contenido dentro del bloque del Label
            padding= 5
       )