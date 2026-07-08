import ttkbootstrap as tb
import nexus_core.design_tokens as design

class LabelTextWidget(tb.Label):
    def __init__(self, tbframe: tb.Frame, text:str):
       super().__init__(
           tbframe, 
           text= text, 
           font=(design.TYPOGRAPHY["font.family.sans"], design.TYPOGRAPHY['font.size.body']),
            justify="center",  # 🎯 Asegura que el texto se mantenga centrado internamente
            anchor="center",    # 🎯 Centra el contenido dentro del bloque del Label
            padding= 5
       )