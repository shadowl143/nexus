import ttkbootstrap as tb
import nexus_core.design_tokens as design


class LabelTittleWidget(tb.Label):
    DEFAULT_PADX = 15
    DEFAULT_PADY = 15

    def __init__(self, tbframe: tb.Frame, text: str):
        super().__init__(
            tbframe,
            text=text,
            font=(
                design.TYPOGRAPHY["font.family.sans"],
                design.TYPOGRAPHY["font.size.h1"],
            ),
            justify="center",  # 🎯 Asegura que el texto se mantenga centrado internamente
            anchor="center",  # 🎯 Centra el contenido dentro del bloque del Label
            padding=5,
            style="App.TLabel",
        )

    # Defaults para pack
    def pack(self, **kwargs):
        kwargs.setdefault("padx", self.DEFAULT_PADX)
        kwargs.setdefault("pady", self.DEFAULT_PADY)
        return super().pack(**kwargs)

    # Defaults para grid
    def grid(self, **kwargs):
        kwargs.setdefault("padx", self.DEFAULT_PADX)
        kwargs.setdefault("pady", self.DEFAULT_PADY)
        return super().grid(**kwargs)
